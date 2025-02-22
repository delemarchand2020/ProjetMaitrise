import json
import argparse
import shutil
import os

def clear_bias_fields(data):
    for entry in data:
        entry['bias'] = ""
        entry['bias_hints'] = []
    return data

def main(file_path):
    # Vérifier si le fichier existe
    if not os.path.isfile(file_path):
        print(f"Le fichier {file_path} n'existe pas.")
        return

    # Créer une sauvegarde du fichier
    backup_path = file_path.replace('.json', '_modif.json')
    shutil.copy(file_path, backup_path)
    print(f"Sauvegarde créée : {backup_path}")

    # Lire le fichier JSON
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Modifier les champs 'bias' et 'bias_hints'
    updated_data = clear_bias_fields(data)

    # Écrire les modifications dans le fichier JSON
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(updated_data, file, ensure_ascii=False, indent=4)

    print(f"Le fichier {file_path} a été mis à jour avec succès.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Modifier un fichier JSON pour vider les champs 'bias' et 'bias_hints'.")
    parser.add_argument('--file_path', required=True, help="Chemin vers le fichier JSON à modifier.")

    args = parser.parse_args()
    main(args.file_path)
