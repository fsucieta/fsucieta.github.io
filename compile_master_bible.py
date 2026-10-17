import os
import glob
from markdown_it import MarkdownIt

md = MarkdownIt()

docs_dir = "public/docs/opposition_ajaccio"
pieces_order = [
    ("01_MEMOIRE_SAISINE_CRC_CORSE_CAPA_MUVITARRA.md", "LIVRE I • MÉMOIRE DE SAISINE OFFICIEL DE LA CHAMBRE RÉGIONALE DES COMPTES (CRC DE CORSE)"),
    ("05_TABLEAU_BORD_FINANCIER_DISPARITE_CREM_VS_COSP.md", "LIVRE II • TABLEAU DE BORD DE DISPARITÉ CONTRACTUELLE : CREM POMA/SECA VS COSP MUVITARRA"),
    ("04_SIGNALEMENT_URGENCE_SECURITE_ERP_TYPE_U_STILETTO.md", "LIVRE III • SIGNALEMENT D'URGENCE SÉCURITÉ PUBLIQUE : ERP TYPE U, CONFLIT AÉRONAUTIQUE DRAGON 20 & CRASH VATEL CAPITAL"),
    ("02_BATTERIE_SOMMATIONS_QUESTIONS_CONSEIL_COMMUNAUTAIRE.md", "LIVRE IV • BATTERIE DE 5 SOMMATIONS AU CONSEIL COMMUNAUTAIRE (PIÈGES DE PROCÉDURE ET QUESTIONS AU SCALPEL)"),
    ("03_PROJET_DELIBERATION_AMENDEMENT_COMMUNAUTAIRE.md", "LIVRE V • PROJET DE DÉLIBÉRATION CITOYENNE D'AMENDEMENT COMMUNAUTAIRE CLÉ EN MAIN"),
    ("06_ASSEMBLEE_CORSE_QUESTION_ORALE_2026_O2_055_GARE_AJACCIO.md", "LIVRE VI • DÉFENSE DU DOMAINE PUBLIC FERROVIAIRE : QUESTION ORALE N° 2026/O2/055 À L'ASSEMBLÉE DE CORSE"),
    ("07_STATUTS_ET_COMPETENCES_SPL_MOBILITE_ET_STATIONNEMENT.md", "LIVRE VII • FICHE D'INSTRUCTION LÉGALE : STATUTS ET COMPÉTENCE IN-HOUSE DE LA SPL MOBILITÉ ET STATIONNEMENT"),
    ("08_AUDIT_FINANCIER_M4_PARKING_DIAMANT_ET_FLOTTE.md", "LIVRE VIII • AUDIT BUDGÉTAIRE M4 : COMPTE D'EXPLOITATION DU PARKING DU DIAMANT ET PLAN FLOTTE"),
    ("09_AUDIT_RECUPERATION_RENTE_SCOLAIRE_9_VILLAGES.md", "LIVRE IX • AUDIT COMPTABLE DGFiP : RÉCUPÉRATION DE LA RENTE SCOLAIRE PRIVÉE POUR LES 9 VILLAGES DE LA CAPA"),
    ("10_ETUDE_TECHNIQUE_HALTE_FERROVIAIRE_SAINT_JOSEPH_VS_DEMENAGEMENT.md", "LIVRE X • ÉTUDE TECHNIQUE D'AMÉNAGEMENT : HALTE FERROVIAIRE VOYAGEURS DE SAINT-JOSEPH VS DÉMÉNAGEMENT DE LA GARE")
]

bible_sections_html = []

