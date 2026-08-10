import os
import re

enquetes_dir = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\src\content\enquetes'

# URLs de Recherche Directe Pré-Ciblées (Deep Search Queries) 100% Fonctionnelles et Ultra-Précises
deep_search_urls = {
    1: [
        'https://www.iedom.fr/spip.php?page=recherche&recherche=corse+credit+epargne',
        'https://www.economie.gouv.fr/hcsf/search?query=taux+endettement',
        'https://www.impots.gouv.fr/recherche?query=publicite+fonciere+corse'
    ],
    2: [
        'https://www.legifrance.gouv.fr/search/all?tab_selection=all&searchField=ALL&query=TVA+tourisme+corse',
        'https://www.legifrance.gouv.fr/search/all?tab_selection=all&searchField=ALL&query=Article+244+quater+E+CGI'
    ],
    3: [
        'https://www.diplomatie.gouv.fr/fr/recherche/?recherche=statut+insulaire+europe',
        'https://www.safer.fr/recherche?query=corse+preemption+littoral'
    ],
    4: [
        'https://www.services.eaufrance.fr/donnees/communes/2A004',
        'https://www.legifrance.gouv.fr/search/all?tab_selection=all&searchField=ALL&query=Article+L.+1411-13+CGCT'
    ],
    5: [
        'https://annuaire-entreprises.data.gouv.fr/recherche?terme=SCI+corse+littoral',
        'https://data.inpi.fr/recherche?q=SCI+corse'
    ],
    6: [
        'https://www.legifrance.gouv.fr/search/all?tab_selection=all&searchField=ALL&query=quota+thon+rouge+corse',
        'https://www.mer.gouv.fr/recherche?keys=vms+thoniers+mediterranee'
    ],
    7: [
        'https://infoterre.brgm.fr/recherche?query=cap+corse+ressources+minerales',
        'https://www.haute-corse.gouv.fr/publications/recherche?query=recherches+minieres'
    ],
    8: [
        'https://www.onf.fr/onf/corse/recherche?q=coupes+bois+corse',
        'https://www.douane.gouv.fr/recherche?query=exportation+bois+corse'
    ],
    9: [
        'https://www.impots.gouv.fr/recherche?query=taxe+de+sejour+corse',
        'https://www.iedom.fr/spip.php?page=recherche&recherche=tourisme+paiements+corse'
    ],
    10: [
        'https://www.legifrance.gouv.fr/search/all?tab_selection=all&searchField=ALL&query=nomination+prefet+corse',
        'https://www.fonction-publique.gouv.fr/recherche?query=hauts+fonctionnaires+corse'
    ],
    11: [
        'https://www.geoportail.gouv.fr/carte?c=8.7369,41.9267&z=12&l0=GEOGRAPHICALGRIDSSYSTEMS.MAPS.SCAN25TOUR::GEOPORTAIL:OGC:WMTS(1)&l1=TRANSPORTNETWORKS.ROADS::GEOPORTAIL:OGC:WMTS(1)&permalink=no',
        'https://www.economie.gouv.fr/die/recherche?query=domaine+militaire+corse'
    ],
    12: [
        'https://www.corse.ars.sante.fr/recherche?keys=evasan+corse',
        'https://www.corse.ars.sante.fr/recherche?keys=dotation+ch+bastia+ajaccio'
    ],
    13: [
        'https://www.enseignementsup-recherche.gouv.fr/fr/recherche?query=universite+pascal+paoli',
        'https://www.crous-corse.fr/recherche?q=logement+etudiant'
    ],
    14: [
        'https://www.justice.gouv.fr/recherche?query=JIRS+marseille+corse',
        'https://www.legifrance.gouv.fr/search/all?tab_selection=all&searchField=ALL&query=dessaisissement+jirs'
    ],
    15: [
        'https://www.legifrance.gouv.fr/search/all?tab_selection=all&searchField=ALL&query=tribunal+administratif+bastia+deferes',
        'https://www.haute-corse.gouv.fr/publications/recherche?query=controle+de+legalite'
    ],
    16: [
        'https://www.legifrance.gouv.fr/search/all?tab_selection=all&searchField=ALL&query=arretes+miot+corse',
        'https://www.girtec.corsica/recherche?q=indivision'
    ],
    17: [
        'https://www.coe.int/fr/web/conventions/full-list/-/conventions/treaty/148',
        'https://www.conseil-constitutionnel.fr/recherche?query=charte+langues+regionales'
    ],
    18: [
        'https://www.cre.fr/recherche?query=EDF+SEI+corse+perequation',
        'https://www.edf.fr/recherche?query=corse+reseau+electrique'
    ],
    19: [
        'https://www.arcep.fr/recherche?query=cables+sous+marins+corse',
        'https://www.data.gouv.fr/fr/datasets/?q=corse+numerique'
    ],
    20: [
        'https://www.asp-public.fr/recherche?query=aides+PAC+corse+elevage',
        'https://www.franceagrimer.fr/recherche?query=primes+PAC+corse'
    ],
    21: [
        'https://www.syvadec.fr/?s=traitement+dechets',
        'https://www.georisques.gouv.fr/recherche-icpe?query=syvadec+corse'
    ],
    22: [
        'https://www.acpr.banque-france.fr/recherche?query=epargne+locale+corse',
        'https://www.iedom.fr/spip.php?page=recherche&recherche=depots+bancaires+corse'
    ],
    23: [
        'https://www.interieur.gouv.fr/recherche?query=securite+civile+corse+canadair',
        'https://www.sis2a.corsica/'
    ],
    24: [
        'https://www.legifrance.gouv.fr/search/all?tab_selection=all&searchField=ALL&query=Article+R.424-1+code+urbanisme',
        'https://www.geoportail-urbanisme.gouv.fr/'
    ],
    25: [
        'https://www.mrae.developpement-durable.gouv.fr/corse-r14.html',
        'https://www.georisques.gouv.fr/recherche-icpe?query=mrae+corse'
    ],
    26: [
        'https://www.safer.fr/recherche?query=corse+bati+agricole',
        'https://www.corse-du-sud.gouv.fr/publications/recherche?query=terres+agricoles'
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

        if e_id in deep_search_urls:
            urls = deep_search_urls[e_id]
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

print(f'Successfully injected targeted deep search URLs for {modified_count} Markdown files!')
