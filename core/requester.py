import requests

session = requests.Session()
session.headers.update({"User-Agent": "VulnEye Scanner"})

def fetch(url):
    try:
        response = session.get(url, timeout=5, allow_redirects=True)
        return response
    except:
        return None
