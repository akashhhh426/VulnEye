import requests

def check_methods(url):
    issues = []
    try:
        response = requests.options(url, timeout=5)
        allowed = response.headers.get("Allow", "")

        dangerous = ["PUT", "DELETE", "TRACE"]

        for method in dangerous:
            if method in allowed:
                issues.append(f"Dangerous HTTP method enabled: {method}")

    except:
        pass

    return issues
