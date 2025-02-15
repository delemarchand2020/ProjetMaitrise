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
    keyword = "Reste à faire"
    keyword_count = 0
    sections_with_keyword = []

    # Nombre total de sections (constante)
    total_sections = 28 + 5  # Remplacez par le nombre réel de sections

    section_pattern = re.compile(r'^(.*?)[\n\r]')
    special_sections = {"Résumé", "Abstract", "Remerciements"}

    for page_num in range(total_pages):
        page = document.load_page(page_num)
        text = page.get_text()

        # Vérifier si la page est vide
        if not text.strip():
            empty_pages += 1
            continue

        # Compter les occurrences du mot-clé
        if keyword in text:
            keyword_count += 1
            # Extraire le titre de la section
            section_title_match = section_pattern.search(text)
            if section_title_match:
                section_title = section_title_match.group(1).strip()
                sections_with_keyword.append(section_title)

    # Calculer le nombre moyen de pages par section
    if total_sections:
        avg_pages_per_section = total_pages / total_sections
    else:
        avg_pages_per_section = 0

    # Estimer le nombre de pages restant à finir
    estimated_pages_left = keyword_count * avg_pages_per_section

    # Calculer le pourcentage d'avancement
    realistic_progress = ((total_pages - empty_pages - estimated_pages_left) / (total_pages - empty_pages)) * 100
    pessimistic_progress = ((total_pages - empty_pages - estimated_pages_left * 1.3) / (total_pages - empty_pages)) * 100
    optimistic_progress = ((total_pages - empty_pages - estimated_pages_left * 0.7) / (total_pages - empty_pages)) * 100

    return {
        "total_pages": total_pages,
        "empty_pages": empty_pages,
        "keyword_count": keyword_count,
        "sections_with_keyword": sections_with_keyword,
        "total_sections": total_sections,
        "avg_pages_per_section": avg_pages_per_section,
        "estimated_pages_left": estimated_pages_left,
        "pessimistic_progress": pessimistic_progress,
        "realistic_progress": realistic_progress,
        "optimistic_progress": optimistic_progress
    }

def generate_markdown_report(stats):
    report = f"""# Rapport d'Analyse du Document

- **Nombre total de pages** : {stats["total_pages"]}
- **Nombre de pages vides** : {stats["empty_pages"]}
- **Nombre de sections à finir (avec "Reste à faire")** : {stats["keyword_count"]}
- **Nombre total de sections** : {stats["total_sections"]}
- **Nombre moyen de pages par section** : {stats["avg_pages_per_section"]:.2f}
- **Estimation des pages restant à finir** : {stats["estimated_pages_left"]:.2f}
- **Pourcentage d'avancement (pessimiste)** : {stats["pessimistic_progress"]:.2f}%
- **Pourcentage d'avancement (réaliste)** : {stats["realistic_progress"]:.2f}%
- **Pourcentage d'avancement (optimiste)** : {stats["optimistic_progress"]:.2f}%

## Sections avec "Reste à faire"
"""

    for i, section in enumerate(stats["sections_with_keyword"], start=1):
        report += f"{i}. {section}\n"

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
