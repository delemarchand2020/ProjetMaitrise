import os
import pymupdf as fitz  # Utilisation de PyMuPDF
import re

# Fonction utilitaire pour le débogage
def debug_print(message, debug=False):
    if debug:
        print(message)

def find_first_pdf():
    # Lister les fichiers dans le répertoire courant
    files = os.listdir('.')
    # Filtrer les fichiers pour ne garder que ceux avec l'extension .pdf
    pdf_files = [file for file in files if file.lower().endswith('.pdf')]

    if not pdf_files:
        raise FileNotFoundError("Aucun fichier PDF trouvé dans le répertoire courant.")

    # Retourner le premier fichier PDF trouvé
    return pdf_files[0]

def analyze_pdf(file_path, debug=False):
    document = fitz.open(file_path)
    total_pages = len(document)
    empty_pages = 0
    keyword = r"Reste à faire \[(\d+) page\(s\) estimée\(s\)\]"
    keyword_count = 0
    sections_with_keyword = []
    total_estimated_pages_by_author = 0

    section_pattern = re.compile(r'^(.*?)[\n\r]')

    for page_num in range(total_pages):
        page = document.load_page(page_num)
        text = page.get_text()

        # Vérifier si la page est vide
        if not text.strip():
            empty_pages += 1
            continue

        # Compter les occurrences du mot-clé et extraire le nombre de pages estimées
        matches = re.findall(keyword, text)
        for match in matches:
            keyword_count += 1
            estimated_pages = int(match)
            total_estimated_pages_by_author += estimated_pages
            # Extraire le titre de la section
            section_title_match = section_pattern.search(text)
            if section_title_match:
                section_title = section_title_match.group(1).strip()
                sections_with_keyword.append((section_title, estimated_pages))

    # Calculer le pourcentage d'avancement selon les estimations de l'auteur
    author_estimated_progress = ((total_pages - empty_pages - total_estimated_pages_by_author) / (total_pages - empty_pages)) * 100

    return {
        "total_pages": total_pages,
        "empty_pages": empty_pages,
        "keyword_count": keyword_count,
        "sections_with_keyword": sections_with_keyword,
        "author_estimated_progress": author_estimated_progress,
        "total_estimated_pages_by_author": total_estimated_pages_by_author
    }

def generate_markdown_report(stats):
    report = f"""# Rapport d'avancement du rapport de mémoire de Denis Lemarchand

- **Nombre total de pages** : {stats["total_pages"]}
- **Nombre de pages vides** : {stats["empty_pages"]}
- **Nombre de sections à finir** : {stats["keyword_count"]}
- **Total des pages restantes estimées** : {stats["total_estimated_pages_by_author"]}
- **Pourcentage d'avancement** : {stats["author_estimated_progress"]:.2f}%

## Résumé des sections à finir
"""

    for i, (section, estimated_pages) in enumerate(stats["sections_with_keyword"], start=1):
        report += f"- {section} (estimé : {estimated_pages} pages)\n"

    return report

# Trouver le premier fichier PDF dans le répertoire courant
pdf_path = find_first_pdf()

# Analyser le PDF avec débogage activé
debug_mode = True  # Changez à False pour désactiver le débogage
stats = analyze_pdf(pdf_path, debug=debug_mode)

# Générer le rapport Markdown
markdown_report = generate_markdown_report(stats)

# Écrire le rapport dans un fichier Markdown
with open("rapport_analyse.md", "w", encoding="utf-8") as f:
    f.write(markdown_report)

print(f"Rapport généré avec succès dans 'rapport_analyse.md' pour le fichier PDF '{pdf_path}'")
