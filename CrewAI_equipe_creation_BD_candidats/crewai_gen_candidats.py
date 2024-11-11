from textwrap import dedent

import agentops
from crewai import Agent, Crew, Process, Task
from dotenv import load_dotenv

load_dotenv()

agentops.init()

model_llm = "gpt-4"
nombre_profil_candidats = 1
fichier_postes = "postes_generes.json"
langue_de_travail = "français"

print("## Équipe de création des profils candidats fictifs")
print("---------------------------------------------------")

# ============== définition des agents =======================

chef_equipe = Agent(
    role="Chef d'équipe",
    goal="Organiser le travail de l'équipe afin d'atteindre ton objectif de rendement",
    backstory=dedent(
        """
        Tu es un chef d'équipe et tu organises le travail de tes collaborateurs.
        """
    ),
    allow_delegation=False,
    verbose=True,
    llm=model_llm
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
    llm=model_llm
)

# ============== définition des tâches =======================

passer_commande = Task(
    description=f"""Tu dois demander à ton équipe de produire des profils de candidats idéaux, voici les instructions:
        Instructions
        ------------
        Tu dois organiser le travail pour produire {nombre_profil_candidats} profils.        
        A partir du fichier {fichier_postes}, passe la commande à ton équipe em prenant la description des postes.
        Tu passes une commande à la fois.
        """,
    expected_output="Ta commande est simplement la lecture de la description du poste.",
    agent=chef_equipe,
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
        """,
    expected_output="Le CV du candidat idéal selon les instructions.",
    agent=redacteur_profil_candidat,
)

completer_profil_candidat = Task(
    description=f"""Tu dois rédiger un texte structuré en {langue_de_travail}, voici les instructions:
        Instructions
        ------------
        Tu dois compléter le CV du candidat idéal qui répond au poste à pourvoir.
        Tu dois ajouter au CV les informations suivantes :
            * Nom et prénom
            * Passion et loisirs
            * pourquoi il est le bon candidat pour le poste
        """,
    expected_output="Le CV du candidat idéal complété selon les instructions.",
    agent=redacteur_personna_candidat,
)

# ============== définition de l'équipe =======================

crew = Crew(
    agents=[chef_equipe, redacteur_poste, redacteur_profil_candidat, redacteur_profil_candidat],
    tasks=[passer_commande, redaction_poste, redaction_profil_candidat, completer_profil_candidat],
    verbose=True,  # You can set it to 1 or 2 to different logging levels
    process=Process.sequential,
)

# ============== définition de l'équipe =======================

result = crew.kickoff()

print("######################")
print(result)

