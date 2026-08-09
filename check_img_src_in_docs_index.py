import re

html_path = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\docs\index.html'

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

img_tags = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)

print(f"Total <img src=...> trouvés dans docs/index.html: {len(img_tags)}")
for idx, src in enumerate(img_tags, 1):
    print(f"Image #{idx:02d}: {src}")
