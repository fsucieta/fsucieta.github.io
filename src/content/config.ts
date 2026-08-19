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
    sources: z.array(z.object({
      name: z.string(),
      url: z.string(),
      sha256: z.string().optional()
    })).optional()
  })
});

export const collections = { enquetes };
