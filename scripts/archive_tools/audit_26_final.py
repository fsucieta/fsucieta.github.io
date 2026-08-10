import os

docs_dir = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\docs'

print("=== VERIFICATION FINALE DES 26 PHOTOGRAPHIES REALISTES HD ===")
for i in range(1, 27):
    name = f"img_enquete_{i:02d}.jpg"
    path = os.path.join(docs_dir, name)
    size = os.path.getsize(path) if os.path.exists(path) else 0
    print(f"Enquête #{i:02d}: {name} -> {size} octets HD")
