def check_headers(response):
    issues = []
    headers = response.headers

    required = [
        "Content-Security-Policy",
        "X-Frame-Options",
        "Strict-Transport-Security",
        "X-Content-Type-Options"
    ]

    for header in required:
        if header not in headers:
            issues.append(f"Missing security header: {header}")

    return issues
