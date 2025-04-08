import os
import json
import subprocess
import argparse
import shutil

# Chemin du répertoire à nettoyer
dir_to_clean = r"C:\Users\delem\AppData\Local\CrewAI"

def load_api_keys(file_path):
    """Charge les clés API à partir d'un fichier JSON."""
    with open(file_path, 'r') as file:
        return json.load(file)

def run_command(command, cwd=None):
    """Exécute une commande shell et affiche la sortie en temps réel."""
    process = subprocess.Popen(
        command, shell=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
    )
    for line in process.stdout:
        print(line, end="")
    process.wait()
    if process.returncode != 0:
        raise RuntimeError(f"Command failed: {command}")

def nettoyer_cache_crewai():
    try:
        shutil.rmtree(dir_to_clean, ignore_errors=True)  # Suppression récursive, ignore les erreurs
    except Exception as e:
        print(f"Une erreur s'est produite lors du nettoyage du répertoire {dir_to_clean} : {e}")

def set_environment(api_keys):
    """Configure les variables d'environnement nécessaires."""
    for key, value in api_keys.items():
        os.environ[key] = value

def execute_step(step, args):
    """Exécute une étape spécifique."""
    if step == 1:
        os.environ["OPIK_PROJECT_NAME"] = "agentai_gen_postes"
        print("Étape 1 : Génération des postes")
        run_command(
            f"python agentai_gen_postes.py --nombre_postes 1 --metier \"{args.metier}\" --file_path output\\postes_generes.json",
            cwd="..\\AgentIA_generation_postes"
        )
    elif step == 2:
        nettoyer_cache_crewai()
        print("Étape 2 : Génération des candidates féminines")
        run_command(
            "python crewai_gen_candidats.py --fichier_postes ..\\AgentIA_generation_postes\\output\\postes_generes.json --output_path output\\ --file_name candidat_f.json --langue_de_travail français --genre féminin --poste_num 1",
            cwd="..\\CrewAI_equipe_creation_BD_candidats"
        )
    elif step == 3:
        os.environ["OPIK_PROJECT_NAME"] = "agentai_gen_profil_recruteur"
        print(f"Étape 3 : Génération du recruteur pour le secteur {args.secteur} avec stéréotype sur le genre féminin")
        run_command(
            f"python agentai_gen_recruteurs.py --biais \"stéréotype sur le genre féminin\" --langue_de_travail français --genre masculin --secteur \"{args.secteur}\" --file_path output\\recruteurs_generes.json",
            cwd="..\\AgentAI_creation_BD_recruteurs"
        )
    elif step == 4:
        nettoyer_cache_crewai()
        print("Étape 4 : Génération de la première conversation")
        run_command(
            "python gen_full_crewai_conversation.py --fichier_db_postes ..\\AgentIA_generation_postes\\output\\postes_generes.json --fichier_db_recruteurs ..\\AgentAI_creation_BD_recruteurs\\output\\recruteurs_generes.json --fichier_db_candidats ..\\CrewAI_equipe_creation_BD_candidats\\output\\candidat_f.json --output_file conversation_1.json --index 0",
            cwd="..\\Simulation_conversation"
        )
    elif step == 5:
        nettoyer_cache_crewai()
        print("Étape 5 : Génération des candidats masculins")
        run_command(
            "python crewai_gen_candidats.py --fichier_postes ..\\AgentIA_generation_postes\\output\\postes_generes.json --output_path output\\ --file_name candidat_m.json --langue_de_travail français --genre masculin --poste_num 1",
            cwd="..\\CrewAI_equipe_creation_BD_candidats"
        )
    elif step == 6:
        os.environ["OPIK_PROJECT_NAME"] = "agentai_gen_profil_recruteur"
        print(f"Étape 6 : Modification du recruteur pour le secteur {args.secteur} : retrait du stéréotype")
        run_command(
            f"python modif_recruteurs.py --file_path output\\recruteurs_generes.json",
            cwd="..\\AgentAI_creation_BD_recruteurs"
        )
    elif step == 7:
        nettoyer_cache_crewai()
        print("Étape 7 : Génération de la deuxième conversation")
        run_command(
            "python gen_full_crewai_conversation.py --fichier_db_postes ..\\AgentIA_generation_postes\\output\\postes_generes.json --fichier_db_recruteurs ..\\AgentAI_creation_BD_recruteurs\\output\\recruteurs_generes.json --fichier_db_candidats ..\\CrewAI_equipe_creation_BD_candidats\\output\\candidat_m.json --output_file conversation_2.json --index 0",
            cwd="..\\Simulation_conversation"
        )
    elif step == 8:
        nettoyer_cache_crewai()
        print("Étape 8 : Génération du rapport EDI")
        run_command(
            "python gen_rapport_EDI.py --file1 ..\\Simulation_conversation\\output\\conversation_1.json --file2 ..\\Simulation_conversation\\output\\conversation_2.json --output_dir output\\ --output_file rapport_audit.md",
            cwd="..\\Equipe_agents_EDI"
        )
        nettoyer_cache_crewai()

# Orchestration des scripts
def main():
    parser = argparse.ArgumentParser(description="Orchestration des scripts EDI.")
    parser.add_argument(
        "--metier",
        type=str,
        default="ingénieur.e infra cloud",
        help="Métier pour la génération des postes."
    )
    parser.add_argument(
        "--secteur",
        type=str,
        default="informatique",
        help="Secteur d'activité pour la génération des recruteurs."
    )
    parser.add_argument(
        "--api_keys_file",
        type=str,
        default="api_keys.json",
        help="Chemin vers le fichier JSON contenant les clés API."
    )
    parser.add_argument(
        "--steps",
        type=int,
        nargs='+',
        default=[1, 2, 3, 4, 5, 6, 7],
        help="Liste des étapes à exécuter."
    )
    args = parser.parse_args()

    try:
        # Charger les clés API
        api_keys = load_api_keys(args.api_keys_file)
        set_environment(api_keys)

        nettoyer_cache_crewai()

        for step in args.steps:
            execute_step(step, args)

        print("Les étapes spécifiées ont été exécutées avec succès !")
    except RuntimeError as e:
        print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    main()
