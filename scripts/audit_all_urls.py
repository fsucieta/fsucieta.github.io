import os
import re
import urllib.request
import ssl

enquetes_dir = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\src\content\enquetes'
urls_to_test = []

for filename in sorted(os.listdir(enquetes_dir)):
    if filename.endswith('.md'):
        filepath = os.path.join(enquetes_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            matches = re.findall(r'url:\s*"([^"]+)"', content)
            for m in matches:
                urls_to_test.append((filename, m))

print(f"Total URLs to audit: {len(urls_to_test)}")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

failed_urls = []
working_urls = []

for filename, url in urls_to_test:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    try:
        resp = urllib.request.urlopen(req, timeout=6, context=ctx)
        code = resp.getcode()
        if code in [200, 301, 302]:
            print(f"[OK 200] {filename} -> {url}")
            working_urls.append((filename, url))
        else:
            print(f"[FAIL {code}] {filename} -> {url}")
            failed_urls.append((filename, url, f"Status {code}"))
    except Exception as e:
        print(f"[FAIL ERROR] {filename} -> {url} : {e}")
        failed_urls.append((filename, url, str(e)))

print("\n--- AUDIT SUMMARY ---")
print(f"Working URLs: {len(working_urls)}")
print(f"Failed URLs: {len(failed_urls)}")

with open("scripts/audit_report.txt", "w", encoding="utf-8") as f:
    f.write(f"FAILED URLS REPORT ({len(failed_urls)} failures):\n")
    for fn, u, err in failed_urls:
        f.write(f"File: {fn} | URL: {u} | Error: {err}\n")
