import sys
import argparse
import json
from colorama import Fore, init
from concurrent.futures import ThreadPoolExecutor

from core.requester import fetch
from core.crawler import crawl
from core.reporter import generate_report
from modules.headers import check_headers
from modules.methods import check_methods
from modules.sensitive_paths import check_paths
from modules.version_detector import detect_version
from modules.injection import check_reflection, check_sql_errors
from modules.cors import check_cors
from modules.ratelimit import check_ratelimit

init(autoreset=True)

def banner():
    print(Fore.RED + r"""
██╗   ██╗██╗   ██╗██╗     ███╗   ██╗███████╗██╗   ██╗███████╗
██║   ██║██║   ██║██║     ████╗  ██║██╔════╝╚██╗ ██╔╝██╔════╝
██║   ██║██║   ██║██║     ██╔██╗ ██║█████╗   ╚████╔╝ █████╗  
╚██╗ ██╔╝██║   ██║██║     ██║╚██╗██║██╔══╝    ╚██╔╝  ██╔══╝  
 ╚████╔╝ ╚██████╔╝███████╗██║ ╚████║███████╗   ██║   ███████╗
  ╚═══╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝
                 VulnEye Enterprise
""")

parser = argparse.ArgumentParser()
parser.add_argument("target", help="Target URL")
parser.add_argument("--threads", type=int, default=10, help="Number of threads")
parser.add_argument("--json", action="store_true", help="Output JSON report")
parser.add_argument("--crawl", action="store_true", help="Enable crawling")

args = parser.parse_args()

banner()

target = args.target
print(Fore.CYAN + f"[+] Target: {target}")
print(Fore.YELLOW + "[*] Starting Enterprise Scan...\n")

response = fetch(target)

if not response:
    print(Fore.RED + "Target unreachable.")
    sys.exit()

urls = {target}

if args.crawl:
    urls |= crawl(target)

all_findings = []
scanned = 0

def scan(url):
    findings = []
    res = fetch(url)
    if not res:
        return []

    for issue in check_headers(res):
        findings.append({"title": issue, "severity": "Medium", "owasp": "A05", "evidence": url})

    for issue in detect_version(res):
        findings.append({"title": issue, "severity": "Medium", "owasp": "A06", "evidence": url})

    findings += check_sql_errors(res, url)
    findings += check_reflection(url)
    findings += check_cors(res, url)

    for issue in check_methods(url):
        findings.append({"title": issue, "severity": "High", "owasp": "A05", "evidence": url})

    return findings


with ThreadPoolExecutor(max_workers=args.threads) as executor:
    results = executor.map(scan, urls)

for result in results:
    all_findings += result
    scanned += 1
    print(Fore.GREEN + f"[✓] Progress: {scanned}/{len(urls)}")

all_findings += check_ratelimit(target)

print(Fore.YELLOW + f"\nScan Finished. Total Findings: {len(all_findings)}")

if args.json:
    print(json.dumps(all_findings, indent=4))
else:
    report_file = generate_report(target, all_findings)
    print(Fore.CYAN + f"Report saved: {report_file}")
