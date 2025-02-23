import argparse
import os
import json

def read_file(file_path, encoding='utf-8'):
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            return file.read()
    except UnicodeDecodeError:
        # Si l'encodage UTF-8 échoue, essayer avec un autre encodage
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            return file.read()

def create_markdown(md_content, json_content_1, json_content_2, output_path):
    with open(output_path, 'w', encoding='utf-8') as md_file:
        # Ajouter le contenu du rapport d'audit
        md_file.write("# Rapport d'Audit avec annexes\n\n")
        md_file.write(md_content)
        md_file.write("\n\n")

        # Ajouter les fichiers JSON en annexe
        md_file.write("## Annexe: entrevue 1\n\n")
        md_file.write("```json\n")
        md_file.write(json.dumps(json_content_1, indent=4, ensure_ascii=False))
        md_file.write("\n```\n\n")

        md_file.write("## Annexe: entrevue 2\n\n")
        md_file.write("```json\n")
        md_file.write(json.dumps(json_content_2, indent=4, ensure_ascii=False))
        md_file.write("\n```\n")

def main():
    parser = argparse.ArgumentParser(description="Générer un fichier Markdown avec un rapport d'audit et des annexes JSON.")
    parser.add_argument("--directory", required=True, help="Chemin vers le répertoire contenant les fichiers et où le fichier Markdown sera généré.")
    parser.add_argument("--md_file", required=True, help="Nom du fichier Markdown du rapport d'audit.")
    parser.add_argument("--json_file_1", required=True, help="Nom du premier fichier JSON.")
    parser.add_argument("--json_file_2", required=True, help="Nom du second fichier JSON.")
    parser.add_argument("--output_md", required=True, help="Nom du fichier Markdown généré.")

    args = parser.parse_args()

    # Construire les chemins complets des fichiers
    md_path = os.path.join(args.directory, args.md_file)
    json_path_1 = os.path.join(args.directory, args.json_file_1)
    json_path_2 = os.path.join(args.directory, args.json_file_2)
    output_path = os.path.join(args.directory, args.output_md)

    # Lire les fichiers
    md_content = read_file(md_path)

    with open(json_path_1, 'r', encoding='utf-8') as file:
        json_content_1 = json.load(file)

    with open(json_path_2, 'r', encoding='utf-8') as file:
        json_content_2 = json.load(file)

    # Créer le fichier Markdown
    create_markdown(md_content, json_content_1, json_content_2, output_path)

if __name__ == "__main__":
    main()


#python rapport_analyse_2_conv_pdf.py --directory ../Equipe_agents_EDI/Cas_interessants/Audit_pertinents/cas_6 --md_file rapport_audit.md --json_file_1 conversation_1.json --json_file_2 conversation_2.json --output_md rapport_audit_avec_annexes.md

