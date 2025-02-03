import agentops
import argparse
import os
import json
from textwrap import dedent
from crewai import Agent, Crew, Process, Task, LLM
from crewai_tools import FileReadTool, FileWriterTool
from dotenv import load_dotenv

load_dotenv()

llm_creative = LLM(
    model="gpt-4o",
    temperature=0.9,
    top_p=0.9,
    frequency_penalty=0.2,
    presence_penalty=0.2,
)

llm_doer = LLM(
    model="gpt-4o",
    temperature=0.2,
    top_p=0.85,
    frequency_penalty=0.0,
    presence_penalty=0.0,
)

llm_middle_creative = LLM(
    model="gpt-4o",
    temperature=0.8,
    top_p=0.9,
    frequency_penalty=0.1,
    presence_penalty=0.1,
)

file_read_tool = FileReadTool()
#file_writer_tool = FileWriterTool()

print("## Équipe de création des profils candidats fictifs")
print("---------------------------------------------------")

# ============== définition des agents =======================

preparateur_poste = Agent(
    role="Préparateur",
    goal="Fournir les informations requises pour créer un descriptif de poste",
    backstory=dedent(
        """
        Tu vas chercher les informations et les transmettre pour la rédaction du poste.
        """
    ),
    allow_delegation=False,
    verbose=True,
    llm=llm_doer,
    tools=[file_read_tool],
)

redacteur_poste = Agent(
    role="Rédacteur de poste",
    goal="Produire un descriptif de poste selon les informations fournies",
    backstory=dedent(
        """
        Tu es un rédacteur expérimenté pour produire un descriptif de poste très vendeur.
        """
    ),
    allow_delegation=False,
    verbose=True,
    llm=llm_creative
)

redacteur_profil_candidat = Agent(
    role="Rédacteur de profil de candidat",
    goal="Créer un profil de candidat idéal selon un descriptif de poste",
    backstory=dedent(
        """
        Tu es un rédacteur expérimenté pour produire un profil de candidat idéal et réaliste.
        """
    ),
    allow_delegation=False,
    verbose=True,
    llm=llm_creative
)

redacteur_personna_candidat = Agent(
    role="Rédacteur de personna",
    goal="Créer un personna selon un profil de candidat",
    backstory=dedent(
        """
        Tu es un rédacteur expérimenté pour produire un personna réaliste pour compléter un profil de candidat. 
        """
    ),
    allow_delegation=False,
    verbose=True,
    llm=llm_middle_creative,
    #tools=[file_writer_tool],
)

# ============== définition des tâches =======================

preparer_commande = Task(
    description="""Tu dois transmettre les informations au rédacteur de produire un profil de candidat idéal, voici les instructions:
        Instructions
        ------------       
        A partir du fichier {fichier_postes}, passe la commande au rédacteur em prenant la description d'un poste.
        Tu passes les informations d'un seul poste à la fois.
        Parmi tous les postes, tu choisis le poste numéro {poste_num}.
        """,
    expected_output="Un texte contenant les informations sur le poste avec sa référence poste_num = {poste_num}.",
    agent=preparateur_poste,
)

redaction_poste = Task(
    description="""Tu dois rédiger un texte structuré en {langue_de_travail}, voici les instructions:
        Instructions
        ------------
        Tu dois extraire les informations du poste, les mettre en forme selon le format suivant :
        Un paragraphe sur la compagnie :
        - nom de la compagnie
        - localisation
        - [imagine une brève description de la raison d'être de la compagnie]
        Un paragraphe sur le poste offert [le poste doit être écrit de manière non genré] :
        - numéro du poste : {poste_num}
        - titre du poste
        - description
        - responsabilités clés
        Un paragraphe sur le profil de candidat recherché :
        - compétences requises
        - niveau d'expérience requis (junior, intermédiaire ou senior)
        - niveau d'études requis si pertinent
        - [imagine les qualités humaines que recherche la compagnie en rapport avec sa raison d'être]
        Un paragraphe pour motiver les candidats à envoyer leur candidature :
        - [imagine un court texte très vendeur pour expliquer pourquoi postuler]
        """,
    expected_output="Le descriptif du poste selon les instructions.",
    agent=redacteur_poste,
)

redaction_profil_candidat = Task(
    description="""Tu dois rédiger un texte structuré en {langue_de_travail}, voici les instructions:
        Instructions
        ------------
        Tu dois générer un profil de candidat idéal qui répond au poste à pourvoir.
        Le profil de candidat est anonyme et contient uniquement les informations suivantes :
            * Formations académiques et certifications.
            * Compétences techniques/métiers.
            * Compétences humaines et relationnelles.
            * Expériences professionnelles
        Les formations et les certifications doivent avoir des dates d'obtention sur la même ligne que leur titre.
        Les expériences doivent avoir des dates de réalisation sur la même ligne que leur titre.
        Les dates doivent être cohérentes (expérience qui se termine avant qu'une autre débute).
        Les expériences professionnelles tiennent compte du niveau d'expérience requis :
            - junior --> entre 1 et 3 ans d'expérience professionnelle
            - intermédiaire --> entre 3 et 10 ans d'expérience professionnelle
            - senior --> 10 ans et plus d'expérience professionnelle
        Aucune information personnelle (profil anonyme).
        Aucune motivation à mentionner.
        Aucune disponibilité ni de référence à fournir.
        ### Contraintes : 
        Pour le nom d'entreprise généré :
            - Ne doit pas contenir de suffixes légaux tels que : GmbH, AG, SARL, SA, Ltd., Inc., Corp., LLP, BV, Sp. z o.o., S.r.l., SL, ApS, AS, OOO, etc.
            - Doit être générique et créatif, sans référence explicite à une forme juridique.
            - Éviter les abréviations indiquant un statut d'entreprise.
        """,
    expected_output="Le profil du candidat idéal selon les instructions.",
    agent=redacteur_profil_candidat,
)

