import { defineConfig } from 'astro/config';

// Configuration d'Astro pour générer le site statique dans le dossier docs/ (compatible GitHub Pages)
// site : URL de base du site sur GitHub Pages (indispensable pour que les chemins CSS/JS soient corrects)
export default defineConfig({
  site: 'https://fsucieta.github.io',
  output: 'static',
  outDir: './docs',
  build: {
    format: 'directory'
  }
});
