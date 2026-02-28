from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from core.requester import fetch

visited = set()

def crawl(base_url):
    urls = set()
    response = fetch(base_url)
    if not response:
        return urls

    soup = BeautifulSoup(response.text, "html.parser")

    for link in soup.find_all("a", href=True):
        full_url = urljoin(base_url, link["href"])
        parsed = urlparse(full_url)

        if parsed.netloc == urlparse(base_url).netloc:
            urls.add(full_url)

    return urls
