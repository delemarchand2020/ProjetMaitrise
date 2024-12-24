import agentops
from dotenv import load_dotenv
from textwrap import dedent
import json
from crewai import Agent, Task, Crew, Process, LLM
from crewai.flow.flow import Flow, listen, start
from recruiters_data_utils import RecruiterDataUtils
from candidates_data_utils import CandidateDataUtils
from jobs_data_utils import JobDataUtils

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

# Définition des agents et de leurs tâches
def create_agents_and_tasks(profil_poste, profil_recruteur, profil_candidat):
    biais = False if RecruiterDataUtils.get_bias(profil_recruteur) == "" else True
    recruteur = Agent(
        role=f"{RecruiterDataUtils.get_recruiter_full_name(profil_recruteur)}, un recruteur",
        goal=dedent(
            f"""
            Tes responsabilités sont : {RecruiterDataUtils.get_responsibilities(profil_recruteur)}.
            Tu recherches un candidat pour le poste suivant :
                Titre du poste : {JobDataUtils.get_job_title(profil_poste)}
                Nom de l'entreprise : {JobDataUtils.get_company_name(profil_poste)}
                Description du poste : {JobDataUtils.get_job_description(profil_poste)}
                Responsabilités : {JobDataUtils.get_responsibilities(profil_poste)}
                Compétences requises : {JobDataUtils.get_skills_required(profil_poste)}
                Localisation : {JobDataUtils.get_location(profil_poste)}
                Niveau d'expérience : {JobDataUtils.get_experience_level(profil_poste)}
                Éducation requise : {JobDataUtils.get_education_required(profil_poste)}
            """
            ),
        backstory=dedent(
            f"""
            {RecruiterDataUtils.get_role_description(profil_recruteur)}.
            Ses passions et loisirs sont : {RecruiterDataUtils.get_passions_hobbies(profil_recruteur)}.
            {RecruiterDataUtils.get_bias(profil_recruteur) if biais else ""}.
            {RecruiterDataUtils.get_bias_hints(profil_recruteur) if biais else ""}.
            """
            ),
        verbose=True,
        llm=llm_creative
    )

    candidat = Agent(
        role=f"{CandidateDataUtils.get_candidate_full_name(profil_candidat)}, un(e) candidat(e)",
        goal=dedent(
            f"""
            Tu postules au poste de {JobDataUtils.get_job_title(profil_poste)} pour la compagnie {JobDataUtils.get_company_name(profil_poste)}.
            Tu penses que tu es un bon candidat car tu possèdes : {CandidateDataUtils.get_why_is_a_good_fit(profil_candidat)}.
            Ta motivation est grande pour obtenir ce job !
            """
            ),
        backstory=dedent(
            f"""
            Tes passions et loisirs : {CandidateDataUtils.get_passions_hobbies(profil_candidat)}.
            Tes Formation et certifications : {CandidateDataUtils.get_academic_background_certifications(profil_candidat)}.
            Tes compétences techniques et professionnelles : {CandidateDataUtils.get_technical_professional_skills(profil_candidat)}.
            Tes compétences interpersonnelles : {CandidateDataUtils.get_interpersonal_soft_skills(profil_candidat)}.
            Tes expériences professionnelles : {CandidateDataUtils.get_professional_experiences(profil_candidat)}.
            """
            ),
        verbose=True,
        llm=llm_creative
    )

    task_recruteur = Task(
        description=dedent(
            """
            C'est une première entrevue.
            --------------------------------------------------------------------------
            L’historique de la conversation de l'entrevue est :
            {historique}
            --------------------------------------------------------------------------
            Tu dois :
            1) Obtenir une vision générale du/de la candidat(e).
            2) Ne pas aborder trop en profondeur les détails techniques ou technologiques.
            --------------------------------------------------------------------------
            Variables :
            historique : Historique de la conversation.
            max_echanges : Nombre maximum d’échanges autorisés (1 question + 1 réponse = 1 échange).
            reponse : Dernière réponse du/de la candidat(e).
            --------------------------------------------------------------------------
            Consignes :
            Prend connaissance de l'historique.
            Tu ne dois pas dépasser {max_echanges} échanges.
            Si le nombre d’échanges restant avant d’atteindre {max_echanges} est 1, termine l’entretien en formulant tes conclusions (pas de nouvelle question).
            Sinon, réagis brièvement à la dernière réponse du/de la candidat(e) ({reponse}) et pose une question courte en restant général (pas de question trop technique).
            """
            ),
        expected_output="Une question courte et pertinente en rapport avec ce que tu cherches à atteindre et selon tes convictions.",
        agent=recruteur
    )

    task_candidat = Task(
        description=dedent(
            """
            Historique de la conversation : {historique}. 
            Réponds succinctement à la dernière question du recruteur : {question}.
            """
            ),
        expected_output="Une réponse courte mettant en avant ta motivation.",
        agent=candidat
    )
    return recruteur, task_recruteur, candidat, task_candidat


