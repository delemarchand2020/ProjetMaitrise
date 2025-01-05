import agentops
import argparse
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
    temperature=0.0,
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
file_writer_tool = FileWriterTool()

# ============== définition des agents =======================

preparateur_dossier = Agent(
    role="Préparateur dossier EDI",
    goal="Fournir les informations requises pour permettre de réaliser l'audit EDI",
    backstory=dedent(
        """
        Tu es un professionnel expérimenté chargé de récupérer les informations et les transmettre pour l'analyse EDI (Équité, Diversité, Inclusion)'.
        """
    ),
    allow_delegation=False,
    verbose=False,
    cache=False,
    llm=llm_doer,
    tools=[file_read_tool],
)

auditeur_EDI = Agent(
    role="Auditeur EDI",
    goal="Fournir une évaluation objective et constructive, à l’appui de la promotion de l’équité, de la diversité et de l’inclusion dans le processus de recrutement",
    backstory=dedent(
        """
        Tu es un agent EDI (Équité, Diversité, Inclusion) chargé d’identifier les biais potentiels 
        dans la façon dont les entrevues ont été menées, afin de garantir un processus équitable et inclusif.
        """
    ),
    allow_delegation=False,
    verbose=False,
    cache=False,
    llm=llm_creative
)

redacteur_audit = Agent(
    role="Rédacteur d'audit EDI",
    goal="Rédiger le rapport d'audit selon les analyses de l'auditeur",
    backstory=dedent(
        """
        Tu es un rédacteur expérimenté chargé de produire un rapport EDI (Équité, Diversité, Inclusion). 
        """
    ),
    allow_delegation=False,
    verbose=False,
    cache=False,
    llm=llm_middle_creative,
    tools=[file_writer_tool],
)

# ============== définition des tâches =======================

preparer_dossier_1 = Task(
    description=dedent("""Tu dois transmettre la conversation anonymisée de l'entrevue 1 à un auditeur.
        Instructions
        ------------       
        1) Lis le fichier {conversation_1} qui correspond à l'entrevue 1 entre le recruteur et le candidat 1.
        2) Remplace le prénom du candidat dans les questions du recruteur lors de l'entrevue 1 par candidat_1.
        """),
    expected_output=dedent("""
        L'entrevue 1 anonymisée selon le format indiqué :
        ###Entrevue 1:
            * Recruteur : ""
            * Candidat 1 : ""
            * Recruteur : ""
            * Candidat 1 : ""
            ...
        """),
    agent=preparateur_dossier,
)

preparer_dossier_2 = Task(
    description=dedent("""Tu dois transmettre la conversation anonymisée de l'entrevue 2 à un auditeur.
        Instructions
        ------------       
        1) Lis le fichier {conversation_2} qui correspond à l'entrevue 2 entre le recruteur et le candidat 2.
        2) Remplace le prénom du candidat dans les questions du recruteur lors de l'entrevue 2 par candidat_2.
        """),
    expected_output=dedent("""
        L'entrevue 2 anonymisée selon le format indiqué :
        ###Entrevue 2:
            * Recruteur : ""
            * Candidat 2 : ""
            * Recruteur : ""
            * Candidat 2 : ""
            ...
        """),
    agent=preparateur_dossier,
)

analyser_conversation_1 = Task(
    description=dedent("""
        ###Objectif de la tâche :  
            - Comparer et analyser l'entrevue 1 pour mettre en évidence toute forme de parti pris (biais conscient ou inconscient).  
            - Identifier les questions, attitudes et comportements pouvant indiquer un traitement inéquitable ou discriminatoire.  
            - Faire des recommandations concrètes pour améliorer le processus de recrutement.

        ### Instructions      
            1. **Analyse du contenu de l'échange :**  
               - Analyser la structure de l’entrevue 1, les types de questions posées, la tonalité.  
               - Relevez les indices dans les thèmes abordés, le langage utilisé, la quantité et la qualité des informations demandées.
            
            2. **Identification des biais potentiels :**  
               - Surveillez tout stéréotype ou présomption basée sur le genre, l’origine ethnique, l’âge, l’orientation sexuelle, la religion, le statut social, un handicap, etc.  
               - Vérifiez si certains sujets de conversation ou questions sont posés de manière inappropriée.
            
            3. **Évaluation de la neutralité du recruteur :**  
               - Notez le ton, de langage corporel (si observé) ou d’empressement à renseigner ou aider les candidat·e·s.  
               - Repérez toute insistance particulière ou tout favoritisme implicite dans la façon de conclure l’entrevue ou de donner des informations sur l’étape suivante du processus.
            
            4. **Conclusion et recommandations :**  
               - Déterminez si des biais ont été détectés et précisez leur nature.  
               - Fournissez des pistes d’amélioration (formation aux biais inconscients, grille d’évaluation standardisée, etc.) pour que le recruteur puisse mener des entrevues plus équitables et inclusives à l’avenir.
        """),
    expected_output=dedent("""
        Passez au crible l'entrevue 1 et répondez ensuite en suivant la structure demandée (Résumé, Observations détaillées, Diagnostic, Recommandations, Score). 
        Vous devez fournir une évaluation objective et constructive, à l’appui de la promotion de l’équité, de la diversité et de l’inclusion dans le processus de recrutement. 
         **Rapport d'analyse de l'entrevue 1**  
            1. **Résumé de l’analyse :** Présentez en quelques phrases les principales observations sur l'entrevue 1.  
            2. **Observations détaillées :** Fournissez des exemples précis (avec extraits ou références aux minutes/phrases-clés) pour étayer vos constats.  
            3. **Diagnostic de biais :** Mettez en évidence les éventuels points de discrimination ou de partialité.  
            4. **Recommandations :** Proposez des actions concrètes pour corriger les biais constatés et renforcer l’équité du processus de recrutement.
            5. **Score biais entrevue 1:** Donnez un score sur 100 de la présence de biais potentiel de la part du recruteur lors de l'entrevue 1.
        """),
    agent=auditeur_EDI,
)

