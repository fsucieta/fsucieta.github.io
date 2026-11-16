export type Lang6 = 'it' | 'es' | 'pt' | 'ru' | 'zh' | 'ja';

export interface UiLabels {
  sealedBadge: string;
  citizenCell: string;
  pubDate: string;
  openDataTools: string;
  forensicStandard: string;
  backTo10: string;
  supportBtn: string;
  donShort: string;
  isoCardBadge: string;
  readDossier: string;
  footerTitle: string;
  footerSub: string;
  cardHeaderTag: string;
  householdTitle: string;
  forensicTitle: string;
  auditSectionTitle: string;
  solutionsSectionTitle: string;
  munitionsBadge: string;
  munitionsTitle: string;
  motto: string;
  authorSig: string;
}

export const uiLabels: Record<Lang6, UiLabels> = {
  it: {
    sealedBadge: "ATTO OPPOSABILE SCELLATO",
    citizenCell: "CELLULA D'ISTRUZIONE",
    pubDate: "DATA DI PUBBLICAZIONE",
    openDataTools: "STRUMENTI OPEN DATA",
    forensicStandard: "NORMA FORENSE",
    backTo10: "← Ritorna alle 10 inchieste sigillate",
    supportBtn: "SOSTENERE L'INCHIESTA",
    donShort: "DONA",
    isoCardBadge: "ISO 27037 SCELLATO",
    readDossier: "Consultare il Dossier",
    footerTitle: "L'OCHJU — CELLULA D'INVESTIGAZIONE CITTADINA & OPEN DATA",
    footerSub: "Edizione cittadina indipendente senza scopo di lucro (LCEN) · Norma forense ISO/IEC 27037.",
    cardHeaderTag: "👁️ U SAPÈ CITADINU : COSA COSTA ALLA TUA FAMIGLIA",
    householdTitle: "In parole povere per la tua famiglia:",
    forensicTitle: "⚖️ PROVE UFFICIALI CERTIFICATO ISO/IEC 27037",
    auditSectionTitle: "1. AUTOPSIA FORENSE DEI CONTI E REGISTRI UFFICIALI",
    solutionsSectionTitle: "2. IL PIANO DI SOVRANITÀ E RICORSO LEGALE (40% SOLUZIONI)",
    munitionsBadge: "⚖️ MUNIZIONI CITTADINE — ACCESSO DIRETTO",
    munitionsTitle: "I fatti sono sigillati. Scarica i dossier operativi per agire nei consigli comunali e in tribunale:",
    motto: "« Il Sapere condiviso è il nostro contropotere. L'OCHJU è lo sguardo che non si distoglie più. »",
    authorSig: "— Cellula d'Investigazione L'OCHJU"
  },
  es: {
    sealedBadge: "ACTO OPONIBLE SELLADO",
    citizenCell: "CÉLULA DE INSTRUCCIÓN",
    pubDate: "FECHA DE PUBLICACIÓN",
    openDataTools: "HERRAMIENTAS OPEN DATA",
    forensicStandard: "NORMA FORENSE",
    backTo10: "← Volver a las 10 investigaciones selladas",
    supportBtn: "APOYAR LA INVESTIGACIÓN",
    donShort: "DONAR",
    isoCardBadge: "ISO 27037 SELLADO",
    readDossier: "Consultar el Expediente",
    footerTitle: "L'OCHJU — CÉLULA DE INVESTIGACIÓN CIUDADANA Y OPEN DATA",
    footerSub: "Edición ciudadana independiente sin ánimo de lucro (LCEN) · Norma forense ISO/IEC 27037.",
    cardHeaderTag: "👁️ U SAPÈ CITADINU : QUÉ LE CUESTA A SU HOGAR",
    householdTitle: "En términos claros para su familia:",
    forensicTitle: "⚖️ PRUEBAS OFICIALES SELLADAS ISO/IEC 27037",
    auditSectionTitle: "1. AUTOPSIA FORENSE DE LAS CUENTAS Y REGISTROS OFICIALES",
    solutionsSectionTitle: "2. PLAN DE SOBERANÍA Y ACCIÓN LEGAL (40% SOLUCIONES)",
    munitionsBadge: "⚖️ MUNICIÓN CIUDADANA — ACCESO DIRECTO",
    munitionsTitle: "Los hechos están sellados. Descargue los expedientes clave para actuar ante municipios y tribunales:",
    motto: "« El Saber compartido es nuestro contrapoder. L'OCHJU es la mirada que ya no se desvía. »",
    authorSig: "— Célula de Investigación L'OCHJU"
  },
  pt: {
    sealedBadge: "ATO OPONÍVEL SELADO",
    citizenCell: "CÉLULA DE INSTRUÇÃO",
    pubDate: "DATA DE PUBLICAÇÃO",
    openDataTools: "FERRAMENTAS OPEN DATA",
    forensicStandard: "NORMA FORENSE",
    backTo10: "← Voltar às 10 investigações seladas",
    supportBtn: "APOIAR A INVESTIGAÇÃO",
    donShort: "DOAR",
    isoCardBadge: "ISO 27037 SELADO",
    readDossier: "Consultar o Processo",
    footerTitle: "L'OCHJU — CÉLULA DE INVESTIGAÇÃO CIDADÃ & OPEN DATA",
    footerSub: "Edição cidadã independente sem fins lucrativos (LCEN) · Norma forense ISO/IEC 27037.",
    cardHeaderTag: "👁️ U SAPÈ CITADINU : O QUE ISTO CUSTA À SUA FAMÍLIA",
    householdTitle: "Em linguagem direta para a sua família:",
    forensicTitle: "⚖️ PROVAS OFICIAIS SELADAS ISO/IEC 27037",
    auditSectionTitle: "1. AUTÓPSIA FORENSE DAS CONTAS E REGISTOS OFICIAIS",
    solutionsSectionTitle: "2. PLANO DE SOBERANIA E RECURSO LEGAL (40% SOLUÇÕES)",
    munitionsBadge: "⚖️ MUNIÇÕES CIDADÃS — ACESSO DIRETO",
    munitionsTitle: "Os factos estão selados. Descarregue os dossiês para agir nos municípios e nos tribunais:",
    motto: "« O Saber partilhado é o nosso contrapoder. L'OCHJU é o olhar que já não se desvia. »",
    authorSig: "— Célula de Investigação L'OCHJU"
  },
  ru: {
    sealedBadge: "ЗАВЕРЕННЫЙ ОФИЦИАЛЬНЫЙ АКТ",
    citizenCell: "РАССЛЕДОВАТЕЛЬСКАЯ ГРУППА",
    pubDate: "ДАТА ПУБЛИКАЦИИ",
    openDataTools: "ИНСТРУМЕНТЫ OPEN DATA",
    forensicStandard: "СУДЕБНЫЙ СТАНДАРТ",
    backTo10: "← Вернуться к 10 расследованиям",
    supportBtn: "ПОДДЕРЖАТЬ РАССЛЕДОВАНИЕ",
    donShort: "ДОНАТ",
    isoCardBadge: "ISO 27037 ЗАВЕРЕНО",
    readDossier: "Открыть досье",
    footerTitle: "L'OCHJU — ГРАЖДАНСКАЯ ИССЛЕДОВАТЕЛЬСКАЯ ЯЧЕЙКА И OPEN DATA",
    footerSub: "Независимое некоммерческое гражданское издание (LCEN) · Стандарт ISO/IEC 27037.",
    cardHeaderTag: "👁️ U SAPÈ CITADINU : СКОЛЬКО ЭТО СТОИТ КАЖДОЙ СЕМЬЕ",
    householdTitle: "Прямым языком для вашей семьи:",
    forensicTitle: "⚖️ ОФИЦИАЛЬНЫЕ ДОКАЗАТЕЛЬСТВА ISO/IEC 27037",
    auditSectionTitle: "1. СУДЕБНО-ЭКОНОМИЧЕСКИЙ АУДИТ СЧЕТОВ И РЕЕСТРОВ",
    solutionsSectionTitle: "2. ПЛАН СУВЕРЕНИТЕТА И ПРАВОВЫХ ДЕЙСТВИЙ (40% РЕШЕНИЯ)",
    munitionsBadge: "⚖️ ГРАЖДАНСКИЙ АРСЕНАЛ — ПРЯМОЙ ДОСТУП",
    munitionsTitle: "Факты зафиксированы. Скачайте готовые материалы для подачи в муниципалитеты и суды:",
    motto: "« Общее знание — наш противовес власти. L'OCHJU — взгляд, который больше не отводится. »",
    authorSig: "— Расследовательская ячейка L'OCHJU"
  },
  zh: {
    sealedBadge: "已公证封存抗辩卷宗",
    citizenCell: "调查侦查小组",
    pubDate: "发布日期",
    openDataTools: "开源数据工具",
    forensicStandard: "司法鉴定标准",
    backTo10: "← 返回全部 10 项封存调查",
    supportBtn: "支持本项调查",
    donShort: "捐助",
    isoCardBadge: "ISO 27037 已封存",
    readDossier: "查阅完整卷宗",
    footerTitle: "L'OCHJU — 公民调查与开源数据中心",
    footerSub: "非营利独立公民调查媒体 (LCEN) · ISO/IEC 27037 数字取证标准。",
    cardHeaderTag: "👁️ U SAPÈ CITADINU : 这一丑闻对每个家庭的直接代价",
    householdTitle: "直白解读给您的家庭：",
    forensicTitle: "⚖️ ISO/IEC 27037 官方封存证据清单",
    auditSectionTitle: "1. 官方账目与公共登记簿司法审计",
    solutionsSectionTitle: "2. 主权恢复方案与法律行动路线 (40% 解决方案)",
    munitionsBadge: "⚖️ 公民法律工具箱 — 直接查阅",
    munitionsTitle: "所有事实均已完成数字封存，可直接下载以下档案向市政当局或法院提起行动：",
    motto: "« 共享知识就是我们的制衡力量。L'OCHJU 是永不移开的凝视。 »",
    authorSig: "— L'OCHJU 调查小组"
  },
  ja: {
    sealedBadge: "公証封緘済み対抗証拠文書",
    citizenCell: "調査担当部門",
    pubDate: "公開日",
    openDataTools: "オープンデータ解析ツール",
    forensicStandard: "フォレンジック規格",
    backTo10: "← 10件の封緘調査ファイルへ戻る",
    supportBtn: "この調査を支援する",
    donShort: "寄付",
    isoCardBadge: "ISO 27037 封緘済み",
    readDossier: "調査ファイルを開く",
    footerTitle: "L'OCHJU — 市民調査報道・オープンデータ機関",
    footerSub: "非営利独立市民メディア (LCEN) · ISO/IEC 27037 フォレンジック規格準拠。",
    cardHeaderTag: "👁️ U SAPÈ CITADINU : ご家庭への直接的な負担",
    householdTitle: "ご家族にとっての分かりやすい意味：",
    forensicTitle: "⚖️ ISO/IEC 27037 公式封緘証拠記録",
    auditSectionTitle: "1. 公会計および国家登記簿のフォレンジック監査",
    solutionsSectionTitle: "2. 主権回復計画および法的対抗措置 (40% 解決策)",
    munitionsBadge: "⚖️ 市民行動ツールキット — 直接アクセス",
    munitionsTitle: "すべての事実は暗号封緘済みです。自治体や裁判所へ提出可能な公式資料をダウンロードできます：",
    motto: "« 共有された知こそが我々の対抗力である。L'OCHJU は決して逸らされない眼差しである。 »",
    authorSig: "— L'OCHJU 調査部門"
  }
};

interface MetricItem {
  label: string;
  value: string;
  sub: string;
  colorClass: string;
}

interface EnqueteContentData {
  title: string;
  subtitle: string;
  category: string;
  date: string;
  author: string;
  chapeau: string;
  imageCaption: string;
  metrics: MetricItem[];
  householdSummary: string;
  proofs: { title: string; detail: string }[];
  auditParagraphs: string[];
  solutionsList: string[];
  transmissionSlug: string;
}

export interface TranslatedEnquete {
  title: string;
  subtitle: string;
  category: string;
  date: string;
  author: string;
  chapeau: string;
  imageCaption: string;
  bodyHtml: string;
}

function renderHtml(lang: Lang6, d: EnqueteContentData): string {
  const u = uiLabels[lang];
  const cards = d.metrics.map(m => `
    <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
      <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">${m.label}</span>
      <span class="text-xl md:text-2xl font-black ${m.colorClass} font-mono">${m.value}</span>
      <span class="text-[10px] text-slate-400 block mt-1">${m.sub}</span>
    </div>
  `).join('');

  const proofsHtml = d.proofs.map(p => `
    <div class="p-3 rounded-xl bg-slate-950/70 border border-slate-800">
      <div class="text-slate-400 text-[10px] uppercase font-mono">${p.title}</div>
      <div class="text-slate-200 font-bold text-xs font-mono mt-1">${p.detail}</div>
    </div>
  `).join('');

  const auditHtml = d.auditParagraphs.map(p => `<p>${p}</p>`).join('\n');
  const solHtml = d.solutionsList.map(s => `<li>${s}</li>`).join('\n');

  return `
<div class="my-8 not-prose rounded-2xl border-2 border-amber-500/50 bg-gradient-to-b from-slate-900 via-slate-950 to-slate-950 p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="border-b border-amber-500/30 pb-5 mb-5">
    <div class="flex items-center gap-2 mb-2">
      <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
      <span class="text-xs font-mono font-bold tracking-widest uppercase text-amber-400">${u.cardHeaderTag}</span>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-4 gap-4 my-4">
      ${cards}
    </div>
    <p class="text-sm font-sans text-slate-200 leading-relaxed m-0">
      <strong class="text-amber-300">${u.householdTitle}</strong> ${d.householdSummary}
    </p>
  </div>
  <div class="space-y-3">
    <div class="text-[11px] font-mono text-emerald-400 font-bold uppercase tracking-wider">${u.forensicTitle}</div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">${proofsHtml}</div>
  </div>
</div>

<h2>${u.auditSectionTitle}</h2>
${auditHtml}

<h2>${u.solutionsSectionTitle}</h2>
<ul>
${solHtml}
</ul>

<div class="my-10 p-6 rounded-2xl bg-slate-900/90 border border-emerald-500/40 not-prose">
  <div class="text-xs font-mono font-bold uppercase tracking-wider text-emerald-400 mb-2">${u.munitionsBadge}</div>
  <p class="text-xs text-slate-300 font-sans mb-4">${u.munitionsTitle}</p>
  <div class="flex flex-wrap gap-3 font-mono text-xs">
    <a href="/transmissions/${d.transmissionSlug}/01_KIT_PRESSE_INVESTIGATION/" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-rose-300 border border-rose-500/30 font-bold">📰 Press Kit →</a>
    <a href="/transmissions/${d.transmissionSlug}/02_BORDEREAU_TRANSMISSION_JUDICIAIRE/" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-emerald-500/30 font-bold">⚖️ Legal Dossier →</a>
    <a href="/transmissions/${d.transmissionSlug}/03_NOTE_INTERPELLATION_PARLEMENTAIRE/" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-cyan-500/30 font-bold">🏛️ Motion / Bill →</a>
  </div>
</div>

<div class="text-center font-serif italic text-amber-400 text-sm mt-8 border-t border-slate-800 pt-6">
  <strong>${u.motto}</strong>
  <br><br>
  <span class="text-xs text-slate-400 font-sans opacity-75">${u.authorSig}</span>
</div>
  `.trim();
}

