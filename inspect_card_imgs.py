import re

html_path = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\docs\index_v2.html'
with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Find grid section
grid_match = re.search(r'<div class="grid-26" id="fichesGrid">(.*?)<\/section>', html, re.DOTALL)
if grid_match:
    grid_html = grid_match.group(1)
    imgs = re.findall(r'src="(.*?)"', grid_html)
    print(f"Found {len(imgs)} image tags in fichesGrid:")
    for idx, img in enumerate(imgs, 1):
        print(f"  Card #{idx:02d}: {img}")
else:
    print("Could not find fichesGrid")
