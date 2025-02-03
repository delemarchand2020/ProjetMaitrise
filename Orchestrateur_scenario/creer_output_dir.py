import os

def recreer_repertoires_output():
    """Recrée tous les répertoires 'output' nécessaires s'ils n'existent pas."""
    directories = [
        "..\\AgentIA_generation_postes\\output",
        "..\\CrewAI_equipe_creation_BD_candidats\\output",
        "..\\AgentAI_creation_BD_recruteurs\\output",
        "..\\Simulation_conversation\\output",
        "..\\Equipe_agents_EDI\\output"
    ]

    for dir_path in directories:
        abs_path = os.path.abspath(dir_path)
        try:
            os.makedirs(abs_path, exist_ok=True)  # Crée le répertoire s'il n'existe pas
            print(f"Répertoire créé (ou déjà existant) : {abs_path}")
        except Exception as e:
            print(f"Erreur lors de la création du répertoire {abs_path}: {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    recreer_repertoires_output()
