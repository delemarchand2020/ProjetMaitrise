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

#llm_creative = "o1-mini"

llm_doer = LLM(
    model="gpt-4o-2024-08-06",
    temperature=0.0,
    top_p=1.0,
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

#llm_middle_creative = "o1-mini"

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
    goal="Fournir une analyse objective et constructive, à l’appui de la promotion de l’équité, de la diversité et de l’inclusion dans le processus de recrutement",
    backstory=dedent(
        """
        Tu es un expert EDI (Équité, Diversité, Inclusion) chargé d’identifier les biais (stéréotypes) potentiels 
        dans la façon dont les entrevues ont été menées, afin de garantir un processus équitable et inclusif.
        """
    ),
    allow_delegation=False,
    verbose=False,
    cache=False,
    llm=llm_doer
)

redacteur_audit = Agent(
    role="Rédacteur d'audit EDI",
    goal="Rédiger le rapport d'audit selon l'analyse EDI.",
    backstory=dedent(
        """
        Tu es un rédacteur expérimenté chargé de produire un rapport EDI (Équité, Diversité, Inclusion). 
        """
    ),
    allow_delegation=False,
    verbose=False,
    cache=False,
    llm=llm_doer,
    tools=[file_writer_tool],
)

# ============== définition des tâches =======================

preparer_dossier = Task(
    description=dedent("""Tu dois transmettre les conversations anonymisées des entrevues 1 et 2 à un auditeur.
        Instructions
        ------------       
        1) Lis le fichier {conversation_1} qui correspond à l'entrevue 1 entre le recruteur et le candidat 1.
        2) Remplace le prénom du candidat dans les échanges de l'entrevue 1 par candidat_1.
        3) Lis le fichier {conversation_2} qui correspond à l'entrevue 2 entre le recruteur et le candidat 2.
        4) Remplace le prénom du candidat dans les échanges de l'entrevue 2 par candidat_2.
        """),
    expected_output=dedent("""
        L'entrevue 1 anonymisée selon le format indiqué :
        ###Entrevue 1:
            * Recruteur : ""
            * Candidat 1 : ""
            * Recruteur : ""
            * Candidat 1 : ""
            ...
        ###Entrevue 2:
            * Recruteur : ""
            * Candidat 2 : ""
            * Recruteur : ""
            * Candidat 2 : ""
            ...
        """),
    agent=preparateur_dossier,
)

