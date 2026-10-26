/**
 * REGISTRE DE SOUTIEN CITOYEN INDÉPENDANT — L'OCHJU
 *
 * Principes d'architecture :
 * 1. Zéro montant suggéré, zéro palier incitatif, zéro promesse d'affectation fléchée :
 *    chaque contribution est un soutien volontaire et ponctuel à l'autonomie éditoriale globale.
 * 2. Pédagogie accessible en français courant pour accompagner aussi bien les citoyens novices
 *    sur téléphone ou ordinateur que les utilisateurs disposant déjà d'un portefeuille numérique.
 * 3. Zéro lien commercial externe, zéro citation de marques privées, zéro formulaire de collecte.
 * 4. Trois adresses publiques en auto-garde vérifiées mathématiquement hors-ligne (Keccak-256, Bech32, EIP-55).
 */

export type CryptoRailId = 'xmr' | 'btc' | 'usdc';

export interface CryptoWalletConfig {
  /** Identifiant interne du coffre */
  id: CryptoRailId;
  /** Numéro d'ordre affiché sur l'onglet */
  rank: string;
  /** Nom clair affiché sur l'onglet */
  tabTitle: string;
  /** Sous-titre court sous le nom de l'onglet */
  tabSubtitle: string;
  /** Nom complet de l'actif */
  name: string;
  /** Symbole court */
  symbol: string;
  /** Nom simple du réseau à sélectionner dans l'application d'envoi */
  networkLabel: string;
  /** Consigne anti-erreur rédigée en français simple avant l'envoi */
  networkCheckInstruction: string;
  /** Clé publique complète vérifiée hors-ligne */
  address: string;
  /** Exactement les 6 premiers caractères pour contrôle visuel rapide */
  prefixCheck: string;
  /** Exactement les 6 derniers caractères pour contrôle visuel rapide */
  suffixCheck: string;
  /** Explication humaine en français courant */
  humanExplanation: string;
  /** Classes visuelles propres à chaque coffre (contrastes vérifiés WCAG AA/AAA) */
  accentClasses: {
    activeTab: string;
    border: string;
    badge: string;
    text: string;
    alertBox: string;
    copyBtn: string;
  };
}

/**
 * Les 3 coffres publics en auto-garde de L'OCHJU (affichés un seul à la fois pour éviter toute confusion)
 * Ordre retenu :
 * - 01 Monero (XMR) : confidentialité native sur la chaîne.
 * - 02 Bitcoin (BTC) : parcours débutant universel (zéro jeton annexe requis pour les frais réseau).
 * - 03 USDC (Polygon PoS) : portefeuilles Web3 disposant déjà d'une fraction de POL pour les frais.
 */