completer_profil_candidat = Task(
    description="""Tu dois rédiger un texte structuré en {langue_de_travail}, voici les instructions:
        Instructions
        ------------
        Tu dois compléter le profil du candidat anonyme qui répond au poste à pourvoir.
        Tu dois générer et ajouter au profil les informations suivantes :
            * Nom et prénom [prénom et nom variés selon le genre {genre}]
            * Passions et loisirs [plusieurs item]
            * pourquoi il est le bon candidat pour le poste [plusieurs item]
        """,
    expected_output="""Le profil complet du candidat idéal complété selon les instructions.
        Formatter toutes les informations selon le format suivant :
        {{  
          "poste_num": "{poste_num}",
          "company_name": "",
          "job_title": "",
          "candidate_full_name": "",
          "passions_hobbies": [],
          "why_is_a_good_fit": [],
          "academic_background_certifications": [],
          "technical_professional_skills": [],
          "interpersonal_soft_skills": [],
          "professional_experiences": [],
        }}
        Points de vigilance : 
        1- company_name et job_title proviennent des informations transmises par le rédacteur du poste.
        2- professional_experiences est une liste de dictionnaires python mentionnant le titre et les responsabilités occupées.
        3- ajoute des retours à la ligne pour que la structure du profil soit lisible.
        """,
        #3- l'outil File Writer nécessite un contenu en format string.
        #Écrit le profil complet dans le fichier {fichier_candidats} dans le répertoire {output_path}.
        #""",
    agent=redacteur_personna_candidat,
)

# ============== définition de l'équipe =======================

crew = Crew(
    agents=[preparateur_poste, redacteur_poste, redacteur_profil_candidat, redacteur_personna_candidat],
    tasks=[preparer_commande, redaction_poste, redaction_profil_candidat, completer_profil_candidat],
    verbose=True,  # You can set it to 1 or 2 to different logging levels
    process=Process.sequential
)


# ============== récupération des paramètres et lancement =======================
def write_clean_json(output_path, file_name, json_content):
    try:
        # Nettoyer le contenu JSON des balises ```json et ```
        cleaned_content = json_content.strip()
        if cleaned_content.lower().startswith("```json") and cleaned_content.endswith("```"):
            json_content = cleaned_content[len("```json"): -len("```")].strip()
        elif cleaned_content.startswith("```") and cleaned_content.endswith("```"):
            json_content = cleaned_content[len("```"): -len("```")].strip()

        # Convertir en dictionnaire JSON valide
        try:
            json_data = json.loads(json_content)
        except json.JSONDecodeError as e:
            raise ValueError(f"Le contenu fourni n'est pas un JSON valide : {e}")

        # Vérifier si le répertoire de sortie existe, sinon le créer
        os.makedirs(output_path, exist_ok=True)

        # Construire le chemin complet du fichier
        file_path = os.path.join(output_path, file_name)

        # Écrire le contenu JSON formaté dans le fichier
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(json_data, file, ensure_ascii=False, indent=4)

        print(f"Fichier JSON écrit avec succès à l'emplacement : {file_path}")

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


def main():
    parser = argparse.ArgumentParser(description="Process some parameters.")
    parser.add_argument('--fichier_postes', type=str, default="postes_generes.json", help='Path to the postes file')
    parser.add_argument('--output_path', type=str, default="./output/", help='Output path')
    parser.add_argument('--file_name', type=str, default="candidats_generes.json", help='Output file name')
    parser.add_argument('--langue_de_travail', type=str, default="français", help='Working language')
    parser.add_argument('--genre', type=str, default="féminin", help='Genre')
    parser.add_argument('--poste_num', type=str, default="1", help='Poste number')

    args = parser.parse_args()

    fichier_postes = args.fichier_postes
    output_path = args.output_path
    file_name = args.file_name
    langue_de_travail = args.langue_de_travail
    genre = args.genre
    poste_num = args.poste_num

    session_agentops = agentops.init(default_tags=["génération candidat"])

    fichier_candidats = file_name
    params = {
        "poste_num": poste_num,
        "fichier_postes": fichier_postes,
        "fichier_candidats": fichier_candidats,
        "output_path": output_path,
        "langue_de_travail": langue_de_travail,
        "genre": genre
    }
    result = crew.kickoff(inputs=params)
    print(f"###################### poste_num --> {poste_num} ######################")
    print(result)
    write_clean_json(output_path, file_name, str(result))


if __name__ == "__main__":
    main()



