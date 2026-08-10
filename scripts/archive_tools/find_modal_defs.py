html = open(r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\docs\index.html', encoding='utf-8', errors='ignore').read()
lines = html.split('\n')
for i, line in enumerate(lines):
    if 'openModal' in line or 'function' in line and 'Modal' in line:
        print(f"{i}: {line.strip()[:100]}")
