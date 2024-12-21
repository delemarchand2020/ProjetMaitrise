import agentops
from dotenv import load_dotenv

import json
from crewai import Agent, Task, Crew, Process
from crewai.flow.flow import Flow, listen, start, or_

load_dotenv()

# Définition des agents
recruteur = Agent(
    role="Recruteur",
    goal="Évaluer les compétences et l'expérience du candidat pour un poste spécifique.",
    backstory="Un recruteur cherchant à pourvoir un poste clé dans son entreprise.",
    verbose=True
)

candidat = Agent(
    role="Candidat",
    goal="Répondre aux questions du recruteur et présenter ses compétences et expériences.",
    backstory="Un professionnel expérimenté à la recherche de nouvelles opportunités.",
    verbose=True
)

# Définition des tâches
task_recruteur = Task(
    description="Pose une question au candidat concernant son expérience professionnelle.",
    expected_output="Une question courte et pertinente sur l'expérience du candidat.",
    agent=recruteur
)

task_candidat = Task(
    description="Réponds à la question du recruteur.",
    expected_output="Une réponse courte mettant en avant ton expérience.",
    agent=candidat
)

# Définition du Flow
class EntretienFlow(Flow):
    def __init__(self, max_echanges):
        super().__init__()
        self.max_echanges = max_echanges
        self.echanges_actuels = 1
        self.conversation = []

    @start()
    def debut_entretien(self):
        # Le recruteur initie la conversation
        question_initiale = "Pouvez-vous me parler de votre expérience professionnelle récente ?"
        self.enregistrer_echange("Recruteur", question_initiale)
        return question_initiale

    @listen(debut_entretien)
    def reponse_candidat(self, question):
        # Le candidat répond à la question du recruteur
        crew = Crew(
            agents=[candidat],
            tasks=[task_candidat],
            process=Process.sequential,
            verbose=True
        )
        result = crew.kickoff(inputs={'input': question})
        reponse = result.tasks_output[0].raw  # Accéder à la sortie brute de la première tâche
        self.enregistrer_echange("Candidat", reponse)
        return reponse

    @listen(or_(reponse_candidat, "continuer_entretien"))
    def question_suivante_recruteur(self, reponse):
        if "Entretien terminé." not in reponse:
            # Le recruteur pose une nouvelle question basée sur la réponse du candidat
            crew = Crew(
                agents=[recruteur],
                tasks=[task_recruteur],
                process=Process.sequential,
                verbose=True
            )
            result = crew.kickoff(inputs={'input': reponse})
            question = result.tasks_output[0].raw  # Accéder à la sortie brute de la première tâche
            self.enregistrer_echange("Recruteur", question)
            return question

    @listen(question_suivante_recruteur)
    def continuer_entretien(self, message):
        # Vérifie si le nombre maximal d'échanges est atteint
        if self.echanges_actuels >= self.max_echanges:
            return self.terminer_entretien()
        else:
            self.echanges_actuels += 1
            return self.reponse_candidat(message)

    def enregistrer_echange(self, agent, message):
        # Enregistre l'échange dans la conversation
        self.conversation.append({"agent": agent, "message": message})

    def terminer_entretien(self):
        # Sauvegarde la conversation dans un fichier JSON
        with open('conversation.json', 'w', encoding='utf-8') as f:
            json.dump(self.conversation, f, ensure_ascii=False, indent=2)
        return "Entretien terminé."

# Exécuter le Flow
if __name__ == "__main__":
    max_echanges = 5  # Définissez le nombre maximal d'échanges souhaité
    session_agentops = agentops.init()
    flow = EntretienFlow(max_echanges)
    result = flow.kickoff()
    print(result)
    flow.terminer_entretien()
