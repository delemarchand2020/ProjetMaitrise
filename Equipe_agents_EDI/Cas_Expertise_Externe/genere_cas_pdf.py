import json
import argparse
import pypandoc
import textwrap
import os

# Charger les fichiers JSON
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Convertir le contenu JSON en chaîne formatée
def json_to_pretty_string(json_obj):
    return json.dumps(json_obj, indent=4, ensure_ascii=False)

# Charger le fichier Markdown
def load_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Ajuster la largeur des lignes pour s'adapter à la page PDF
def adjust_line_width(text, width=80):
    # Utiliser textwrap pour diviser les lignes trop longues
    return "\n".join(textwrap.fill(line, width=width) for line in text.splitlines())

# Créer un fichier Markdown combiné
def create_markdown(json1_path, json2_path, md_path, output_md_path):
    json1 = load_json(json1_path)
    json2 = load_json(json2_path)
    md_content = load_markdown(md_path)

    json1_str = json_to_pretty_string(json1)
    json2_str = json_to_pretty_string(json2)

    # Ajuster la largeur des lignes JSON
    json1_str = adjust_line_width(json1_str)
    json2_str = adjust_line_width(json2_str)

    # Consignes en Markdown avec le barème sous forme de tableau
    consignes = """
**Votre mission :**

1. **Lecture des entrevues :** pour chaque cas sélectionné, lisez dans l'ordre les deux transcriptions d'entrevues.
2. **Observations :** notez sur un papier vos observations concernant la présence ou l'absence de manifestations de biais de type stéréotype pour chaque conversation anonymisée.
3. **Score de biais :** attribuez un score de présence de biais pour chaque conversation en utilisant le même barème que celui utilisé par notre agent IA EDI.
4. **Lecture du rapport EDI :** lisez le rapport EDI fourni, à lire après avoir fait vos propres observations et attribution de scores.
5. **Comparaison et évaluation :** comparez vos résultats avec ceux du rapport EDI et notez qualitativement vos observations sur le rapport.

**Points importants :**

- Vous n'avez pas à évaluer le réalisme ou la pertinence des conversations.
- Vous n'avez pas accès aux profils des protagonistes ni à la description du poste.
- Nous vous demandons uniquement de nous indiquer si, face à ces transcriptions d'entrevues (réelles ou non), vous feriez les mêmes observations que notre agent EDI.

**Barème :**

| **Score de biais** | **Interprétation**                                                 |
|---------------------|---------------------------------------------------------------------|
| 100 sur 100        | La présence de biais est confirmée sans aucun doute.               |
| 0 sur 100          | La présence de biais est inexistante sans aucun doute.            |
| 5 à 10 sur 100     | La présence de biais est très peu probable.                         |
| 10 à 30 sur 100    | La présence de biais est peu probable.                             |
| 30 à 50 sur 100    | La présence de biais est probable.                                |
| 50 à 70 sur 100    | La présence de biais est moyennement probable.                     |
| 70 à 90 sur 100    | La présence de biais est très probable.                            |
| 90 à 100 sur 100   | La présence de biais est très fortement probable.                  |

Je vous remercie par avance pour votre collaboration et votre expertise. Vos retours me seront précieux pour améliorer l'approche en IA dans ce domaine.
"""

    # Créer le contenu Markdown combiné avec les nouveaux titres et consignes
    combined_md = "# Demande d'évaluation de cas pour l'étude des biais de genre\n\n"
    combined_md += consignes + "\n"
    combined_md += '<div style="page-break-after: always;"></div>\n'
    combined_md += f"## Première conversation\n\n```json\n{json1_str}\n```\n\n"
    combined_md += '<div style="page-break-after: always;"></div>\n'
    combined_md += f"## Seconde conversation\n\n```json\n{json2_str}\n```\n\n"
    combined_md += '<div style="page-break-after: always;"></div>\n'
    combined_md += f"{md_content}\n"

    # Écrire le contenu combiné dans un nouveau fichier Markdown
    with open(output_md_path, 'w', encoding='utf-8') as output_file:
        output_file.write(combined_md)

# Convertir un fichier Markdown en PDF
def convert_md_to_pdf(input_md_path, output_pdf_path):
    output = pypandoc.convert_file(input_md_path, 'pdf', outputfile=output_pdf_path)
    assert output == ""
    print(f"PDF généré avec succès : {output_pdf_path}")

def main():
    parser = argparse.ArgumentParser(description="Générer un fichier PDF à partir de fichiers JSON et Markdown.")
    parser.add_argument('directory', type=str, help="Répertoire par défaut contenant tous les fichiers.")
    parser.add_argument('json1', type=str, help="Nom du premier fichier JSON.")
    parser.add_argument('json2', type=str, help="Nom du deuxième fichier JSON.")
    parser.add_argument('md', type=str, help="Nom du fichier Markdown existant.")
    parser.add_argument('output_md', type=str, help="Nom du fichier Markdown de sortie.")
    parser.add_argument('output_pdf', type=str, help="Nom du fichier PDF de sortie.")

    args = parser.parse_args()

    # Construire les chemins complets en utilisant le répertoire par défaut
    json1_path = os.path.join(args.directory, args.json1)
    json2_path = os.path.join(args.directory, args.json2)
    md_path = os.path.join(args.directory, args.md)
    output_md_path = os.path.join(args.directory, args.output_md)
    output_pdf_path = os.path.join(args.directory, args.output_pdf)

    # Créer le fichier Markdown combiné
    create_markdown(json1_path, json2_path, md_path, output_md_path)

    # Convertir le fichier Markdown en PDF
    convert_md_to_pdf(output_md_path, output_pdf_path)

if __name__ == "__main__":
    main()
