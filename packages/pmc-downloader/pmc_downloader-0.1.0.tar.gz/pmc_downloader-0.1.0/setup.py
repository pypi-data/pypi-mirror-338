from setuptools import setup, find_packages

with open(r"C:\Users\Çağatay\Desktop\ProjeDosyaları\VSCode\library\README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pmc_downloader",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "biopython>=1.81"
    ],
    python_requires=">=3.8",
    description="PubMed Central (PMC) Open Access Articles Downloader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
    ],
    keywords="pubmed pmc literature scientific-articles bioinformatics",
)