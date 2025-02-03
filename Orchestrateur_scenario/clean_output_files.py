import os

def supprimer_fichiers_output():
    """Supprime uniquement les fichiers dans les dossiers 'output' sans supprimer les répertoires."""
    # Répertoires de travail où les fichiers output sont générés
    directories = [
        "..\\AgentIA_generation_postes\\output",
        "..\\CrewAI_equipe_creation_BD_candidats\\output",
        "..\\AgentAI_creation_BD_recruteurs\\output",
        "..\\Simulation_conversation\\output",
        "..\\Equipe_agents_EDI\\output"
    ]

    for dir_path in directories:
        abs_path = os.path.abspath(dir_path)
        if os.path.exists(abs_path) and os.path.isdir(abs_path):
            for file_name in os.listdir(abs_path):
                file_path = os.path.join(abs_path, file_name)
                if os.path.isfile(file_path):  # Vérifie si c'est un fichier
                    try:
                        os.remove(file_path)
                        print(f"Supprimé : {file_path}")
                    except Exception as e:
                        print(f"Erreur lors de la suppression de {file_path}: {e}")
        else:
            print(f"Le dossier {abs_path} n'existe pas, aucune suppression nécessaire.")

# Exemple d'utilisation
if __name__ == "__main__":
    supprimer_fichiers_output()
