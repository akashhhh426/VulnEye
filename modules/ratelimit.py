import requests
import time

def check_ratelimit(url):
    findings = []
    test_url = url

    try:
        for _ in range(5):
            requests.get(test_url, timeout=3)

        findings.append({
            "title": "No visible rate limiting detected",
            "severity": "Low",
            "owasp": "A04 Insecure Design",
            "evidence": url
        })

    except:
        pass

    return findings
