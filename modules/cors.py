def check_cors(response, url):
    findings = []

    origin = response.headers.get("Access-Control-Allow-Origin")

    if origin == "*":
        findings.append({
            "title": "CORS Misconfiguration: Wildcard Origin Allowed",
            "severity": "Medium",
            "owasp": "A05 Security Misconfiguration",
            "evidence": url
        })

    return findings
