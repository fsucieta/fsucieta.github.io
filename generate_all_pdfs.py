import os
import subprocess
import glob

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(CHROME_PATH):
    CHROME_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

html_files = sorted(glob.glob("public/docs/opposition_ajaccio/*.html"))
print(f"Total HTML files to convert: {len(html_files)}")
print(f"Using browser engine: {CHROME_PATH}")

for h in html_files:
    pdf_out = h.replace(".html", ".pdf")
    abs_html = os.path.abspath(h)
    abs_pdf = os.path.abspath(pdf_out)
    
    cmd = [
        CHROME_PATH,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={abs_pdf}",
        f"file:///{abs_html.replace(os.sep, '/')}"
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(abs_pdf):
        size_kb = os.path.getsize(abs_pdf) / 1024
        print(f"OK: {os.path.basename(abs_pdf)} ({size_kb:.1f} KB)")
    else:
        print(f"FAILED: {h} - {res.stderr}")