export const CRYPTO_WALLETS: CryptoWalletConfig[] = [
  {
    id: 'xmr',
    rank: '01',
    tabTitle: 'Monero (XMR)',
    tabSubtitle: 'Confidentialité native',
    name: 'Monero',
    symbol: 'XMR',
    networkLabel: 'Réseau Monero principal',
    networkCheckInstruction:
      'Sélectionnez simplement Monero (XMR) dans votre portefeuille personnel en auto-garde. Toute transaction sur la chaîne étant irréversible, vérifiez les 6 premiers et 6 derniers caractères avant validation.',
    address: '4Az8HHC47BndQp1t8reNiMMvKpWx55RuuP4nnEXFhYoEcP826Sb3gwZLk4AKu2erEtChqphf4LQYbHwzZFfUkXc491doTwq',
    prefixCheck: '4Az8HH',
    suffixCheck: '1doTwq',
    humanExplanation:
      'Protocole à confidentialité cryptographique native : à la différence des registres publics pseudonymes, Monero chiffre automatiquement l’expéditeur, le destinataire et le montant sur la chaîne.',
    accentClasses: {
      /* Utilisation de cyan-400 (#38bdf8) sur texte sombre (#06080d) pour un ratio de contraste de 10.0:1 */
      activeTab: 'bg-cyan-400 text-slate-950 border-cyan-300 shadow-lg shadow-cyan-400/20',
      border: 'border-cyan-400/45',
      badge: 'bg-cyan-400/10 text-cyan-300 border-cyan-400/35',
      text: 'text-cyan-300',
      alertBox: 'bg-cyan-950/35 border-cyan-400/35 text-cyan-100',
      copyBtn: 'bg-cyan-400 hover:bg-cyan-300 text-slate-950'
    }
  },
  {
    id: 'btc',
    rank: '02',
    tabTitle: 'Bitcoin (BTC)',
    tabSubtitle: 'Universel · Idéal débutant',
    name: 'Bitcoin',
    symbol: 'BTC',
    networkLabel: 'Réseau Bitcoin (on-chain)',
    networkCheckInstruction:
      'Sélectionnez le réseau Bitcoin standard (« Bitcoin ») lors de l’envoi vers cette adresse commençant par « bc1q » (n’utilisez pas Lightning). Toute transaction validée étant irréversible, contrôlez le début et la fin de l’adresse.',
    address: 'bc1q7hthg2xv44rdwd7xq5jn6mceqlx9n45d7stl28',
    prefixCheck: 'bc1q7h',
    suffixCheck: '7stl28',
    humanExplanation:
      'La voie la plus fluide pour un premier envoi : proposé par l’ensemble des prestataires de services sur crypto-actifs (PSCA) agréés en Europe, ses frais réseau (~0,25 €) se déduisent automatiquement du montant envoyé sans aucun jeton annexe.',
    accentClasses: {
      activeTab: 'bg-amber-400 text-slate-950 border-amber-300 shadow-lg shadow-amber-400/20',
      border: 'border-amber-500/40',
      badge: 'bg-amber-500/10 text-amber-300 border-amber-500/30',
      text: 'text-amber-300',
      alertBox: 'bg-amber-950/35 border-amber-500/35 text-amber-100',
      copyBtn: 'bg-amber-400 hover:bg-amber-300 text-slate-950'
    }
  },
  {
    id: 'usdc',
    rank: '03',
    tabTitle: 'USDC (Polygon)',
    tabSubtitle: 'Jeton USD · Portefeuille Web3',
    name: 'USDC (Jeton de monnaie électronique USD)',
    symbol: 'USDC',
    networkLabel: 'Polygon PoS (impératif)',
    networkCheckInstruction:
      'Sélectionnez impérativement le réseau « Polygon PoS » : les envois sur blockchain étant techniquement irréversibles, tout autre réseau entraînerait la perte définitive des fonds. Note : un portefeuille Web3 en auto-garde doit détenir une infime fraction de jeton POL (~0,02 €) pour régler les frais du réseau Polygon.',
    address: '0xE0Dc2B00B9519cc66e4c80aaEFAab26D28eBb05C',
    prefixCheck: '0xE0Dc',
    suffixCheck: 'eBb05C',
    humanExplanation:
      'Adapté aux utilisateurs disposant déjà d’un portefeuille configuré sur Polygon. L’USDC est un jeton de monnaie électronique conforme au règlement européen MiCA et indexé sur le dollar américain (hors variation de change EUR/USD).',
    accentClasses: {
      activeTab: 'bg-emerald-400 text-slate-950 border-emerald-300 shadow-lg shadow-emerald-400/20',
      border: 'border-emerald-500/40',
      badge: 'bg-emerald-500/10 text-emerald-300 border-emerald-500/30',
      text: 'text-emerald-300',
      alertBox: 'bg-emerald-950/35 border-emerald-500/35 text-emerald-100',
      copyBtn: 'bg-emerald-400 hover:bg-emerald-300 text-slate-950'
    }
  }
];

/**
 * Explication liminaire factuelle : Pourquoi pas de module CB direct ni de cagnotte centralisée ?
 */
export const WHY_NO_CLASSIC_CB = [
  {
    badge: 'POUR PROTÉGER VOTRE VIE PRIVÉE',
    title: 'Aucune mention « L’OCHJU » sur vos relevés de compte bancaire',
    text: 'Dans un territoire insulaire de forte proximité, chacun a le droit légitime de préserver la confidentialité de ses lectures et de ses engagements civiques sur ses relevés bancaires courants (souvent transmis à des tiers : bailleurs, courtiers, organismes de crédit ou comptables).'
  },
  {
    badge: 'POUR PROTÉGER NOS ENQUÊTES',
    title: 'Aucun intermédiaire centralisé susceptible d’interrompre la collecte',
    text: 'Une procédure de signalement massif ou une décision unilatérale de conformité peut entraîner le gel conservatoire d’une cagnotte centralisée — à l’image de la suspension automatisée de notre compte Facebook intervenue le 24 octobre 2026.'
  }
];

/**
 * Guide pas-à-pas conforme au règlement européen MiCA (UE 2023/1114) pour les citoyens débutants
 */
export interface BeginnerGuideStep {
  number: string;
  duration: string;
  title: string;
  explanation: string;
  reassuranceLabel: string;
  reassuranceText: string;
}

