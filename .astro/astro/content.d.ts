declare module 'astro:content' {
	interface RenderResult {
		Content: import('astro/runtime/server/index.js').AstroComponentFactory;
		headings: import('astro').MarkdownHeading[];
		remarkPluginFrontmatter: Record<string, any>;
	}
	interface Render {
		'.md': Promise<RenderResult>;
	}

	export interface RenderedContent {
		html: string;
		metadata?: {
			imagePaths: Array<string>;
			[key: string]: unknown;
		};
	}
}

declare module 'astro:content' {
	type Flatten<T> = T extends { [K: string]: infer U } ? U : never;

	export type CollectionKey = keyof AnyEntryMap;
	export type CollectionEntry<C extends CollectionKey> = Flatten<AnyEntryMap[C]>;

	export type ContentCollectionKey = keyof ContentEntryMap;
	export type DataCollectionKey = keyof DataEntryMap;

	type AllValuesOf<T> = T extends any ? T[keyof T] : never;
	type ValidContentEntrySlug<C extends keyof ContentEntryMap> = AllValuesOf<
		ContentEntryMap[C]
	>['slug'];

	/** @deprecated Use `getEntry` instead. */
	export function getEntryBySlug<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(
		collection: C,
		// Note that this has to accept a regular string too, for SSR
		entrySlug: E,
	): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;

	/** @deprecated Use `getEntry` instead. */
	export function getDataEntryById<C extends keyof DataEntryMap, E extends keyof DataEntryMap[C]>(
		collection: C,
		entryId: E,
	): Promise<CollectionEntry<C>>;

	export function getCollection<C extends keyof AnyEntryMap, E extends CollectionEntry<C>>(
		collection: C,
		filter?: (entry: CollectionEntry<C>) => entry is E,
	): Promise<E[]>;
	export function getCollection<C extends keyof AnyEntryMap>(
		collection: C,
		filter?: (entry: CollectionEntry<C>) => unknown,
	): Promise<CollectionEntry<C>[]>;

	export function getEntry<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(entry: {
		collection: C;
		slug: E;
	}): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof DataEntryMap,
		E extends keyof DataEntryMap[C] | (string & {}),
	>(entry: {
		collection: C;
		id: E;
	}): E extends keyof DataEntryMap[C]
		? Promise<DataEntryMap[C][E]>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(
		collection: C,
		slug: E,
	): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof DataEntryMap,
		E extends keyof DataEntryMap[C] | (string & {}),
	>(
		collection: C,
		id: E,
	): E extends keyof DataEntryMap[C]
		? Promise<DataEntryMap[C][E]>
		: Promise<CollectionEntry<C> | undefined>;

	/** Resolve an array of entry references from the same collection */
	export function getEntries<C extends keyof ContentEntryMap>(
		entries: {
			collection: C;
			slug: ValidContentEntrySlug<C>;
		}[],
	): Promise<CollectionEntry<C>[]>;
	export function getEntries<C extends keyof DataEntryMap>(
		entries: {
			collection: C;
			id: keyof DataEntryMap[C];
		}[],
	): Promise<CollectionEntry<C>[]>;

	export function render<C extends keyof AnyEntryMap>(
		entry: AnyEntryMap[C][string],
	): Promise<RenderResult>;

	export function reference<C extends keyof AnyEntryMap>(
		collection: C,
	): import('astro/zod').ZodEffects<
		import('astro/zod').ZodString,
		C extends keyof ContentEntryMap
			? {
					collection: C;
					slug: ValidContentEntrySlug<C>;
				}
			: {
					collection: C;
					id: keyof DataEntryMap[C];
				}
	>;
	// Allow generic `string` to avoid excessive type errors in the config
	// if `dev` is not running to update as you edit.
	// Invalid collection names will be caught at build time.
	export function reference<C extends string>(
		collection: C,
	): import('astro/zod').ZodEffects<import('astro/zod').ZodString, never>;

	type ReturnTypeOrOriginal<T> = T extends (...args: any[]) => infer R ? R : T;
	type InferEntrySchema<C extends keyof AnyEntryMap> = import('astro/zod').infer<
		ReturnTypeOrOriginal<Required<ContentConfig['collections'][C]>['schema']>
	>;