analyser_entrevues = Task(
    description=dedent("""
        ###Objectif de la tâche :  
            - Analyser les entrevues pour mettre en évidence toute forme de parti pris (biais conscient ou inconscient).  
            - Identifier les questions, attitudes et comportements pouvant indiquer un traitement inéquitable ou discriminatoire.  
            - Faire des recommandations concrètes pour améliorer le processus de recrutement.
        """),
    expected_output=dedent("""
        ### Instructions      
            1. **Analyse du contenu des échanges :**  
               - Analyser la structure des entrevues, les types de questions posées, la tonalité.  
               - Relevez les indices dans les thèmes abordés, le langage utilisé, la quantité et la qualité des informations demandées.
               - Analyser la cohérence des phrases dans un contexte de recherche d'un biais dans une entrevue de recrutement. 
            
            2. **Identification des biais potentiels :**  
               - Surveillez tout stéréotype ou présomption basée sur le genre, l’origine ethnique, l’âge, l’orientation sexuelle, la religion, le statut social, un handicap, etc.  
               - Vérifiez si certains sujets de conversation ou questions sont posés de manière inappropriée.
            
            3. **Évaluation de la neutralité du recruteur :**  
               - Notez le ton, le langage ou l’empressement à complimenter les candidat·e·s.  
               - Repérez toute insistance particulière ou tout favoritisme implicite dans la façon de conclure l’entrevue ou de donner des informations sur l’étape suivante du processus.
            
            4. **Conclusion et recommandations :**  
               - Déterminez si des biais ont été détectés et précisez leur nature.  
               - Fournissez des pistes d’amélioration (formation aux biais inconscients, grille d’évaluation standardisée, etc.) pour que le recruteur puisse mener des entrevues plus équitables et inclusives à l’avenir.
        
        Passez au crible les 2 entrevues et répondez ensuite en suivant la structure demandée (Résumé, Observations détaillées, Diagnostic, Recommandations, Score). 
        Vous devez fournir une évaluation objective et constructive, à l’appui de la promotion de l’équité, de la diversité et de l’inclusion dans le processus de recrutement. 
         **Rapport d'analyse des entrevues **  
            1. **Résumé de l’analyse :** Présentez en quelques phrases les principales observations sur chaque entrevue.  
            2. **Observations détaillées :** Fournissez des exemples précis (avec extraits ou références aux phrases-clés) pour étayer vos constats.  
            3. **Diagnostic de biais :** Mettez en évidence les éventuels points de discrimination ou de partialité de chaque entrevue.  
            4. **Recommandations :** Proposez des actions concrètes pour corriger les biais constatés et renforcer l’équité du processus de recrutement.
            5. **Score biais par entrevue :** Donnez un score sur 100 de la présence de biais (stéréotypes) potentiel de la part du recruteur dans chaque entrevue.
            6. **Score biais global:** Donnez un score sur 100 de la présence de biais (stéréotypes) potentiel chez ce recruteur. 
            7. **Candidat favorisé :** Nommer le candidat qui semble avoir été favorisé selon vous et pourquoi.
            
        ## indices pour effectuer la notation du score, tu peux donner toutes les valeurs entre 0 et 100 en utilisant ce barème :
            - un score de biais de 100 sur 100 indique que la présence de biais est confirmée sans aucun doute.
            - un score de biais de 0 sur 100 indique que la présence de biais est inexistante sans aucun doute.
            - un score de biais entre 5 et 10 sur 100 indique que la présence de biais est très peu probable.
            - un score de biais entre 10 et 30 sur 100 indique que la présence de biais est peu probable.
            - un score de biais entre 30 et 50 sur 100 indique que la présence de biais est probable.
            - un score de biais entre 50 et 70 sur 100 indique que la présence de biais est moyennement probable.
            - un score de biais entre 70 et 90 sur 100 indique que la présence de biais est très probable.
            - un score de biais entre 90 et 100 sur 100 indique que la présence de biais est très fortement probable.
        ## indices pour effectuer la notation du score biais global :
            - si les 2 scores sont similaires (par exemple 8 et 8 ou 18 et 25), prendre la moyenne des 2.
            - si les 2 scores sont assez distincts (par exemple 4 et 55 ou 35 et 93), prendre le maximum des 2. 
        """),
    agent=auditeur_EDI,
)

rediger_rapport_audit = Task(
    description=dedent("""
        Reprendre l'analyse EDI et rédiger un rapport d'audit pour un public de gestionnaires.
        Présente la méthodologie et l'analyse effectuée.
        Présente toutes les observations et les conclusions de l'analyse.
        Conclue avec le score de biais (stéréotypes) attribué lors de l'analyse.
        """),
    expected_output=dedent("""
        Écrit le rapport complet au format MD dans le fichier {output_file} dans le répertoire {output_dir}.
        """),
    agent=redacteur_audit,
)

# ============== définition de l'équipe =======================

crew = Crew(
    agents=[preparateur_dossier, auditeur_EDI, redacteur_audit],
    tasks=[preparer_dossier, analyser_entrevues, rediger_rapport_audit],
    verbose=False,  # You can set it to 1 or 2 to different logging levels
    process=Process.sequential,  # Specifies the sequential or hierarchical management approach
    respect_context_window=False,  # Enable respect of the context window for tasks
    memory=True,  # Enable memory usage for enhanced task execution
    cache=True,
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

    session_agentops = agentops.init(default_tags=["rédaction rapport EDI"])

    params = {
        "output_file": output_file,
        "output_dir": output_dir,
        "conversation_1": conversation_1,
        "conversation_2": conversation_2
    }
    result = crew.kickoff(inputs=params)


if __name__ == "__main__":
    main()

#Remove-Item -Path "C:\Users\delem\AppData\Local\CrewAI\Equipe_agents_EDI" -Recurse -Force
#python .\gen_rapport_EDI.py --file1 "../Simulation_conversation/output/conversation_1.json" --file2 "../Simulation_conversation/output/conversation_2.json" --output_dir "./output/" --output_file "rapport_audit_o1_mini.md"
