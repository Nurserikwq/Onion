from bs4 import BeautifulSoup as bs
import requests
from urllib.parse import urljoin
import os

domain = "https://arxiv.org"
url = "https://arxiv.org/list/gr-qc/2025?skip=0&show=50"
filetype = ".pdf"
title = "Download PDF"

def get_url(url):
    return bs(requests.get(url).text, "html.parser")

for link in get_url(url).find_all("a"):
    relative_link = link.get("href")

    if relative_link is not None and relative_link.startswith('/pdf/'):
        absolute_url = urljoin(domain, relative_link)
        print(absolute_url)

        filename = relative_link.split("/")[-1] + ".pdf" if not relative_link.endswith(".pdf") else relative_link.split("/")[-1]
        filepath = os.path.join("pdfs", filename)

        response = requests.get(absolute_url)
        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"✅ Saved: {filepath}")