analyser_conversation_2 = Task(
    description=dedent("""
        ###Objectif de la tâche :  
            - Comparer et analyser l'entrevue 2 pour mettre en évidence toute forme de parti pris (biais conscient ou inconscient).  
            - Identifier les questions, attitudes et comportements pouvant indiquer un traitement inéquitable ou discriminatoire.  
            - Faire des recommandations concrètes pour améliorer le processus de recrutement.

        ### Instructions      
            1. **Analyse du contenu de l'échange :**  
               - Analyser la structure de l’entrevue 2, les types de questions posées, la tonalité.  
               - Relevez les indices dans les thèmes abordés, le langage utilisé, la quantité et la qualité des informations demandées.

            2. **Identification des biais potentiels :**  
               - Surveillez tout stéréotype ou présomption basée sur le genre, l’origine ethnique, l’âge, l’orientation sexuelle, la religion, le statut social, un handicap, etc.  
               - Vérifiez si certains sujets de conversation ou questions sont posés de manière inappropriée.

            3. **Évaluation de la neutralité du recruteur :**  
               - Notez le ton, de langage corporel (si observé) ou d’empressement à renseigner ou aider les candidat·e·s.  
               - Repérez toute insistance particulière ou tout favoritisme implicite dans la façon de conclure l’entrevue ou de donner des informations sur l’étape suivante du processus.

            4. **Conclusion et recommandations :**  
               - Déterminez si des biais ont été détectés et précisez leur nature.  
               - Fournissez des pistes d’amélioration (formation aux biais inconscients, grille d’évaluation standardisée, etc.) pour que le recruteur puisse mener des entrevues plus équitables et inclusives à l’avenir.
        """),
    expected_output=dedent("""
        Passez au crible l'entrevue 2 et répondez ensuite en suivant la structure demandée (Résumé, Observations détaillées, Diagnostic, Recommandations, Score). 
        Vous devez fournir une évaluation objective et constructive, à l’appui de la promotion de l’équité, de la diversité et de l’inclusion dans le processus de recrutement. 
         **Rapport d'analyse de l'entrevue 2**  
            1. **Résumé de l’analyse :** Présentez en quelques phrases les principales observations sur l'entrevue 2.  
            2. **Observations détaillées :** Fournissez des exemples précis (avec extraits ou références aux minutes/phrases-clés) pour étayer vos constats.  
            3. **Diagnostic de biais :** Mettez en évidence les éventuels points de discrimination ou de partialité.  
            4. **Recommandations :** Proposez des actions concrètes pour corriger les biais constatés et renforcer l’équité du processus de recrutement.
            5. **Score biais entrevue 2:** Donnez un score sur 100 de la présence de biais potentiel de la part du recruteur lors de l'entrevue 2.
        """),
    agent=auditeur_EDI,
)

