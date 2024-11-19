import agentops
from textwrap import dedent
from crewai import Agent, Crew, Process, Task
from crewai_tools import FileReadTool, FileWriterTool
from dotenv import load_dotenv

load_dotenv()

model_llm = "gpt-4o"

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
    goal="Créer un profil de candidat idéal selon un descriptif de poste",
    backstory=dedent(
        """
        Tu es un rédacteur expérimenté pour produire un profil de candidat idéal et réaliste.
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
        Tu es un rédacteur expérimenté pour produire un personna réaliste pour compléter un profil de candidat. 
        """
    ),
    allow_delegation=False,
    verbose=True,
    llm=model_llm,
    tools=[file_writer_tool],
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
        3- l'outil File Writer nécessite un contenu en format string.
        4- ajoute des retours à la ligne pour que la structure du profil soit lisible.
        
        Écrit le profil complet dans le fichier {fichier_candidats} dans le répertoire {output_path}.
        """,
    agent=redacteur_personna_candidat,
)

# ============== définition de l'équipe =======================

crew = Crew(
    agents=[preparateur_poste, redacteur_poste, redacteur_profil_candidat, redacteur_personna_candidat],
    tasks=[preparer_commande, redaction_poste, redaction_profil_candidat, completer_profil_candidat],
    verbose=True,  # You can set it to 1 or 2 to different logging levels
    process=Process.sequential
)

# ============== définition de l'équipe =======================
fichier_postes = "postes_generes.json"
output_path = "./output/"
langue_de_travail = "français"
genre = "féminin"

session_agentops = agentops.init()

for poste_num in ["6"]:
    fichier_candidats = f"candidats_generes_{session_agentops.session_id}.json"
    params = {"poste_num": poste_num, "fichier_postes": fichier_postes, "fichier_candidats": fichier_candidats,
             "output_path": output_path, "langue_de_travail": langue_de_travail, "genre": genre}
    result = crew.kickoff(inputs=params)
    print(f"###################### poste_num --> {poste_num} ######################")
    print(result)


