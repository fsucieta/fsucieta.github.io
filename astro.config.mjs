import { defineConfig } from 'astro/config';

// Configuration d'Astro pour générer le site statique dans le dossier docs/ (compatible GitHub Pages)
export default defineConfig({
  output: 'static',
  outDir: './docs',
  build: {
    format: 'file'
  }
});
