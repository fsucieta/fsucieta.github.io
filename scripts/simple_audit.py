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

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

failed = []
ok = []

for filename, url in urls_to_test:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        resp = urllib.request.urlopen(req, timeout=3, context=ctx)
        ok.append((filename, url, resp.getcode()))
    except Exception as e:
        failed.append((filename, url, str(e)))

print(f"RESULTS: {len(ok)} WORKING, {len(failed)} FAILED")
print("\n--- FAILED LINKS LIST ---")
for fn, u, err in failed:
    print(f"FAILED [{fn}]: {u} -> {err}")
