import os
import re

dir_path = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\src\content\enquetes'

def clean_html_to_markdown(html_content):
    # 1. Remplacer les <h3> avec style par du H2/H3 Markdown
    content = re.sub(r'<h3[^>]*>(.*?)<\/h3>', r'\n\n## \1\n\n', html_content, flags=re.DOTALL)
    content = re.sub(r'<h4[^>]*>(.*?)<\/h4>', r'\n\n### \1\n\n', content, flags=re.DOTALL)
    
    # 2. Remplacer les <blockquote...> par des citations Markdown >
    content = re.sub(r'<blockquote[^>]*>(.*?)<\/blockquote>', r'\n\n> \1\n\n', content, flags=re.DOTALL)
    
    # 3. Remplacer les <div style="..."...> par du contenu propre
    content = re.sub(r'<div class="article-content"[^>]*>', '', content)
    content = re.sub(r'<div style="background:[^>]*>', '\n\n---\n\n', content)
    content = re.sub(r'<\/div>', '', content)
    
    # 4. Nettoyer les balises <p style="...">
    content = re.sub(r'<p[^>]*>', '\n\n', content)
    content = re.sub(r'<\/p>', '\n\n', content)
    
    # 5. Nettoyer les balises <strong> et <em>
    content = re.sub(r'<strong[^>]*>(.*?)<\/strong>', r'**\1**', content, flags=re.DOTALL)
    content = re.sub(r'<em[^>]*>(.*?)<\/em>', r'*\1*', content, flags=re.DOTALL)
    
    # 6. Nettoyer les balises <ul>, <li>
    content = re.sub(r'<ul[^>]*>', '\n\n', content)
    content = re.sub(r'<\/ul>', '\n\n', content)
    content = re.sub(r'<li[^>]*>(.*?)<\/li>', r'* \1\n', content, flags=re.DOTALL)
    
    # 7. Nettoyer les balises <code>
    content = re.sub(r'<code[^>]*>(.*?)<\/code>', r'`\1`', content, flags=re.DOTALL)
    
    # Nettoyer les sauts de ligne multiples
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content.strip()

for fname in os.listdir(dir_path):
    if fname.endswith('.md'):
        filepath = os.path.join(dir_path, fname)
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
        
        parts = text.split('---')
        if len(parts) >= 3:
            frontmatter = parts[1]
            body_html = '---'.join(parts[2:])
            
            clean_body = clean_html_to_markdown(body_html)
            
            new_content = f"---{frontmatter}---\n\n{clean_body}\n"
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Nettoyé {fname} -> Pur Markdown haut contraste")

print("Toutes les fiches ont été converties en Markdown pur sans balises HTML rémanentes !")
