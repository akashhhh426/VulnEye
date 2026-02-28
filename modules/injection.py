import random
import string
from core.requester import fetch

def check_reflection(url):
    findings = []

    test_string = "VULNEYE_TEST_" + ''.join(random.choices(string.ascii_uppercase, k=5))

    if "?" in url:
        test_url = url + test_string
    else:
        test_url = url + "?v=" + test_string

    response = fetch(test_url)

    if response and test_string in response.text:
        findings.append({
            "title": "Possible Reflected Input",
            "severity": "Medium",
            "owasp": "A03 Injection",
            "evidence": url
        })

    return findings


def check_sql_errors(response, url):
    findings = []

    sql_errors = [
        "SQL syntax",
        "mysql_fetch",
        "ORA-01756",
        "SQLite error",
        "Warning: mysql",
    ]

    for error in sql_errors:
        if error.lower() in response.text.lower():
            findings.append({
                "title": "SQL Error Pattern Detected",
                "severity": "High",
                "owasp": "A03 Injection",
                "evidence": url
            })

    return findings