	type ContentEntryMap = {
		"enquetes": {
"01-le-grand-verrou-financier.md": {
	id: "01-le-grand-verrou-financier.md";
  slug: "01-le-grand-verrou-financier";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"02-le-mythe-des-subventions.md": {
	id: "02-le-mythe-des-subventions.md";
  slug: "02-le-mythe-des-subventions";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"03-etude-comparative-outre-mer-europe.md": {
	id: "03-etude-comparative-outre-mer-europe.md";
  slug: "03-etude-comparative-outre-mer-europe";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"04-la-marchandisation-de-l-eau.md": {
	id: "04-la-marchandisation-de-l-eau.md";
  slug: "04-la-marchandisation-de-l-eau";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"05-l-empire-des-sci-non-residentes.md": {
	id: "05-l-empire-des-sci-non-residentes.md";
  slug: "05-l-empire-des-sci-non-residentes";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"06-le-pillage-des-quotas-de-peche.md": {
	id: "06-le-pillage-des-quotas-de-peche.md";
  slug: "06-le-pillage-des-quotas-de-peche";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"07-le-cadastre-minier-secret.md": {
	id: "07-le-cadastre-minier-secret.md";
  slug: "07-le-cadastre-minier-secret";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"08-le-pillage-de-la-foret-corse.md": {
	id: "08-le-pillage-de-la-foret-corse.md";
  slug: "08-le-pillage-de-la-foret-corse";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"09-l-evasion-des-capitaux-touristiques.md": {
	id: "09-l-evasion-des-capitaux-touristiques.md";
  slug: "09-l-evasion-des-capitaux-touristiques";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"10-la-tutelle-de-la-haute-fonction-publique.md": {
	id: "10-la-tutelle-de-la-haute-fonction-publique.md";
  slug: "10-la-tutelle-de-la-haute-fonction-publique";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"11-l-emprise-et-les-servitudes-militaires.md": {
	id: "11-l-emprise-et-les-servitudes-militaires.md";
  slug: "11-l-emprise-et-les-servitudes-militaires";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"12-la-dependance-sanitaire-evasan.md": {
	id: "12-la-dependance-sanitaire-evasan.md";
  slug: "12-la-dependance-sanitaire-evasan";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"13-le-sous-investissement-educatif.md": {
	id: "13-le-sous-investissement-educatif.md";
  slug: "13-le-sous-investissement-educatif";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"14-le-dessaisissement-judiciaire-jirs.md": {
	id: "14-le-dessaisissement-judiciaire-jirs.md";
  slug: "14-le-dessaisissement-judiciaire-jirs";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"15-le-controle-de-legalite-et-censure.md": {
	id: "15-le-controle-de-legalite-et-censure.md";
  slug: "15-le-controle-de-legalite-et-censure";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"16-la-continuite-des-arretes-miot.md": {
	id: "16-la-continuite-des-arretes-miot.md";
  slug: "16-la-continuite-des-arretes-miot";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"17-le-verrou-de-la-charte-europeenne.md": {
	id: "17-le-verrou-de-la-charte-europeenne.md";
  slug: "17-le-verrou-de-la-charte-europeenne";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"18-le-monopole-energetique-edf-sei.md": {
	id: "18-le-monopole-energetique-edf-sei.md";
  slug: "18-le-monopole-energetique-edf-sei";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"19-la-dependance-numerique-et-data.md": {
	id: "19-la-dependance-numerique-et-data.md";
  slug: "19-la-dependance-numerique-et-data";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"20-l-accaparement-des-primes-pac.md": {
	id: "20-l-accaparement-des-primes-pac.md";
  slug: "20-l-accaparement-des-primes-pac";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"21-le-scandale-des-dechets-syvadec.md": {
	id: "21-le-scandale-des-dechets-syvadec.md";
  slug: "21-le-scandale-des-dechets-syvadec";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"22-la-captation-bancaire-et-epargne.md": {
	id: "22-la-captation-bancaire-et-epargne.md";
  slug: "22-la-captation-bancaire-et-epargne";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"23-la-sous-dotation-de-la-securite-civile.md": {
	id: "23-la-sous-dotation-de-la-securite-civile.md";
  slug: "23-la-sous-dotation-de-la-securite-civile";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"24-le-radar-d-urbanisme-permis-tacites.md": {
	id: "24-le-radar-d-urbanisme-permis-tacites.md";
  slug: "24-le-radar-d-urbanisme-permis-tacites";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"25-la-transparence-des-petitionnaires-mrae.md": {
	id: "25-la-transparence-des-petitionnaires-mrae.md";
  slug: "25-la-transparence-des-petitionnaires-mrae";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"26-la-speculation-sur-le-bati-agricole.md": {
	id: "26-la-speculation-sur-le-bati-agricole.md";
  slug: "26-la-speculation-sur-le-bati-agricole";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
"27-le-telepherique-angelo-ajaccio.md": {
	id: "27-le-telepherique-angelo-ajaccio.md";
  slug: "27-le-telepherique-angelo-ajaccio";
  body: string;
  collection: "enquetes";
  data: InferEntrySchema<"enquetes">
} & { render(): Render[".md"] };
};

	};

	type DataEntryMap = {
		
	};

	type AnyEntryMap = ContentEntryMap & DataEntryMap;

	export type ContentConfig = typeof import("./../../src/content/config.js");
}