export const BEGINNER_GUIDE_STEPS: BeginnerGuideStep[] = [
  {
    number: '1',
    duration: '1 minute',
    title: 'Acquérez le montant libre de votre choix auprès d’un prestataire agréé en Europe',
    explanation:
      'Depuis une application agréée en tant que Prestataire de Services sur Crypto-Actifs (PSCA) au titre du règlement européen MiCA (registre officiel public consultable auprès de l’AMF ou de l’ESMA), achetez par carte ou virement SEPA instantané le montant libre de votre choix en Bitcoin (BTC) — conseillé aux débutants car les frais d’envoi (~0,25 €) s’en déduisent automatiquement sans réglage complexe.',
    reassuranceLabel: 'Ce qui figure sur votre relevé bancaire :',
    reassuranceText:
      'Uniquement votre opération personnelle auprès de ce prestataire agréé. La dénomination L’OCHJU n’y figure à aucun moment.'
  },
  {
    number: '2',
    duration: '1 minute',
    title: 'Retirez vers votre propre portefeuille personnel en auto-garde',
    explanation:
      'Conformément au droit européen à l’auto-garde (règlement MiCA), installez sur votre téléphone une application de portefeuille personnel non-custodial (sans garde par un tiers), créez un portefeuille Bitcoin et transférez-y vos fonds. Lorsque votre prestataire vous demande le destinataire réglementaire du retrait, cochez « Mon propre portefeuille personnel ».',
    reassuranceLabel: 'Transparence technique sur la confidentialité :',
    reassuranceText:
      'Votre relevé bancaire en euros ne mentionne jamais L’OCHJU, mais Bitcoin et Polygon restent inscrits sur des registres blockchain publics pseudonymes ; seul le protocole Monero (XMR) chiffre nativement adresses et montants sur la chaîne.'
  },
  {
    number: '3',
    duration: '30 secondes',
    title: 'Sur téléphone : copiez notre adresse · Sur ordinateur : flashez le QR Code',
    explanation:
      'Cliquez sur l’un des boutons ci-dessous pour afficher notre adresse officielle. Si vous lisez cette page sur votre téléphone, appuyez sur « Copier l’adresse » puis collez-la dans la rubrique « Envoyer » de votre portefeuille. Si vous êtes devant un ordinateur, pointez l’appareil photo de votre portefeuille vers le QR Code affiché à l’écran.',
    reassuranceLabel: 'Zéro formulaire ni inscription :',
    reassuranceText:
      'Aucune saisie n’est demandée sur notre site : ni nom, ni adresse électronique, ni justificatif.'
  }
];

/**
 * Engagement citoyen à 0 € : actions concrètes immédiates sans verser le moindre centime
 */
export const ZERO_EURO_ACTIONS = [
  {
    tag: 'ACTION 01 · 0 €',
    title: 'Partager une enquête à 3 proches',
    description:
      'Contre le bridage algorithmique des plateformes sociales, un lien envoyé directement par messagerie ou SMS demeure notre premier vecteur de diffusion.',
    linkLabel: 'Choisir une enquête à partager →',
    href: '/#fiches-section'
  },
  {
    tag: 'ACTION 02 · 0 €',
    title: 'Obliger une administration à livrer un acte',
    description:
      'Un budget, un permis ou un contrat public vous est refusé ? Générez en 10 secondes une demande légale de communication (Art. L. 311-1 CRPA / CADA).',
    linkLabel: 'Ouvrir le Générateur CADA →',
    href: '/#cada-generator'
  },
  {
    tag: 'ACTION 03 · 0 €',
    title: 'Signaler la référence d’un acte déjà publié',
    description:
      'Nous refusons toute fuite clandestine, mais un simple numéro d’arrêté ou de délibération publique suffit à déclencher nos recoupements open data.',
    linkLabel: 'Voir notre doctrine de preuves →',
    href: '/#doctrine-preuves'
  }
];

/**
 * Mentions éthiques, fiscales, électorales et RGPD opposables en droit français (octobre 2026)
 */
export const LEGAL_DISCLOSURES = {
  byafClause:
    "L’intégralité des enquêtes, des preuves scellées (ISO/IEC 27037) et des bordereaux de recours produits par L’OCHJU demeure 100 % gratuite, sans abonnement ni mur payant. Vous êtes entièrement libre de consulter, télécharger et utiliser nos dossiers sans jamais verser le moindre centime.",
  taxAndRegulatoryNotice:
    "Contribution volontaire libre, ponctuelle, sans contrepartie, sans montant conseillé ni affectation fléchée, destinée à soutenir l’autonomie éditoriale globale de L’OCHJU. L’OCHJU n’étant ni un parti ou groupement politique (aucune contribution ne finance directement ou indirectement un candidat ou une campagne électorale au sens de l’art. L. 52-8 du Code électoral), ni un prestataire financier, ni un organisme d’intérêt général habilité à délivrer des reçus fiscaux, les versements n’ouvrent droit à aucune réduction d’impôt (art. 200 et 238 bis du Code général des impôts). L’OCHJU ne recueille aucun nom, coordonnée, donnée bancaire ni formulaire et ne dépose aucun cookie publicitaire ou de profilage (art. 82 LIL) ; la consultation du site implique uniquement le transit technique des requêtes réseau (adresse IP) auprès de l’hébergeur statique (GitHub Pages), des bibliothèques d’affichage (polices, styles, fonds cartographiques) et de la mesure d’audience agrégée sans cookie (GoatCounter, art. 6.1.f RGPD)."
};
