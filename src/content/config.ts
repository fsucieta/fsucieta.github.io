import { defineCollection, z } from 'astro:content';

const enquetes = defineCollection({
  type: 'content',
  schema: z.object({
    id: z.number(),
    title: z.string(),
    subtitle: z.string(),
    category: z.string(),
    ref: z.string(),
    author: z.string(),
    date: z.string(),
    tool: z.string(),
    chapeau: z.string(),
    math: z.string().optional(),
    image: z.string(),
    imageCaption: z.string().optional(),
    // Champs audio bilingues (optionnels) — utilisés par le composant AudioBriefing
    audioBriefingFr: z.string().optional(), // Chemin vers le fichier audio FR (ex: /audio/01-briefing-fr.mp3)
    audioBriefingEn: z.string().optional(), // Chemin vers le fichier audio EN (ex: /audio/01-briefing-en.mp3)
    // Statut d'investigation : 'cloturee' (scellée, preuve définitive) ou 'en_cours' (instruction citoyenne & appel à pièces)
    status: z.enum(['cloturee', 'en_cours']).default('cloturee'),
    // Communes mentionnées dans l'enquête — utilisé par le moteur d'interconnexion cartographique
    communes: z.array(z.string()).optional(),
    sources: z.array(z.object({
      name: z.string(),
      url: z.string(),
      pdfDirect: z.string().optional(),
      sha256: z.string().optional()
    })).optional()
  })
});

const investigations = defineCollection({
  type: 'content',
  schema: z.object({
    id: z.number(),
    title: z.string(),
    subtitle: z.string(),
    category: z.string(),
    ref: z.string(),
    author: z.string(),
    date: z.string(),
    tool: z.string(),
    chapeau: z.string(),
    math: z.string().optional(),
    image: z.string(),
    imageCaption: z.string().optional(),
    // Champs audio bilingues (optionnels) — EN version
    audioBriefingFr: z.string().optional(),
    audioBriefingEn: z.string().optional(),
    // Investigation status: 'cloturee' or 'en_cours'
    status: z.enum(['cloturee', 'en_cours']).default('cloturee'),
    // Communes mentionnées dans l'investigation (identiques aux enquêtes FR correspondantes)
    communes: z.array(z.string()).optional(),
    sources: z.array(z.object({
      name: z.string(),
      url: z.string(),
      pdfDirect: z.string().optional(),
      sha256: z.string().optional()
    })).optional()
  })
});

export const collections = { enquetes, investigations };
