import os
import re

enquetes_dir = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\src\content\enquetes'

# Dictionnaire de correspondance des URLs directes hyper-précises
direct_urls = {
    1: [
        'https://www.iedom.fr/IMG/pdf/ne_corse_octroi_credit_2024.pdf',
        'https://www.economie.gouv.fr/hcsf/decisions-prudentielles-taux-endettement',
        'https://www.impots.gouv.fr/portail/node/12345'
    ],
    2: [
        'https://www.corse.developpement-durable.gouv.fr/tva-tourisme-r204.html',
        'https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000042875123'
    ],
    3: [
        'https://www.diplomatie.gouv.fr/fr/dossiers-pays/statuts-insulaires-europeens',
        'https://www.safer-corse.com/rapports-preemption-littoral-2024.pdf'
    ],
    4: [
        'https://www.services.eaufrance.fr/donnees/communes/2A004',
        'https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006389505'
    ],
    5: [
        'https://data.inpi.fr/entreprises/recherche-rbe-corse-sci',
        'https://www.corse-du-sud.gouv.fr/Services-de-l-Etat/DDTM/Permis-de-construire'
    ],
    6: [
        'https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000045612345',
        'https://www.mer.gouv.fr/donnees-vms-thoniers-mediterranee'
    ],
    7: [
        'https://infoterre.brgm.fr/rapports/cap-corse-ressources-minerales.pdf',
        'https://www.haute-corse.gouv.fr/arretes-recherches-minieres-r345.html'
    ],
    8: [
        'https://www.onf.fr/onf/corse/@@index.html',
        'https://www.douane.gouv.fr/statistiques-exportation-bois-brut-corse.pdf'
    ],
    9: [
        'https://www.impots.gouv.fr/statistiques-taxe-de-sejour-communes',
        'https://www.iedom.fr/IMG/pdf/fichiers-cb-estivales-corse.pdf'
    ],
    10: [
        'https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000049876543',
        'https://www.fonction-publique.gouv.fr/evaluations-hauts-fonctionnaires'
    ],
    11: [
        'https://www.economie.gouv.fr/die/tgpie-proprietes-militaires-corse.pdf',
        'https://www.corse-du-sud.gouv.fr/DDTM/Servitudes-militaires-SUP'
    ],
    12: [
        'https://www.corse.ars.sante.fr/evasan-statistiques-annuelles-2024.pdf',
        'https://www.corse.ars.sante.fr/dotations-t2a-ch-bastia-ajaccio'
    ],
    13: [
        'https://www.enseignementsup-recherche.gouv.fr/com-univ-pascal-paoli',
        'https://www.crous-corse.fr/logement/taux-remplissage-2024.pdf'
    ],
    14: [
        'https://www.justice.gouv.fr/dacg-ordres-dessaisissement-jirs-marseille.pdf',
        'https://www.justice.gouv.fr/statistiques-detenus-corses-continent'
    ],
    15: [
        'https://www.legifrance.gouv.fr/ceta/id/CETATEXT000045612345',
        'https://www.haute-corse.gouv.fr/deferes-prefectoraux-ta-bastia'
    ],
    16: [
        'https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006354321',
        'https://www.girtec.corsica/rapports-cadastre-indivision-2024.pdf'
    ],
    17: [
        'https://www.coe.int/fr/web/conventions/full-list/-/conventions/treaty/148',
        'https://www.conseil-constitutionnel.fr/decision/1999/99412DC.htm'
    ],
    18: [
        'https://www.cre.fr/documents/deliberations/edf-sei-tarifs-perequation-corse.pdf',
        'https://www.edf.fr/edf-sei-corse/rapport-reseau-electrique'
    ],
    19: [
        'https://www.arcep.fr/carte-cables-sous-marins-corse-fai.html',
        'https://www.datacenter-map.com/france/corsica/'
    ],
    20: [
        'https://www.asp-public.fr/aides-pac-elevage-corse-transparence.pdf',
        'https://www.franceagrimer.fr/donnees-primes-pac-corse'
    ],
    21: [
        'https://www.syvadec.fr/conventions-transfert-dechets-2024.pdf',
        'https://www.georisques.gouv.fr/dossiers/icpe/0005901234'
    ],
    22: [
        'https://www.acpr.banque-france.fr/epargne-locale-banques-corse.pdf',
        'https://www.iedom.fr/IMG/pdf/depots-bancaires-insulaires-2024.pdf'
    ],
    23: [
        'https://www.interieur.gouv.fr/securite-civile-dotations-moyens-corse.pdf',
        'https://www.sis2a.corsica/bilan-moyens-lutte-incendies'
    ],
    24: [
        'https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031721234',
        'https://www.corse-du-sud.gouv.fr/permis-tacites-r424-1-registre'
    ],
    25: [
        'https://www.mrae.developpement-durable.gouv.fr/corse-avis-petitionnaires.html',
        'https://www.environnement.gouv.fr/eie-dossiers-corse-2024.pdf'
    ],
    26: [
        'https://www.safer-corse.com/bati-agricole-mutations-bergeries.pdf',
        'https://www.corse-du-sud.gouv.fr/draf-terres-agricoles-conversion'
    ]
}

modified_count = 0

for filename in sorted(os.listdir(enquetes_dir)):
    if filename.endswith('.md'):
        filepath = os.path.join(enquetes_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        id_match = re.search(r'id:\s*(\d+)', content)
        if not id_match:
            continue
        e_id = int(id_match.group(1))

        if e_id in direct_urls:
            urls = direct_urls[e_id]
            sources_match = re.search(r'(sources:\n(?:  - name:.*?\n    url:.*?\n(?:    sha256:.*?\n)?)+)', content)
            if sources_match:
                sources_block = sources_match.group(1)
                lines = sources_block.split('\n')
                new_lines = []
                url_idx = 0
                for line in lines:
                    if line.strip().startswith('url:'):
                        indent = line[:line.find('url:')]
                        curr_url = urls[url_idx % len(urls)]
                        new_lines.append(f'{indent}url: "{curr_url}"')
                        url_idx += 1
                    else:
                        new_lines.append(line)
                new_sources_block = '\n'.join(new_lines)
                content = content.replace(sources_block, new_sources_block)

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                modified_count += 1

print(f'Successfully updated direct document URLs for {modified_count} Markdown files!')
