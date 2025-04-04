import os
import re
import time
from typing import List, Optional
import requests
from Bio import Entrez
import xml.etree.ElementTree as ET

class PMCDownloader:
    def __init__(
        self,
        email: str,
        api_key: str,
        output_dir: str,
        search_terms: str,
        max_results: int = 1000,
        request_delay: float = 1.0,
        max_retries: int = 3,
        timeout: float = 15.0
    ):
        self.email = email
        self.api_key = api_key
        self.output_dir = output_dir
        self.search_terms = search_terms
        self.max_results = max_results
        self.request_delay = request_delay
        self.max_retries = max_retries
        self.timeout = timeout

        try:
            os.makedirs(self.output_dir, exist_ok=True)
            if not os.access(self.output_dir, os.W_OK):
                raise PermissionError(f"Output directory '{self.output_dir}' is not writable")
        except OSError as e:
            raise RuntimeError(f"Failed to create output directory: {str(e)}")

    def _sanitize_filename(self, title: str) -> str:
        title = re.sub(r'[^\w\s-]', '', title).strip()
        return re.sub(r'[-\s]+', '-', title)[:100]

    def _set_entrez_parameters(self):
        Entrez.email = self.email
        Entrez.api_key = self.api_key
        time.sleep(self.request_delay)  # Rate limiting

    def download_pdf(self, pmc_id: str, title: str, output_dir: Optional[str] = None) -> bool:
        output_dir = output_dir or self.output_dir
        pmc_id_clean = pmc_id.replace('PMC', '') 
        pdf_url = f"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{pmc_id_clean}/pdf/"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "application/pdf"
        }

        for attempt in range(self.max_retries):
            try:
                response = requests.get(
                    pdf_url,
                    headers=headers,
                    timeout=self.timeout,
                    allow_redirects=True
                )
                
                if response.status_code == 200 and 'application/pdf' in response.headers.get('Content-Type', ''):
                    safe_title = self._sanitize_filename(title)
                    filename = os.path.join(output_dir, f"{pmc_id}_{safe_title}.pdf")
                    
                    with open(filename, 'wb') as f:
                        f.write(response.content)
                        
                    print(f"✅ Successfully downloaded: {pmc_id} - {safe_title}")
                    return True
                
                print(f"❌ PDF is not accessible: {pmc_id} - HTTP {response.status_code}")
                return False

            except requests.exceptions.RequestException as e:
                print(f"⚠️ Download error (Trial {attempt + 1}/{self.max_retries}): {pmc_id} - {str(e)}")
                time.sleep(2 ** attempt)

        print(f"❌ Maximum number of attempts exceeded: {pmc_id}")
        return False

    def parse_article_title(self, article_xml: str) -> str:
        try:
            namespaces = {
                'jats': 'http://www.ncbi.nlm.nih.gov/JATS1',
                'xml': 'http://www.w3.org/XML/1998/namespace',
                'xlink': 'http://www.w3.org/1999/xlink'
            }
            
            root = ET.fromstring(article_xml)
            
            xpaths = [
                './/jats:article-title',  
                './/title-group/jats:article-title', 
                './/article-title', 
                './/title',  
                './/dc:title', 
            ]
            
            for xpath in xpaths:
                title_elem = root.find(xpath, namespaces)
                if title_elem is not None:
                    title_text = ''.join(title_elem.itertext()).strip()
                    if title_text:
                        return title_text
        
            citation_elem = root.find('.//jats:citation-title', namespaces)
            if citation_elem is not None:
                return citation_elem.text.strip()
                
        except ET.ParseError as e:
            print(f"⚠️ XML parse hatası: {str(e)}")
        except Exception as e:
            print(f"⚠️ Başlık çıkarım hatası: {str(e)}")
        
        if 'article-title' in article_xml:
            start = article_xml.find('<article-title>') + len('<article-title>')
            end = article_xml.find('</article-title>')
            if start > 0 and end > start:
                return article_xml[start:end].strip()
        
        return "Başlıksız"

    def search_articles(self) -> List[str]:
        self._set_entrez_parameters()
        
        try:
            search_handle = Entrez.esearch(
                db="pmc",
                term=self.search_terms,
                retmax=self.max_results,
                usehistory="y",
                sort="relevance"
            )
            search_results = Entrez.read(search_handle)
            search_handle.close()
            
            pmc_ids = search_results.get("IdList", [])
            print(f"🔍 Total number of articles found: {len(pmc_ids)}")
            return pmc_ids
            
        except Exception as e:
            print(f"🔥 Fatal error during search: {str(e)}")
            return []

    def download_articles(self, pmc_ids: List[str], download_count: int) -> int:
        if not pmc_ids:
            print("⚠️ No article found to download.")
            return 0

        valid_count = min(download_count, len(pmc_ids))
        success_count = 0

        print(f"⏳ Downloading total {valid_count} articles...")
        
        for pmc_id in pmc_ids[:valid_count]:
            try:
                self._set_entrez_parameters()
                with Entrez.efetch(db="pmc", id=pmc_id, rettype="full", retmode="xml") as fetch_handle:
                    article_xml = fetch_handle.read()
                    
                title = self.parse_article_title(article_xml)
                if self.download_pdf(pmc_id, title):
                    success_count += 1
                    
            except Exception as e:
                print(f"⚠️Error while processing the article: {pmc_id} - {str(e)}")

        print(f"✅ Total {success_count}/{valid_count} articles successfully downloaded.")
        return success_count
