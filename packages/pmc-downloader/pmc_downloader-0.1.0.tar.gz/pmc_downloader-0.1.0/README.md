# PMCDownloader

**PMCDownloader** is a Python library built to streamline the process of searching and downloading open-access articles from **PubMed Central (PMC)**. Whether you need to collect articles for research, manage references, or automate data extraction, this tool simplifies the process, offering a reliable way to retrieve metadata and PDFs of relevant articles.

## Purpose

PMCDownloader allows researchers and developers to efficiently:
- **Search** for scientific articles in **PubMed Central (PMC)** using customizable search terms.
- **Download** full-text PDFs of the articles directly to your local storage.
- Retrieve detailed **metadata** for each article, facilitating better organization and management of references.
- Automate the **downloading process** with robust error handling, retries, and rate-limiting.

This tool is especially beneficial for:
- **Automating research tasks** like bulk downloading academic papers.
- **Ensuring reproducibility** of research by retrieving articles directly from a trusted, open-access repository.
- **Saving time** by eliminating manual article search and download steps.

## Features

- **Custom Search**: Allows you to search PMC for articles based on specific search terms (e.g., disease, topic, author).
- **Metadata Retrieval**: Fetch article metadata, including titles, publication details, and more.
- **PDF Downloads**: Download the full-text PDFs of articles directly from PMC.
- **Directory Customization**: Specify the output directory for storing the downloaded PDFs.
- **Rate Limiting & Robust Error Handling**: Handles retries, timeouts, and rate-limiting to ensure stable operation even under high load.
- **Search Filters**: Filter search results by article type, publication status, and other criteria to refine your results.
- **Max Results Control**: Control the number of search results returned, making it easier to manage large datasets.

## Installation

To install the library via `pip`, run the following command:

```bash
pip install pmc_downloader
```

## Example Usage
```bash
from pmc_downloader import PMCDownloader

downloader = PMCDownloader(
    email="your@email.com",
    api_key="your_api_key",
    search_terms="machine learning cancer",
    output_dir="./articles",
    max_results=50
)

pmc_ids = downloader.search_articles()
downloader.download_articles(pmc_ids, download_count=10)
```
## Example Search Query
```bash
search_query = '''
(
  "student-teacher interaction"[Title/Abstract] OR
  "educational outcomes"[Title/Abstract]
)
AND ("open access"[filter])
NOT ("online learning" OR "AI")
'''

```
## Parameters
### Mandatory Parameters:

 - email: Registered email for NCBI API
 - api_key: Your NCBI API key
 - search_terms: PubMed search query
 - output_dir: Directory where downloaded files will be saved

### Optional Parameters:

 - max_results (default: 1000): Maximum search results
 - request_delay (default: 1.0): Wait time between API requests (seconds)
 - timeout (default: 15.0): Download process timeout period
 - max_retries (default: 3): Maximum number of retries for failed requests
