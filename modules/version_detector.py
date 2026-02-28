def detect_version(response):
    findings = []

    server = response.headers.get("Server", "")

    if "Apache/2.2" in server:
        findings.append("Outdated Apache version detected")

    if "nginx/1.10" in server:
        findings.append("Outdated Nginx version detected")

    return findings
