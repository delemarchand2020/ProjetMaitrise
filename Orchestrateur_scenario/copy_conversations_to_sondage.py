import os
import shutil
import re


def copier_conversations():
    """Copie les fichiers conversation_1.json et conversation_2.json dans le répertoire cible avec un nouvel indice."""

    # Définition des chemins
    source_dir = "..\\Simulation_conversation\\output"
    target_dir = "..\\sondages\\conversations"

    # Vérifier si le dossier cible existe, sinon le créer
    os.makedirs(target_dir, exist_ok=True)

    # Lister tous les fichiers existants au format conversation_nn.json
    existing_files = [f for f in os.listdir(target_dir) if re.match(r"conversation_\d{2}\.json", f)]

    # Trouver le plus grand indice nn
    max_index = 0
    for filename in existing_files:
        match = re.search(r"conversation_(\d{2})\.json", filename)
        if match:
            max_index = max(max_index, int(match.group(1)))

    # Déterminer les nouveaux indices mm
    new_index_1 = max_index + 1
    new_index_2 = new_index_1 + 1

    # Chemins des fichiers source
    source_file_1 = os.path.join(source_dir, "conversation_1.json")
    source_file_2 = os.path.join(source_dir, "conversation_2.json")

    # Chemins des fichiers cibles
    target_file_1 = os.path.join(target_dir, f"conversation_{new_index_1:02d}.json")
    target_file_2 = os.path.join(target_dir, f"conversation_{new_index_2:02d}.json")

    # Copier les fichiers s'ils existent
    if os.path.exists(source_file_1):
        shutil.copy(source_file_1, target_file_1)
        print(f"Copié : {source_file_1} → {target_file_1}")

    if os.path.exists(source_file_2):
        shutil.copy(source_file_2, target_file_2)
        print(f"Copié : {source_file_2} → {target_file_2}")


# Exemple d'utilisation
if __name__ == "__main__":
    copier_conversations()