const dataById: Record<number, Record<Lang6, EnqueteContentData>> = {
  2: {
    it: {
      title: "Il Mito Invertito: Quando la Corsica Sovvenziona lo Stato Francese",
      subtitle: "Commissioni di gestione Bercy (Art. 1641 CGI), IVA turistica e continuità territoriale congelata: 809,15 M€ netti prelevati ogni anno senza ritorno (4.919 € per famiglia).",
      category: "FISCO & BILANCIO PUBBLICO",
      date: "Novembre 2026",
      author: "Cellula Finanziaria L'OCHJU",
      chapeau: "Da mezzo secolo si ripete che la Corsica vive sotto assistenza finanziaria. L'audit dei registri generali del Ministero delle Finanze, della Corte dei Conti e del Senato ribalta il mito: lo Stato preleva 1,45 miliardi di euro di imposte annue contro 1,03 miliardi di spese civili reali, drenando 809,15 milioni di euro netti ogni anno (4.919 € per famiglia) verso Parigi, per un debito sovrano ricalcolato a 2,09 miliardi di euro.",
      imageCaption: "Audit contabile DGFiP / Corte dei Conti — Flussi fiscali netti Corsica-Stato",
      metrics: [
        { label: "Drenaggio Netto Annuo", value: "809,15 M€", sub: "Senza ritorno verso Parigi", colorClass: "text-rose-400" },
        { label: "Costo per Famiglia", value: "4.919 € / anno", sub: "Prelevati in più sul reddito locale", colorClass: "text-amber-400" },
        { label: "Valore Totale Estratto", value: "906 M€ / anno", sub: "Incluso pozzo di carbonio forestale", colorClass: "text-cyan-400" },
        { label: "Debito Sovrano Cumulato", value: "2,09 Mld €", sub: "Calcolo certificato ISO 27037", colorClass: "text-emerald-400" }
      ],
      householdSummary: "Mentre i media nazionali presentano l'isola come un peso fiscale, i registri della DGFiP dimostrano che ogni nucleo familiare corso finanzia lo Stato centrale per 4.919 € netti all'anno tra commissioni su tasse locali (Art. 1641 CGI), IVA estiva, giochi d'azzardo e dotazione di continuità territoriale congelata da 17 anni.",
      proofs: [
        { title: "Registri DGFiP & Corte dei Conti", detail: "1,45 Mld € prelevati vs 1,03 Mld € di spesa civile operativa reale" },
        { title: "Senato & Art. 1641 CGI", detail: "Congelamento continuità territoriale + commissione statale sulle tasse locali" }
      ],
      auditParagraphs: [
        "L'analisi incrociata dei documenti di bilancio del Ministero dell'Economia, dei rapporti senatoriali (r488, r714, r302) e della Banca di Francia dimostra che il saldo fiscale netto della Corsica è strutturalmente favorevole allo Stato centrale.",
        "Oltre alle imposte dirette e all'IVA generata da 3 milioni di turisti, le grandi catene commerciali versano l'imposta sulle società presso le loro sedi parigine, privando l'isola della base fiscale reale."
      ],
      solutionsList: [
        "Pubblicazione integrale del conto territoriale delle imposte e trasferimenti certificato da audit indipendente.",
        "Indicizzazione immediata della dotazione di continuità territoriale e soppressione del prelievo Bercy Art. 1641 CGI.",
        "Localizzazione fiscale dell'imposta sulle società generata dalla grande distribuzione operante sull'isola."
      ],
      transmissionSlug: "enquete-02-mythe-subventions"
    },
    es: {
      title: "El Mito Invertido: Cuando Córcega Subvenciona al Estado Francés",
      subtitle: "Comisiones de gestión fiscal (Art. 1641 CGI), IVA estival y continuidad territorial congelada: 809,15 M€ anuales drenados sin retorno (4.919 € por hogar).",
      category: "FISCALIDAD Y PRESUPUESTO",
      date: "Noviembre 2026",
      author: "Célula Financiera L'OCHJU",
      chapeau: "Durante medio siglo se ha presentado a Córcega como un territorio subsidiado. La auditoría de los libros contables del Ministerio de Hacienda, el Tribunal de Cuentas y el Senado demuestra lo contrario: el Estado recauda 1.450 M€ anuales frente a 1.030 M€ de gasto civil operativo, extrayendo 809,15 M€ netos cada año (4.919 € por hogar) hacia París.",
      imageCaption: "Auditoría contable DGFiP / Tribunal de Cuentas — Flujos fiscales netos",
      metrics: [
        { label: "Drenaje Neto Anual", value: "809,15 M€", sub: "Transferidos sin retorno a París", colorClass: "text-rose-400" },
        { label: "Costo por Hogar", value: "4.919 € / año", sub: "Carga neta sobre familias locales", colorClass: "text-amber-400" },
        { label: "Valor Extraído Total", value: "906 M€ / año", sub: "Incluyendo sumidero de carbono", colorClass: "text-cyan-400" },
        { label: "Deuda Soberana", value: "2,09 Mil M€", sub: "Cálculo certificado ISO 27037", colorClass: "text-emerald-400" }
      ],
      householdSummary: "Los registros oficiales de Hacienda desmienten el discurso oficial: cada familia corsa aporta 4.919 € netos anuales al presupuesto central mediante comisiones estatales sobre tributos locales (Art. 1641 CGI), IVA turístico y una dotación de transporte congelada desde hace 17 años.",
      proofs: [
        { title: "Contabilidad DGFiP / Tribunal de Cuentas", detail: "1.450 M€ recaudados vs 1.030 M€ de gasto operativo civil" },
        { title: "Informes del Senado y Art. 1641 CGI", detail: "Congelación de continuidad territorial y fuga del impuesto de sociedades" }
      ],
      auditParagraphs: [
        "El cruce de datos de la DGFiP, el Banco de Francia y los informes del Senado confirma un flujo neto de salida hacia el tesoro central.",
        "Las grandes superficies transfieren su impuesto de sociedades a sus sedes en la Francia continental, distorsionando las estadísticas oficiales."
      ],
      solutionsList: [
        "Auditoría pública anual obligatoria de todos los flujos fiscales isla-Estado.",
        "Actualización indexada de la dotación de continuidad territorial y eliminación de comisiones del Art. 1641 CGI.",
        "Tributación territorial efectiva sobre los beneficios generados en la isla por grupos continentales."
      ],
      transmissionSlug: "enquete-02-mythe-subventions"
    },
    pt: {
      title: "O Mito Invertido: Quando a Córsega Subsidia o Estado Francês",
      subtitle: "Taxas de gestão Bercy (Art. 1641 CGI), IVA turístico e continuidade territorial congelada: 809,15 M€ anuais drenados sem retorno (4.919 € por família).",
      category: "FISCALIDADE E ORÇAMENTO",
      date: "Novembro 2026",
      author: "Célula Financeira L'OCHJU",
      chapeau: "Durante meio século repetiu-se que a Córsega vive de subsídios. A auditoria às contas oficiais das Finanças, do Tribunal de Contas e do Senado prova o inverso: o Estado arrecada 1,45 mil milhões de euros por ano contra apenas 1,03 mil milhões em despesa civil real, drenando 809,15 milhões de euros líquidos por ano (4.919 € por família).",
      imageCaption: "Auditoria DGFiP / Tribunal de Contas — Fluxos fiscais líquidos Córsega-Estado",
      metrics: [
        { label: "Drenagem Líquida Anual", value: "809,15 M€", sub: "Sem retorno para a ilha", colorClass: "text-rose-400" },
        { label: "Custo por Família", value: "4.919 € / ano", sub: "Retirado do rendimento insular", colorClass: "text-amber-400" },
        { label: "Valor Extraído Total", value: "906 M€ / ano", sub: "Incluindo sumidouro florestal de CO₂", colorClass: "text-cyan-400" },
        { label: "Dívida Soberana", value: "2,09 Mil M€", sub: "Cálculo certificado ISO 27037", colorClass: "text-emerald-400" }
      ],
      householdSummary: "As contas públicas provam que cada família corsa financia o Estado central em 4.919 € líquidos por ano devido a comissões estatais sobre impostos locais (Art. 1641 CGI), IVA do turismo e dotações de transporte congeladas há 17 anos.",
      proofs: [
        { title: "Contas DGFiP e Tribunal de Contas", detail: "1,45 mil M€ cobrados vs 1,03 mil M€ em despesa civil operacional" },
        { title: "Relatórios do Senado e Art. 1641 CGI", detail: "Congelamento da continuidade territorial e evasão fiscal corporativa" }
      ],
      auditParagraphs: [
        "O cruzamento de séries do Banco de França, do INSEE e das finanças públicas mostra um saldo fiscal líquido negativo para a ilha.",
        "As grandes cadeias retalhistas declaram o imposto sobre lucros em Paris apesar de gerarem receitas na Córsega."
      ],
      solutionsList: [
        "Publicação integral do balanço fiscal territorial auditado anualmente.",
        "Revalorização imediata da dotação de continuidade territorial e fim da taxa Bercy (Art. 1641 CGI).",
        "Tributação na ilha dos lucros gerados localmente por grupos nacionais."
      ],
      transmissionSlug: "enquete-02-mythe-subventions"
    },
    ru: {
      title: "Перевернутый миф: как Корсика субсидирует французское государство",
      subtitle: "Комиссии Минфина (ст. 1641 CGI), летний НДС и замороженные транспортные дотации: 809,15 млн € чистого оттока в год (4 919 € с семьи).",
      category: "НАЛОГИ И БЮДЖЕТ",
      date: "Ноябрь 2026",
      author: "Финансовая ячейка L'OCHJU",
      chapeau: "Полвека Корсику изображали дотационным регионом. Судебный аудит счетов Минфина (DGFiP), Счетной палаты и докладов Сената полностью опровергает этот миф: государство собирает на острове 1,45 млрд € налогов в год против 1,03 млрд € реальных гражданских расходов, изымая 809,15 млн € чистого профицита ежегодно (4 919 € на семью).",
      imageCaption: "Аудит DGFiP / Счетной палаты — Чистые налоговые потоки Корсика–Париж",
      metrics: [
        { label: "Чистый отток в год", value: "809,15 млн €", sub: "Без возврата на остров", colorClass: "text-rose-400" },
        { label: "Нагрузка на семью", value: "4 919 € / год", sub: "Чистое изъятие на домохозяйство", colorClass: "text-amber-400" },
        { label: "Полная стоимость", value: "906 млн € / год", sub: "С учетом лесного углеродного стока", colorClass: "text-cyan-400" },
        { label: "Суверенный долг", value: "2,09 млрд €", sub: "Расчет по стандарту ISO 27037", colorClass: "text-emerald-400" }
      ],
      householdSummary: "Официальная бухгалтерия опровергает миф о дотациях: каждая корсиканская семья перечисляет центру на 4 919 € в год больше, чем получает обратно, из-за комиссий на местные налоги (ст. 1641 CGI), туристического НДС и 17-летней заморозки транспортной дотации.",
      proofs: [
        { title: "Реестры DGFiP и Счетная палата", detail: "1,45 млрд € сборов против 1,03 млрд € реальных гражданских расходов" },
        { title: "Доклады Сената и ст. 1641 CGI", detail: "Замороженная дотация непрерывности и отток налога на прибыль сетей" }
      ],
      auditParagraphs: [
        "Сопоставление отчетов Банка Франции, INSEE и парламентских докладов подтверждает системный фискальный дисбаланс.",
        "Крупные торговые сети платят корпоративный налог по месту регистрации головных офисов в Париже, искажая региональный баланс."
      ],
      solutionsList: [
        "Ежегодная публикация независимого фискального баланса между островом и государством.",
        "Немедленная индексация дотации территориальной непрерывности и отмена сбора по ст. 1641 CGI.",
        "Зачисление налога на прибыль розничных сетей по месту фактической выручки на острове."
      ],
      transmissionSlug: "enquete-02-mythe-subventions"
    },
    zh: {
      title: "反转的神话：科西嘉如何反过来补贴法国政府",
      subtitle: "财政部管理抽成 (CGI 第1641条)、旅游增值税与冻结17年的交通拨款：每年净抽走 8.0915 亿欧元（每户 4,919 欧元）。",
      category: "税收与公共财政",
      date: "2026年11月",
      author: "L'OCHJU 金融调查组",
      chapeau: "半个世纪以来，官方叙事将科西嘉描绘成“依赖补贴”的地区。对法国财政部 (DGFiP)、审计法院及参议院报告的司法审计揭穿了这一神话：中央政府每年在岛上征收 14.5 亿欧元税款，实际民用支出仅 10.3 亿欧元，每年净抽走 8.0915 亿欧元（每户 4,919 欧元）。",
      imageCaption: "DGFiP 与审计法院核算图 — 科西嘉与巴黎净财政资金流向",
      metrics: [
        { label: "年度净流出", value: "8.0915 亿€", sub: "无本地财政回流", colorClass: "text-rose-400" },
        { label: "每户年净负担", value: "4,919 € / 年", sub: "平均每个家庭净流失", colorClass: "text-amber-400" },
        { label: "综合抽血总额", value: "9.06 亿€ / 年", sub: "含森林碳汇生态价值", colorClass: "text-cyan-400" },
        { label: "累计主权债权", value: "20.9 亿€", sub: "ISO 27037 审计核算", colorClass: "text-emerald-400" }
      ],
      householdSummary: "官方账簿证明科西嘉并非“靠救济生存”：通过地方税管理费（CGI 第1641条）、夏季游客增值税和冻结17年的交通补贴，每个科西嘉家庭每年实际上向巴黎净贡献 4,919 欧元。",
      proofs: [
        { title: "DGFiP 与法国审计法院账目", detail: "年征税 14.5 亿欧元 vs 实际民用运营支出 10.3 亿欧元" },
        { title: "法国参议院报告与 CGI 第1641条", detail: "地域连续性拨款冻结及零售集团企业税外流" }
      ],
      auditParagraphs: [
        "交叉比对法兰西银行、INSEE 与参议院公开文件，确认岛屿财政长期存在向中央净输血的结构性失衡。",
        "大型连锁零售商在岛上盈利，却将企业所得税缴纳至巴黎总部所在地，人为掩盖了岛屿真实税收贡献。"
      ],
      solutionsList: [
        "每年公开经独立审计的岛屿-中央双向财政收支全账。",
        "立即恢复交通连续性拨款通胀挂钩并废除 CGI 第1641条地方税抽成。",
        "强制大型企业按在科西嘉实际营业额就地缴纳企业所得税。"
      ],
      transmissionSlug: "enquete-02-mythe-subventions"
    },
    ja: {
      title: "逆転した神話：コルシカがフランス国家を補助している実態",
      subtitle: "財務省の徴収手数料（CGI第1641条）・観光消費税・17年凍結の交通交付金：年間8億915万ユーロ（1世帯4,919ユーロ）の純流出。",
      category: "税制・公共財政",
      date: "2026年11月",
      author: "L'OCHJU 財政調査部門",
      chapeau: "半世紀にわたりコルシカは「国からの補助金頼み」と語られてきました。財務省(DGFiP)・会計検査院・上院報告書のフォレンジック監査はその神話を覆します。国家は島から年間14.5億ユーロの税収を徴収する一方、実質的な民生支出は10.3億ユーロにとどまり、毎年8億915万ユーロ（1世帯4,919ユーロ）がパリへ純流出しています。",
      imageCaption: "DGFiP・会計検査院監査 — コルシカと国家間の純財政フロー",
      metrics: [
        { label: "年間純流出額", value: "8億915万€", sub: "島内還元なしの純移転", colorClass: "text-rose-400" },
        { label: "1世帯あたり負担", value: "4,919 € / 年", sub: "各家庭からの純流出額", colorClass: "text-amber-400" },
        { label: "総抽出価値", value: "9億600万€ / 年", sub: "森林炭素吸収源の価値を含む", colorClass: "text-cyan-400" },
        { label: "累計主権債権額", value: "20.9億€", sub: "ISO 27037 準拠算出", colorClass: "text-emerald-400" }
      ],
      householdSummary: "公的帳簿は真逆の事実を示しています。地方税徴収手数料（CGI第1641条）、観光VAT、17年間凍結された離島航路交付金などにより、コルシカの各家庭は毎年4,919ユーロを中央政府へ純拠出しています。",
      proofs: [
        { title: "DGFiP・仏会計検査院公式帳簿", detail: "年間税収14.5億ユーロ 対 実質民生支出10.3億ユーロ" },
        { title: "上院報告書・CGI第1641条", detail: "交通交付金の長期凍結と大手流通の法人税パリ流出" }
      ],
      auditParagraphs: [
        "フランス銀行・INSEE・上院資料のクロス検証により、島外への恒常的な純資金流出が裏付けられました。",
        "大手流通チェーンが島内で上げた利益の法人税をパリ本社所在地で納税するため、統計上の税収が過小計上されています。"
      ],
      solutionsList: [
        "独立監査を経た島・国家間の完全な財政収支バランスシートの年次公開。",
        "交通交付金の物価連動復帰およびCGI第1641条による地方税手数料の撤廃。",
        "島内店舗の売上に応じた法人税の地域内帰属の法制化。"
      ],
      transmissionSlug: "enquete-02-mythe-subventions"
    }
  },
  4: {
    it: {
      title: "Il Castello d'Acqua Saccheggiato: Come Veolia ed EDF Confiscano l'Acqua della Corsica",
      subtitle: "112,9 M€ incassati ogni anno da Veolia (Kyrnolia/SDEC/CEOC), 1,09 miliardi di m³ nelle turbine EDF e 1 litro su 2 perso nei tubi forati.",
      category: "ACQUA & RISORSE",
      date: "Ottobre 2026",
      author: "Cellula d'Investigazione L'OCHJU",
      chapeau: "Chiamata il 'castello d'acqua del Mediterraneo', la Corsica subisce tagli estivi nonostante 8-10 miliardi di m³ di pioggia e neve annui. I registri ufficiali dimostrano che l'85% dell'acqua dolce finisce in mare, EDF turbina 1,09 miliardi di m³ (23 volte l'acqua potabile), 42 milioni di m³ si perdono nelle tubature e il gruppo Veolia incassa 112,9 M€/anno fatturando fino al doppio rispetto alla gestione pubblica di Corte.",
      imageCaption: "Audit SISPEA / BNPE Hub'Eau / Registri INPI — Drenaggio idrico in Corsica",
      metrics: [
        { label: "Incassato da Veolia", value: "112,9 M€ / anno", sub: "SDEC 60,8 M€ + CEOC 51,1 M€ + Kyrnolia 1,1 M€", colorClass: "text-rose-400" },
        { label: "Turbine EDF", value: "1,09 Mld m³", sub: "23× l'intera acqua potabile dell'isola", colorClass: "text-cyan-400" },
        { label: "Perdite di Rete", value: "42 Milioni m³", sub: "Quasi 1 litro su 2 perso nel sottosuolo", colorClass: "text-amber-400" },
        { label: "Sovrapprezzo Bolletta", value: "+250 a +315 €", sub: "In più ogni anno rispetto a Corte pubblica", colorClass: "text-emerald-400" }
      ],
      householdSummary: "Mentre l'azienda pubblica di Corte fattura 343,20 €/anno per 120 m³, le famiglie sotto gestione Veolia (Ajaccio, Porto-Vecchio, Calvi, Propriano) pagano tra 594 € e 660 €/anno, subendo inoltre un sovrapprezzo contrattuale del +15% scoperto dall'audit di Porto-Vecchio di ottobre 2026.",
      proofs: [
        { title: "Conti Ufficiali Veolia 2025 (INPI)", detail: "112 941 976 € di ricavi tramite SDEC (514709211), CEOC (817503576) e Kyrnolia (808578181)" },
        { title: "Audit Porto-Vecchio (Ottobre 2026)", detail: "Formula tariffaria viziata (+15% alle famiglie) e 42 Mm³ di perdite SISPEA" }
      ],
      auditParagraphs: [
        "Dietro il nome locale 'Kyrnolia' (0 dipendenti diretti) operano le casse centrali di Veolia che trasferiscono margini verso Aubervilliers tramite il GIE Veolia Eau France (SIREN 808 297 980).",
        "Nel frattempo, la legge 2026-554 ha bloccato le grandi dighe (Calacuccia, Tolla, Sampolo, Rizzanese) a favore di EDF fino al 2096 rifiutando il pompaggio a circuito chiuso (STEP)."
      ],
      solutionsList: [
        "Creazione della Regia Pubblica Unica dell'Acqua Insulare (RSEI) sul modello virtuoso di Corte e Bastia.",
        "Tariffa equa a scaglioni: primi 30 m³/anno GRATUITI (acqua vitale), prezzo di costo (2,80 €/m³) alle famiglie e +300% sulle piscine di lusso.",
        "Piano ingegneristico +175 milioni m³/anno in 8 anni: riparazione perdite (85% rendimento), dighe sotterranee alluvionali, STEP e captazione sorgenti sottomarine."
      ],
      transmissionSlug: "enquete-04-marchandisation-eau"
    },
    es: {
      title: "El Castillo de Agua Saqueado: Cómo Veolia y EDF Confiscan el Agua de Córcega",
      subtitle: "112,9 M€ anuales cobrados por Veolia, 1.090 millones de m³ en turbinas de EDF y 1 de cada 2 litros perdidos en tuberías rotas.",
      category: "AGUA Y RECURSOS",
      date: "Octubre 2026",
      author: "Célula de Investigación L'OCHJU",
      chapeau: "A pesar de recibir entre 8.000 y 10.000 millones de m³ de lluvia y nieve al año, Córcega sufre cortes estivales porque el 85% del agua va al mar, EDF turbina 1.090 millones de m³, se fugan 42 millones de m³ en tuberías deterioradas y Veolia cobra 112,9 M€/año facturando el doble que la gestión pública de Corte.",
      imageCaption: "Auditoría SISPEA / BNPE Hub'Eau / Registros INPI — Gestión del agua en Córcega",
      metrics: [
        { label: "Cobrado por Veolia", value: "112,9 M€ / año", sub: "SDEC 60,8 M€ + CEOC 51,1 M€ + Kyrnolia 1,1 M€", colorClass: "text-rose-400" },
        { label: "Turbinas de EDF", value: "1,09 Mil M m³", sub: "23× toda el agua potable de la isla", colorClass: "text-cyan-400" },
        { label: "Pérdidas en Red", value: "42 Millones m³", sub: "Casi la mitad perdida bajo tierra", colorClass: "text-amber-400" },
        { label: "Sobrecoste Familiar", value: "+250 a +315 €", sub: "Extra al año frente a Corte pública", colorClass: "text-emerald-400" }
      ],
      householdSummary: "En Corte (gestión pública), una familia paga 343,20 €/año por 120 m³. Con Veolia (Ajaccio, Porto-Vecchio, Calvi, Propriano), la misma factura sube a 594–660 €/año, agravada por un sobrecargo indebido del +15% detectado en la auditoría de Porto-Vecchio en octubre de 2026.",
      proofs: [
        { title: "Cuentas Oficiales Veolia 2025 (INPI)", detail: "112.941.976 € recaudados vía SDEC, CEOC y Kyrnolia hacia GIE Aubervilliers" },
        { title: "Auditoría Porto-Vecchio (Oct. 2026)", detail: "Fórmula tarifaria sesgada (+15% a familias) y 42 Mm³ de fugas SISPEA" }
      ],
      auditParagraphs: [
        "La marca local 'Kyrnolia' oculta un entramado de tres sociedades dirigidas por el mismo apoderado de Veolia que desvía beneficios hacia París.",
        "La Ley 2026-554 bloqueó los cuatro grandes embalses insulares bajo control exclusivo de EDF hasta 2096."
      ],
      solutionsList: [
        "Creación de la Empresa Pública Única del Agua de Córcega (RSEI) siguiendo el modelo de Corte y Bastia.",
        "Tarifa social progresiva: primeros 30 m³/año GRATUITOS, tarifa de coste para hogares y recargo del +300% a piscinas privadas.",
        "Plan técnico +175 millones m³/año: reparación de fugas hasta el 85% de rendimiento, presas subterráneas aluviales y captación submarina."
      ],
      transmissionSlug: "enquete-04-marchandisation-eau"
    },
    pt: {
      title: "O Castelo de Água Pilhado: Como a Veolia e a EDF Confiscam a Água da Córsega",
      subtitle: "112,9 M€ anuais cobrados pela Veolia, 1,09 mil milhões de m³ nas turbinas da EDF e 1 em cada 2 litros perdidos em condutas rotas.",
      category: "ÁGUA E RECURSOS",
      date: "Outubro 2026",
      author: "Célula de Investigação L'OCHJU",
      chapeau: "Embora receba 8 a 10 mil milhões de m³ de chuva e neve por ano, a Córsega sofre restrições no verão porque 85% escorre para o mar, a EDF turbina 1,09 mil milhões de m³, 42 milhões de m³ perdem-se em fugas e a Veolia cobra 112,9 M€/ano faturando o dobro da gestão pública de Corte.",
      imageCaption: "Auditoria SISPEA / BNPE Hub'Eau / Registos INPI — Água na Córsega",
      metrics: [
        { label: "Recebido pela Veolia", value: "112,9 M€ / ano", sub: "SDEC 60,8 M€ + CEOC 51,1 M€ + Kyrnolia 1,1 M€", colorClass: "text-rose-400" },
        { label: "Turbinas da EDF", value: "1,09 Mil M m³", sub: "23× toda a água potável da ilha", colorClass: "text-cyan-400" },
        { label: "Perdas na Rede", value: "42 Milhões m³", sub: "Quase metade desperdiçada no subsolo", colorClass: "text-amber-400" },
        { label: "Sobretaxa Familiar", value: "+250 a +315 €", sub: "Mais caro por ano face a Corte pública", colorClass: "text-emerald-400" }
      ],
      householdSummary: "Em Corte (gestão pública), uma família paga 343,20 €/ano por 120 m³. Sob concessão da Veolia (Ajaccio, Porto-Vecchio, Calvi, Propriano), a fatura sobe para 594–660 €/ano, com uma sobretaxa contratual de +15% comprovada pela auditoria de Porto-Vecchio de outubro de 2026.",
      proofs: [
        { title: "Contas Oficiais Veolia 2025 (INPI)", detail: "112.941.976 € via SDEC, CEOC e Kyrnolia drenados para Aubervilliers" },
        { title: "Auditoria Porto-Vecchio (Out. 2026)", detail: "Fórmula de preços viciada (+15% às famílias) e 42 Mm³ de fugas SISPEA" }
      ],
      auditParagraphs: [
        "Sob o nome local 'Kyrnolia' esconde-se a estrutura da Veolia que remete lucros através da central de compras GIE Veolia Eau France.",
        "Entretanto, a Lei 2026-554 entregou o controlo das quatro grandes barragens à EDF até 2096."
      ],
      solutionsList: [
        "Criação da Gestão Pública Única da Água da Córsega (RSEI) com transferência integral dos trabalhadores.",
        "Tarifa justa: 30 m³/ano gratuitos (água vital), preço de custo familiar e +300% para piscinas de luxo.",
        "Plano +175 milhões m³/ano em 8 anos: reparação de redes (85%), barragens aluviais subterrâneas e bombagem STEP."
      ],
      transmissionSlug: "enquete-04-marchandisation-eau"
    },
    ru: {
      title: "Разграбленная водонапорная башня: как Veolia и EDF конфискуют воду Корсики",
      subtitle: "112,9 млн € в год собирает Veolia, 1,09 млрд м³ уходят в турбины EDF и половина питьевой воды теряется в дырявых трубах.",
      category: "ВОДА И РЕСУРСЫ",
      date: "Октябрь 2026",
      author: "Исследовательская ячейка L'OCHJU",
      chapeau: "Несмотря на 8–10 млрд м³ осадков в год, на Корсике каждое лето вводят запреты на воду: 85% уходит в море, турбины EDF спускают 1,09 млрд м³, 42 млн м³ утекают в землю, а концерн Veolia собирает 112,9 млн € в год по тарифам вдвое выше муниципального водоканала Корте.",
      imageCaption: "Аудит SISPEA / BNPE Hub'Eau / Реестры INPI — Водоснабжение Корсики",
      metrics: [
        { label: "Сборы Veolia", value: "112,9 млн € / год", sub: "SDEC 60,8 + CEOC 51,1 + Kyrnolia 1,1 млн €", colorClass: "text-rose-400" },
        { label: "Турбины EDF", value: "1,09 млрд м³", sub: "В 23 раза больше всей питьевой воды", colorClass: "text-cyan-400" },
        { label: "Утечки в сетях", value: "42 млн м³", sub: "До 50% потерь в сельских трубах", colorClass: "text-amber-400" },
        { label: "Переплата семьи", value: "+250–315 € / год", sub: "Дороже, чем в муниципальном Корте", colorClass: "text-emerald-400" }
      ],
      householdSummary: "Муниципальная служба Корте берет 343,20 €/год за 120 м³, тогда как под управлением Veolia семьи платят 594–660 €/год, включая переплату +15% из-за искаженной формулы, вскрытой аудитом Порто-Веккьо в октябре 2026 года.",
      proofs: [
        { title: "Балансы Veolia 2025 (INPI)", detail: "112 941 976 € выручки через SDEC, CEOC и Kyrnolia с выводом средств в Париж" },
        { title: "Аудит Порто-Веккьо (Окт. 2026)", detail: "Незаконная наценка +15% и утечки 42 млн м³ по базе SISPEA" }
      ],
      auditParagraphs: [
        "Под местной вывеской Kyrnolia (0 сотрудников) скрывается трехступенчатая схема Veolia, выводящая прибыль в Обервилье через GIE Veolia Eau France.",
        "Закон № 2026-554 закрепил крупнейшие плотины острова за EDF до 2096 года, блокируя замкнутое гидроаккумулирование STEP."
      ],
      solutionsList: [
        "Создание Единой общественной водной службы Корсики (RSEI) по образцу Корте и Бастии.",
        "Социальный тариф: 30 м³/год бесплатно, себестоимость для жителей и +300% для элитных бассейнов.",
        "Инженерный план +175 млн м³/год: ремонт труб до 85% КПД, подземные аллювиальные запруды и замкнутый цикл ГЭС."
      ],
      transmissionSlug: "enquete-04-marchandisation-eau"
    },
    zh: {
      title: "被掠夺的水塔：威立雅与法国电力如何垄断科西嘉水资源",
      subtitle: "威立雅年收 1.129 亿欧元、EDF 涡轮吞噬 10.9 亿立方米淡水、近一半饮用水渗漏地下：人为制造水荒的真相。",
      category: "水资源与公共事业",
      date: "2026年10月",
      author: "L'OCHJU 调查组",
      chapeau: "科西嘉每年降水量高达 80 至 100 亿立方米，却年年夏季停水限水：85% 雨水直排入海，EDF 发电消耗 10.9 亿立方米（为全岛饮用水的 23 倍），破旧管道渗漏 4200 万立方米，威立雅年收 1.129 亿欧元，水费比科尔泰市营水厂贵一倍。",
      imageCaption: "SISPEA / BNPE / INPI 审计档案 — 科西嘉水资源与水费对比",
      metrics: [
        { label: "威立雅年收入", value: "1.129 亿€ / 年", sub: "SDEC 6080万 + CEOC 5110万 + Kyrnolia", colorClass: "text-rose-400" },
        { label: "EDF 水电消耗", value: "10.9 亿 m³", sub: "全岛饮用水总量的 23 倍", colorClass: "text-cyan-400" },
        { label: "管网渗漏浪费", value: "4200 万 m³", sub: "农村管网漏损率接近 50%", colorClass: "text-amber-400" },
        { label: "家庭额外多付", value: "+250~315 €", sub: "每年比科尔泰市营水厂多付费用", colorClass: "text-emerald-400" }
      ],
      householdSummary: "科尔泰市营水厂每户年水费仅 343.20 欧元（120 m³），而威立雅特许经营区高达 594 至 660 欧元；2026年10月韦基奥港独立审计还查明威立雅通过缺失工资指数条款向居民多收了 15% 水费。",
      proofs: [
        { title: "威立雅 2025 官方财报 (INPI)", detail: "三家子公司合计营收 112,941,976 欧元，利润经巴黎总社抽走" },
        { title: "韦基奥港 2026年10月审计", detail: "证实水价公式多收 +15% 且全岛年渗漏 4200 万立方米" }
      ],
      auditParagraphs: [
        "看似本土企业的“Kyrnolia”实际零雇员，只是威立雅（SDEC 与 CEOC）掩护每年向巴黎近郊总部转移资金的外壳。",
        "2026年6月通过的 2026-554 号法律将四大公有水库锁定归 EDF 独家控制至 2096 年，拒绝闭环抽水蓄能改造。"
      ],
      solutionsList: [
        "参照科尔泰与巴斯蒂亚成功经验，成立科西嘉统一公共水务局 (RSEI)，依法保留全部一线技术工人。",
        "实行阶梯公平水价：前 30 m³/年生命用水免费，家庭按成本价计费，豪华泳池夏季加征 +300%。",
        "8年+1.75亿 m³工程计划：修复管网至 85% 利用率、河床地下蓄水坝、闭环抽水蓄能及海底淡水泉收集。"
      ],
      transmissionSlug: "enquete-04-marchandisation-eau"
    },
    ja: {
      title: "略奪された貯水塔：ヴェオリアとEDFによるコルシカ水資源の独占",
      subtitle: "ヴェオリアの年間収益1億1,290万ユーロ、EDFタービンが消費する10.9億m³、漏水で失われる4,200万m³の全貌。",
      category: "水資源・公共インフラ",
      date: "2026年10月",
      author: "L'OCHJU 調査部門",
      chapeau: "年間80〜100億m³もの降水がありながら毎夏断水が起きる理由は人為的なものです。85%が貯水されず海へ流れ、EDFの発電が10.9億m³（全飲料水の23倍）を消費し、老朽管から4,200万m³が漏水、民間大手ヴェオリアが公営コルテの倍額で年間1億1,290万ユーロを徴収しています。",
      imageCaption: "SISPEA / BNPE / INPI 公的監査 — コルシカの水利権と水道料金",
      metrics: [
        { label: "ヴェオリア年間売上", value: "1億1,290万€", sub: "SDEC 60.8M + CEOC 51.1M + Kyrnolia", colorClass: "text-rose-400" },
        { label: "EDF発電取水量", value: "10.9億 m³", sub: "島内全飲料水の23倍", colorClass: "text-cyan-400" },
        { label: "水道管漏水量", value: "4,200万 m³", sub: "農村部では約半数が地下へ流出", colorClass: "text-amber-400" },
        { label: "家庭の過剰負担", value: "+250〜315 €", sub: "公営コルテ水道との年間差額", colorClass: "text-emerald-400" }
      ],
      householdSummary: "公営水道コルテの年間料金343.20ユーロ（120m³）に対し、ヴェオリア委託地域では594〜660ユーロに達します。さらに2026年10月のポルト＝ヴェッキオ独立監査で、契約算定式の不備による+15%の過剰請求が発覚しました。",
      proofs: [
        { title: "ヴェオリア2025年公式決算 (INPI)", detail: "3子会社計 112,941,976ユーロの売上とパリ本社GIEへの資金還流" },
        { title: "ポルト＝ヴェッキオ監査 (2026年10月)", detail: "+15%の不当上乗せ請求およびSISPEA公式漏水量4,200万m³" }
      ],
      auditParagraphs: [
        "地元企業風の「Kyrnolia」は従業員ゼロの窓口会社であり、実態は同一代理人が統括するヴェオリアの3層集金装置です。",
        "2026年6月の法律第2026-554号は島の主要4ダムを2096年までEDFの独占管理下に置き、揚水式閉ループ(STEP)化を拒否しています。"
      ],
      solutionsList: [
        "コルテ・バスティア型の完全公営化を全島へ拡大し、労働法L.1224-1条で現場職員の雇用を100%継承した統一公営水道局(RSEI)を設立。",
        "段階的公正料金の導入：生活最低水30m³/年を無料化、家庭は原価水準、豪華プール等には夏季+300%課税。",
        "8年間・年+1.75億m³確保計画：漏水修復(有収率85%)、地下河川堰、STEP循環、海底湧水回収を実施。"
      ],
      transmissionSlug: "enquete-04-marchandisation-eau"
    }
  },
  7: {
    it: {
      title: "Il Catasto Minerario Segreto e il Piano IRM: Le Ricchezze Nascoste del Sottosuolo",
      subtitle: "Radiografia dei permessi di esplorazione BRGM: rame, antimonio, terre rare e litio sottratti alla consultazione comunale.",
      category: "RISORSE MINERARIE & TRANSIZIONE",
      date: "Agosto 2026",
      author: "Cellula Geologica L'OCHJU",
      chapeau: "Dipinta per decenni come priva di risorse geologiche strategiche, la Corsica ospita giacimenti critici (antimonio, rame, litio, terre rare). L'analisi dei perimetri BRGM e del Codice Minerario rivela campagne di prospezione statali condotte senza consenso dei comuni né tutela PADDUC.",
      imageCaption: "Cartografia mineraria BRGM / Codice Minerario — Perimetri di prospezione in Corsica",
      metrics: [
        { label: "Minerali Strategici", value: "4 Classi Critiche", sub: "Antimonio, Rame, Terre Rare, Litio", colorClass: "text-amber-400" },
        { label: "Ritorno Fiscale Locale", value: "0,00 €", sub: "Canoni statali senza royalty comunali", colorClass: "text-rose-400" },
        { label: "Tutela PADDUC", value: "Aggirata", sub: "Titoli minerari opponibili ai piani locali", colorClass: "text-cyan-400" },
        { label: "Trasparenza Cittadina", value: "Sigillata", sub: "Dati grezzi BRGM pubblici in accesso aperto", colorClass: "text-emerald-400" }
      ],
      householdSummary: "Mentre il Codice Minerario riformato consente allo Stato di rilanciare l'inventario strategico (IRM) su montagne e falde acquifere corse, i comuni e i residenti sono tenuti all'oscuro delle campagne di campionamento e dei rischi ambientali di metalli pesanti e amianto naturale.",
      proofs: [
        { title: "Archivi Geologici BRGM & Decreto 2025-851", detail: "Rilancio inventario nazionale risorse critiche su aree schisto-granitiche corse" },
        { title: "Sentenza CAA Versailles 22VE02499", detail: "Precedente giurisprudenziale sui permessi estrattivi e obblighi ambientali" }
      ],
      auditParagraphs: [
        "L'incrocio delle coordinate geologiche WGS84 dei vecchi giacimenti di antimonio (Capo Corso) e rame con i nuovi perimetri d'indagine IRM mostra una ripresa sistematica della mappatura strategica.",
        "Senza modifica costituzionale o blocco giuridico locale, lo Stato mantiene la proprietà sovrana del sottosuolo ai sensi del Codice Minerario."
      ],
      solutionsList: [
        "Diritto di veto vincolante dell'Assemblea di Corsica e dei consigli comunali su qualsiasi permesso di prospezione o concessione.",
        "Studio d'impatto idrologico pubblico indipendente obbligatorio prima di ogni sondaggio su falde montane.",
        "Pubblicazione integrale dei dati geochimici BRGM sulla mappa civica dei 360 comuni."
      ],
      transmissionSlug: "enquete-07-cadastre-minier"
    },
    es: {
      title: "El Catastro Minero Secreto y el Plan IRM: Las Riquezas Ocultas del Subsuelo",
      subtitle: "Radiografía de los permisos de prospección del BRGM: cobre, antimonio, tierras raras y materiales críticos sin consulta municipal.",
      category: "MINERÍA Y TRANSICIÓN ENERGÉTICA",
      date: "Agosto 2026",
      author: "Célula Geológica L'OCHJU",
      chapeau: "Presentada históricamente como carente de riqueza mineral, Córcega alberga yacimientos críticos (antimonio, cobre, tierras raras). Una investigación sobre las campañas de exploración del Estado y las concesiones otorgadas al margen de la autonomía municipal del PADDUC.",
      imageCaption: "Cartografía minera BRGM / Código Minero — Perímetros en Córcega",
      metrics: [
        { label: "Metales Críticos", value: "4 Familias", sub: "Antimonio, Cobre, Tierras Raras, Litio", colorClass: "text-amber-400" },
        { label: "Regalía Municipal", value: "0,00 €", sub: "Exclusividad estatal del subsuelo", colorClass: "text-rose-400" },
        { label: "Protección PADDUC", value: "Vulnerada", sub: "Prioridad jurídica de títulos mineros", colorClass: "text-cyan-400" },
        { label: "Acceso Ciudadano", value: "Certificado", sub: "Coordenadas WGS84 verificadas", colorClass: "text-emerald-400" }
      ],
      householdSummary: "La reforma del Código Minero (Decreto 2025-851) permite al Estado francés inventariar y asignar permisos sobre el subsuelo corso sin consulta vinculante a los municipios ni garantías contra la contaminación hídrica.",
      proofs: [
        { title: "Registros BRGM y Decreto 2025-851", detail: "Reactivación del inventario estratégico de recursos minerales críticos" },
        { title: "Sentencia CAA Versalles 22VE02499", detail: "Jurisprudencia aplicable sobre permisos y control ambiental" }
      ],
      auditParagraphs: [
        "El cruce entre archivos históricos mineros y los programas de exploración moderna confirma el interés estratégico por los macizos de Córcega.",
        "La normativa actual otorga a París el control unilateral del subsuelo por encima de la planificación territorial local."
      ],
      solutionsList: [
        "Derecho de veto vinculante de la Asamblea de Córcega y los ayuntamientos ante todo permiso minero.",
        "Moratoria inmediata en cuencas hidrográficas vulnerables y zonas con presencia natural de amianto.",
        "Transparencia total en línea de cada campaña geológica en el mapa de los 360 municipios."
      ],
      transmissionSlug: "enquete-07-cadastre-minier"
    },
    pt: {
      title: "O Cadastro Mineiro Secreto e o Plano IRM: As Riquezas Ocultas do Subsolo",
      subtitle: "Radiografia das licenças de prospeção BRGM: cobre, antimónio, terras raras e minerais críticos sem consulta municipal.",
      category: "RECURSOS MINEIROS E TRANSIÇÃO",
      date: "Agosto 2026",
      author: "Célula Geológica L'OCHJU",
      chapeau: "Retratada durante décadas como pobre em recursos geológicos, a Córsega possui depósitos estratégicos (antimónio, cobre, terras raras). Investigação às campanhas estatais de prospeção e concessões emitidas à revelia da autonomia local e do PADDUC.",
      imageCaption: "Cartografia mineira BRGM — Perímetros de exploração na Córsega",
      metrics: [
        { label: "Minerais Críticos", value: "4 Classes", sub: "Antimónio, Cobre, Terras Raras, Lítio", colorClass: "text-amber-400" },
        { label: "Retorno Municipal", value: "0,00 €", sub: "Tutela central exclusiva do subsolo", colorClass: "text-rose-400" },
        { label: "Proteção PADDUC", value: "Contornada", sub: "Precedência jurídica de títulos estatais", colorClass: "text-cyan-400" },
        { label: "Transparência", value: "Selada", sub: "Dados geológicos públicos abertos", colorClass: "text-emerald-400" }
      ],
      householdSummary: "O Código Mineiro reformado permite ao Estado inventariar e licenciar a exploração do subsolo corso sem autorização vinculativa das populações locais nem salvaguardas ambientais independentes.",
      proofs: [
        { title: "Fichas BRGM e Decreto 2025-851", detail: "Reabertura do inventário de matérias-primas críticas" },
        { title: "Acórdão CAA Versailles 22VE02499", detail: "Jurisprudência sobre licenças extrativas e obrigações ambientais" }
      ],
      auditParagraphs: [
        "O cruzamento de levantamentos geológicos históricos com o plano IRM revela o regresso da prospeção de metais críticos na ilha.",
        "As autarquias locais ficam desprovidas de veto perante licenças concedidas pelo governo central."
      ],
      solutionsList: [
        "Direito de veto vinculativo da Assembleia da Córsega e das câmaras municipais sobre qualquer licença mineira.",
        "Avaliação hidrológica independente obrigatória antes de qualquer perfuração.",
        "Publicação aberta de todos os perímetros no radar cartográfico dos 360 municípios."
      ],
      transmissionSlug: "enquete-07-cadastre-minier"
    },
    ru: {
      title: "Секретный горный кадастр и план IRM: скрытые богатства недр Корсики",
      subtitle: "Рентген разрешений на геологоразведку BRGM: медь, сурьма, редкоземельные элементы в обход муниципалитетов.",
      category: "НЕДРА И РЕСУРСЫ",
      date: "Август 2026",
      author: "Геологическая ячейка L'OCHJU",
      chapeau: "Вопреки официальному тезису об отсутствии полезных ископаемых, недра Корсики содержат критические минералы (сурьму, медь, редкоземельные металлы). Расследование скрытых государственных программ разведки в обход полномочий местных общин и плана PADDUC.",
      imageCaption: "Горная картография BRGM — Участки разведки на Корсике",
      metrics: [
        { label: "Критические металлы", value: "4 группы", sub: "Сурьма, медь, редкоземы, литий", colorClass: "text-amber-400" },
        { label: "Доход общин", value: "0,00 €", sub: "Исключительная монополия центра", colorClass: "text-rose-400" },
        { label: "Защита PADDUC", value: "Обойдена", sub: "Приоритет горного кодекса над планом", colorClass: "text-cyan-400" },
        { label: "Открытые данные", value: "Заверено", sub: "Координаты WGS84 опубликованы", colorClass: "text-emerald-400" }
      ],
      householdSummary: "Обновленный Горный кодекс (Декрет 2025-851) дает Парижу право проводить инвентаризацию и выдавать разрешения на разведку без права вето со стороны мэрий и жителей горных долин.",
      proofs: [
        { title: "Данные BRGM и Декрет 2025-851", detail: "Возобновление национального учета стратегических минералов" },
        { title: "Решение суда Версаля 22VE02499", detail: "Судебная практика по экологическому контролю добычи" }
      ],
      auditParagraphs: [
        "Наложение исторических горных архивов на план IRM показывает возобновление интереса к рудным зонам Кап-Корса и центральной Корсики.",
        "Действующее законодательство оставляет недра в исключительной собственности центрального правительства."
      ],
      solutionsList: [
        "Введение обязательного права вето Ассамблеи Корсики и муниципальных советов на любые буровые работы.",
        "Независимая гидрологическая экспертиза защиты горных водоносных горизонтов.",
        "Публикация всех геохимических данных BRGM на карте 360 коммун."
      ],
      transmissionSlug: "enquete-07-cadastre-minier"
    },
    zh: {
      title: "秘密矿产档案与 IRM 计划：科西嘉被掩盖的地下矿藏",
      subtitle: "法国地质矿产局 (BRGM) 勘探区透视：铜、锑、稀土与关键矿产如何绕开地方市镇自治权。",
      category: "矿产资源与能源转型",
      date: "2026年8月",
      author: "L'OCHJU 地质调查组",
      chapeau: "长期以来外界被告知科西嘉缺乏地质矿产，但实证档案揭示岛屿花岗岩与片岩基底蕴含关键矿藏（锑、铜、稀土）。本调查揭露中央政府无视地方土地规划 (PADDUC) 推进矿产普查的秘密布局。",
      imageCaption: "BRGM 矿产勘查地图 — 科西嘉重点区块分布",
      metrics: [
        { label: "关键战略矿种", value: "4 大类", sub: "锑、铜、稀土元素、锂资源", colorClass: "text-amber-400" },
        { label: "地方矿税留存", value: "0.00 €", sub: "地下矿权完全收归中央", colorClass: "text-rose-400" },
        { label: "PADDUC 保护", value: "被架空", sub: "矿法权限凌驾地方空间规划", colorClass: "text-cyan-400" },
        { label: "公民数据公开", value: "已封存", sub: "WGS84 坐标全量核验公开", colorClass: "text-emerald-400" }
      ],
      householdSummary: "2025年法国《矿业法》改革（2025-851号令）允许中央直接启动战略资源普查 (IRM)，而地方市镇对水源安全及天然石棉粉尘风险却没有否决权。",
      proofs: [
        { title: "BRGM 地质档案与 2025-851 号令", detail: "重启全岛关键原材料战略普查区块" },
        { title: "凡尔赛行政上诉法院 22VE02499 判决", detail: "矿产勘探许可与环境评估义务司法先例" }
      ],
      auditParagraphs: [
        "比对历史锑矿档案（科西嘉角）与最新 IRM 计划边界，确认中央正系统性重绘岛屿地下资源版图。",
        "现行法律下地下资源收益归国家所有，生态代价却留给当地村镇。"
      ],
      solutionsList: [
        "赋予科西嘉议会及受影响市镇对一切矿产勘探与开采许可的强制否决权。",
        "在任何钻探前强制执行独立水文与生态影响公开听证。",
        "在 360 市镇地理信息平台全量透明公开所有 BRGM 地球化学坐标。"
      ],
      transmissionSlug: "enquete-07-cadastre-minier"
    },
    ja: {
      title: "秘密の鉱業台帳とIRM計画：隠されたコルシカの地下資源",
      subtitle: "フランス地質鉱山局(BRGM)探査区画の徹底解析：自治体の同意なく進む銅・アンチモン・レアアース調査。",
      category: "鉱物資源・エネルギー移行",
      date: "2026年8月",
      author: "L'OCHJU 地質調査部門",
      chapeau: "資源に乏しいとされてきたコルシカの花崗岩・片岩地帯には、アンチモン・銅・レアアース等の重要鉱物が賦存しています。自治体の土地計画(PADDUC)を無視して進められる国家の鉱物探査と鉱業法上の特権を暴きます。",
      imageCaption: "BRGM 鉱区地図 — コルシカ島内の探査対象区域",
      metrics: [
        { label: "重要戦略鉱物", value: "4 種別", sub: "アンチモン・銅・レアアース・リチウム", colorClass: "text-amber-400" },
        { label: "自治体への還元", value: "0.00 €", sub: "地下資源権は中央政府が独占", colorClass: "text-rose-400" },
        { label: "PADDUC保護", value: "形骸化", sub: "鉱業法が地域土地計画に優越", colorClass: "text-cyan-400" },
        { label: "市民データ公開", value: "封緘済み", sub: "WGS84 座標を完全公開", colorClass: "text-emerald-400" }
      ],
      householdSummary: "2025年鉱業法改正(政令2025-851)により、国は自治体や住民の拒否権なしに重要鉱物インベントリ(IRM)および試掘調査を進められる仕組みとなっています。",
      proofs: [
        { title: "BRGM 記録・政令 2025-851", detail: "重要原材料の戦略的資源調査計画" },
        { title: "ヴェルサイユ控訴院判決 22VE02499", detail: "鉱業許可と環境保全義務に関する重要判例" }
      ],
      auditParagraphs: [
        "歴史的鉱山記録と現代のIRM探査計画を照合すると、カップ・コルスや山岳地帯の戦略的鉱区への再評価が確認されます。",
        "現行制度では試掘段階から住民の合意形成プロセスが法的に欠落しています。"
      ],
      solutionsList: [
        "コルシカ議会および関係自治体に対し、あらゆる探査・採掘許可への法的拒否権を付与。",
        "水源帯および自然石綿地域での掘削前における独立水文影響評価の義務化。",
        "360自治体GISマップ上でのBRGM地質・鉱区データの完全公開。"
      ],
      transmissionSlug: "enquete-07-cadastre-minier"
    }
  },
  11: {
    it: {
      title: "Il Santuario Confiscato: 2.842 Ettari Militari e il Sistema delle Rendite Statali (50 M€/anno)",
      subtitle: "Base aerea 126 Solenzara, Aspretto, Camp Raffalli e Diane: trattato ONU n° 38665, appalto da 91 M€ e 19,75 M€ di tasse non pagate ai comuni.",
      category: "DIFESA & TERRITORIO",
      date: "Ottobre 2026",
      author: "Cellula d'Investigazione L'OCHJU",
      chapeau: "Un quarto delle pianure costiere della Corsica è chiuso dietro filo spinato militare. I documenti ufficiali — dal trattato bilaterale USA-Francia depositato all'ONU all'appalto da 91 M€ per le piste e alle 2.848 particelle catastali — dimostrano che lo Stato incassa fino a 50 M€/anno affittando il cielo e le basi alla NATO mentre rifiuta di pagare 19,75 M€ di imposte fondiarie dovute ai comuni corsi.",
      imageCaption: "Audit catastale DGFiP / Trattato ONU n° 38665 — 2.842 ettari militari in Corsica",
      metrics: [
        { label: "Terre Bloccate", value: "2.842 ettari", sub: "24,8% delle pianure costiere dell'isola", colorClass: "text-rose-400" },
        { label: "Terreni Agricoli Incolti", value: "327 ettari", sub: "A Ventiseri = 35 aziende agricole bloccate", colorClass: "text-amber-400" },
        { label: "Incassato da Parigi", value: "50 M€ / anno", sub: "Affitto poligono NATO e carburante esentasse", colorClass: "text-emerald-400" },
        { label: "Tasse Dovute ai Comuni", value: "19,75 M€", sub: "Arretrati esigibili su 5 anni (Art. 1382 CGI)", colorClass: "text-cyan-400" }
      ],
      householdSummary: "Le basi militari non pagano 1 centesimo di tassa fondiaria ai comuni sostenendo di essere improduttive. Ma lo Stato le sfrutta commercialmente (ore di volo NATO a 4.500–7.800 €, rivendita di cherosene, antenne 4G/5G): secondo il Consiglio di Stato l'esenzione fiscale decade e 7 comuni hanno diritto a 19,75 M€ di arretrati.",
      proofs: [
        { title: "Trattato ONU Vol. 2190 n° 38665 & BOAMP 440653", detail: "Accordo USAFE Solenzara/Diane e appalto piste da 91 M€" },
        { title: "Rapporto MRAe 2025-DKCOR3 & Catasto DGFiP", detail: "41 milioni litri d'acqua prelevati/anno, 28 M€ inquinamento PFAS e 327 ha incolti" }
      ],
      auditParagraphs: [
        "La Base Aerea 126 di Solenzara non ospita alcuno squadrone francese permanente: opera come poligono commerciale NATO e deposito munizioni statunitense.",
        "I 137 appalti militari e gli affitti per telecomunicazioni fruttano fino a 53,1 M€/anno allo Stato, mentre la base pompa 41.200 m³ dal fiume Travo anche durante i divieti agricoli."
      ],
      solutionsList: [
        "Applicazione immediata dell'Art. 1382 CGI e richiesta esecutiva di 19,75 M€ di imposte fondiarie arretrate da parte dei 7 comuni.",
        "Restituzione gratuita dei 327 ettari agricoli inutilizzati di Ventiseri per insediare 35 giovani agricoltori (1.800 t/anno di cibo).",
        "Trasferimento del sito d'Aspretto alla città di Ajaccio (Delibere 14/207 e 21/017) e bonifica integrale dei PFAS a spese dello Stato."
      ],
      transmissionSlug: "enquete-11-emprise-militaire"
    },
    es: {
      title: "El Santuario Confiscado: 2.842 Hectáreas Militares y Rentas Estatales de 50 M€/año",
      subtitle: "BA 126 Solenzara, Aspretto, Camp Raffalli y Diane: tratado ONU n.º 38665, contrato de 91 M€ y 19,75 M€ de impuestos impagados a los municipios.",
      category: "DEFENSA Y TERRITORIO",
      date: "Octubre 2026",
      author: "Célula de Investigación L'OCHJU",
      chapeau: "Una cuarta parte de las llanuras costeras de Córcega permanece cercada bajo dominio militar. El tratado EE. UU.-Francia registrado en la ONU, el contrato BOAMP de 91 M€ y las 2.848 parcelas catastrales prueban que el Estado ingresa hasta 50 M€/año alquilando el espacio aéreo a la OTAN mientras evade 19,75 M€ en impuestos locales.",
      imageCaption: "Auditoría catastral DGFiP / Tratado ONU n.º 38665 — 2.842 hectáreas militares",
      metrics: [
        { label: "Suelo Bloqueado", value: "2.842 ha", sub: "24,8% de las llanuras litorales", colorClass: "text-rose-400" },
        { label: "Tierra Fértil Baldía", value: "327 ha", sub: "En Ventiseri = 35 explotaciones bloqueadas", colorClass: "text-amber-400" },
        { label: "Ingresos de París", value: "50 M€ / año", sub: "Alquiler de tiro OTAN y combustible", colorClass: "text-emerald-400" },
        { label: "Deuda Fiscal Local", value: "19,75 M€", sub: "Atrasos exigibles a 5 años (Art. 1382 CGI)", colorClass: "text-cyan-400" }
      ],
      householdSummary: "El Estado alega que sus bases no pagan impuesto predial por ser improductivas. Al explotarlas comercialmente (polígono OTAN, antenas 4G/5G, venta de queroseno), la jurisprudencia del Consejo de Estado anula su exención fiscal: 7 municipios pueden reclamar 19,75 M€ de inmediato.",
      proofs: [
        { title: "Tratado ONU n.º 38665 y BOAMP 440653", detail: "Acuerdo USAFE Solenzara/Diane y reforma de pistas de 91 M€" },
        { title: "Informe MRAe 2025-DKCOR3 y DGFiP", detail: "41M L/año extraídos del río Travo, 28 M€ en contaminación PFAS y 327 ha ociosas" }
      ],
      auditParagraphs: [
        "La Base Aérea 126 carece de escuadrón francés permanente y funciona como centro de tiro comercial de la OTAN (4.500 a 7.800 €/hora de vuelo).",
        "Mientras los agricultores sufren restricciones estivales, los pozos militares bombean sin limitación."
      ],
      solutionsList: [
        "Liquidación inmediata de 19,75 M€ de impuesto predial atrasado por los 7 ayuntamientos afectados (Art. 1382 CGI).",
        "Restitución de las 327 hectáreas agrícolas de Ventiseri y descontaminación PFAS a cargo del Estado.",
        "Devolución de las 18 hectáreas de Aspretto al municipio de Ajaccio conforme a los votos de la Asamblea de Córcega."
      ],
      transmissionSlug: "enquete-11-emprise-militaire"
    },
    pt: {
      title: "O Santuário Confiscado: 2.842 Hectares Militares e Rendas de 50 M€/Ano",
      subtitle: "BA 126 Solenzara, Aspretto, Camp Raffalli e Diane: tratado ONU n.º 38665, contrato de 91 M€ e 19,75 M€ de impostos devidos aos municípios.",
      category: "DEFESA E TERRITÓRIO",
      date: "Outubro 2026",
      author: "Célula de Investigação L'OCHJU",
      chapeau: "Um quarto das planícies litorais da Córsega está vedado por arame farpado militar. O tratado EUA-França registado na ONU, o contrato de 91 M€ para pistas e 2.848 parcelas cadastrais provam que o Estado fatura até 50 M€/ano alugando o espaço aéreo à NATO sem pagar 19,75 M€ em impostos prediais locais.",
      imageCaption: "Auditoria DGFiP / Tratado ONU n.º 38665 — 2.842 hectares militares",
      metrics: [
        { label: "Terras Bloqueadas", value: "2.842 ha", sub: "24,8% das planícies costeiras", colorClass: "text-rose-400" },
        { label: "Terra Fértil ao Abandono", value: "327 ha", sub: "Em Ventiseri = 35 explorações bloqueadas", colorClass: "text-amber-400" },
        { label: "Receita de Paris", value: "50 M€ / ano", sub: "Aluguer NATO e querosene sem impostos", colorClass: "text-emerald-400" },
        { label: "Dívida Fiscal Local", value: "19,75 M€", sub: "Retroativos de 5 anos (Art. 1382 CGI)", colorClass: "text-cyan-400" }
      ],
      householdSummary: "O Estado alega isenção fiscal afirmando que os terrenos não geram receita. Como fatura exercícios da NATO, combustível e antenas 4G/5G, a isenção cai automaticamente por lei (Art. 1382 CGI) e 7 municípios têm direito a 19,75 M€.",
      proofs: [
        { title: "Tratado ONU n.º 38665 e BOAMP 440653", detail: "Acordo USAFE Solenzara/Diane e contrato de pistas de 91 M€" },
        { title: "Relatório MRAe 2025-DKCOR3 e DGFiP", detail: "41M L/ano bombeados no rio Travo, 28 M€ poluição PFAS e 327 ha inativos" }
      ],
      auditParagraphs: [
        "A Base Aérea 126 atua sobretudo como polígono pago de treino internacional da NATO e depósito americano de munições.",
        "Durante secas severas, os furos da base operam em pleno regime enquanto os agricultores são racionados."
      ],
      solutionsList: [
        "Emissão imediata de cobrança fiscal pelos 7 municípios no valor de 19,75 M€ em atraso.",
        "Devolução gratuita dos 327 hectares agrícolas ociosos em Ventiseri após descontaminação PFAS estatal.",
        "Transferência do sítio naval de Aspretto para o município de Ajaccio."
      ],
      transmissionSlug: "enquete-11-emprise-militaire"
    },
    ru: {
      title: "Конфискованная земля: 2 842 гектара военных баз и 50 млн € ежегодной ренты",
      subtitle: "Авиабаза Соленцара, Аспретто, Камп Рафалли: договор ООН № 38665, контракт на 91 млн € и 19,75 млн € налоговых долгов мэриям.",
      category: "ОБОРОНА И ТЕРРИТОРИЯ",
      date: "Октябрь 2026",
      author: "Исследовательская ячейка L'OCHJU",
      chapeau: "Четверть плодородных прибрежных равнин Корсики закрыта колючей проволокой. Договор Франции и США в ООН, тендер на 91 млн € и 2 848 кадастровых участков доказывают: Париж зарабатывает до 50 млн €/год на аренде неба силам НАТО, уклоняясь от уплаты 19,75 млн € местного земельного налога.",
      imageCaption: "Кадастровый аудит DGFiP / Договор ООН № 38665",
      metrics: [
        { label: "Занято военными", value: "2 842 га", sub: "24,8% всех прибрежных равнин", colorClass: "text-rose-400" },
        { label: "Заброшенная пашня", value: "327 га", sub: "В Вентизери (хватит на 35 ферм)", colorClass: "text-amber-400" },
        { label: "Доход государства", value: "50 млн € / год", sub: "Аренда полигона НАТО и топливо", colorClass: "text-emerald-400" },
        { label: "Долг перед мэриями", value: "19,75 млн €", sub: "Налог за 5 лет (ст. 1382 CGI)", colorClass: "text-cyan-400" }
      ],
      householdSummary: "По ст. 1382 CGI госимущество освобождено от налога только если не приносит коммерческого дохода. Поскольку базы сдаются силам НАТО (4 500–7 800 €/летный час) и операторам связи, 7 муниципалитетов вправе взыскать 19,75 млн €.",
      proofs: [
        { title: "Договор ООН № 38665 и BOAMP 440653", detail: "Соглашение ВВС США в Соленцаре и ремонт ВПП за 91 млн €" },
        { title: "Отчет MRAe 2025-DKCOR3 и DGFiP", detail: "Откачка 41 млн л воды в год из реки Траво и загрязнение PFAS на 28 млн €" }
      ],
      auditParagraphs: [
        "На авиабазе BA 126 нет постоянной французской боевой эскадрильи: она работает как платный тренировочный полигон НАТО.",
        "В засушливые летние месяцы военные скважины работают без ограничений, тогда как фермерам запрещен полив."
      ],
      solutionsList: [
        "Выставление 7 мэриями исполнительных налоговых требований на 19,75 млн € к государству.",
        "Возврат 327 га неиспользуемых пахотных земель Вентизери молодым фермерам после очистки от PFAS.",
        "Передача 18 га базы Аспретто муниципалитету Аяччо по резолюциям Ассамблеи Корсики."
      ],
      transmissionSlug: "enquete-11-emprise-militaire"
    },
    zh: {
      title: "被征用的圣殿：2,842 公顷军事用地与国家每年 5000 万欧元租借收益",
      subtitle: "索伦扎拉空军基地、阿斯普雷托及戴安娜靶场：联合国第38665号条约、9100万欧元跑道合同及拖欠地方市镇 1975 万欧元房产税。",
      category: "国防与领土主权",
      date: "2026年10月",
      author: "L'OCHJU 调查组",
      chapeau: "科西嘉四分之一的平坦沿海平原被铁丝网封锁。联合国备案的美法双边条约、9100万欧元跑道招标及 2,848 宗地籍档案证实：中央政府将空域与靶场出租给北约军队每年创收近 5000 万欧元，却依法欠缴当地市镇 1975 万欧元地方税。",
      imageCaption: "DGFiP 地籍审计 / 联合国条约第 38665 号 — 2,842 公顷军事用地",
      metrics: [
        { label: "军事圈占土地", value: "2,842 公顷", sub: "占全岛平坦沿海平原 24.8%", colorClass: "text-rose-400" },
        { label: "荒废肥沃农田", value: "327 公顷", sub: "文蒂塞里围栏内闲置可建 35 座农场", colorClass: "text-amber-400" },
        { label: "巴黎年度创收", value: "5000 万€ / 年", sub: "北约靶场租费与免税航空煤油", colorClass: "text-emerald-400" },
        { label: "拖欠地方税款", value: "1975 万€", sub: "近5年法定可追缴地产税 (CGI 1382)", colorClass: "text-cyan-400" }
      ],
      householdSummary: "根据法国《税收总法》第1382条，国有设施唯有“完全不产生商业收入”才能免缴地方房产税。基地通过向北约收费（4,500–7,800 €/飞行小时）及出租通信基站获利，7座市镇依法有权追讨 1975 万欧元税款。",
      proofs: [
        { title: "联合国第 38665 号条约与 BOAMP 440653", detail: "美军使用索伦扎拉基地协议与 9100 万欧元跑道合同" },
        { title: "MRAe 2025-DKCOR3 环评与地籍档案", detail: "每年从特拉沃河抽水 4100 万升及 2800 万欧元 PFAS 污染待治理" }
      ],
      auditParagraphs: [
        "索伦扎拉 126 空军基地并无常驻法国战机中队，实质为北约联军付费实弹演训中心及美军弹药库。",
        "即便在旱季禁灌令期间，基地深井仍满负荷抽水洗刷跑道。"
      ],
      solutionsList: [
        "7个受影响市镇依据 CGI 第1382条立即向国家开具 1975 万欧元欠税催缴通知。",
        "由国家出资彻底清除 PFAS 污染后，无偿归还文蒂塞里 327 公顷闲置农田用于本地农业。",
        "响应科西嘉议会决议，将阿斯普雷托基地 18 公顷海岸归还阿雅克肖市。"
      ],
      transmissionSlug: "enquete-11-emprise-militaire"
    },
    ja: {
      title: "接収された聖域：2,842ヘクタールの軍事基地と国家の年5,000万ユーロ収益構造",
      subtitle: "ソレンザラ空軍基地・アスプレット：国連条約第38665号、9,100万ユーロ滑走路契約、そして自治体への固定資産税1,975万ユーロ未払い。",
      category: "防衛・領土主権",
      date: "2026年10月",
      author: "L'OCHJU 調査部門",
      chapeau: "コルシカ島の平坦な沿岸平野の約4分の1が軍用有刺鉄線で封鎖されています。国連登録の仏米軍事条約、9,100万ユーロの滑走路入札、2,848筆の地籍調査により、国がNATO軍への空域貸与等で年最大5,000万ユーロを稼ぎつつ、地元自治体へ1,975万ユーロの税金を未払いである事実が判明しました。",
      imageCaption: "DGFiP 地籍監査 / 国連条約第38665号 — 軍事接収2,842ヘクタール",
      metrics: [
        { label: "軍用封鎖面積", value: "2,842 ha", sub: "島内平坦沿岸地の24.8%を占有", colorClass: "text-rose-400" },
        { label: "放置された優良農地", value: "327 ha", sub: "ヴェンティゼリ基地内（35農場分に相当）", colorClass: "text-amber-400" },
        { label: "パリの年間収益", value: "5,000万€ / 年", sub: "NATO演習料・非課税ジェット燃料等", colorClass: "text-emerald-400" },
        { label: "自治体への未払税額", value: "1,975万€", sub: "過去5年分の請求可能固定資産税", colorClass: "text-cyan-400" }
      ],
      householdSummary: "仏一般税法典第1382条は「収益を生まない公用資産」に限り非課税としています。NATOへの有償訓練貸与（1飛行時間4,500〜7,800ユーロ）や携帯基地局賃貸を行う以上、非課税特権は失効し7自治体は1,975万ユーロを請求できます。",
      proofs: [
        { title: "国連条約第38665号・BOAMP 440653", detail: "在欧米空軍ソレンザラ協定および9,100万ユーロ滑走路改修契約" },
        { title: "環境庁MRAe 2025-DKCOR3・地籍データ", detail: "トラヴォ川から年4,100万L取水、PFAS汚染浄化費2,800万ユーロ未計上" }
      ],
      auditParagraphs: [
        "ソレンザラ第126空軍基地には仏軍常駐戦闘機隊はなく、実質的にNATO各国の有償実弾演習・米軍弾薬備蓄拠点として運用されています。",
        "干ばつ時の農業取水禁止期間中も、基地内の深井戸は無制限に稼働し続けています。"
      ],
      solutionsList: [
        "関係7自治体による一般税法典第1382条に基づく未払固定資産税1,975万ユーロの即時請求。",
        "国費でのPFAS土壌浄化完了後、ヴェンティゼリの未使用肥沃農地327haを若手農家へ無償返還。",
        "コルシカ議会決議に沿ったアスプレット海軍基地18haのアジャクシオ市への返還。"
      ],
      transmissionSlug: "enquete-11-emprise-militaire"
    }
  },
  18: {
    it: {
      title: "Il Monopolio EDF SEI e la Rendita Coloniale: L'Inganno delle Centrali Termiche",
      subtitle: "Dal blocco settantennale delle dighe fino al 2096 alla rendita garantita al 9,55% su Ricanto (6,3 miliardi € in 20 anni).",
      category: "ENERGIA & BENI STRATEGICI",
      date: "Ottobre 2026",
      author: "Cellula Energia L'OCHJU",
      chapeau: "La Corsica dispone già di 523 MW di energia pulita (220,7 MW idroelettrici e 284,6 MW solari) a fronte di un picco massimo invernale storico di soli 400 MW. Eppure la legge del 29 giugno 2026 ha bloccato le dighe a EDF fino al 2096, limitato il solare cittadino al 30% e imposto una centrale termica da 800 M€ a Ricanto con profitto garantito del 9,55% (6,3 Mld € su 20 anni).",
      imageCaption: "Audit CRE 2026-111 / Legge 2026-554 / Bilanci KPMG EDF PEI",
      metrics: [
        { label: "Capacità Pulita Esistente", value: "523 MW", sub: "Contro picco invernale storico di 400 MW", colorClass: "text-emerald-400" },
        { label: "Dighe Confiscate", value: "Fino al 2096", sub: "Legge n° 2026-554 (70 anni di monopolio EDF)", colorClass: "text-rose-400" },
        { label: "Rendita Termica Ricanto", value: "6,3 Mld €", sub: "9,55% garantito su 20 anni per olio di colza", colorClass: "text-amber-400" },
        { label: "Risparmio STEP Negato", value: "350 M€", sub: "Riconosciuti dalla CRE ma bloccati alle dighe pubbliche", colorClass: "text-cyan-400" }
      ],
      householdSummary: "Paghiamo nella bolletta elettrica (CSPE) miliardi di euro per bruciare olio importato a Ricanto mentre l'energia solare corsa di mezzogiorno viene tagliata per decreto e lo Stato vieta alle dighe pubbliche di stoccare quell'energia con pompe a circuito chiuso (STEP).",
      proofs: [
        { title: "Legge 2026-554 & Decreto ECOR2410407A", detail: "Concessioni dighe per 70 anni + tasso remunerazione Ricanto 9,55%" },
        { title: "Delibera CRE 2026-111 & Bilancio KPMG EDF PEI", detail: "Riconoscimento 350 M€ di risparmio STEP (9,75% WACC)" }
      ],
      auditParagraphs: [
        "L'isola produce già più megawatt puliti (523 MW) del suo fabbisogno di picco invernale (400 MW), ma l'assenza di stoccaggio pubblico idroelettrico impedisce l'autonomia.",
        "Mentre la CRE approva il 9,75% per un progetto privato STEP, blocca l'equipaggiamento in circuito chiuso delle 4 dighe pubbliche esistenti."
      ],
      solutionsList: [
        "Conversione immediata delle dighe di Calacuccia, Tolla, Sampolo e Rizzanese in pompaggio-turbinaggio STEP.",
        "Eliminazione del tetto arbitrario del 30% al fotovoltaico cittadino e sviluppo delle comunità energetiche.",
        "Audit giurisdizionale e parlamentare sui 6,3 miliardi € di sovvenzioni garantite a EDF PEI."
      ],
      transmissionSlug: "enquete-18-monopole-energetique-edf"
    },
    es: {
      title: "El Monopolio EDF SEI y la Renta Colonial: La Farsa de las Centrales Térmicas",
      subtitle: "Del bloqueo de presas hasta 2096 a la renta garantizada del 9,55% en Ricanto (6.300 millones € en 20 años).",
      category: "ENERGÍA Y BIENES ESTRATÉGICOS",
      date: "Octubre 2026",
      author: "Célula Energética L'OCHJU",
      chapeau: "Córcega cuenta ya con 523 MW limpios (220,7 MW hidroeléctricos y 284,6 MW solares) frente a un pico máximo histórico de 400 MW. Sin embargo, la Ley de junio de 2026 bloqueó las presas para EDF hasta 2096, limitó la energía solar al 30% e impuso la planta térmica de Ricanto (800 M€) con un retorno garantizado del 9,55% (6.300 M€ en 20 años).",
      imageCaption: "Auditoría CRE 2026-111 / Ley 2026-554 / Cuentas KPMG EDF PEI",
      metrics: [
        { label: "Capacidad Limpia Real", value: "523 MW", sub: "Frente a 400 MW de pico máximo histórico", colorClass: "text-emerald-400" },
        { label: "Presas Confiscadas", value: "Hasta 2096", sub: "Ley 2026-554 (70 años para EDF)", colorClass: "text-rose-400" },
        { label: "Renta Térmica Ricanto", value: "6.300 M€", sub: "9,55% garantizado 20 años por quemar colza", colorClass: "text-amber-400" },
        { label: "Ahorro STEP Reconocido", value: "350 M€", sub: "Negado a las presas públicas de la isla", colorClass: "text-cyan-400" }
      ],
      householdSummary: "La factura eléctrica financia una central térmica de 800 M€ con rentabilidad privada blindada mientras se desconecta el excedente solar gratuito al mediodía y se impide el bombeo reversible (STEP) en nuestras presas.",
      proofs: [
        { title: "Ley 2026-554 y Orden ECOR2410407A", detail: "Monopolio hidroeléctrico de 70 años y tasa garantizada del 9,55%" },
        { title: "CRE 2026-111 y Cuentas EDF PEI KPMG", detail: "Ahorro confirmado de 350 M€ por bombeo STEP (WACC 9,75%)" }
      ],
      auditParagraphs: [
        "Las 6.319 instalaciones solares y los 4 embalses cubren sobradamente la potencia pico si se almacenase la energía diurna.",
        "La regulación estatal prioriza el negocio de generación térmica importada sobre la soberanía energética limpia."
      ],
      solutionsList: [
        "Equipamiento inmediato de los embalses públicos existentes con turbinas reversibles STEP.",
        "Eliminación del tope del 30% al autoconsumo solar e impulso al almacenamiento distribuido.",
        "Anulación de la renta garantizada del 9,55% sobre la central de Ricanto."
      ],
      transmissionSlug: "enquete-18-monopole-energetique-edf"
    },
    pt: {
      title: "O Monopólio EDF SEI e a Renda Colonial: A Farsa das Centrais Térmicas",
      subtitle: "Do bloqueio das barragens até 2096 à renda garantida de 9,55% em Ricanto (6,3 mil M€ em 20 anos).",
      category: "ENERGIA E BENS ESTRATÉGICOS",
      date: "Outubro 2026",
      author: "Célula Energética L'OCHJU",
      chapeau: "A Córsega já dispõe de 523 MW limpos (220,7 MW hídricos e 284,6 MW solares) face a um pico máximo de 400 MW. Ainda assim, a Lei de junho de 2026 entregou as barragens à EDF até 2096, limitou a energia solar a 30% e impôs a central térmica de Ricanto (800 M€) com retorno garantido de 9,55%.",
      imageCaption: "Auditoria CRE 2026-111 / Lei 2026-554 / Contas KPMG EDF PEI",
      metrics: [
        { label: "Capacidade Limpa Atual", value: "523 MW", sub: "Acima do pico máximo histórico de 400 MW", colorClass: "text-emerald-400" },
        { label: "Barragens Bloqueadas", value: "Até 2096", sub: "Lei 2026-554 (monopólio de 70 anos)", colorClass: "text-rose-400" },
        { label: "Renda Térmica Ricanto", value: "6,3 Mil M€", sub: "Retorno de 9,55% garantido por 20 anos", colorClass: "text-amber-400" },
        { label: "Poupança STEP Negada", value: "350 M€", sub: "Admitida pela CRE mas vedada ao setor público", colorClass: "text-cyan-400" }
      ],
      householdSummary: "Os consumidores pagam na tarifa elétrica uma renda de 6,3 mil milhões € para queimar óleo importado em Ricanto enquanto a eletricidade solar diurna é desperdiçada por falta de bombagem reversível nas barragens públicas.",
      proofs: [
        { title: "Lei 2026-554 e Despacho ECOR2410407A", detail: "Concessões hídricas por 70 anos e remuneração de 9,55% em Ricanto" },
        { title: "CRE 2026-111 e Auditoria KPMG EDF PEI", detail: "Poupança líquida de 350 M€ confirmada em sistema STEP" }
      ],
      auditParagraphs: [
        "Os 284,6 MW solares e os 220,7 MW hidroelétricos tornam tecnicamente obsoletas as centrais térmicas a combustíveis importados.",
        "O regulador aprova retornos de 9,75% a consórcios privados enquanto impede a modernização pública."
      ],
      solutionsList: [
        "Conversão das quatro grandes barragens públicas em sistema reversível STEP de circuito fechado.",
        "Fim do teto regulatório de 30% ao solar cidadão na rede insular.",
        "Revisão pública dos contratos garantidos à EDF PEI."
      ],
      transmissionSlug: "enquete-18-monopole-energetique-edf"
    },
    ru: {
      title: "Энергетическая монополия EDF SEI и колониальная рента: фикция тепловых электростанций",
      subtitle: "Блокировка плотин до 2096 года и гарантированная доходность 9,55% на ТЭС Риканто (6,3 млрд € за 20 лет).",
      category: "ЭНЕРГЕТИКА И МОНОПОЛИИ",
      date: "Октябрь 2026",
      author: "Энергетическая ячейка L'OCHJU",
      chapeau: "На Корсике уже действует 523 МВт чистой генерации (220,7 МВт ГЭС и 284,6 МВт СЭС) при историческом зимнем пике потребления не выше 400 МВт. Тем не менее закон от 29 июня 2026 года передал плотины EDF до 2096 года, ограничил солнечную генерацию порогом 30% и навязал ТЭС Риканто за 800 млн € с гарантированной доходностью 9,55%.",
      imageCaption: "Аудит CRE 2026-111 / Закон 2026-554 / Отчет KPMG EDF PEI",
      metrics: [
        { label: "Чистая мощность", value: "523 МВт", sub: "Выше исторического пика спроса (400 МВт)", colorClass: "text-emerald-400" },
        { label: "Плотины под замком", value: "До 2096 г.", sub: "Закон 2026-554 (70 лет монополии)", colorClass: "text-rose-400" },
        { label: "Рента ТЭС Риканто", value: "6,3 млрд €", sub: "9,55% годовых за сжигание рапсового масла", colorClass: "text-amber-400" },
        { label: "Упущенная экономия ГАЭС", value: "350 млн €", sub: "Признана регулятором CRE (WACC 9,75%)", colorClass: "text-cyan-400" }
      ],
      householdSummary: "Через тарифы граждане оплачивают 6,3 млрд € за сжигание привозного топлива в Риканто, тогда как дневную солнечную энергию отключают по квоте 30%, а существующие ГЭС не переводят в режим ГАЭС.",
      proofs: [
        { title: "Закон 2026-554 и Приказ ECOR2410407A", detail: "70-летняя монополия EDF на плотины и ставка 9,55% для Риканто" },
        { title: "CRE 2026-111 и Аудит KPMG EDF PEI", detail: "Подтвержденная экономия 350 млн € от ГАЭС (STEP)" }
      ],
      auditParagraphs: [
        "6 319 солнечных установок и четыре публичные ГЭС полностью закрывают баланс острова при наличии замкнутого гидроаккумулирования.",
        "Государство субсидирует частный консорциум (9,75% WACC), запрещая модернизацию общественных плотин."
      ],
      solutionsList: [
        "Оснащение плотин Калакучча, Толла, Самполо и Риццанезе насосами замкнутого цикла ГАЭС (STEP).",
        "Отмена 30%-го ограничения для солнечной генерации граждан и фермерских хозяйств.",
        "Независимый аудит и пересмотр гарантированной доходности по ТЭС Риканто."
      ],
      transmissionSlug: "enquete-18-monopole-energetique-edf"
    },
    zh: {
      title: "EDF SEI 能源垄断与殖民租金：热电厂骗局与岛屿富足资源",
      subtitle: "从锁定四大水坝至 2096 年到里坎托热电厂 9.55% 保底暴利（20 年抽血 63 亿欧元）。",
      category: "能源与战略公共品",
      date: "2026年10月",
      author: "L'OCHJU 能源调查组",
      chapeau: "科西嘉已拥有 523 兆瓦清洁装机（水电 220.7 MW + 太阳能 284.6 MW），远超全岛历史最高冬季峰值负荷（400 MW）。然而法国政府于2026年6月29日立法将公有水坝锁定给 EDF 直至 2096 年，将民用光伏强行限制在 30% 阈值，并强推造价 8 亿欧元的里坎托热电厂，保障其 20 年 9.55% 年化回报（63 亿欧元）。",
      imageCaption: "CRE 2026-111 / 第 2026-554 号法律 / EDF PEI 毕马威审计",
      metrics: [
        { label: "现有清洁产能", value: "523 MW", sub: "高于历史最高冬季峰值 400 MW", colorClass: "text-emerald-400" },
        { label: "水坝被锁定年限", value: "直至 2096年", sub: "2026-554 号法律授予 EDF 70 年特权", colorClass: "text-rose-400" },
        { label: "里坎托热电租金", value: "63 亿€", sub: "20 年 9.55% 国家保底收益焚烧菜籽油", colorClass: "text-amber-400" },
        { label: "被否决抽蓄节能", value: "3.5 亿€", sub: "CRE 已确认净省成本却禁止公有水坝改造", colorClass: "text-cyan-400" }
      ],
      householdSummary: "公共电费账单被迫补贴 63 亿欧元用于焚烧进口燃油与菜籽油，同时正午免费太阳能被迫弃光限发，公有水坝被禁止加装闭环抽水蓄能机组 (STEP)。",
      proofs: [
        { title: "第 2026-554 号法律与部长令 ECOR2410407A", detail: "70 年水电专营权与里坎托 9.55% 资本回报率" },
        { title: "CRE 第 2026-111 号决议与 KPMG 财报", detail: "确认阿雅克肖抽水蓄能 (STEP) 可净省 3.5 亿欧元" }
      ],
      auditParagraphs: [
        "岛上 6,319 座屋顶及农用光伏电站配合现有四大水坝即可实现 100% 清洁电力自给。",
        "国家能源监管机构允许大陆私人联合体获得 9.75% 保底 WACC，却阻挠科西嘉利用公有水坝发电蓄能。"
      ],
      solutionsList: [
        "立即在卡拉库恰、托拉、桑波洛、里扎内塞四大水库加装闭环抽水蓄能 (STEP) 机组。",
        "取消对公民与农企光伏发电不合理的 30% 上网封顶限制。",
        "撤销对 EDF PEI 旗下里坎托热电厂 20 年 9.55% 的公共电价担保。"
      ],
      transmissionSlug: "enquete-18-monopole-energetique-edf"
    },
    ja: {
      title: "EDF SEIの独占と植民地型レント：火力発電所の虚構と島の豊かな再生資源",
      subtitle: "2096年までの70年ダム囲い込みとリカント火力発電所への9.55%保証利回り（20年間で63億ユーロ）。",
      category: "エネルギー・戦略資源",
      date: "2026年10月",
      author: "L'OCHJU エネルギー調査部門",
      chapeau: "コルシカ島は歴史的冬期最大需要400MWを上回る523MWのクリーン発電容量（水力220.7MW＋太陽光284.6MW）を既に有しています。しかし2026年6月29日法により4大ダムが2096年までEDFに独占委譲され、市民太陽光に30%上限が課され、年間9.55%の利回りを保証する8億ユーロ規模のリカント火力発電所（20年間で63億ユーロ）が強行されました。",
      imageCaption: "CRE 2026-111 / 法律2026-554号 / KPMG EDF PEI 監査",
      metrics: [
        { label: "既存クリーン発電", value: "523 MW", sub: "島内最大需要ピーク400 MWを超過", colorClass: "text-emerald-400" },
        { label: "ダム独占期間", value: "2096年まで", sub: "2026-554号法による70年囲い込み", colorClass: "text-rose-400" },
        { label: "リカント火力利権", value: "63億€", sub: "輸入菜種油燃焼に対し20年間9.55%保証", colorClass: "text-amber-400" },
        { label: "阻まれたSTEP節約額", value: "3.5億€", sub: "CRE承認済みながら公営ダムへの導入を禁止", colorClass: "text-cyan-400" }
      ],
      householdSummary: "日中の余剰太陽光発電が出力抑制される一方、電気料金の賦課金を通じて年間9.55%の利回りが保証された輸入油火力が維持され、公営ダムでの閉ループ揚水発電(STEP)は禁止されています。",
      proofs: [
        { title: "法律 2026-554号・省令 ECOR2410407A", detail: "70年間水力権保護とリカント発電所9.55%報酬率" },
        { title: "CRE決議 2026-111・KPMG監査報告書", detail: "揚水式(STEP)による3.5億ユーロの純削減効果を確認" }
      ],
      auditParagraphs: [
        "島内6,319か所の太陽光と4大公営ダムに揚水設備を組み合わせれば、輸入燃料に頼らない完全自給が可能です。",
        "規制委員会は民間コンソーシアムへWACC 9.75%を認可する一方、公営ダムの蓄電転換を認めていません。"
      ],
      solutionsList: [
        "既存の4大公営ダムへの閉ループ揚水発電(STEP)の即時導入。",
        "市民・農業用太陽光に対する恣意的な30%出力上限の撤廃。",
        "EDF PEIリカント火力計画への公的9.55%保証スキームの見直し・廃止。"
      ],
      transmissionSlug: "enquete-18-monopole-energetique-edf"
    }
  },
  22: {
    it: {
      title: "La Captazione Bancaria e la Fuga del Risparmio Isolano",
      subtitle: "Radiografia del sistema bancario in Corsica: meno del 40% dei depositi locali viene reinvestito nell'economia dell'isola.",
      category: "BANCHE & RISPARMIO",
      date: "Ottobre 2026",
      author: "Cellula Finanziaria L'OCHJU",
      chapeau: "Le filiali bancarie in Corsica raccolgono oltre 7,3 miliardi di euro di depositi liquidi da famiglie e imprese. Eppure l'audit dei bilanci monetari IEDOM e Banca di Francia rivela un drenaggio sistematico: meno del 40% di questo risparmio finanzia l'economia produttiva locale, mentre i capitali vengono deviati sui mercati parigini.",
      imageCaption: "Statistiche monetarie IEDOM / Banca di Francia / ACPR — Depositi vs Crediti locali",
      metrics: [
        { label: "Depositi Raccolti", value: "7,3 Mld €", sub: "Risparmio liquido di famiglie e PMI corse", colorClass: "text-amber-400" },
        { label: "Reinvestimento Locale", value: "< 40%", sub: "Rifiuti sistematici a giovani e artigiani", colorClass: "text-rose-400" },
        { label: "Drenaggio Finanziario", value: "2,57 Mld €", sub: "Risparmio esportato verso mercati esterni", colorClass: "text-cyan-400" },
        { label: "Fonti Ufficiali", value: "IEDOM / ACPR", sub: "Dati monetari Banca di Francia certificati", colorClass: "text-emerald-400" }
      ],
      householdSummary: "I vostri depositi bancari in Corsica superano i 7,3 miliardi di euro, ma quando un artigiano, un agricoltore o una giovane coppia chiede un prestito locale, le reti bancarie centralizzano e razionano il credito per dirottare la liquidità fuori dall'isola.",
      proofs: [
        { title: "Statistiche IEDOM / Banca di Francia", detail: "Raccolta depositi vs volume crediti produttivi in Corsica" },
        { title: "Indagini CCI di Corsica & ACPR", detail: "Sottofinanziamento cronico delle PMI e creazione d'impresa locale" }
      ],
      auditParagraphs: [
        "Nonostante un tasso di risparmio precauzionale tra i più alti di Francia, i criteri di rating algoritmici decisi fuori dall'isola bloccano gli investimenti produttivi.",
        "I depositi raccolti agli sportelli locali alimentano i portafogli obbligazionari e azionari dei gruppi bancari a Parigi."
      ],
      solutionsList: [
        "Creazione di una Cassa Territoriale di Investimento Pubblico orientata ai depositi locali.",
        "Obbligo di trasparenza trimestrale sul rapporto Crediti Locali / Depositi per ogni istituto bancario.",
        "Garanzia regionale dedicata ai primi insediamenti agricoli, artigianali e abitativi."
      ],
      transmissionSlug: "enquete-02-mythe-subventions"
    },
    es: {
      title: "La Captación Bancaria y la Fuga del Ahorro Insular",
      subtitle: "Radiografía del sistema bancario en Córcega: menos del 40% de los depósitos locales se reinvierte en la economía productiva de la isla.",
      category: "BANCA Y AHORRO LÍQUIDO",
      date: "Octubre 2026",
      author: "Célula Financiera L'OCHJU",
      chapeau: "Las redes bancarias recaudan más de 7.300 millones de euros en depósitos líquidos de familias y empresas de Córcega. Sin embargo, los datos del IEDOM y el Banco de Francia revelan que menos del 40% se presta localmente, desviando el ahorro hacia mercados financieros parisinos.",
      imageCaption: "Estadísticas IEDOM / Banco de Francia / ACPR — Captación de depósitos",
      metrics: [
        { label: "Depósitos Captados", value: "7.300 M€", sub: "Ahorro líquido de hogares y pymes", colorClass: "text-amber-400" },
        { label: "Reinversión Local", value: "< 40%", sub: "Racionamiento crónico de crédito local", colorClass: "text-rose-400" },
        { label: "Fuga de Liquidez", value: "2.570 M€", sub: "Desviados hacia mercados continentales", colorClass: "text-cyan-400" },
        { label: "Fuentes Oficiales", value: "IEDOM / ACPR", sub: "Series monetarias Banco de Francia", colorClass: "text-emerald-400" }
      ],
      householdSummary: "Aunque las familias corsas acumulan más de 7.300 millones de euros en sus cuentas, las entidades centralizan las decisiones de crédito en París y niegan financiación a jóvenes agricultores, artesanos y compradores locales.",
      proofs: [
        { title: "Estadísticas IEDOM / Banco de Francia", detail: "Desfase entre depósitos captados y crédito productivo local" },
        { title: "Informes CCI de Córcega y ACPR", detail: "Barreras de acceso crediticio para empresas locales" }
      ],
      auditParagraphs: [
        "El ahorro de precaución en Córcega figura entre los más elevados de Francia, pero la liquidez es absorbida diariamente por las tesorerías centrales.",
        "La falta de una banca de desarrollo insular agrava la dependencia exterior."
      ],
      solutionsList: [
        "Creación de un fondo público insular de coinversión respaldado por el ahorro local.",
        "Publicación obligatoria de la ratio crédito local / depósitos por entidad bancaria.",
        "Líneas de aval territorial para acceso a primera vivienda y relevo agrícola."
      ],
      transmissionSlug: "enquete-02-mythe-subventions"
    },
    pt: {
      title: "A Captação Bancária e a Fuga da Poupança Insular",
      subtitle: "Radiografia da banca na Córsega: menos de 40% dos depósitos locais é reinvestido na economia produtiva da ilha.",
      category: "BANCA E POUPANÇA",
      date: "Outubro 2026",
      author: "Célula Financeira L'OCHJU",
      chapeau: "As agências bancárias na Córsega captam mais de 7,3 mil milhões de euros em depósitos líquidos de famílias e empresas. Contudo, os balanços monetários do IEDOM e do Banco de França expõem que menos de 40% financia a economia local, drenando o capital para mercados financeiros em Paris.",
      imageCaption: "Estatísticas IEDOM / Banco de França / ACPR — Depósitos vs Crédito Local",
      metrics: [
        { label: "Depósitos Captados", value: "7,3 Mil M€", sub: "Poupança líquida de famílias e PME", colorClass: "text-amber-400" },
        { label: "Reinvestimento Local", value: "< 40%", sub: "Restrição severa ao crédito produtivo", colorClass: "text-rose-400" },
        { label: "Drenagem Financeira", value: "2,57 Mil M€", sub: "Transferidos para praças externas", colorClass: "text-cyan-400" },
        { label: "Fontes Oficiais", value: "IEDOM / ACPR", sub: "Estatísticas Banco de França", colorClass: "text-emerald-400" }
      ],
      householdSummary: "As famílias corsas mantêm 7,3 mil milhões € nos bancos da ilha, mas menos de 40% regressa em empréstimos locais a artesãos, agricultores ou jovens compradores.",
      proofs: [
        { title: "Séries IEDOM / Banco de França", detail: "Volume de depósitos locais vs crédito produtivo concedido" },
        { title: "Inquéritos CCI da Córsega e ACPR", detail: "Subfinanciamento estrutural do tecido empresarial insular" }
      ],
      auditParagraphs: [
        "A taxa de poupança das famílias na Córsega está entre as mais altas, mas os modelos bancários centralizados canalizam a liquidez para fora da ilha.",
        "Sem transparência nos rácios de reinvestimento, a poupança insular financia projetos especulativos externos."
      ],
      solutionsList: [
        "Instituição de um fundo territorial de investimento orientado para a economia produtiva local.",
        "Divulgação pública obrigatória do rácio Crédito Local / Depósitos por cada banco.",
        "Garantias públicas regionais para jovens empreendedores, agricultores e habitação."
      ],
      transmissionSlug: "enquete-02-mythe-subventions"
    },
    ru: {
      title: "Банковская монополизация и отток сбережений жителей острова",
      subtitle: "Анализ банковской системы Корсики: менее 40% собранных депозитов реинвестируется в местную экономику.",
      category: "БАНКИ И СБЕРЕЖЕНИЯ",
      date: "Октябрь 2026",
      author: "Финансовая ячейка L'OCHJU",
      chapeau: "Отделения банков на Корсике собирают свыше 7,3 млрд евро ликвидных вкладов населения и бизнеса. Однако статистика IEDOM и Банка Франции доказывает, что менее 40% этих средств возвращается в реальный сектор острова в виде кредитов — капитал ежедневно уходит на финансовые рынки Парижа.",
      imageCaption: "Монетарная статистика IEDOM / Банк Франции / ACPR",
      metrics: [
        { label: "Собранные депозиты", value: "7,3 млрд €", sub: "Ликвидные сбережения семей и МСП", colorClass: "text-amber-400" },
        { label: "Доля местных кредитов", value: "< 40%", sub: "Хроническое ограничение финансирования", colorClass: "text-rose-400" },
        { label: "Выведенный капитал", value: "2,57 млрд €", sub: "Переток на континентальные рынки", colorClass: "text-cyan-400" },
        { label: "Источники данных", value: "IEDOM / ACPR", sub: "Официальная статистика Банка Франции", colorClass: "text-emerald-400" }
      ],
      householdSummary: "При одном из самых высоких уровней сбережений во Франции корсиканские предприниматели, фермеры и молодые семьи сталкиваются с жестким дефицитом кредитов из-за централизованного оттока банковской ликвидности.",
      proofs: [
        { title: "Данные IEDOM / Банк Франции", detail: "Соотношение собранных вкладов и производственных кредитов" },
        { title: "Опросы Торгово-промышленной палаты (CCI)", detail: "Барьеры кредитования для малого бизнеса на острове" }
      ],
      auditParagraphs: [
        "Крупнейшие банковские сети используют остров как донорский резервуар дешевой ликвидности.",
        "Отсутствие региональных нормативов реинвестирования обескровливает местное производство."
      ],
      solutionsList: [
        "Создание территориального инвестиционного фонда развития с опорой на местный капитал.",
        "Обязательная ежеквартальная публикация коэффициента реинвестирования для каждого банка.",
        "Целевые региональные гарантии по кредитам на жилье, ремесла и сельское хозяйство."
      ],
      transmissionSlug: "enquete-02-mythe-subventions"
    },
    zh: {
      title: "银行资金虹吸与海岛居民储蓄外流",
      subtitle: "科西嘉银行业透视：当地吸纳的存款中不到 40% 回流用于本土实体经济。",
      category: "银行与金融储蓄",
      date: "2026年10月",
      author: "L'OCHJU 金融调查组",
      chapeau: "科西嘉各商业银行网点从本地家庭和企业吸纳超过 73 亿欧元流动存款。但 IEDOM 与法兰西银行货币资产负债表揭示：仅有不到 40% 的储蓄转化为本地信贷，巨额资金被每日抽调至巴黎金融市场运作。",
      imageCaption: "IEDOM / 法兰西银行 / ACPR 货币统计 — 存款与本地信贷剪刀差",
      metrics: [
        { label: "岛内吸纳存款", value: "73 亿€", sub: "当地家庭与中小企业流动储蓄", colorClass: "text-amber-400" },
        { label: "本地信贷回流率", value: "< 40%", sub: "青年购房与本地工匠长期信贷紧缩", colorClass: "text-rose-400" },
        { label: "净外流储蓄规模", value: "25.7 亿€", sub: "输往法国本土资本市场", colorClass: "text-cyan-400" },
        { label: "官方数据来源", value: "IEDOM / ACPR", sub: "法兰西银行及审慎监管局档案", colorClass: "text-emerald-400" }
      ],
      householdSummary: "科西嘉居民储蓄率位居全法前列，但当岛内年轻人购房、农民扩张或手工业者申请贷款时，总部设在大陆的银行机构却严格惜贷，将当地存款资金调往岛外。",
      proofs: [
        { title: "IEDOM 与法兰西银行统计", detail: "本地吸存总量 vs 本土实体贷款投放对比" },
        { title: "科西嘉工商会 (CCI) 与 ACPR 报告", detail: "本土中小企业融资困境系统性调查" }
      ],
      auditParagraphs: [
        "法国主要银行集团长期把科西嘉视为高利润的纯存款采集池，而非信贷支持区。",
        "高度集中的风控模型将本地小微产业排除在信贷白名单之外。"
      ],
      solutionsList: [
        "设立地方公共投资基金，引导本地储蓄优先支持本土实业。",
        "强制所有驻岛银行按季度公布“本地贷款 / 本地存款”比率。",
        "为青年首套自住住房、农业接班与手工业提供地方公共信贷担保。"
      ],
      transmissionSlug: "enquete-02-mythe-subventions"
    },
    ja: {
      title: "銀行システムによる資金吸収と島民貯蓄の島外流出",
      subtitle: "コルシカ金融構造の徹底分析：地元預金の40%未満しか島内実体経済へ再投資されていない実態。",
      category: "銀行・個人貯蓄",
      date: "2026年10月",
      author: "L'OCHJU 金融調査部門",
      chapeau: "コルシカ島の銀行支店は住民と地元企業から73億ユーロ以上の流動預金を集めています。しかしIEDOMとフランス銀行の通貨統計によると、島内の生産的融資へ回るのは40%未満に留まり、資金の大部分がパリの金融市場へ吸い上げられています。",
      imageCaption: "IEDOM / フランス銀行 / ACPR 統計 — 預金吸収額と島内融資額",
      metrics: [
        { label: "島内総預金残高", value: "73億€", sub: "住民と地元中小企業の流動資産", colorClass: "text-amber-400" },
        { label: "島内再投資比率", value: "< 40%", sub: "地元事業者・若年層への恒常的な融資抑制", colorClass: "text-rose-400" },
        { label: "島外流出規模", value: "25.7億€", sub: "本土の金融市場へ毎日移転される流動性", colorClass: "text-cyan-400" },
        { label: "公式統計典拠", value: "IEDOM / ACPR", sub: "フランス銀行公式マネー統計", colorClass: "text-emerald-400" }
      ],
      householdSummary: "コルシカは貯蓄率が極めて高いにもかかわらず、パリ本社の審査基準により地元農家や職人、若い世帯への融資が絞り込まれ、島民の預金が島外の投資商品に流用されています。",
      proofs: [
        { title: "IEDOM / フランス銀行統計", detail: "支店預金総額と島内事業融資実績の乖離" },
        { title: "コルシカ商工会議所(CCI)・ACPR調査", detail: "地元企業の資金調達障壁に関する公式報告" }
      ],
      auditParagraphs: [
        "大手銀行網は島を低コストの預金供給源として扱い、地域密着型与信を縮小しています。",
        "地域再投資比率の公開義務がないことが資金流出を助長しています。"
      ],
      solutionsList: [
        "地域貯蓄を原資としたコルシカ公共投資基金の創設。",
        "島内で営業する全銀行に対する「地域融資／預金比率」の四半期開示義務化。",
        "農業新規就農・職人事業・地域住民の初回住宅取得向けの公的信用保証の拡充。"
      ],
      transmissionSlug: "enquete-02-mythe-subventions"
    }
  },
  23: {
    it: {
      title: "Il Diritto di Salvare: E se la Corsica Costruisse la Propria Protezione Civile Sovrana?",
      subtitle: "I contribuenti pagano 203 €/ab. (vs 85 € a Parigi) per proteggere 3 milioni di turisti mentre lo Stato blocca i Canadair di Olbia a 15 min e cancella 52,8 M€.",
      category: "PROTEZIONE CIVILE & RISCHI",
      date: "Settembre 2026",
      author: "Cellula Rischi L'OCHJU",
      chapeau: "I bilanci OFGL, i decreti SDACR e i rapporti del Senato rivelano un triplo fallimento dello Stato in Corsica: sovrapprezzo turistico pagato all'80% dai residenti (203 €/ab. in Alta Corsica vs 85 € media nazionale), soli 5 Canadair su 12 operativi il 24 luglio 2026 e il rifiuto di stipulare accordi diretti con i Canadair di Olbia a 15 minuti di volo.",
      imageCaption: "Audit OFGL / Rapporti Senato 838 & 393 / Decreto SDACR 135/2023",
      metrics: [
        { label: "Costo per Abitante (2B)", value: "203 € / anno", sub: "Contro 85 € media nazionale (+138%)", colorClass: "text-rose-400" },
        { label: "Canadair Operativi", value: "5 su 12", sub: "Il 24 luglio 2026 al picco dell'ondata di calore", colorClass: "text-amber-400" },
        { label: "Volo Olbia vs Nîmes", value: "15m vs 1h30", sub: "Accordo diretto con la Sardegna bloccato da Parigi", colorClass: "text-cyan-400" },
        { label: "Sprechi Duplicati", value: "4,5 M€ / anno", sub: "Due stati maggiori paralleli (EPISC)", colorClass: "text-emerald-400" }
      ],
      householdSummary: "Ogni famiglia paga più del doppio della media nazionale per finanziare i soccorsi a 3 milioni di turisti (con una chiave TSCA ferma al parco auto del 2003), mentre le ambulanze rurali mancano fino a 4 ore e i Canadair devono partire da Nîmes (1h30) invece che da Olbia (14 minuti).",
      proofs: [
        { title: "Rapporti Senato 838 & 393 + Decreto 2024-124", detail: "Flotta ridotta 5/12, taglio 52,8 M€ e 60% voli Dragon in EVASAN" },
        { title: "SDACR 135/2023 & Risposta JOAN 3779", detail: "Vuoti ambulanza 1h32-4h e chiave fiscale TSCA congelata al 2003" }
      ],
      auditParagraphs: [
        "Mentre la manutenzione privata Sabena Technics FNI costa 30 M€/anno con lo Stato azionista tramite Bpifrance, la Corsica non possiede alcun aereo antincendio proprio.",
        "Trasportare pompieri stagionali in traghetto costa 3,5–6 M€ a stagione: esattamente quanto 70–120 posti permanenti locali."
      ],
      solutionsList: [
        "Flotta aerea propria: 3 anfibi Air Tractor Fire Boss (< 12 min ovunque), 1 elicottero pesante a Corte e corridoio immediato Olbia-Figari (Art. 2 CEDU).",
        "Fusione unica Cumpagnia Corsa di Prutezzione Civile (CCPC) a Corte recuperando 4,5 M€/anno dai doppioni e +9 M€ da tassa sicurezza 3 €/passeggero.",
        "4 rotture tecnologiche a saldo 0 €: sensori AI + droni FireSwarm (< 8 min), ritardanti bio-alghe (zero tossici), cortine d'acqua a gravità OEHC e 120 pompieri fissi nelle vallate."
      ],
      transmissionSlug: "enquete-23-securite-civile"
    },
    es: {
      title: "El Derecho a Salvar: ¿Y si Córcega Construyera su Propia Protección Civil Soberana?",
      subtitle: "Los hogares pagan 203 €/hab. (vs 85 € media) por 3 millones de turistas mientras París bloquea los Canadair de Olbia a 15 min y recorta 52,8 M€.",
      category: "PROTECCIÓN CIVIL Y RIESGOS",
      date: "Septiembre 2026",
      author: "Célula de Riesgos L'OCHJU",
      chapeau: "Las cuentas de OFGL y los informes del Senado muestran un triple fracaso estatal: sobrecoste turístico financiado al 80% por impuestos locales (203 €/hab. frente a 85 €), solo 5 Canadair operativos de 12 en julio de 2026, y la prohibición de pactos directos con la base sarda de Olbia a 15 minutos de Bonifacio.",
      imageCaption: "Auditoría OFGL / Informes Senado 838 y 393 / Decreto SDACR 135/2023",
      metrics: [
        { label: "Coste por Habitante (2B)", value: "203 € / año", sub: "Frente a 85 € media nacional (+138%)", colorClass: "text-rose-400" },
        { label: "Canadair Disponibles", value: "5 de 12", sub: "El 24 de julio de 2026 en plena ola de calor", colorClass: "text-amber-400" },
        { label: "Vuelo Olbia vs Nimes", value: "15m vs 1h30", sub: "Cooperación directa con Cerdeña bloqueada", colorClass: "text-cyan-400" },
        { label: "Duplicidades (EPISC)", value: "4,5 M€ / año", sub: "Dos estados mayores administrativos redundantes", colorClass: "text-emerald-400" }
      ],
      householdSummary: "Con una tasa TSCA congelada en el parque móvil de 2003, el contribuyente corso paga el doble para proteger a 3 millones de visitantes, mientras faltan ambulancias rurales hasta 4 horas y los refuerzos aéreos tardan 90 minutos desde Nimes.",
      proofs: [
        { title: "Informes Senado 838 y 393 + Decreto 2024-124", detail: "5/12 aviones activos, recorte de 52,8 M€ y 60% de helicópteros en traslados SAMU" },
        { title: "SDACR 135/2023 y Respuesta JOAN 3779", detail: "Vacíos de ambulancia de hasta 4h y cálculo congelado desde 2003" }
      ],
      auditParagraphs: [
        "El mantenimiento de flota (30 M€/año) está monopolizado por Sabena Technics donde el propio Estado es accionista vía Bpifrance.",
        "Llevar brigadas estivales en ferry cuesta 3,5–6 M€, equivalente a crear de 70 a 120 plazas fijas anuales."
      ],
      solutionsList: [
        "Flota propia: 3 anfibios Fire Boss (< 12 min), 1 helicóptero pesado en Corte y corredor transfronterizo Olbia-Figari (Art. 2 CEDH).",
        "Mando único Cumpagnia Corsa di Prutezzione Civile (CCPC) en Corte con equilibrio presupuestario de 14,85 M€ (tasa de 3 €/pasajero + fin duplicidades).",
        "Innovación integral: drones FireSwarm IA (< 8 min), retardantes vegetales biodegradables, cortinas hidráulicas por gravedad OEHC y 120 bomberos fijos rurales."
      ],
      transmissionSlug: "enquete-23-securite-civile"
    },
    pt: {
      title: "O Direito de Salvar: E se a Córsega Construísse a Sua Proteção Civil Soberana?",
      subtitle: "Residentes pagam 203 €/hab. (vs 85 € média) por 3 milhões de turistas enquanto Paris bloqueia os Canadair de Olbia a 15 min e corta 52,8 M€.",
      category: "PROTEÇÃO CIVIL E RISCOS",
      date: "Setembro 2026",
      author: "Célula de Riscos L'OCHJU",
      chapeau: "As contas OFGL e os relatórios do Senado comprovam uma tripla falha: sobrecusto turístico pago a 80% pelos contribuintes locais (203 €/hab. na Alta Córsega vs 85 € média nacional), apenas 5 Canadair de 12 operacionais em julho de 2026 e o bloqueio de acordos diretos com Olbia (Sardenha) a 15 minutos.",
      imageCaption: "Auditoria OFGL / Relatórios Senado 838 e 393 / Decreto SDACR 135/2023",
      metrics: [
        { label: "Custo por Habitante (2B)", value: "203 € / ano", sub: "Contra 85 € média nacional (+138%)", colorClass: "text-rose-400" },
        { label: "Canadairs Ativos", value: "5 em 12", sub: "Em 24 de julho de 2026 no pico de calor", colorClass: "text-amber-400" },
        { label: "Voo Olbia vs Nîmes", value: "15m vs 1h30", sub: "Corredor direto com a Sardenha bloqueado", colorClass: "text-cyan-400" },
        { label: "Desperdício Duplicado", value: "4,5 M€ / ano", sub: "Duas direções administrativas paralelas", colorClass: "text-emerald-400" }
      ],
      householdSummary: "Com o imposto TSCA congelado na frota automóvel de 2003, os residentes suportam mais do dobro do custo nacional enquanto as ambulâncias rurais faltam até 4 horas e os aviões vêm de Nîmes (1h30) em vez de Olbia (14 minutos).",
      proofs: [
        { title: "Relatórios Senado 838 & 393 + Decreto 2024-124", detail: "Frota 5/12 operacional, corte de 52,8 M€ e 60% voos em EVASAN" },
        { title: "SDACR 135/2023 & Resposta JOAN 3779", detail: "Falhas ambulância 1h32-4h e chave fiscal TSCA de 2003" }
      ],
      auditParagraphs: [
        "A manutenção da frota (30 M€/ano) está concedida em monopólio à Sabena Technics onde o próprio Estado é acionista via Bpifrance.",
        "O transporte sazonal por ferry custa 3,5–6 M€, equivalente a 70–120 postos profissionais permanentes."
      ],
      solutionsList: [
        "Frota aérea insular: 3 anfíbios Fire Boss (< 12 min), 1 helicóptero pesado em Corte e pacto Olbia-Figari (Art. 2 CEDH).",
        "Comando unificado CCPC em Corte financiando +14,85 M€ sem défice (taxa 3 €/passageiro + fim de duplicações).",
        "4 inovações: drones FireSwarm IA (< 8 min), retardantes vegetais, cortinas gravíticas OEHC e 120 bombeiros permanentes."
      ],
      transmissionSlug: "enquete-23-securite-civile"
    },
    ru: {
      title: "Право спасать: что если Корсика создаст суверенную гражданскую оборону?",
      subtitle: "Жители платят 203 €/чел. (вместо 85 €) за 3 млн туристов, пока Париж блокирует Canadair из Ольбии в 15 минутах лета и урезает 52,8 млн €.",
      category: "ГРАЖДАНСКАЯ ЗАЩИТА И РИСКИ",
      date: "Сентябрь 2026",
      author: "Ячейка рисков L'OCHJU",
      chapeau: "Данные OFGL и доклады Сената доказывают тройной провал государства: 80% расходов на летний туризм несут местные жители (203 €/чел. против 85 € по стране), лишь 5 из 12 самолетов Canadair были исправны 24 июля 2026 года, а прямое соглашение с сардинской базой Ольбия (14 минут полета) запрещено Парижем.",
      imageCaption: "Аудит OFGL / Доклады Сената 838 и 393 / SDACR 135/2023",
      metrics: [
        { label: "Нагрузка на жителя (2B)", value: "203 € / год", sub: "Против 85 € по стране (+138%)", colorClass: "text-rose-400" },
        { label: "Исправных Canadair", value: "5 из 12", sub: "На пике жары 24 июля 2026 года", colorClass: "text-amber-400" },
        { label: "Ольбия vs Ним", value: "15м vs 1ч30", sub: "Запрет прямого реагирования из Сардинии", colorClass: "text-cyan-400" },
        { label: "Лишние штабы (EPISC)", value: "4,5 млн € / год", sub: "Дублирование двух центров управления", colorClass: "text-emerald-400" }
      ],
      householdSummary: "Финансирование по налогу TSCA заморожено на автопарке 2003 года. Местные налогоплательщики несут двойную нагрузку, сельские машины скорой помощи отсутствуют до 4 часов, а самолеты летят из Нима 1,5 часа вместо 14 минут из Ольбии.",
      proofs: [
        { title: "Доклады Сената 838, 393 и Декрет 2024-124", detail: "Сокращение финансирования на 52,8 млн €, монополия Sabena Technics" },
        { title: "SDACR 135/2023 и ответ JOAN 3779", detail: "Окна без скорой помощи 1ч32–4ч и формула TSCA от 2003 года" }
      ],
      auditParagraphs: [
        "Государство выступает одновременно заказчиком и совладельцем монополиста ТО Sabena Technics (через Bpifrance).",
        "Перевозка сезонных отрядов паромом обходится в 3,5–6 млн € за лето, что равно содержанию 70–120 постоянных пожарных."
      ],
      solutionsList: [
        "Собственный флот: 3 амфибии Fire Boss (подлет < 12 мин), тяжелый вертолет в Корте и пакт Ольбия–Фигари (ст. 2 ЕКПЧ).",
        "Объединенное командование CCPC в Корте и сбалансированный бюджет 14,85 млн € (сбор 3 €/пассажир + отказ от дублей).",
        "Внедрение БПЛА FireSwarm (< 8 мин), биоразлагаемых ретардантов, гравитационных водяных завес OEHC и 120 постоянных ставок в селах."
      ],
      transmissionSlug: "enquete-23-securite-civile"
    },
    zh: {
      title: "拯救之权：如果科西嘉建立自主的民防救援体系会怎样？",
      subtitle: "岛民人均承担 203 €（全国均值 85 €）却要掩护 300 万游客安全，中央削减 5280 万 € 预算并禁止 15 分钟可达的奥尔比亚灭火机直援。",
      category: "民防安全与灾害风险",
      date: "2026年9月",
      author: "L'OCHJU 风险调查组",
      chapeau: "OFGL 财政账目与法国参议院报告证实三重失职：本地纳税人承担 80% 消防预算（上科西嘉人均 203 € 对比全法 85 €），2026年7月24日热浪峰值期间全国 12 架灭火机仅 5 架适航，且巴黎严禁向 15 分钟航程外的撒丁岛奥尔比亚基地直接求援。",
      imageCaption: "OFGL / 参议院第 838 及 393 号报告 / SDACR 第 135/2023 号令",
      metrics: [
        { label: "人均消防负担 (2B)", value: "203 € / 年", sub: "高于全法均值 85 € (+138%)", colorClass: "text-rose-400" },
        { label: "可用灭火机", value: "仅 5 / 12 架", sub: "2026年7月24日热浪高峰实况", colorClass: "text-amber-400" },
        { label: "奥尔比亚 vs 尼姆", value: "15分 vs 1.5时", sub: "跨海直援撒丁岛合作被巴黎封锁", colorClass: "text-cyan-400" },
        { label: "机构重复浪费", value: "450 万€ / 年", sub: "双套指挥体系与双报警中心内耗", colorClass: "text-emerald-400" }
      ],
      householdSummary: "政府对科西嘉的保险税拨款 (TSCA) 竟冻结在 2003 年的汽车保有量上；居民每年多缴 138% 的费用，农村救护车却面临长达 4 小时的空窗，飞机只能从尼姆远道飞来。",
      proofs: [
        { title: "参议院 838 & 393 号报告 + 2024-124 法令", detail: "削减 5280 万欧元预算、5/12 可用率及 60% 救援直升机转作医疗转运" },
        { title: "SDACR 135/2023 与部长答复 3779", detail: "农村 1.5–4 小时救护真空与 2003 年冻结公式" }
      ],
      auditParagraphs: [
        "国家通过公共银行持有维修垄断商 Sabena Technics 股份，导致飞机失修却无人受罚。",
        "每年夏季渡轮调兵花费 350–600 万欧元，足可在当地设立 70 至 120 个常驻专业消防岗位。"
      ],
      solutionsList: [
        "自建航空队：3 架 Fire Boss 两栖扑火机（12 分钟全岛到达）、科尔泰重型直升机及奥尔比亚 14 分钟直通走廊（援引欧洲人权公约第2条）。",
        "合并建立科尔泰统一民防指挥部 (CCPC)，通过 3 €/人登岛安全费与砍掉重复机构实现 1485 万 € 零赤字闭环。",
        "四大技术突破：FireSwarm 人工智能无人机（< 8 分钟打击）、海藻无毒阻燃剂、OEHC 重力水幕盾及新增 120 名乡村常驻消防员。"
      ],
      transmissionSlug: "enquete-23-securite-civile"
    },
    ja: {
      title: "救命の権利：もしコルシカが独自の主権的防災・消防システムを築いたら？",
      subtitle: "住民1人203ユーロ（全国平均85ユーロ）で年300万人の観光客を支えつつ、国は15分で届くオルビア消防艇の出動を禁じ5,280万ユーロを削減。",
      category: "防災・民間防衛",
      date: "2026年9月",
      author: "L'OCHJU 防災調査部門",
      chapeau: "OFGL会計データと仏上院報告書は国家の三重の失策を証明しています。住民が運営費の80%（オート＝コルスで1人年203€対全国平均85€）を負担する一方、2026年7月24日の猛暑ピークにカナデア消防艇12機中5機しか稼働せず、ボニファシオから15分のサルデーニャ島オルビア基地との直接連携もパリにより禁止されています。",
      imageCaption: "OFGL監査 / 上院報告書838・393号 / SDACR県令135/2023",
      metrics: [
        { label: "住民1人当り負担(2B)", value: "203 € / 年", sub: "全国平均85€比で+138%の重税", colorClass: "text-rose-400" },
        { label: "稼働可能カナデア", value: "12機中 5機", sub: "2026年7月24日猛暑時の実態", colorClass: "text-amber-400" },
        { label: "オルビア 対 ニーム", value: "15分 vs 1時間半", sub: "サルデーニャとの即時連携が政治的に禁止", colorClass: "text-cyan-400" },
        { label: "重複機構の浪費", value: "450万€ / 年", sub: "2つの司令部と2つの指令室を維持", colorClass: "text-emerald-400" }
      ],
      householdSummary: "国からの保険税交付金(TSCA)は2003年時点の車両台数で凍結されており、島民が2倍以上の税を負担する一方で農村部では救急車の空白時間が最大4時間発生しています。",
      proofs: [
        { title: "上院報告838・393号 & 政令2024-124", detail: "5,280万€削減、機体稼働低下、ヘリの60%が救急転用" },
        { title: "SDACR 135/2023 & 議会答弁3779", detail: "最大4時間の救急空白と2003年固定計算式" }
      ],
      auditParagraphs: [
        "整備を独占するサベナ・テクニクス(年3,000万€)には公的銀行Bpifranceを通じフランス政府自身が出資しています。",
        "夏季にフェリーで本土隊を輸送する費用(年350〜600万€)で、地元に70〜120人の常勤消防士を通年雇用できます。"
      ],
      solutionsList: [
        "独自航空隊：水陸両用Fire Boss 3機（全島12分以内到達）、コルテ重ヘリ配備、欧州人権条約2条に基づくオルビア14分緊急回廊の開設。",
        "コルテ統一民防隊(CCPC)による重複司令部の廃止（年450万€節約）と入島安全税3€等による1,485万€ゼロ赤字予算の構築。",
        "AI早期検知・FireSwarmドローン(8分以内消火)、植物由来無毒難燃剤、OEHC重力水幕シールド、農村部120名の常勤化。"
      ],
      transmissionSlug: "enquete-23-securite-civile"
    }
  },
  26: {
    it: {
      title: "Il Monopolio dei Depositi Petroliferi: L'Autopsia del Cartello dei Carburanti",
      subtitle: "Multa Antitrust da 187,5 milioni € (Decisione 25-D-07): come il cartello di Lucciana e Vazzio confisca l'IVA ridotta al 13% e sottrae 48 M€/anno ai corsi.",
      category: "ENERGIA & MONOPOLI",
      date: "Settembre 2026",
      author: "Cellula Antitrust L'OCHJU",
      chapeau: "Perché i cittadini corsi pagano il carburante 10–25 centesimi al litro in più del continente nonostante godano per legge dell'IVA ridotta al 13% invece del 20%? La Decisione n° 25-D-07 dell'Autorità della Concorrenza e 191.000 rilevazioni prezzi smascherano un cartello di stoccaggio che estrae 48 M€ all'anno dalle famiglie.",
      imageCaption: "Decisione Autorità Concorrenza 25-D-07 (187,5 M€ multa) — Depositi Vazzio & Lucciana",
      metrics: [
        { label: "Sanzione Antitrust", value: "187,5 M€", sub: "Decisione 25-D-07 del 17 nov. 2025", colorClass: "text-rose-400" },
        { label: "Prelievo illecito annuo", value: "48 M€ / anno", sub: "Sovrapprezzo di 10–25 centesimi al litro", colorClass: "text-amber-400" },
        { label: "IVA Ridotta Confiscata", value: "13% vs 20%", sub: "Vantaggio fiscale assorbito dai margini privati", colorClass: "text-cyan-400" },
        { label: "Rilevazioni Cittadine", value: "191.000 Dati", sub: "Audit comparato con i prezzi continentali", colorClass: "text-emerald-400" }
      ],
      householdSummary: "Lo Stato applica l'IVA al 13% in Corsica per compensare l'insularità, ma il monopolio privato dei due depositi petroliferi di Vazzio e Lucciana (DPLC) assorbe quel vantaggio fiscale prima ancora che arrivi alla pompa e vieta la benzina economica SP95-E10.",
      proofs: [
        { title: "Autorità Concorrenza Decisione 25-D-07", detail: "Condanna storica da 187,49 M€ contro il cartello petrolifero in Corsica" },
        { title: "Ricorso Consiglio di Stato & Tribunale Marsiglia", detail: "Articoli L. 420-1 e L. 410-2 Codice di Commercio" }
      ],
      auditParagraphs: [
        "Su 400 milioni di litri consumati ogni anno, il sovrapprezzo al netto delle tasse eccede ampiamente il costo reale del trasporto marittimo.",
        "La mancata distribuzione dell'E10 priva inoltre gli automobilisti dell'opzione più economica disponibile ovunque sul continente."
      ],
      solutionsList: [
        "Gestione pubblica strategica dei depositi di Vazzio e Lucciana con accesso trasparente e non discriminatorio.",
        "Obbligo di distribuzione immediata del carburante SP95-E10 su tutta la rete.",
        "Azioni collettive di risarcimento dei consumatori e trasportatori locali sulla base della Decisione 25-D-07."
      ],
      transmissionSlug: "enquete-26-depots-petroliers"
    },
    es: {
      title: "El Monopolio de los Depósitos Petrolíferos: Autopsia del Cártel de Carburantes",
      subtitle: "Multa récord de 187,5 M€ (Decisión 25-D-07): cómo el cártel de Lucciana y Vazzio confisca el IVA reducido del 13% y extrae 48 M€/año.",
      category: "ENERGÍA Y MONOPOLIOS",
      date: "Septiembre 2026",
      author: "Célula Antimonopolio L'OCHJU",
      chapeau: "¿Por qué las familias corsas pagan la gasolina de 10 a 25 céntimos más cara por litro pese a contar por ley con un IVA reducido del 13%? La Decisión 25-D-07 de la Autoridad de Competencia (187,5 M€ de multa) y 191.000 registros ciudadanos prueban una captura de 48 millones de euros al año.",
      imageCaption: "Decisión Autoridad de Competencia 25-D-07 — Depósitos de Vazzio y Lucciana",
      metrics: [
        { label: "Multa Antimonopolio", value: "187,5 M€", sub: "Decisión 25-D-07 de Competencia", colorClass: "text-rose-400" },
        { label: "Sobrecoste Anual", value: "48 M€ / año", sub: "+10 a +25 céntimos por litro en 400M L", colorClass: "text-amber-400" },
        { label: "IVA Reducido Capturado", value: "13% vs 20%", sub: "Beneficio fiscal retenido por el cártel", colorClass: "text-cyan-400" },
        { label: "Base Empírica Precios", value: "191.000 Logs", sub: "Comparativa frente a estaciones continentales", colorClass: "text-emerald-400" }
      ],
      householdSummary: "El IVA reducido al 13% debería abaratar el combustible en Córcega, pero el control cerrado de los terminales portuarios (DPLC) neutraliza esa ventaja en los márgenes mayoristas y bloquea la venta de gasolina económica SP95-E10.",
      proofs: [
        { title: "Decisión Antimonopolio 25-D-07", detail: "Sanción oficial de 187,49 M€ al cártel de almacenamiento DPLC" },
        { title: "Consejo de Estado y Tribunal de Marsella", detail: "Infracción de los artículos L. 420-1 y L. 410-2 del Código de Comercio" }
      ],
      auditParagraphs: [
        "El sobreprecio antes de impuestos supera con creces el coste real del flete marítimo.",
        "La ausencia de SP95-E10 obliga a los conductores a comprar combustibles más caros."
      ],
      solutionsList: [
        "Requisición o gestión pública abierta de los depósitos portuarios de Lucciana y Vazzio.",
        "Introducción obligatoria del carburante SP95-E10 en todas las gasolineras de la isla.",
        "Demandas colectivas de indemnización civil amparadas en la resolución firme 25-D-07."
      ],
      transmissionSlug: "enquete-26-depots-petroliers"
    },
    pt: {
      title: "O Monopólio dos Depósitos Petrolíferos: Autópsia do Cartel dos Combustíveis",
      subtitle: "Multa de 187,5 M€ (Decisão 25-D-07): como o cartel de Lucciana e Vazzio confisca o IVA reduzido de 13% e retira 48 M€/ano.",
      category: "ENERGIA E MONOPÓLIOS",
      date: "Setembro 2026",
      author: "Célula Antitruste L'OCHJU",
      chapeau: "Porque pagam os corsos mais 10 a 25 cêntimos por litro do que no continente apesar da taxa reduzida de IVA de 13%? A Decisão 25-D-07 da Autoridade da Concorrência e 191.000 registos de preços expõem um cartel de 37 anos que extrai 48 milhões de euros por ano às famílias.",
      imageCaption: "Decisão Autoridade Concorrência 25-D-07 — Depósitos Vazzio e Lucciana",
      metrics: [
        { label: "Coima Antitruste", value: "187,5 M€", sub: "Decisão oficial 25-D-07 (nov. 2025)", colorClass: "text-rose-400" },
        { label: "Extração Anual Ilícita", value: "48 M€ / ano", sub: "Sobretaxa de 10–25 cêntimos/litro", colorClass: "text-amber-400" },
        { label: "IVA Reduzido Absorvido", value: "13% vs 20%", sub: "Benefício fiscal desviado antes da bomba", colorClass: "text-cyan-400" },
        { label: "Registos Empíricos", value: "191.000 Dados", sub: "Auditoria comparativa de preços na bomba", colorClass: "text-emerald-400" }
      ],
      householdSummary: "O IVA reduzido de 13% criado para aliviar a insularidade acaba nos bolsos do monopólio dos depósitos de Vazzio e Lucciana, que ainda proíbe o combustível mais barato SP95-E10.",
      proofs: [
        { title: "Autoridade da Concorrência Decisão 25-D-07", detail: "Sanção de 187,49 M€ ao cartel de depósitos DPLC" },
        { title: "Conselho de Estado & Tribunal de Marselha", detail: "Violação dos arts. L. 420-1 e L. 410-2 do Código Comercial" }
      ],
      auditParagraphs: [
        "Num volume anual de 400 milhões de litros, a margem insular pré-impostos excede em muito o frete marítimo.",
        "A falta de transparência contratual prolongou-se por 37 anos sob inação regulatória."
      ],
      solutionsList: [
        "Regulação pública de acesso aberto aos terminais de Lucciana e Vazzio.",
        "Obrigatoriedade de comercialização de SP95-E10 em toda a ilha.",
        "Ações populares de restituição civil fundamentadas na Decisão 25-D-07."
      ],
      transmissionSlug: "enquete-26-depots-petroliers"
    },
    ru: {
      title: "Монополия топливных терминалов: вскрытие нефтяного картеля Корсики",
      subtitle: "Антимонопольный штраф 187,5 млн € (Решение 25-D-07): как картель Лучианы и Ваццио присваивает льготный НДС 13% и забирает 48 млн €/год.",
      category: "ЭНЕРГЕТИКА И КАРТЕЛИ",
      date: "Сентябрь 2026",
      author: "Антимонопольная ячейка L'OCHJU",
      chapeau: "Почему на Корсике топливо стоит на 10–25 центов за литр дороже материка при законодательной льготе НДС 13% вместо 20%? 80-страничное Решение 25-D-07 Антимонопольного органа и база из 191 000 замеров цен раскрывают картельный сговор на терминалах, выкачивающий 48 млн € ежегодно.",
      imageCaption: "Решение Антимонопольного органа 25-D-07 — Терминалы Лучиана и Ваццио",
      metrics: [
        { label: "Штраф картелю", value: "187,5 млн €", sub: "Решение 25-D-07 от 17.11.2025", colorClass: "text-rose-400" },
        { label: "Ежегодный ущерб", value: "48 млн € / год", sub: "Наценка 10–25 центов на 400 млн л", colorClass: "text-amber-400" },
        { label: "Присвоенный НДС", value: "13% vs 20%", sub: "Налоговая льгота уходит в маржу картеля", colorClass: "text-cyan-400" },
        { label: "База замеров цен", value: "191 000 записей", sub: "Сравнение цен с материковой Францией", colorClass: "text-emerald-400" }
      ],
      householdSummary: "Сниженный НДС 13% не доходит до водителей: закрытый контроль над двумя нефтебазами (DPLC) позволяет завышать оптовые цены и запрещать продажу дешевого бензина SP95-E10.",
      proofs: [
        { title: "Решение Антимонопольного органа 25-D-07", detail: "Штраф 187,49 млн € за сговор участников терминалов DPLC" },
        { title: "Государственный совет и Коммерческий суд", detail: "Нарушение ст. L. 420-1 и L. 410-2 Коммерческого кодекса" }
      ],
      auditParagraphs: [
        "Разница оптовой цены до налогов многократно превышает реальную стоимость морского фрахта на танкеры.",
        "Отсутствие конкуренции и государственного контроля поддерживало схему на протяжении 37 лет."
      ],
      solutionsList: [
        "Перевод портовых нефтебаз Лучианы и Ваццио под открытое публичное регулирование с недискриминационным доступом.",
        "Обязательный ввод в продажу бензина SP95-E10 на всех АЗС острова.",
        "Коллективные гражданские иски перевозчиков и граждан о компенсации ущерба на базе решения 25-D-07."
      ],
      transmissionSlug: "enquete-26-depots-petroliers"
    },
    zh: {
      title: "燃油库垄断：科西嘉燃油卡特尔 1.875 亿欧元反垄断案剖析",
      subtitle: "法国竞争管理局第 25-D-07 号重罚：卢恰纳与瓦齐奥油库垄断集团如何吞噬 13% 优惠增值税并每年抽血 4800 万欧元。",
      category: "能源与反垄断",
      date: "2026年9月",
      author: "L'OCHJU 反垄断调查组",
      chapeau: "科西嘉依法享有 13% 低增值税（大陆为 20%），为何岛民每升油却反而贵 10 至 25 欧分？80 页的竞争管理局第 25-D-07 号处罚决定（罚款 1.875 亿欧元）与 19.1 万条加油站价格监测，撕开了长达 37 年、每年套取 4800 万欧元的油库卡特尔机制。",
      imageCaption: "反垄断裁决 25-D-07 — 瓦齐奥与卢恰纳储油库垄断网",
      metrics: [
        { label: "反垄断巨额罚单", value: "1.875 亿€", sub: "2025年11月第 25-D-07 号裁决", colorClass: "text-rose-400" },
        { label: "年度超额抽血", value: "4800 万€ / 年", sub: "4亿升年销量每升溢价 10–25 欧分", colorClass: "text-amber-400" },
        { label: "被截留优惠税率", value: "13% vs 20%", sub: "减税红利全被批发垄断利润吞噬", colorClass: "text-cyan-400" },
        { label: "公民价格实测", value: "19.1 万条", sub: "对比法国本土油价的实证数据库", colorClass: "text-emerald-400" }
      ],
      householdSummary: "国家给予科西嘉的 13% 低税率优惠并未惠及居民，而是被垄断全岛两大油库的 DPLC 集团在批发环节直接吞并，且当地禁止供应平价 SP95-E10 汽油。",
      proofs: [
        { title: "竞争管理局第 25-D-07 号裁决书", detail: "对科西嘉燃油储存卡特尔处以 1.8749 亿欧元罚款" },
        { title: "法国最高行政法院与马赛商事法院", detail: "违反《商法典》L. 420-1 与 L. 410-2 条反卡特尔条款" }
      ],
      auditParagraphs: [
        "扣除税费后的离岸加价幅度远远超出实际海运成本，构成典型的地域垄断剥削。",
        "包括农村加油站在内的机场与陆路终端全部被纳入统一配额与价格控制。"
      ],
      solutionsList: [
        "对卢恰纳与瓦齐奥港油库实施公共接管或强制开放无歧视第三方仓储准入。",
        "强制全岛加油站供应价格更低的 SP95-E10 标号汽油。",
        "依据既成裁决 25-D-07，支持本地运输企业与家庭提起民事赔偿集体诉讼。"
      ],
      transmissionSlug: "enquete-26-depots-petroliers"
    },
    ja: {
      title: "石油備蓄基地の独占：コルシカ燃料カルテルのフォレンジック解剖",
      subtitle: "公取委による1億8,750万ユーロ制裁(決定25-D-07)：ルッチャナとヴァッツィオのカルテルが13%軽減VATを横取りし年4,800万ユーロを搾取する手口。",
      category: "エネルギー・独占禁止",
      date: "2026年9月",
      author: "L'OCHJU 公正取引調査部門",
      chapeau: "コルシカ島は本土(20%)より低い13%の軽減付加価値税(VAT)が法制化されているにも関わらず、なぜガソリン価格が1リットルあたり10〜25セントも高いのか？競争当局の80ページに及ぶ決定第25-D-07号（課徴金1億8,750万ユーロ）と19万1,000件の価格ログが、年4,800万ユーロを吸い上げる37年間のカルテル構造を証明しました。",
      imageCaption: "仏競争当局決定 25-D-07 — ルッチャナ・ヴァッツィオ燃料基地独占網",
      metrics: [
        { label: "独禁法制裁金", value: "1億8,750万€", sub: "2025年11月 決定25-D-07", colorClass: "text-rose-400" },
        { label: "年間不当超過利益", value: "4,800万€ / 年", sub: "年4億Lに対し1Lあたり10〜25¢上乗せ", colorClass: "text-amber-400" },
        { label: "横取りされた軽減税率", value: "13% vs 20%", sub: "島民向けの減税分を民間卸が吸収", colorClass: "text-cyan-400" },
        { label: "価格ログ実測データ", value: "191,000 件", sub: "本土価格との比較フォレンジックDB", colorClass: "text-emerald-400" }
      ],
      householdSummary: "離島負担軽減のための13%軽減VATは、島内2大貯蔵ターミナル(DPLC)の独占体制によって給油所へ届く前に吸収され、さらに安価なSP95-E10ガソリンの販売も封じられています。",
      proofs: [
        { title: "フランス競争当局 決定25-D-07号", detail: "コルシカ燃料カルテルに対し1億8,749万ユーロの課徴金命令" },
        { title: "国務院・マルセイユ経済裁判所", detail: "商法典 L.420-1条およびL.410-2条違反" }
      ],
      auditParagraphs: [
        "税引前の上乗せ幅は実際の海上輸送コストをはるかに上回っており、空港燃料から農村スタンドまで支配下に置かれていました。",
        "37年間の行政の黙認により独占価格が常態化していました。"
      ],
      solutionsList: [
        "ルッチャナおよびヴァッツィオ両燃料ターミナルの公的開放と非差別的アクセス義務化。",
        "島内全給油所における安価なSP95-E10燃料の取り扱い義務付け。",
        "確定した決定25-D-07号を根拠とする市民・運送業者による損害賠償集団訴訟の支援。"
      ],
      transmissionSlug: "enquete-26-depots-petroliers"
    }
  },
  27: {
    it: {
      title: "La Funivia Urbana 'Angelo' (Parte 1/2): Il Miraggio Finanziario e la Rendita Privata",
      subtitle: "38,26 milioni € di costruzione e 23,89 milioni € di rendita decennale al gruppo POMA mentre la rete bus urbana viene tagliata.",
      category: "INFRASTRUTTURE & POTERE",
      date: "Agosto 2026",
      author: "Cellula d'Investigazione L'OCHJU",
      chapeau: "Inaugurata nell'ottobre 2025 ad Ajaccio (Saint-Joseph – Mezzavia), la funivia 'Angelo' è costata 38,26 M€ di lavori (fino a 62 M€ consolidati) e garantisce 23,89 M€ di gestione decennale a una filiale privata con 50.000 € di capitale, coprendo solo il ~20% dei costi con i biglietti mentre i bus pubblici subiscono l'austerità.",
      imageCaption: "Audit ROB CAPA 2025 / Decreto prefettizio DUP — Funivia urbana Angelo Ajaccio",
      metrics: [
        { label: "Costo Lavori", value: "38,26 M€", sub: "Fino a 62 M€ costo consolidato", colorClass: "text-rose-400" },
        { label: "Rendita POMA (10 anni)", value: "23,89 M€", sub: "A una filiale da 50.000 € di capitale", colorClass: "text-amber-400" },
        { label: "Copertura Biglietti", value: "~20%", sub: "80% del deficit coperto dalle tasse locali", colorClass: "text-cyan-400" },
        { label: "Finanziamento Pubblico", value: "70% PTIC", sub: "Fondi statali & FEDER su opere private", colorClass: "text-emerald-400" }
      ],
      householdSummary: "I biglietti coprono solo circa un quinto delle spese di gestione: ogni anno i contribuenti di Ajaccio versano 2,39 M€ garantiti alla società privata di gestione mentre mancano autobus moderni per i quartieri.",
      proofs: [
        { title: "ROB CAPA 2025/2026 & Decreto DUP 2A-2023-12-04", detail: "38,26 M€ opere + 23,89 M€ gestione decennale garantita" },
        { title: "Portali Ufficiali PTIC / FEDER / angelo.corsica", detail: "Tasso di copertura tariffaria ufficiale al 20%" }
      ],
      auditParagraphs: [
        "L'investimento pubblico al 70% tramite PTIC ed erogazioni europee FEDER ha finanziato un'infrastruttura rigida che genera un disavanzo strutturale permanente.",
        "Il contratto di gestione tutela il margine del consorzio privato indipendentemente dal numero reale di passeggeri."
      ],
      solutionsList: [
        "Audit finanziario indipendente completo del contratto di esercizio POMA e revisione degli obiettivi di traffico.",
        "Riorientamento dei fondi pubblici sulla rete autobus urbana elettrica e sul servizio ferroviario della piana d'Ajaccio.",
        "Pubblicazione integrale di tutti gli allegati tecnici e finanziari del contratto presso la CAPA."
      ],
      transmissionSlug: "enquete-27-telepherique-angelo"
    },
    es: {
      title: "El Teleférico Urbano 'Angelo' (Parte 1/2): El Espejismo Financiero y la Renta Privada",
      subtitle: "38,26 millones € de construcción y 23,89 millones € de renta decenal a POMA mientras se asfixia a la red pública de autobuses.",
      category: "INFRAESTRUCTURAS Y PODER",
      date: "Agosto 2026",
      author: "Célula de Investigación L'OCHJU",
      chapeau: "Inaugurado en octubre de 2025 en Ajaccio, el teleférico 'Angelo' costó 38,26 M€ en obra (hasta 62 M€ consolidados) y garantiza 23,89 M€ de explotación en 10 años a una filial privada de 50.000 € de capital, cubriendo apenas el 20% con billetes mientras el autobús público sufre recortes.",
      imageCaption: "Auditoría ROB CAPA 2025 / Decreto DUP — Teleférico Angelo",
      metrics: [
        { label: "Coste Construcción", value: "38,26 M€", sub: "Hasta 62 M€ inversión total consolidada", colorClass: "text-rose-400" },
        { label: "Renta POMA (10 años)", value: "23,89 M€", sub: "Garantizada a filial de 50.000 € capital", colorClass: "text-amber-400" },
        { label: "Retorno por Billetes", value: "~20%", sub: "Déficit del 80% pagado por impuestos", colorClass: "text-cyan-400" },
        { label: "Subsidio Estatal PTIC", value: "70% + FEDER", sub: "Inversión pública para renta privada", colorClass: "text-emerald-400" }
      ],
      householdSummary: "La venta de billetes apenas cubre una quinta parte del gasto operativo: las familias de Ajaccio cargan con un déficit estructural garantizado a un consorcio privado.",
      proofs: [
        { title: "ROB CAPA 2025/2026 y Decreto DUP", detail: "38,26 M€ de obra + 2,39 M€/año garantizados durante 10 años" },
        { title: "Registros PTIC / MRAe / angelo.corsica", detail: "Tasa oficial de cobertura tarifaria del ~20%" }
      ],
      auditParagraphs: [
        "El modelo financiero traslada todo el riesgo de demanda a los presupuestos municipales mientras garantiza los ingresos del operador.",
        "Mientras tanto, la flota histórica de autobuses urbanos queda sin renovación."
      ],
      solutionsList: [
        "Auditoría pública completa del contrato concesional y renegociación de la garantía de déficit.",
        "Prioridad presupuestaria a la flota de autobuses y al eje ferroviario Ajaccio–Mezzana.",
        "Acceso ciudadano íntegro a los flujos financieros de la delegación."
      ],
      transmissionSlug: "enquete-27-telepherique-angelo"
    },
    pt: {
      title: "O Teleférico Urbano 'Angelo' (Parte 1/2): A Miragem Financeira e a Renda Privada",
      subtitle: "38,26 M€ de construção e 23,89 M€ de renda a 10 anos ao grupo POMA enquanto a rede pública de autocarros é sacrificada.",
      category: "INFRAESTRUTURAS E PODER",
      date: "Agosto 2026",
      author: "Célula de Investigação L'OCHJU",
      chapeau: "Inaugurado em outubro de 2025 em Ajaccio, o teleférico 'Angelo' custou 38,26 M€ (até 62 M€ consolidados) e assegura 23,89 M€ em 10 anos a uma filial privada com 50.000 € de capital, cobrindo apenas ~20% dos custos com bilhetes enquanto os autocarros enfrentam austeridade.",
      imageCaption: "Auditoria ROB CAPA 2025 / Decreto DUP — Teleférico Angelo",
      metrics: [
        { label: "Custo da Obra", value: "38,26 M€", sub: "Até 62 M€ consolidados", colorClass: "text-rose-400" },
        { label: "Renda POMA (10 anos)", value: "23,89 M€", sub: "A filial com 50.000 € de capital", colorClass: "text-amber-400" },
        { label: "Cobertura Bilhética", value: "~20%", sub: "80% do défice pago por impostos locais", colorClass: "text-cyan-400" },
        { label: "Financiamento Público", value: "70% PTIC", sub: "Fundos estatais e FEDER europeus", colorClass: "text-emerald-400" }
      ],
      householdSummary: "Os bilhetes cobrem só 20% dos custos: os contribuintes de Ajaccio garantem 2,39 M€/ano ao operador privado enquanto os autocarros de bairro sofrem cortes.",
      proofs: [
        { title: "ROB CAPA 2025 e Decreto DUP", detail: "38,26 M€ construção + 23,89 M€ exploração decenal" },
        { title: "Registos PTIC / MRAe / angelo.corsica", detail: "Cobertura tarifária oficial de ~20%" }
      ],
      auditParagraphs: [
        "O modelo transfere o défice estrutural permanente para o contribuinte municipal e protege o operador privado.",
        "A ligação não resolve a saturação rodoviária da entrada da cidade."
      ],
      solutionsList: [
        "Auditoria completa aos anexos financeiros da concessão POMA.",
        "Reorientação dos fundos públicos para os autocarros municipais e ferrovia urbana.",
        "Transparência mensal dos números reais de passageiros."
      ],
      transmissionSlug: "enquete-27-telepherique-angelo"
    },
    ru: {
      title: "Городская канатная дорога «Анжело» (Часть 1/2): финансовый мираж и частная рента",
      subtitle: "38,26 млн € на стройку и 23,89 млн € гарантированной ренты концерну POMA за 10 лет на фоне удушения городских автобусов.",
      category: "ИНФРАСТРУКТУРА И ВЛАСТЬ",
      date: "Август 2026",
      author: "Исследовательская ячейка L'OCHJU",
      chapeau: "Открытая в октябре 2025 года в Аяччо канатная дорога «Анжело» обошлась в 38,26 млн € (до 62 млн € консолидированно) и гарантирует 23,89 млн € дохода частной «дочке» с капиталом 50 000 € за 10 лет. Продажа билетов покрывает лишь ~20% расходов.",
      imageCaption: "Аудит ROB CAPA 2025 / Префектурный декрет DUP",
      metrics: [
        { label: "Стоимость стройки", value: "38,26 млн €", sub: "До 62 млн € общих затрат", colorClass: "text-rose-400" },
        { label: "Рента POMA (10 лет)", value: "23,89 млн €", sub: "Компании с уставным капиталом 50 тыс. €", colorClass: "text-amber-400" },
        { label: "Окупаемость билетами", value: "~20%", sub: "80% убытков покрывает местный бюджет", colorClass: "text-cyan-400" },
        { label: "Госсубсидия PTIC", value: "70% + ЕФРР", sub: "Публичные средства на частную ренту", colorClass: "text-emerald-400" }
      ],
      householdSummary: "Пассажирские билеты покрывают лишь пятую часть затрат — оставшийся структурный дефицит (2,39 млн €/год) полностью ложится на налогоплательщиков Аяччо.",
      proofs: [
        { title: "Бюджет ROB CAPA 2025 и Декрет DUP", detail: "38,26 млн € стройка + 23,89 млн € эксплуатация 10 лет" },
        { title: "Данные PTIC / MRAe / angelo.corsica", detail: "Официальный коэффициент покрытия расходов ~20%" }
      ],
      auditParagraphs: [
        "Контракт защищает доходность частного консорциума независимо от реального пассажиропотока.",
        "На этом фоне историческая сеть городских автобусов остается без финансирования."
      ],
      solutionsList: [
        "Полный финансовый аудит концессионного соглашения POMA и пересмотр гарантии дефицита.",
        "Приоритетное финансирование муниципального автобусного парка и пригородной железной дороги.",
        "Ежемесячная публикация реального пассажиропотока и чистых расходов."
      ],
      transmissionSlug: "enquete-27-telepherique-angelo"
    },
    zh: {
      title: "“安杰洛”城市缆车 (上篇 1/2)：财政幻影与私人运营年金",
      subtitle: "耗资 3826 万欧元建设，并向 POMA 私人子公司提供 10 年 2389 万欧元保底运营费，同时挤占公交预算。",
      category: "基础设施与权力",
      date: "2026年8月",
      author: "L'OCHJU 调查组",
      chapeau: "2025年10月在阿雅克肖通车的“安杰洛”城市缆车建设耗资 3826 万欧元（综合成本高达 6200 万欧元），并向一家注册资本仅 5 万欧元的私人子公司承诺 10 年 2389 万欧元运营年金；其票款收入仅能覆盖约 20% 成本。",
      imageCaption: "ROB CAPA 2025 / 省长 DUP 令 — 阿雅克肖“安杰洛”缆车",
      metrics: [
        { label: "工程建设成本", value: "3826 万€", sub: "综合负债成本高达 6200 万欧元", colorClass: "text-rose-400" },
        { label: "POMA 十年年金", value: "2389 万€", sub: "授予仅 5 万€资本金的私人子公司", colorClass: "text-amber-400" },
        { label: "票款覆盖率", value: "~20%", sub: "80% 运营亏损由地方财政兜底", colorClass: "text-cyan-400" },
        { label: "公共资金占比", value: "70% PTIC", sub: "国家与欧盟资金补贴私人固定收益", colorClass: "text-emerald-400" }
      ],
      householdSummary: "缆车门票收入仅够支付两成运营费，阿雅克肖纳税人每年需向私人运营方保底支付 239 万欧元，而市营公交车队却面临严重资金紧缩。",
      proofs: [
        { title: "CAPA 2025/2026 预算与 DUP 令", detail: "3826 万€工程费 + 2389 万€十年期运营合同" },
        { title: "PTIC / MRAe / angelo.corsica 官方披露", detail: "官方公布成本回收率仅约 20%" }
      ],
      auditParagraphs: [
        "项目 70% 由中央政府 PTIC 及欧盟基金出资，却将长期刚性亏损转嫁给阿雅克肖地方财政。",
        "无论实际客流如何，私人联合体的运营费均受合同保护。"
      ],
      solutionsList: [
        "对 POMA 特许经营合同全部财务附件进行独立公开审计并重谈亏损兜底条款。",
        "将公共资金优先重新配置给城市电动公交车队与既有市郊铁路。",
        "按月公开真实客流量与纳税人净补贴明细。"
      ],
      transmissionSlug: "enquete-27-telepherique-angelo"
    },
    ja: {
      title: "都市ロープウェイ「アンジェロ」(前編 1/2)：財政の蜃気楼と民間運営年金",
      subtitle: "建設費3,826万ユーロ・POMA社への10年間2,389万ユーロ運営保証の一方で圧迫される市営バス網。",
      category: "インフラ・権力構造",
      date: "2026年8月",
      author: "L'OCHJU 調査部門",
      chapeau: "2025年10月にアジャクシオで開業した都市ロープウェイ「アンジェロ」は建設費3,826万ユーロ（連結総コスト最大6,200万ユーロ）を要し、資本金わずか5万ユーロの民間子会社に対し10年間2,389万ユーロの運営費を保証しています。運賃収入は経費の約20%しか賄えず、歴史ある路線バスが緊縮を強いられています。",
      imageCaption: "CAPA 2025予算報告 / 県DUP令 — アンジェロ都市ロープウェイ",
      metrics: [
        { label: "建設工事費", value: "3,826万€", sub: "関連債務を含め最大6,200万€", colorClass: "text-rose-400" },
        { label: "POMA 10年契約額", value: "2,389万€", sub: "資本金5万€の民間子会社へ保証", colorClass: "text-amber-400" },
        { label: "運賃回収率", value: "約20%", sub: "残り80%の赤字を地方税で補填", colorClass: "text-cyan-400" },
        { label: "国・EU公的資金", value: "70% PTIC", sub: "公費投入による民間安定収益モデル", colorClass: "text-emerald-400" }
      ],
      householdSummary: "公式試算でも運賃による経費回収率は約20%にとどまり、実際の利用者数に関わらずアジャクシオの納税者が年約239万ユーロを民間へ支払い続ける契約構造になっています。",
      proofs: [
        { title: "CAPA 2025予算方針報告書 & DUP県令", detail: "工事費3,826万€ + 10年運営年金2,389万€" },
        { title: "PTIC / MRAe / angelo.corsica公式FAQ", detail: "公式運賃カバー率 約20%の明記" }
      ],
      auditParagraphs: [
        "建設資金の70%を国のPTIC補助金とEUのERDFで賄いながら、恒常的な赤字リスクはすべて地元自治体が負う構造です。",
        "同時に、日常交通の要である市営バスの更新は棚上げされています。"
      ],
      solutionsList: [
        "POMA運営契約の財務別紙すべての公開監査および赤字補填条項の見直し。",
        "公的予算の都市バス電化およびアジャクシオ通勤鉄道への優先配分。",
        "実際の乗車人員および公費投入額の月次完全公開。"
      ],
      transmissionSlug: "enquete-27-telepherique-angelo"
    }
  },
  28: {
    it: {
      title: "Il Naufragio della Muvitarra (Parte 2/2): Meccanica dell'Asfissia e Piano di Salvataggio",
      subtitle: "Diffida DREAL, 2,9 M€ di debiti CAPA non pagati, 63% della flotta obsoleta e 25,9 M€ di debito assorbito dalla funivia.",
      category: "INFRASTRUTTURE & TRASPORTI",
      date: "Agosto 2026",
      author: "Cellula d'Investigazione L'OCHJU",
      chapeau: "Mentre la funivia assorbe 25,9 M€ di debito pubblico, i conti fiscali e la diffida DREAL rivelano lo strangolamento della società pubblica SPL Muvitarra: 2,9 M€ di prestazioni non pagate dalla CAPA, 11 proroghe precarie e il 63% di autobus obsoleti alla vigilia della scadenza COSP.",
      imageCaption: "Audit DREAL Corsica / Bilanci SPL Muvitarra / Conti CAPA",
      metrics: [
        { label: "Debiti Non Pagati CAPA", value: "2,9 M€", sub: "Prestazioni eseguite ma non regolarizzate", colorClass: "text-rose-400" },
        { label: "Debito Funivia Assorbito", value: "25,9 M€", sub: "Sottratto agli investimenti bus", colorClass: "text-amber-400" },
        { label: "Flotta Autobus Obsoleta", value: "63%", sub: "Senza piano di rinnovo garantito", colorClass: "text-cyan-400" },
        { label: "Proroghe Contrattuali", value: "11 Atti", sub: "Gestione precaria verso il vuoto giuridico", colorClass: "text-emerald-400" }
      ],
      householdSummary: "La città ha indebolito finanziariamente i propri autobus pubblici lasciando 2,9 M€ di fatture scoperte e finanziando una navetta marittima esterna mentre dirottava i capitali sulla funivia.",
      proofs: [
        { title: "Diffida Prefettizia DREAL & Bilanci SPL", detail: "Capitale minimo DREAL 195.500 € a rischio per 2,9 M€ impagati" },
        { title: "ROB CAPA & Statuti Muvitarra", detail: "11 atti aggiuntivi al contratto COSP e 25,9 M€ di debito funivia" }
      ],
      auditParagraphs: [
        "L'indice di asfissia sistemica dimostra che la crisi dei trasporti pubblici di Ajaccio non è dovuta ai lavoratori o all'utenza, ma alla mancata regolarizzazione contabile da parte della CAPA.",
        "Il contratto allungato con 11 emendamenti successivi espone l'operatore pubblico a una paralisi legale."
      ],
      solutionsList: [
        "Regolarizzazione immediata dei 2,9 M€ dovuti dalla CAPA a SPL Muvitarra e ricapitalizzazione.",
        "Contratto COSP pluriennale di 8 anni per rinnovare il 63% della flotta autobus in elettrico.",
        "Integrazione tariffaria unica bus + treno periurbano ad Ajaccio."
      ],
      transmissionSlug: "enquete-28-naufrage-muvitarra"
    },
    es: {
      title: "El Naufragio de Muvitarra (Parte 2/2): Asfixia Financiera y Plan de Rescate Soberano",
      subtitle: "Requerimiento DREAL, 2,9 M€ impagados por la CAPA, 63% de flota obsoleta y 25,9 M€ de deuda absorbida por el teleférico.",
      category: "INFRAESTRUCTURAS Y TRANSPORTE",
      date: "Agosto 2026",
      author: "Célula de Investigación L'OCHJU",
      chapeau: "Las auditorías contables y el requerimiento oficial de la DREAL exponen el estrangulamiento financiero del operador público SPL Muvitarra: 2,9 M€ de servicios sin abonar por la CAPA, un contrato prorrogado mediante 11 adendas, 25,9 M€ de deuda desviados al teleférico y un 63% de autobuses obsoletos.",
      imageCaption: "Auditoría DREAL Córcega / Cuentas SPL Muvitarra / CAPA",
      metrics: [
        { label: "Impago de la CAPA", value: "2,9 M€", sub: "Servicios prestados sin regularizar", colorClass: "text-rose-400" },
        { label: "Deuda del Teleférico", value: "25,9 M€", sub: "Absorbida en detrimento del autobús", colorClass: "text-amber-400" },
        { label: "Flota Obsoleta", value: "63%", sub: "Autobuses urbanos envejecidos", colorClass: "text-cyan-400" },
        { label: "Adendas Precarias", value: "11 Anexos", sub: "Sin contrato COSP estable firmado", colorClass: "text-emerald-400" }
      ],
      householdSummary: "Mientras se desvían 25,9 M€ de deuda hacia el teleférico y se financia una lanzadera marítima para otro municipio, el operador público de autobuses sufre un impago de 2,9 M€ que pone en peligro el servicio diario.",
      proofs: [
        { title: "Requerimiento DREAL y Cuentas SPL", detail: "2,9 M€ adeudados frente a exigencia de capital de 195.500 €" },
        { title: "ROB CAPA y Contrato COSP", detail: "11 prórrogas consecutivas y desviación financiera Muvimare" }
      ],
      auditParagraphs: [
        "La asfixia financiera fabricada amenaza con provocar la paralización administrativa de la red de autobuses de Ajaccio.",
        "La solución técnica pasa por restituir las cuentas del operador público y frenar la sangría presupuestaria."
      ],
      solutionsList: [
        "Abono inmediato de los 2,9 M€ adeudados por la CAPA a SPL Muvitarra.",
        "Firma de un contrato público plurianual estable y plan de renovación de la flota (63%).",
        "Creación de un abono único bus-ferrocarril para toda el área metropolitana."
      ],
      transmissionSlug: "enquete-28-naufrage-muvitarra"
    },
    pt: {
      title: "O Naufrágio da Muvitarra (Parte 2/2): Asfixia Financeira e Plano de Resgate",
      subtitle: "Notificação DREAL, 2,9 M€ por pagar pela CAPA, 63% de frota obsoleta e 25,9 M€ de dívida do teleférico.",
      category: "INFRAESTRUTURAS E TRANSPORTES",
      date: "Agosto 2026",
      author: "Célula de Investigação L'OCHJU",
      chapeau: "O cruzamento contabilístico e a notificação da DREAL expõem o estrangulamento intencional da empresa pública SPL Muvitarra: 2,9 M€ de serviços não pagos pela CAPA, 11 adendas precárias, 25,9 M€ de dívida do teleférico e 63% da frota de autocarros obsoleta.",
      imageCaption: "Auditoria DREAL Córsega / Contas SPL Muvitarra / CAPA",
      metrics: [
        { label: "Dívida CAPA à Frota", value: "2,9 M€", sub: "Serviços prestados não regularizados", colorClass: "text-rose-400" },
        { label: "Dívida do Teleférico", value: "25,9 M€", sub: "Recursos desviados dos autocarros", colorClass: "text-amber-400" },
        { label: "Frota Obsoleta", value: "63%", sub: "Falta de renovação de autocarros", colorClass: "text-cyan-400" },
        { label: "Adendas Contratuais", value: "11 Atos", sub: "Precariedade à beira do vazio jurídico", colorClass: "text-emerald-400" }
      ],
      householdSummary: "O operador público de autocarros foi mantido sob asfixia orçamental com 2,9 M€ em faturas por regularizar enquanto os recursos da aglomeração iam para o teleférico.",
      proofs: [
        { title: "Notificação DREAL e Balanços SPL", detail: "2,9 M€ por pagar face ao requisito mínimo de 195.500 €" },
        { title: "ROB CAPA e Estatutos Muvitarra", detail: "11 adendas sucessivas ao COSP e desvio Muvimare" }
      ],
      auditParagraphs: [
        "O índice de asfixia financeira comprova o enfraquecimento deliberado do operador histórico público.",
        "A ausência de contrato plurianual trava a renovação de 63% dos veículos."
      ],
      solutionsList: [
        "Pagamento imediato dos 2,9 M€ em falta à SPL Muvitarra.",
        "Contrato plurianual público para renovação integral da frota obsoleta.",
        "Passe integrado único entre autocarro municipal e comboio suburbano."
      ],
      transmissionSlug: "enquete-28-naufrage-muvitarra"
    },
    ru: {
      title: "Крушение Muvitarra (Часть 2/2): механика удушения и план спасения",
      subtitle: "Предписание DREAL, 2,9 млн € долга CAPA, 63% износа автобусов и 25,9 млн € долгов канатной дороги.",
      category: "ИНФРАСТРУКТУРА И ТРАНСПОРТ",
      date: "Август 2026",
      author: "Исследовательская ячейка L'OCHJU",
      chapeau: "Финансовые отчеты и официальное предписание префектурного ведомства DREAL вскрывают искусственное удушение муниципального автобусного оператора SPL Muvitarra: 2,9 млн € невыплат со стороны агломерации CAPA, 11 временных допсоглашений, 25,9 млн € долга от канатной дороги и 63% устаревшего парка.",
      imageCaption: "Предписание DREAL / Балансы SPL Muvitarra / Отчет CAPA",
      metrics: [
        { label: "Неоплата со стороны CAPA", value: "2,9 млн €", sub: "Выполненные рейсы не оплачены", colorClass: "text-rose-400" },
        { label: "Долг канатной дороги", value: "25,9 млн €", sub: "Отток средств от автобусного парка", colorClass: "text-amber-400" },
        { label: "Износ парка автобусов", value: "63%", sub: "Критическое старение машин", colorClass: "text-cyan-400" },
        { label: "Временных продлений", value: "11 актов", sub: "Угроза правового вакуума с 1 сентября", colorClass: "text-emerald-400" }
      ],
      householdSummary: "При требуемом DREAL собственном капитале в 195,5 тыс. € невыплата 2,9 млн € со стороны CAPA ставит муниципальные автобусы на грань остановки, пока миллионы уходят на проект канатной дороги.",
      proofs: [
        { title: "Предписание DREAL и отчеты SPL", detail: "2,9 млн € долга агломерации + 25,9 млн € нагрузки канатки" },
        { title: "Бюджет ROB CAPA и устав Muvitarra", detail: "11 поправок к контракту COSP и финансирование чужого парома Muvimare" }
      ],
      auditParagraphs: [
        "Индекс системного удушения показывает, что кризис общественного транспорта вызван искусственным бюджетным голодом.",
        "Срочная нормализация контракта COSP необходима для сохранения рабочих мест и маршрутов."
      ],
      solutionsList: [
        "Немедленное погашение 2,9 млн € задолженности CAPA перед SPL Muvitarra.",
        "Заключение долгосрочного публичного контракта и обновление 63% автобусного парка.",
        "Единый городской билет на муниципальные автобусы и пригородную железную дорогу."
      ],
      transmissionSlug: "enquete-28-naufrage-muvitarra"
    },
    zh: {
      title: "穆维塔拉公交之殇 (下篇 2/2)：财政窒息机制与主权拯救方案",
      subtitle: "DREAL 限期整改令、CAPA 拖欠 290 万欧元、63% 公交车老化以及缆车项目背负 2590 万欧元债务。",
      category: "基础设施与公共交通",
      date: "2026年8月",
      author: "L'OCHJU 调查组",
      chapeau: "交叉审计税务申报与 DREAL 省府警告令，揭示城市共同体 (CAPA) 如何人为削弱公营公交 SPL Muvitarra：拖欠 290 万欧元已执行运营款、连续 11 次临时延期合同、由缆车吞噬 2590 万欧元债务，导致 63% 巴士老化并濒临 9 月 1 日合同真空。",
      imageCaption: "DREAL 警告令 / SPL Muvitarra 财务账目 / CAPA 预算",
      metrics: [
        { label: "CAPA 欠付运营款", value: "290 万€", sub: "已提供公交服务未予结算", colorClass: "text-rose-400" },
        { label: "缆车吸附债务", value: "2590 万€", sub: "挤占阿雅克肖日常公交投资", colorClass: "text-amber-400" },
        { label: "车队老化比例", value: "63%", sub: "长期缺乏新车更新投入", colorClass: "text-cyan-400" },
        { label: "临时合同展期", value: "11 次修正", sub: "公营公交面临合法性真空风险", colorClass: "text-emerald-400" }
      ],
      householdSummary: "当资金不断流向缆车及为外市服务的海上摆渡时，真正服务阿雅克肖普通居民的公营公交却被拖欠 290 万欧元，导致车队 63% 老化。",
      proofs: [
        { title: "DREAL 整改令与 SPL 财务报表", detail: "DREAL 要求 19.55 万€净资产下却被拖欠 290 万€" },
        { title: "CAPA 预算报告与 COSP 合同", detail: "11 次零碎延期与 2590 万€缆车负债压力" }
      ],
      auditParagraphs: [
        "系统性窒息指数证明公交危机并非经营低效，而是人为预算冻结所致。",
        "必须在合同到期真空前建立稳定的多年期公营服务保障。"
      ],
      solutionsList: [
        "CAPA 立即结清拖欠 SPL Muvitarra 的 290 万欧元运营款项。",
        "签署 8 年期稳定公营公交合约，分批更新 63% 老化车队。",
        "打通城市公交与阿雅克肖城际铁路“一卡通”联运。"
      ],
      transmissionSlug: "enquete-28-naufrage-muvitarra"
    },
    ja: {
      title: "ムヴィタッラ市営バスの難破 (後編 2/2)：財政窒息の仕組みと主権的救済計画",
      subtitle: "DREAL是正勧告、CAPAの290万ユーロ未払い、車両の63%老朽化、ロープウェイが吸収した2,590万ユーロの債務。",
      category: "インフラ・公共交通",
      date: "2026年8月",
      author: "L'OCHJU 調査部門",
      chapeau: "財務諸表とDREAL県是正命令の照合により、公営バス会社SPLムヴィタッラの意図的な弱体化が判明しました。CAPAによる290万ユーロの委託費未払い、11回もの暫定延長、ロープウェイによる2,590万ユーロの債務吸収により、車両の63%が老朽化し契約空白の危機に直面しています。",
      imageCaption: "DREAL是正命令 / SPLムヴィタッラ決算 / CAPA予算",
      metrics: [
        { label: "CAPA未払委託費", value: "290万€", sub: "運行済み分の未清算債務", colorClass: "text-rose-400" },
        { label: "ロープウェイ負債", value: "2,590万€", sub: "バス網更新予算を圧迫", colorClass: "text-amber-400" },
        { label: "老朽バス比率", value: "63%", sub: "深刻な車両更新の遅れ", colorClass: "text-cyan-400" },
        { label: "暫定契約延長", value: "11回の改定", sub: "法的空白の危機に直面", colorClass: "text-emerald-400" }
      ],
      householdSummary: "ロープウェイ事業や他自治体向け海上シャトルへ予算が流用される一方、市民の足である公営バスは290万ユーロの未払いにより車両の63%が老朽化しています。",
      proofs: [
        { title: "DREAL是正命令 & SPL財務諸表", detail: "自己資本要件19.55万€に対し290万€の未収金" },
        { title: "CAPA予算報告 & COSP契約記録", detail: "11回の連続暫定延長と2,590万€のロープウェイ債務" }
      ],
      auditParagraphs: [
        "構造的窒息指数は、公営バスの危機が現場ではなく都市共同体(CAPA)の会計措置によって引き起こされたことを示しています。",
        "安定的な複数年公共サービス契約の締結が急務です。"
      ],
      solutionsList: [
        "CAPAからSPLムヴィタッラへの未払金290万ユーロの即時精算。",
        "老朽車両63%を更新するための安定的な複数年公営契約の締結。",
        "市営バスとアジャクシオ近郊鉄道の共通運賃統合の実現。"
      ],
      transmissionSlug: "enquete-28-naufrage-muvitarra"
    }
  }
};

export function getUiLabels(lang: string): UiLabels {
  const key = (['it', 'es', 'pt', 'ru', 'zh', 'ja'].includes(lang) ? lang : 'it') as Lang6;
  return uiLabels[key];
}

export function getTranslatedEnquete(id: number, lang: string): TranslatedEnquete | null {
  const key = (['it', 'es', 'pt', 'ru', 'zh', 'ja'].includes(lang) ? lang : 'it') as Lang6;
  const item = dataById[id]?.[key];
  if (!item) return null;
  return {
    title: item.title,
    subtitle: item.subtitle,
    category: item.category,
    date: item.date,
    author: item.author,
    chapeau: item.chapeau,
    imageCaption: item.imageCaption,
    bodyHtml: renderHtml(key, item)
  };
}
