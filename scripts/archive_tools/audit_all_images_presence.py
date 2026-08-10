import os

docs_dir = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\docs'
public_dir = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\public'

docs_files = set(os.listdir(docs_dir))
public_files = set(os.listdir(public_dir))

print("=== AUDIT DE PRÉSENCE DES IMAGES (01 À 26) ===")

missing_docs = []
missing_public = []

for i in range(1, 27):
    img_name = f"img_enquete_{i:02d}.jpg"
    in_docs = img_name in docs_files
    in_public = img_name in public_files
    print(f"Enquête #{i:02d}: {img_name} -> dans docs/: {in_docs} | dans public/: {in_public}")
    if not in_docs:
        missing_docs.append(img_name)
    if not in_public:
        missing_public.append(img_name)

print(f"\nManquants dans docs/: {len(missing_docs)}")
print(f"Manquants dans public/: {len(missing_public)}")
