import os, shutil, sys
sys.stdout.reconfigure(encoding='utf-8')

d = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack'
archive_dir = os.path.join(d, 'scripts', 'archive_tools')
os.makedirs(archive_dir, exist_ok=True)

# 1. Liste des scripts temporaires de build/debug à déplacer vers scripts/archive_tools/
temp_scripts = [
    'apply_full_domain_specific_sections_01_to_26.py',
    'apply_user_purification_and_images.py',
    'audit_26_final.py',
    'audit_all_images_presence.py',
    'audit_images.py',
    'audit_md_extraction.py',
    'audit_words.js',
    'build_all_26_hd_photographic_illustrations.py',
    'build_batch1.py',
    'build_batch2.py',
    'build_batch3.py',
    'build_batch4.py',
    'build_batch5.py',
    'check_img_src_in_docs_index.py',
    'check_modal.js',
    'check_script_block.js',
    'check_v2_fiches.py',
    'clean_markdown_articles.py',
    'convert_all_section_iv_bullet_lists_to_gfm_tables.py',
    'convert_all_section_ix_protocol_to_tables.py',
    'copy_assets_to_public.py',
    'debug_click.js',
    'debug_syntax.js',
    'deploy_real_photographic_artwork.py',
    'download_26_genuine_photographs.py',
    'enrich_section_x_all_26_articles.py',
    'expand_all_26_articles.py',
    'expand_to_1500w.py',
    'extract_md_files_from_v2.py',
    'extract_tables_from_index_v2.py',
    'find_modal_defs.py',
    'fix_all_svg_images.py',
    'fix_missing_2_photos.py',
    'fix_syntax.py',
    'generate_26_jpg_images.py',
    'inject_batch.js',
    'inject_gfm_tables_all_26_articles.py',
    'inspect_card_imgs.py',
    'inspect_markdown_tables.py',
    'inspect_section_ix_protocol.py',
    'nasa_grade_fix_all_26_articles.py',
    'push_over_1500w.py',
    'refresh_card_images.py',
    'super_expand_to_1500w.py',
    'tailor_all_26_articles_sections_vii_viii_x.py',
    'tailor_section_ix_all_26_articles.py',
    'tailor_section_v_all_26_articles_pulitzer.py',
    'tailor_section_vi_all_26_articles.py',
    'tailor_section_vii_all_26_articles_pulitzer.py',
    'tailor_section_viii_all_26_articles.py',
    'test_modal_execution.js',
    'update_all_md_images_to_jpg.py',
    'upgrade_section_x_all_26_articles_pulitzer.py',
    'verify_section_x_all_26.py'
]

# 2. Fichiers JSON et dumps temporaires à déplacer vers l'archive
temp_data = [
    'batch1_temp.json',
    'batch2_temp.json',
    'batch3_temp.json',
    'batch4_temp.json',
    'batch5_temp.json',
    'full_26_expanded.json',
    'full_26_final_1500w.json',
    'full_26_super_expanded.json'
]

# 3. Fichiers temporaires/inutiles à supprimer définitivement
junk_files = [
    'diff.txt',
    'index_v2.html',
    'old_index.html',
    'temp_check.html'
]

moved_count = 0
deleted_count = 0

for item in temp_scripts + temp_data:
    sp = os.path.join(d, item)
    if os.path.exists(sp):
        shutil.move(sp, os.path.join(archive_dir, item))
        moved_count += 1

for jf in junk_files:
    jp = os.path.join(d, jf)
    if os.path.exists(jp):
        os.remove(jp)
        deleted_count += 1

# 4. Nettoyage des images en double à la racine (les images officielles sont dans public/)
for i in range(1, 27):
    jpg_root = os.path.join(d, f'img_enquete_{i:02d}.jpg')
    svg_root = os.path.join(d, f'img_enquete_{i:02d}.svg')
    if os.path.exists(jpg_root):
        os.remove(jpg_root)
        deleted_count += 1
    if os.path.exists(svg_root):
        os.remove(svg_root)
        deleted_count += 1

print(f"✅ NETTOYAGE EFFECTUÉ AVEC SUCCÈS !")
print(f"📦 {moved_count} scripts/fichiers temporaires archivés dans 'scripts/archive_tools/'")
print(f"🗑️ {deleted_count} fichiers de debug/doublons d'images supprimés de la racine")
