from textwrap import dedent

import agentops
from crewai import Agent, Crew, Process, Task
from crewai_tools import FileReadTool, FileWriterTool
from dotenv import load_dotenv

load_dotenv()

session_agentops = agentops.init()

model_llm = "gpt-4o"
nombre_profil_candidats = 1
poste_num = "2"
fichier_postes = "postes_generes.json"
fichier_candidats = f"candidats_generes_{session_agentops.session_id}.json"
output_path = "./output/"
langue_de_travail = "français"

file_read_tool = FileReadTool()
file_writer_tool = FileWriterTool()

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
    llm=model_llm,
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
    llm=model_llm
)

redacteur_profil_candidat = Agent(
    role="Rédacteur de profil de candidat",
    goal="Créer un CV de candidat idéal selon un descriptif de poste",
    backstory=dedent(
        """
        Tu es un rédacteur expérimenté pour produire un CV de candidat idéal.
        Tu as beaucoup d'expérience pour produire un profil de candidat réaliste. 
        """
    ),
    allow_delegation=False,
    verbose=True,
    llm=model_llm
)

redacteur_personna_candidat = Agent(
    role="Rédacteur de personna",
    goal="Créer un personna selon un profil de candidat",
    backstory=dedent(
        """
        Tu es un rédacteur expérimenté pour produire un personna réaliste. 
        """
    ),
    allow_delegation=False,
    verbose=True,
    llm=model_llm,
    tools=[file_writer_tool],
)

# ============== définition des tâches =======================

preparer_commande = Task(
    description=f"""Tu dois transmettre les informations au rédacteur de produire un profil de candidat idéal, voici les instructions:
        Instructions
        ------------       
        A partir du fichier {fichier_postes}, passe la commande au rédacteur em prenant la description d'un poste.
        Tu passes les informations d'un seul poste à la fois.
        Parmi tous les postes, tu choisis le poste numéro {poste_num}.
        """,
    expected_output="Un texte contenant les informations sur le poste.",
    agent=preparateur_poste,
)

redaction_poste = Task(
    description=f"""Tu dois rédiger un texte structuré en {langue_de_travail}, voici les instructions:
        Instructions
        ------------
        Tu dois extraire les informations du poste, les mettre en forme selon le format suivant :
        Un paragraphe sur la compagnie : 
        - nom
        - localisation
        - [imagine une brève description de la raison d'être de la compagnie]
        Un paragraphe sur le poste offert [le poste doit être écrit de manière non genré] :
        - titre du poste
        - description
        - responsabilités clés
        Un paragraphe sur le profil de candidat recherché :
        - compétences requises
        - niveau d'études requis si pertinent
        - [imagine les qualités humaines que recherche la compagnie en rapport avec sa raison d'être]
        Un paragraphe pour motiver les candidats à envoyer leur candidature :
        - [imagine un court texte très vendeur pour expliquer pourquoi postuler]
        """,
    expected_output="Le descriptif du poste selon les instructions.",
    agent=redacteur_poste,
)

redaction_profil_candidat = Task(
    description=f"""Tu dois rédiger un texte structuré en {langue_de_travail}, voici les instructions:
        Instructions
        ------------
        Tu dois générer un profil de candidat idéal qui répond au poste à pourvoir.
        Un profil de candidat contient les informations suivantes :
            * Formations académiques et certifications.
            * Compétences techniques/métiers.
            * Compétences humaines et relationnelles.
            * Expériences professionnelles.
        Les formations et le certifications doivent avoir des dates d'obtention.
        Les expériences doivent avoir des dates de réalisation.
        Les dates doivent être cohérentes (expérience qui se termine avant qu'une autre débute).
        """,
    expected_output="Le CV du candidat idéal selon les instructions.",
    agent=redacteur_profil_candidat,
)

completer_profil_candidat = Task(
    description=f"""Tu dois rédiger un texte structuré en {langue_de_travail}, voici les instructions:
        Instructions
        ------------
        Tu dois compléter le CV du candidat idéal qui répond au poste à pourvoir (poste_num = {poste_num}).
        Tu dois générer et ajouter au CV les informations suivantes :
            * Nom et prénom
            * Passions et loisirs [plusieurs item]
            * pourquoi il est le bon candidat pour le poste [plusieurs item]
        """,
    expected_output=f"""Le CV complet du candidat idéal complété selon les instructions.
        Formatter toutes les informations en selon le format suivant :
        {{  
          "poste_num": "",
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
        2- l'outil File Writer nécessite un contenu en format string.
        
        Ajoute cette nouvelle entrée dans le fichier {fichier_candidats} dans le répertoire {output_path}.
        """,
    agent=redacteur_personna_candidat,
)

# ============== définition de l'équipe =======================

crew = Crew(
    agents=[preparateur_poste, redacteur_poste, redacteur_profil_candidat, redacteur_profil_candidat],
    tasks=[preparer_commande, redaction_poste, redaction_profil_candidat, completer_profil_candidat],
    verbose=True,  # You can set it to 1 or 2 to different logging levels
    process=Process.sequential,
)

# ============== définition de l'équipe =======================

result = crew.kickoff()

print("######################")
print(result)

