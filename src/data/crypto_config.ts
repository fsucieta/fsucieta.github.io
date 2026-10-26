/**
 * REGISTRE SOUVERAIN DE FINANCEMENT CITOYEN — L'OCHJU
 * 
 * Ce fichier centralise :
 * 1. Le protocole Carte Bancaire découplé par Bon Prépayé Azteco (Air-Gap financier total).
 * 2. Les trois rails cryptographiques directs vérifiés mathématiquement :
 *    - 01 : Monero (XMR) — Somme Keccak-256 vérifiée (0163dd84, Mainnet 0x12).
 *    - 02 : USDC / EURC (Polygon PoS) — Somme EIP-55 vérifiée, conforme MiCA 2026.
 *    - 03 : Bitcoin (BTC) — Somme BIP-0173 Bech32 vérifiée (polymod = 1, Native SegWit).
 */

export type CryptoRailId = 'xmr' | 'usdc' | 'btc';

export interface CryptoWalletConfig {
  /** Identifiant interne unique du rail */
  id: CryptoRailId;
  /** Numéro d'ordre affiché dans l'interface */
  rank: string;
  /** Nom complet affiché */
  name: string;
  /** Symbole monétaire */
  symbol: string;
  /** Réseau technique exact à utiliser par le donateur */
  network: string;
  /** Clé publique de réception vérifiée hors-ligne */
  address: string;
  /** État d'activation du QR Code et de la copie */
  configured: boolean;
  /** Mention technique courte d'en-tête */
  badge: string;
  /** Classes Tailwind sobres associées au niveau de confidentialité */
  accentClasses: {
    border: string;
    badge: string;
    text: string;
    button: string;
  };
  /** Description factuelle et avertissement de transparence blockchain */
  description: string;
  /** Niveau de protection cryptographique sur le registre public */
  ledgerVisibility: string;
}

/**
 * Configuration ordonnée des 3 portefeuilles non-custodiaux de la Cellule
 */
export const CRYPTO_WALLETS: CryptoWalletConfig[] = [
  {
    id: 'xmr',
    rank: '01',
    name: 'Monero',
    symbol: 'XMR',
    network: 'Monero Mainnet (RingCT / Stealth Addresses)',
    address: '4Az8HHC47BndQp1t8reNiMMvKpWx55RuuP4nnEXFhYoEcP826Sb3gwZLk4AKu2erEtChqphf4LQYbHwzZFfUkXc491doTwq',
    configured: true,
    badge: 'STANDARD SOUVERAIN — 100 % OPAQUE',
    accentClasses: {
      border: 'border-cyan-500/40 hover:border-cyan-400/70',
      badge: 'bg-cyan-500/10 text-cyan-300 border-cyan-500/30',
      text: 'text-cyan-300',
      button: 'bg-cyan-500/15 hover:bg-cyan-500/25 text-cyan-200 border-cyan-500/40'
    },
    description:
      "Recommandé en priorité. Le protocole Monero masque mathématiquement l'émetteur, le destinataire et le montant transféré. Aucun tiers ne peut auditer le solde de la cellule.",
    ledgerVisibility: 'Registre chiffré (solde et flux invisibles)'
  },
  {
    id: 'usdc',
    rank: '02',
    name: 'USDC / EURC',
    symbol: 'USDC',
    network: 'Polygon PoS uniquement (EVM)',
    address: '0xE0Dc2B00B9519cc66e4c80aaEFAab26D28eBb05C',
    configured: true,
    badge: 'STABLECOIN AGRÉÉ MiCA — SANS VOLATILITÉ',
    accentClasses: {
      border: 'border-emerald-500/40 hover:border-emerald-400/70',
      badge: 'bg-emerald-500/10 text-emerald-300 border-emerald-500/30',
      text: 'text-emerald-300',
      button: 'bg-emerald-500/15 hover:bg-emerald-500/25 text-emerald-200 border-emerald-500/40'
    },
    description:
      "Actif à valeur fixe (parité euro/dollar) conforme au règlement européen MiCA 2026, contrairement à l'USDT délisté en France. Frais de réseau Polygon inférieurs à 0,05 €.",
    ledgerVisibility: 'Registre Polygon public (privilégier un portefeuille personnel)'
  },
  {
    id: 'btc',
    rank: '03',
    name: 'Bitcoin',
    symbol: 'BTC',
    network: 'Bitcoin Mainnet (Native SegWit Bech32)',
    address: 'bc1q7hthg2xv44rdwd7xq5jn6mceqlx9n45d7stl28',
    configured: true,
    badge: 'RÉSERVE UNIVERSELLE INCENSURABLE',
    accentClasses: {
      border: 'border-amber-500/40 hover:border-amber-400/70',
      badge: 'bg-amber-500/10 text-amber-300 border-amber-500/30',
      text: 'text-amber-300',
      button: 'bg-amber-500/15 hover:bg-amber-500/25 text-amber-200 border-amber-500/40'
    },
    description:
      "Réseau décentralisé mondial. La chaîne Bitcoin étant publiquement consultable, privilégiez le Bon Prépayé Azteco (Volet 01) ou Monero si vous exigez une coupure totale.",
    ledgerVisibility: 'Registre Bitcoin public (transparent)'
  }
];

/**
 * Configuration du Pont Carte Bancaire Air-Gap (Bons Prépayés Azteco)
 */
export const VOUCHER_CONFIG = {
  /** Montants standards des bons Azteco disponibles en Euros */
  denominationsEur: [10, 25, 50, 100],
  /** Distributeur européen de clés numériques & jeux (CB / Apple Pay / PayPal sans KYC crypto) */
  primaryResellerUrl: 'https://deal.kinguin.net/azteco',
  primaryResellerName: 'Kinguin (Partenaire Officiel Azteco)',
  /** Répertoire officiel Azteco (autres revendeurs et points de vente espèces) */
  officialDirectoryUrl: 'https://azte.co/buy',
  /** Canal sécurisé de remise du code à 16 chiffres à la Cellule */
  relayEndpoint: 'https://formsubmit.co/fsucieta@tutamail.com',
  directEncryptedEmail: 'fsucieta@tutamail.com'
};