# Définition du Flow
class EntretienFlow(Flow):
    def __init__(self, max_echanges, profil_poste, profil_recruteur, profil_candidat):
        super().__init__()
        self.max_echanges = max_echanges
        self.poste = JobDataUtils.get_job_title(profil_poste)
        self.echanges_actuels = 1
        self.conversation = []
        self.session_agentops = agentops.init(auto_start_session=False)
        self.recruteur, self.task_recruteur, self.candidat, self.task_candidat = create_agents_and_tasks(profil_poste, profil_recruteur, profil_candidat)
        self.profil_candidat = profil_candidat
        print("Initialisation du flow terminée.")

    @start()
    def debut_entretien(self):
        # Le recruteur initie la conversation
        question_initiale = dedent(
            f"""
            Bonjour {CandidateDataUtils.get_candidate_full_name(self.profil_candidat)},
            vous postulez pour le poste de {self.poste}, dites m'en un peu plus sur vous ?
            """
            )
        self.enregistrer_echange("Recruteur", question_initiale)
        print("Debut entretien.")
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

            print(f"Fin échange {self.echanges_actuels}.")

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
            result = crew.kickoff(inputs={'reponse': reponse, 'historique': self.conversation, 'max_echanges': self.max_echanges})
            question = result.tasks_output[0].raw  # Accéder à la sortie brute de la première tâche
            self.enregistrer_echange("Recruteur", question)
            self.session_agentops.end_session("Success")

        self.terminer_entretien()

    def enregistrer_echange(self, role, message):
        # Enregistre l'échange dans la conversation
        self.conversation.append({"role": role, "message": message})

    def terminer_entretien(self):
        # Sauvegarde la conversation dans un fichier JSON
        with open('conversation.json', 'w', encoding='utf-8') as f:
            json.dump(self.conversation, f, ensure_ascii=False, indent=2)


# Exécuter le Flow
if __name__ == "__main__":
    print("Initialisation ...")
    db_jobs = JobDataUtils("../AgentIA_generation_postes/exemples/postes_generes_new_prompt_gpt4-o1.json")
    db_recruteurs = RecruiterDataUtils("../AgentAI_creation_BD_recruteurs/output/recruteurs_generes.json")
    db_candidats = CandidateDataUtils("../CrewAI_equipe_creation_BD_candidats/output/candidats_generes_638b5426-1127-40ac-af18-ec95d497a799.json")

    candidat = db_candidats.get_candidate_by_index(0)
    recruteur = db_recruteurs.get_recruiter_by_index(0)
    job = db_jobs.get_job_by_index(0)

    if job and candidat and recruteur:
        print(dedent(
            f"""
            Le recruteur {RecruiterDataUtils.get_recruiter_full_name(recruteur)} 
            recherche un candidat pour le poste de {JobDataUtils.get_job_title(job)}.
            Le candidat {CandidateDataUtils.get_candidate_full_name(candidat)} postule.
            """
            ))
        flow = EntretienFlow(max_echanges=10, profil_poste=job, profil_recruteur=recruteur, profil_candidat=candidat)
        flow_result = flow.kickoff()

