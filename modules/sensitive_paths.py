from core.requester import fetch

def check_paths(base_url):
    findings = []

    with open("data/paths.txt") as f:
        paths = f.read().splitlines()

    for path in paths:
        target = base_url.rstrip("/") + path
        response = fetch(target)

        if response and response.status_code == 200:
            findings.append(f"Sensitive path exposed: {target}")

    return findings
