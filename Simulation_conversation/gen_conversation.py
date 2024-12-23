import agentops
from dotenv import load_dotenv

import json
from crewai import Agent, Task, Crew, Process
from crewai.flow.flow import Flow, listen, start

load_dotenv()


# Définition des agents et de leurs tâches
def create_agents_and_tasks():
    recruteur = Agent(
        role="Recruteur",
        goal="Évaluer les compétences et l'expérience du candidat pour un poste spécifique.",
        backstory="Un recruteur cherchant à pourvoir un poste clé dans son entreprise.",
        verbose=True
    )

    candidat = Agent(
        role="Candidat",
        goal="Répondre aux questions du recruteur en présentant ses compétences et ses expériences.",
        backstory="Un professionnel expérimenté à la recherche de nouvelles opportunités.",
        verbose=True
    )

    task_recruteur = Task(
        description="Contexte : {historique}. Poses une courte question au candidat suivant sa dernière réponse : {reponse}.",
        expected_output="Une question courte et pertinente sur l'expérience du candidat.",
        agent=recruteur
    )

    task_candidat = Task(
        description="Contexte : {historique}. Réponds promptement à la dernière question du recruteur : {question}.",
        expected_output="Une courte réponse mettant en avant ton expérience.",
        agent=candidat
    )
    return recruteur, task_recruteur, candidat, task_candidat


# Définition du Flow
class EntretienFlow(Flow):
    def __init__(self, max_echanges, poste):
        super().__init__()
        self.max_echanges = max_echanges
        self.poste = poste
        self.echanges_actuels = 1
        self.conversation = []
        self.session_agentops = agentops.init(auto_start_session=False)
        self.recruteur, self.task_recruteur, self.candidat, self.task_candidat = create_agents_and_tasks()

    @start()
    def debut_entretien(self):
        # Le recruteur initie la conversation
        question_initiale = f"Pouvez-vous me parler de votre expérience professionnelle récente en tant que {self.poste} ?"
        self.enregistrer_echange("Recruteur", question_initiale)
        return question_initiale

    @listen(debut_entretien)
    def entretien(self, question):
        while True:
            # Le candidat répond à la question du recruteur
            self.session_agentops = agentops.start_session(tags=["reponse candidat"])
            crew = Crew(
                agents=[self.candidat],
                tasks=[self.task_candidat],
                process=Process.sequential,
                verbose=True
            )
            result = crew.kickoff(inputs={'question': question, 'historique': self.conversation})
            reponse = result.tasks_output[0].raw  # Accéder à la sortie brute de la première tâche
            self.enregistrer_echange("Candidat", reponse)
            self.session_agentops.end_session("Success")

            self.echanges_actuels += 1

            if self.echanges_actuels > self.max_echanges:
                break

            # Le recruteur pose une nouvelle question basée sur la réponse du candidat
            self.session_agentops = agentops.start_session(tags=["question recruteur"])
            crew = Crew(
                    agents=[self.recruteur],
                    tasks=[self.task_recruteur],
                    process=Process.sequential,
                    verbose=True
            )
            result = crew.kickoff(inputs={'reponse': reponse, 'historique': self.conversation})
            question = result.tasks_output[0].raw  # Accéder à la sortie brute de la première tâche
            self.enregistrer_echange("Recruteur", question)
            self.session_agentops.end_session("Success")

        self.terminer_entretien()

    def enregistrer_echange(self, agent, message):
        # Enregistre l'échange dans la conversation
        self.conversation.append({"agent": agent, "message": message})

    def terminer_entretien(self):
        # Sauvegarde la conversation dans un fichier JSON
        with open('conversation.json', 'w', encoding='utf-8') as f:
            json.dump(self.conversation, f, ensure_ascii=False, indent=2)


# Exécuter le Flow
if __name__ == "__main__":
    flow = EntretienFlow(max_echanges=4, poste="médecin urgentiste")
    flow_result = flow.kickoff()