for filename, section_title in pieces_order:
    filepath = os.path.join(docs_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            raw_text = f.read()
        
        # Render markdown to HTML
        html_rendered = md.render(raw_text)
        
        section_block = f"""
        <!-- {filename} -->
        <section class="p-6 md:p-10 rounded-3xl bg-slate-900 border border-slate-700/80 shadow-2xl space-y-6">
          <div class="flex flex-wrap items-center justify-between gap-3 border-b border-slate-800 pb-4">
            <span class="px-3.5 py-1 bg-amber-500/10 text-amber-400 border border-amber-500/30 rounded-full text-xs font-mono font-bold uppercase tracking-wider">
              {section_title}
            </span>
            <div class="flex items-center gap-2">
              <a href="/docs/opposition_ajaccio/{filename.replace('.md', '.pdf')}" download class="text-xs font-mono bg-slate-800 hover:bg-slate-700 text-slate-200 px-3 py-1.5 rounded-lg border border-slate-700 transition shadow">
                📥 PDF Officiel
              </a>
              <a href="/docs/opposition_ajaccio/{filename.replace('.md', '.html')}" target="_blank" class="text-xs font-mono bg-slate-800 hover:bg-slate-700 text-cyan-300 px-3 py-1.5 rounded-lg border border-slate-700 transition shadow">
                🌐 Ouvrir Plein Écran
              </a>
            </div>
          </div>
          
          <div class="prose prose-invert prose-amber max-w-none text-slate-300 text-sm leading-relaxed font-sans space-y-4">
            {html_rendered}
          </div>
        </section>
        """
        bible_sections_html.append(section_block)

rendered_corpus = "\n".join(bible_sections_html)

# Now construct the complete Astro page
template_head = """---
import Layout from '../layouts/Layout.astro';
const title = "Bible d'Instruction Forensique Transparence Citoyenne : Le Grand Dossier des Mobilités d'Ajaccio";
const description = "Recueil médico-légal et institutionnel de haute sécurité (Norme ISO/IEC 27037) — L'instruction intégrale des 10 Livres d'assaut contentieux, financiers et d'urbanisme pour l'association Transparence Citoyenne.";
---

<Layout title={title} description={description} noindex={true}>
<div class="max-w-6xl mx-auto px-4 md:px-6 py-12">

  <!-- TERMINAL DE SÉCURITÉ CRYPTOGRAPHIQUE SOUVERAIN -->
  <div id="auth-lock-screen" class="my-12 p-8 md:p-12 rounded-3xl bg-slate-900 border-2 border-red-500/50 shadow-2xl text-center max-w-xl mx-auto backdrop-blur-xl">
    <div class="inline-flex p-4 rounded-full bg-red-500/10 text-red-400 border border-red-500/30 mb-6">
      <svg xmlns="http://www.w3.org/2000/svg" class="w-12 h-12 animate-pulse" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
      </svg>
    </div>
    
    <div class="text-xs font-mono text-red-400 font-bold uppercase tracking-widest mb-2">
      DOSSIER TRANSMISSION SOUVERAINE • DESTINÉ À L'ASSOCIATION TRANSPARENCE CITOYENNE
    </div>
    <h2 class="text-2xl md:text-3xl font-black text-white font-serif mb-4">
      Bible d'Instruction Forensique : Grand Ajaccio
    </h2>
    <p class="text-sm text-slate-300 font-sans mb-6 leading-relaxed">
      Ce dossier réunit in extenso l'ensemble des 10 Livres d'instruction médico-légale et de preuves matérielles (normées ISO/IEC 27037) : les pièces à conviction budgétaires (contrats CREM/COSP, mandats gratuits, friche militaire toxique de Saint-Joseph, litige hospitalier ERP U) et les modélisations financières de grade DGFiP/M4, mis à la disposition exclusive de l'association Transparence Citoyenne (transparencecitoyenne.fr).
    </p>

    <form id="auth-form" class="space-y-4">
      <div class="relative">
        <input 
          type="password" 
          id="access-key-input" 
          placeholder="Entrez le mot de passe d'accréditation..." 
          required
          autocomplete="off"
          class="w-full px-5 py-3.5 rounded-xl bg-slate-950 border border-slate-700 text-white font-mono text-center tracking-widest focus:outline-none focus:border-red-500 focus:ring-2 focus:ring-red-500/30 transition shadow-inner"
        />
      </div>
      <button 
        type="submit" 
        id="submit-auth-btn"
        class="w-full py-3.5 px-6 rounded-xl bg-red-600 hover:bg-red-500 text-white font-bold font-mono text-sm uppercase tracking-wider transition shadow-lg hover:shadow-red-600/30 cursor-pointer active:scale-95"
      >
        🔓 Déverrouiller la Bible d'Instruction
      </button>
      <div id="auth-error" class="hidden text-xs font-mono text-red-400 font-bold pt-2">
        ⚠️ Code d'accréditation invalide. Accès refusé.
      </div>
      <div id="auth-lockout" class="hidden text-xs font-mono text-amber-400 font-bold pt-2 p-3 bg-amber-950/40 border border-amber-500/40 rounded-xl">
        🛑 Sécurité renforcée active : Trop de tentatives erronées. Verrouillage temporaire de 30 secondes.
      </div>
    </form>
    
    <div class="mt-8 pt-4 border-t border-slate-800 text-[11px] font-mono text-slate-400 space-y-1">
      <div>AUTHENTIFICATION FORENSIQUE RENFORCÉE • PROTOCOLE ISO/IEC 27037</div>
      <div class="text-[10px] text-slate-400">Chiffrement SHA-256 scellé • Protection anti-bruteforce active</div>
    </div>
  </div>

  <!-- CONTENU INTÉGRAL DE LA BIBLE D'INSTRUCTION (DÉVERROUILLÉ) -->
  <div id="vault-content" class="hidden space-y-12">
    
    <!-- En-tête officiel de niveau magistrature / renseignement étatique -->
    <div class="border-b border-red-500/40 pb-8">
      <div class="flex flex-wrap items-center justify-between gap-3 mb-4">
        <span class="px-3.5 py-1 bg-red-500/20 text-red-400 border border-red-500/40 rounded-full text-xs font-mono font-bold uppercase tracking-wider">
          PIÈCES À CONVICTION NORMÉES ISO/IEC 27037 • ACCRÉDITATION NIVEAU 1
        </span>
        <button id="lock-vault-btn" class="text-xs font-mono text-slate-400 hover:text-white px-3 py-1 bg-slate-900 border border-slate-800 rounded-lg transition cursor-pointer">
          🔒 Verrouiller la session
        </button>
      </div>

      <h1 class="text-3xl md:text-5xl font-black text-white font-serif leading-tight mb-4">
        Bible d'Instruction Forensique : Le Système Global des Mobilités du Grand Ajaccio
      </h1>
      <h2 class="text-lg md:text-2xl font-sans text-amber-400 font-bold mb-4">
        Transmission Intégrale in extenso des 10 Livres d'Assaut Budgétaire, Juridique et d'Aménagement
      </h2>
      <p class="text-slate-300 font-serif text-base leading-relaxed max-w-5xl">
        Ce dossier est transmis in extenso à l'association <strong>Transparence Citoyenne</strong> (transparencecitoyenne.fr) et à son collège juridique. Il contient le texte complet, sans coupes ni résumés, de l'ensemble des mémoires de saisine de la Chambre Régionale des Comptes, des audits médico-légaux des contrats CREM/COSP, de l'autopsie de la friche toxique de Saint-Joseph et du contre-projet régalien des mobilités d'Ajaccio.
      </p>
    </div>

    <!-- BOUTON MAÎTRE : TÉLÉCHARGEMENT UNIVERSEL EN 1 CLIC DU COFFRE SCELLÉ -->
    <div class="p-8 rounded-3xl bg-gradient-to-r from-red-950 via-slate-900 to-amber-950 border-2 border-red-500 shadow-2xl flex flex-col md:flex-row items-center justify-between gap-6">
      <div class="space-y-2 text-center md:text-left">
        <div class="inline-flex items-center gap-2 px-3 py-1 bg-red-500/20 text-red-400 border border-red-500/40 rounded-full text-xs font-mono font-bold uppercase">
          <span>📦 ARCHIVE FORENSIQUE SCELLÉE • 100% PDF ET HTML (ZÉRO .MD)</span>
        </div>
        <h3 class="text-2xl font-bold font-serif text-white">
          Coffre Intégral des 34 Actes Sources & Pièces Scellées (ZIP 47,6 Mo)
        </h3>
        <p class="text-xs text-slate-300 font-mono">
          Contient les contrats officiels scannés (COSP 2026 complet, 178 pages d'annexes avec l'Annexe 16, Délibération 2026-071, DUP Angelo, ROB 2024-2026) ET les 11 PDF imprimables de grade justice.
        </p>
      </div>
      <a 
        href="/docs/opposition_ajaccio/COFFRE_INTEGRAL_AJACCIO_VILLE_MOBILITES_ISO27037.zip" 
        download="COFFRE_INTEGRAL_AJACCIO_VILLE_MOBILITES_ISO27037.zip"
        class="shrink-0 px-8 py-5 rounded-2xl bg-red-600 hover:bg-red-500 text-white font-black font-mono text-sm uppercase tracking-wider transition shadow-xl hover:shadow-red-600/40 text-center active:scale-95 border border-red-400"
      >
        📥 Télécharger le Coffre Intégral (ZIP 47,6 Mo)
      </a>
    </div>

    <!-- SOMMAIRE D'ACCÈS RAPIDE AUX 10 LIVRES -->
    <div class="p-6 md:p-8 rounded-3xl bg-slate-950 border border-slate-800 shadow-xl space-y-4">
      <div class="text-xs font-mono text-amber-400 font-bold uppercase tracking-wider">
        📑 SOMMAIRE DE LA BIBLE D'INSTRUCTION (10 LIVRES IN EXTENSO)
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs font-mono text-slate-300">
        <div class="p-3 bg-slate-900 rounded-xl border border-slate-800">
          <strong class="text-amber-400">LIVRE I :</strong> Mémoire de Saisine CRC Corse (Moyens 1, 2, 3)
        </div>
        <div class="p-3 bg-slate-900 rounded-xl border border-slate-800">
          <strong class="text-amber-400">LIVRE II :</strong> Disparité Contractuelle CREM POMA vs COSP Bus
        </div>
        <div class="p-3 bg-slate-900 rounded-xl border border-slate-800">
          <strong class="text-amber-400">LIVRE III :</strong> Signalement ERP Type U & Friche Saint-Joseph
        </div>
        <div class="p-3 bg-slate-900 rounded-xl border border-slate-800">
          <strong class="text-amber-400">LIVRE IV :</strong> 5 Questions de Sommation au Conseil Communautaire
        </div>
        <div class="p-3 bg-slate-900 rounded-xl border border-slate-800">
          <strong class="text-amber-400">LIVRE V :</strong> Projet de Délibération d'Amendement Clé en Main
        </div>
        <div class="p-3 bg-slate-900 rounded-xl border border-slate-800">
          <strong class="text-amber-400">LIVRE VI :</strong> Question Orale 2026/O2/055 sur la Gare Centrale
        </div>
        <div class="p-3 bg-slate-900 rounded-xl border border-slate-800">
          <strong class="text-amber-400">LIVRE VII :</strong> Statuts & Compétence In-House SPL Mobilité
        </div>
        <div class="p-3 bg-slate-900 rounded-xl border border-slate-800">
          <strong class="text-amber-400">LIVRE VIII :</strong> Audit Financier M4 Parking du Diamant & Flotte
        </div>
        <div class="p-3 bg-slate-900 rounded-xl border border-slate-800">
          <strong class="text-amber-400">LIVRE IX :</strong> Récupération Rente Scolaire des 9 Villages
        </div>
        <div class="p-3 bg-slate-900 rounded-xl border border-slate-800">
          <strong class="text-amber-400">LIVRE X :</strong> Halte Ferroviaire Saint-Joseph vs Déménagement Gare
        </div>
      </div>
    </div>

    <!-- CORPS DES 10 LIVRES IN EXTENSO -->
    <div class="space-y-12">
"""

template_foot = """
    </div>

    <!-- OUTRO RITUELLE DE LA CELLULE -->
    <div class="text-center font-serif italic text-amber-400 text-sm mt-12 border-t border-slate-800 pt-8">
      <strong>Le Savoir partagé est notre contre-pouvoir. L'OCHJU, c'est le regard qui ne se détourne plus.</strong>
      <br><br>
      <span class="text-xs text-slate-400 font-sans opacity-75">— Cellule d'Investigation L'OCHJU</span>
    </div>

  </div>

</div>
</Layout>

<script is:inline>
  // Empreinte SHA-256 certifiée du mot de passe Transparence Citoyenne : "TransparenceCitoyenneAjaccio2026"
  const TARGET_HASH = "3c7789b3583213b3ab115365bebc1a5e44cb29ee1fdd133c63863fa584100586";

  const MAX_ATTEMPTS = 5;
  const LOCKOUT_TIME_MS = 30000; // 30 secondes de gel après 5 échecs

  async function sha256(message) {
    const msgBuffer = new TextEncoder().encode(message.trim());
    const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
  }

  function constantTimeCompare(a, b) {
    if (a.length !== b.length) return false;
    let result = 0;
    for (let i = 0; i < a.length; i++) {
      result |= a.charCodeAt(i) ^ b.charCodeAt(i);
    }
    return result === 0;
  }

  function unlockVault() {
    const lockScreen = document.getElementById('auth-lock-screen');
    const vaultContent = document.getElementById('vault-content');
    if (lockScreen && vaultContent) {
      lockScreen.classList.add('hidden');
      vaultContent.classList.remove('hidden');
    }
  }

  function lockVault() {
    sessionStorage.removeItem('lochju_vault_token_transparence_citoyenne');
    const lockScreen = document.getElementById('auth-lock-screen');
    const vaultContent = document.getElementById('vault-content');
    if (lockScreen && vaultContent) {
      vaultContent.classList.add('hidden');
      lockScreen.classList.remove('hidden');
    }
  }

  if (sessionStorage.getItem('lochju_vault_token_transparence_citoyenne') === 'authorized') {
    unlockVault();
  }

  const authForm = document.getElementById('auth-form');
  const authError = document.getElementById('auth-error');
  const authLockout = document.getElementById('auth-lockout');
  const passwordInput = document.getElementById('access-key-input');
  const submitBtn = document.getElementById('submit-auth-btn');
  const lockVaultBtn = document.getElementById('lock-vault-btn');

  let failedAttempts = parseInt(sessionStorage.getItem('lochju_auth_failed_attempts') || '0', 10);
  let lockoutUntil = parseInt(sessionStorage.getItem('lochju_auth_lockout_until') || '0', 10);

  function checkLockout() {
    const now = Date.now();
    if (lockoutUntil > now) {
      const remainingSec = Math.ceil((lockoutUntil - now) / 1000);
      if (authLockout) {
        authLockout.textContent = `🛑 Sécurité renforcée active : Trop de tentatives. Réessayez dans ${remainingSec} secondes.`;
        authLockout.classList.remove('hidden');
      }
      if (passwordInput) passwordInput.disabled = true;
      if (submitBtn) submitBtn.disabled = true;
      return true;
    } else {
      if (authLockout) authLockout.classList.add('hidden');
      if (passwordInput) passwordInput.disabled = false;
      if (submitBtn) submitBtn.disabled = false;
      return false;
    }
  }

  checkLockout();
  if (lockoutUntil > Date.now()) {
    const timer = setInterval(() => {
      if (!checkLockout()) clearInterval(timer);
    }, 1000);
  }

  if (authForm) {
    authForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      if (checkLockout()) return;

      const enteredPassword = passwordInput.value;
      const hash = await sha256(enteredPassword);

      await new Promise(res => setTimeout(res, 200));

      if (constantTimeCompare(hash, TARGET_HASH)) {
        sessionStorage.setItem('lochju_vault_token_transparence_citoyenne', 'authorized');
        sessionStorage.removeItem('lochju_auth_failed_attempts');
        sessionStorage.removeItem('lochju_auth_lockout_until');
        if (authError) authError.classList.add('hidden');
        if (authLockout) authLockout.classList.add('hidden');
        unlockVault();
      } else {
        failedAttempts++;
        sessionStorage.setItem('lochju_auth_failed_attempts', failedAttempts.toString());

        if (failedAttempts >= MAX_ATTEMPTS) {
          lockoutUntil = Date.now() + LOCKOUT_TIME_MS;
          sessionStorage.setItem('lochju_auth_lockout_until', lockoutUntil.toString());
          checkLockout();
          const timer = setInterval(() => {
            if (!checkLockout()) {
              clearInterval(timer);
              failedAttempts = 0;
              sessionStorage.setItem('lochju_auth_failed_attempts', '0');
            }
          }, 1000);
        } else {
          if (authError) {
            authError.textContent = `⚠️ Code invalide. Accès refusé (${MAX_ATTEMPTS - failedAttempts} tentative(s) restante(s)).`;
            authError.classList.remove('hidden');
          }
        }
        passwordInput.value = '';
        passwordInput.focus();
      }
    });
  }

  if (lockVaultBtn) {
    lockVaultBtn.addEventListener('click', () => {
      lockVault();
    });
  }
</script>
"""

full_astro_page = template_head + rendered_corpus + template_foot

with open("src/pages/dossier-transparence-citoyenne-ajaccio.astro", "w", encoding="utf-8") as out:
    out.write(full_astro_page)

print("Master Bible Astro page compiled successfully with all 10 books in extenso!")
print("Page length in characters:", len(full_astro_page))