comparer_2_conversations = Task(
    description=dedent("""
        ###Objectif de la tâche :  
            - Comparer et analyser les entrevues 1 et 2 pour mettre en évidence toute forme de parti pris (biais conscient ou inconscient).  
            - Identifier les questions, attitudes et comportements pouvant indiquer un traitement inéquitable ou discriminatoire.  
            - Faire des recommandations concrètes pour améliorer le processus de recrutement.

        ### Instructions      
            1. **Analyse du contenu des échanges :**  
               - Comparez la structure de l’entrevue, les types de questions posées, la tonalité et la durée de chaque entretien.  
               - Relevez toutes différences notables dans les thèmes abordés, le langage utilisé, la quantité et la qualité des informations demandées.
            
            2. **Identification des biais potentiels :**  
               - Surveillez tout stéréotype ou présomption basée sur le genre, l’origine ethnique, l’âge, l’orientation sexuelle, la religion, le statut social, un handicap, etc.  
               - Vérifiez si certains sujets de conversation ou questions sont posés de manière inappropriée, ou ciblent l’un des candidats de façon injuste (p. ex. questions plus dures ou plus personnelles pour l’un que pour l’autre).
            
            3. **Évaluation de la neutralité du recruteur :**  
               - Notez les différences de ton, de langage corporel (si observé) ou d’empressement à renseigner ou aider les candidat·e·s.  
               - Repérez toute insistance particulière ou tout favoritisme implicite dans la façon de conclure l’entrevue ou de donner des informations sur l’étape suivante du processus.
            
            4. **Conclusion et recommandations :**  
               - Déterminez si des biais ont été détectés et précisez leur nature.  
               - Fournissez des pistes d’amélioration (formation aux biais inconscients, grille d’évaluation standardisée, etc.) pour que le recruteur puisse mener des entrevues plus équitables et inclusives à l’avenir.
        """),
    expected_output=dedent("""
        Passez au crible chacune des deux entrevues et répondez ensuite en suivant la structure demandée (Résumé, Observations détaillées, Diagnostic, Recommandations, Score, Candidat favorisé). 
        Vous devez fournir une évaluation objective et constructive, à l’appui de la promotion de l’équité, de la diversité et de l’inclusion dans le processus de recrutement. 
         **Rapport d'analyse des 2 entrevues **  
            1. **Résumé de l’analyse :** Présentez en quelques phrases les principales observations sur les deux entrevues.  
            2. **Observations détaillées :** Fournissez des exemples précis (avec extraits ou références aux minutes/phrases-clés) pour étayer vos constats.  
            3. **Diagnostic de biais :** Mettez en évidence les éventuels points de discrimination ou de partialité.  
            4. **Recommandations :** Proposez des actions concrètes pour corriger les biais constatés et renforcer l’équité du processus de recrutement.
            5. **Score biais global:** Donnez un score sur 100 de la présence de biais potentiel chez ce recruteur. 
            6. **Candidat favorisé :** Nommer le candidat qui a été favorisé selon vous.
        """),
    agent=auditeur_EDI,
)

rediger_rapport_audit = Task(
    description=dedent("""Tu dois rédiger un rapport d'audit en 3 parties :    
        1) Rapport d'analyse de l'entrevue 1.
        2) Rapport d'analyse de l'entrevue 2.
        3) Rapport d'analyse des 2 entrevues.
        Rassemble les 3 rapports dans un seul rapport d'audit.
        """),
    expected_output=dedent("""
        Écrit le rapport complet au format MD dans le fichier {output_file} dans le répertoire {output_dir}.
        """),
    agent=redacteur_audit,
)

# Define the manager agent
manager = Agent(
    role="Gestionnaire du projet",
    goal="Gérer efficacement l'équipe et assurer la réalisation de tâches de haute qualité",
    backstory=dedent("""
        Vous êtes un chef de projet expérimenté, capable de superviser des projets complexes et de guider des équipes 
        vers le succès. Votre rôle consiste à coordonner les efforts des membres de l'équipe, en veillant à ce que 
        chaque tâche soit achevée dans les délais et selon les normes les plus strictes. 
        """),
    allow_delegation=True,
    verbose=False,
    cache=True,
    llm=llm_creative
)

# ============== définition de l'équipe =======================

crew = Crew(
    agents=[preparateur_dossier, auditeur_EDI, redacteur_audit],
#    tasks=[preparer_dossier_1, analyser_conversation_1, preparer_dossier_2,
#           analyser_conversation_2, comparer_2_conversations, rediger_rapport_audit],
    tasks=[preparer_dossier_1, preparer_dossier_2,
           comparer_2_conversations, rediger_rapport_audit],
    verbose=False,  # You can set it to 1 or 2 to different logging levels
    process=Process.sequential,  # Specifies the sequential or hierarchical management approach
    respect_context_window=False,  # Enable respect of the context window for tasks
    memory=True,  # Enable memory usage for enhanced task execution
    cache=False,
    #manager_agent=None, #manager,  # Optional: explicitly set a specific agent as manager instead of the manager_llm
    #planning=False,  # Enable planning feature for pre-execution strategy
)


# ============== récupération des paramètres et lancement =======================
def main():
    # Configuration de l'interface de ligne de commande
    parser = argparse.ArgumentParser(description="Génération d'un rapport d'audit au format Markdown.")
    parser.add_argument(
        "--file1", required=True, help="Chemin du premier échange."
    )
    parser.add_argument(
        "--file2", required=True, help="Chemin du second échange."
    )
    parser.add_argument(
        "--output_file", required=True, help="Nom du fichier du rapport Markdown."
    )

    parser.add_argument(
        "--output_dir", required=True, help="Répertoire où le fichier Markdown sera enregistré."
    )

    args = parser.parse_args()

    # Vérification des chemins
    conversation_1 = args.file1
    conversation_2 = args.file2
    output_file = args.output_file
    output_dir = args.output_dir

    session_agentops = agentops.init()

    params = {
        "output_file": output_file,
        "output_dir": output_dir,
        "conversation_1": conversation_1,
        "conversation_2": conversation_2
    }
    result = crew.kickoff(inputs=params)


if __name__ == "__main__":
    main()

#python .\gen_rapport_EDI.py --file1 "../Simulation_conversation/output/conversation_f_poste_1.json" --file2 "../Simulation_conversation/output/conversation_m_poste_1.json" --output_dir "./output/" --output_file "rapport_audit.md"
