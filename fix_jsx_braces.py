with open("src/pages/dossier-transparence-citoyenne-ajaccio.astro", "r", encoding="utf-8") as f:
    text = f.read()

# Replace any curly brace in HTML body to prevent JSX expression evaluation
# We can replace '{' with '&#123;' and '}' with '&#125;' except in script and Astro frontmatter
parts = text.split("</Layout>")
body_part = parts[0]
tail_part = "</Layout>" + parts[1]

# In body_part, everything between <Layout> and </Layout> can have { and } escaped
body_clean = body_part.replace("{", "&#123;").replace("}", "&#125;")
# restore Layout opening tag
body_clean = body_clean.replace("&#123;title&#125;", "{title}").replace("&#123;description&#125;", "{description}").replace("&#123;true&#125;", "{true}")

clean_full = body_clean + tail_part

with open("src/pages/dossier-transparence-citoyenne-ajaccio.astro", "w", encoding="utf-8") as f:
    f.write(clean_full)

print("Escaped all curly braces safely in Astro template!")
