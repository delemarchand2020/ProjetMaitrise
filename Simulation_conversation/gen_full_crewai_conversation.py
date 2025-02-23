import agentops
import argparse
from dotenv import load_dotenv
from textwrap import dedent
import json
from crewai import Agent, Task, Crew, Process, LLM
from crewai.flow.flow import Flow, listen, start
from recruiters_data_utils import RecruiterDataUtils
from candidates_data_utils import CandidateDataUtils
from jobs_data_utils import JobDataUtils

load_dotenv()

model = "gpt-4o" #"mistral/mistral-large-latest" # "gpt-4o"

llm_creative = LLM(
    model=model,
    temperature=0.9,
    top_p=0.9,
    frequency_penalty=0.2,
    presence_penalty=0.2,
)

llm_doer = LLM(
    model=model,
    temperature=0.2,
    top_p=0.85,
    frequency_penalty=0.0,
    presence_penalty=0.0,
)

llm_middle_creative = LLM(
    model=model,
    temperature=0.8,
    top_p=0.9,
    frequency_penalty=0.1,
    presence_penalty=0.1,
)


def recruteur_task_callback(output, flow_instance):
    flow_instance.enregistrer_echange("Recruteur", output.raw)


def candidat_task_callback(output, flow_instance):
    flow_instance.enregistrer_echange("Candidat", output.raw)


# Définition des agents et de leurs tâches
def create_agents_and_tasks(profil_poste, profil_recruteur, profil_candidat, flow_instance):
    biais = False if RecruiterDataUtils.get_bias(profil_recruteur) == "" else True
    recruteur = Agent(
        role=f"{RecruiterDataUtils.get_recruiter_full_name(profil_recruteur)}, un recruteur",
        goal=dedent(
            f"""
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
            Tes passions et loisirs sont : {RecruiterDataUtils.get_passions_hobbies(profil_recruteur)}.
            Tes responsabilités sont : {RecruiterDataUtils.get_responsibilities(profil_recruteur)}.

            {"Tes croyances qui guident ta posture et tes questions :" if biais else ""}
            {RecruiterDataUtils.get_bias(profil_recruteur) if biais else ""}
            {RecruiterDataUtils.get_bias_hints(profil_recruteur) if biais else ""}
            """
        ),
        verbose=True,
        respect_context_window=False,
        llm=llm_creative
    )

    candidat = Agent(
        role=f"{CandidateDataUtils.get_candidate_full_name(profil_candidat)}, un(e) candidat(e)",
        goal=dedent(
            f"""
            Tu postules au poste suivant :
                Titre du poste : {JobDataUtils.get_job_title(profil_poste)}
                Nom de l'entreprise : {JobDataUtils.get_company_name(profil_poste)}
                Description du poste : {JobDataUtils.get_job_description(profil_poste)}
                Responsabilités : {JobDataUtils.get_responsibilities(profil_poste)}
                Compétences requises : {JobDataUtils.get_skills_required(profil_poste)}
                Localisation : {JobDataUtils.get_location(profil_poste)}
                Niveau d'expérience : {JobDataUtils.get_experience_level(profil_poste)}
                Éducation requise : {JobDataUtils.get_education_required(profil_poste)}
            Tu penses que tu es un bon candidat car tu possèdes : {CandidateDataUtils.get_why_is_a_good_fit(profil_candidat)}.
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
        respect_context_window=False,
        llm=llm_creative
    )

    task_recruteur = Task(
        description=dedent(
            """
            Réagis brièvement à la dernière réponse du/de la candidat(e) puis pose une nouvelle question.
            """
        ),
        expected_output=dedent(
            """
            Une ou deux phrases.
            ### contraintes :
                - Ne pose pas une question similaire à ce que tu as déjà posée précédemment.
                - Ne pas faire de compliments exagérés (comme votre expérience est impressionnante), rester professionnel.
                - Varie le type de questions selon les critères suivants :
                    - 50% des questions sur les expériences et les compétences techniques du candidat en rapport avec les responsabilités du poste à combler.
                    - 30% des questions sur les compétences interpersonnelles, relationnelles et humaines du candidat en rapport avec les responsabilités du poste à combler.
                    - 20% des questions sur les hobbies et les passions du candidat.
            """
        ),
        agent=recruteur,
        callback=lambda output: recruteur_task_callback(output, flow_instance)
    )

    task_candidat = Task(
        description=dedent(
            """
            Répond brièvement à la dernière question du recruteur mettant en avant tes compétences ou ton expérience.
            """
        ),
        expected_output=dedent(
            """
            Une ou deux phrases.
            ### contraintes : 
                - Ta réponse devra faire un lien avec les responsabilités du poste visé.
                - Ne pas reprendre mot pour mot la dernière phrase du recruteur.
            """
        ),
        agent=candidat,
        callback=lambda output: candidat_task_callback(output, flow_instance)
    )

    task_initiale = Task(
        description=dedent(
            """
            Question initiale : {question}
            Répond brièvement à la question initiale du recruteur mettant en avant tes compétences et ton expérience 
            en rapport avec les responsabilités du poste auquel tu postules.
            """
        ),
        expected_output=dedent(
            """
            Une ou deux phrases.
            ### contraintes :
                - Commence simplement ta réponse par "Bonjour" sans mentionner ton prénom ou ton nom
                - Ne pas reprendre mot pour mot la phrase du recruteur.
            """
        ),
        agent=candidat,
        callback=lambda output: candidat_task_callback(output, flow_instance)
    )

    task_finale = Task(
        description=dedent(
            """
            Mets fin à l'entrevue.
            Remercie le candidat ou la candidate.
            Explique les prochaines étapes du recrutement.
            Souhaite lui une bonne continuation dans ces recherches.
            """
        ),
        expected_output="Une ou deux phrases.",
        agent=recruteur,
        callback=lambda output: recruteur_task_callback(output, flow_instance)
    )

    task_candidat_finale = Task(
        description=dedent(
            """
            Remercie le recruteur pour cette entrevue en lui souhaitant une belle journée.
            """
        ),
        expected_output=dedent(
            """
            Une seule phrase.
            ### contraintes :
                - Ne pas reprendre mot pour mot la dernière phrase du recruteur.
            """
        ),
        agent=candidat,
        callback=lambda output: candidat_task_callback(output, flow_instance)
    )

    task_recruteur_bais = Task(
        description=dedent(
            f"""
            {"Réagis à la dernière réponse du/de la candidat(e) en te basant sur tes croyances :" if biais else task_recruteur.description}
            {RecruiterDataUtils.get_bias(profil_recruteur) if biais else ""}
            {"Puis pose une nouvelle question en t'inspirant de ces exemples:" if biais else ""}
            {RecruiterDataUtils.get_bias_hints(profil_recruteur) if biais else ""}
            """
        ),
        expected_output=dedent(
            """
            Une ou deux phrases.
            ### contraintes :
                - Ne pose pas une question similaire à ce que tu as déjà posée précédemment.
                - Ne pas faire de compliments exagérés (comme votre expérience est impressionnante), rester professionnel.
            """
        ),
        agent=recruteur,
        callback=lambda output: recruteur_task_callback(output, flow_instance)
    )

    return (recruteur, task_recruteur, candidat, task_candidat, task_initiale, task_finale,
            task_candidat_finale, task_recruteur_bais)


# Définition du Flow
class EntretienFlow(Flow):
    def __init__(self, max_echanges, profil_poste, profil_recruteur, profil_candidat, file_output):
        super().__init__()
        self.max_echanges = max_echanges
        self.poste = JobDataUtils.get_job_title(profil_poste)
        self.echanges_actuels = 1
        self.conversation = []
        self.session_agentops = agentops.init(auto_start_session=False)

        (self.recruteur, self.task_recruteur, self.candidat,
         self.task_candidat, self.task_initiale, self.task_finale, self.task_candidat_finale, self.task_recruteur_bais) = (
            create_agents_and_tasks(profil_poste, profil_recruteur, profil_candidat, flow_instance=self))

        self.profil_candidat = profil_candidat
        self.file_output = file_output

        print("Initialisation du flow terminée.")

    @start()
    def debut_entretien(self):
        # Le recruteur initie la conversation
        question_initiale = dedent(
            f"""
            Bonjour {CandidateDataUtils.get_candidate_first_name(self.profil_candidat)},
            vous postulez pour le poste de {self.poste}, pouvez vous m'en dire un peu plus sur vous et ce qui vous motive dans ce poste ?
            """
        )
        self.enregistrer_echange("Recruteur", question_initiale)
        print("Debut entretien.")
        return question_initiale

    @listen(debut_entretien)
    def entretien(self, question):

        # Le candidat répond à la question du recruteur
        self.session_agentops = agentops.start_session(tags=["échange candidat recruteur"])

        list_task = [self.task_initiale, self.task_recruteur,
                     self.task_candidat, self.task_recruteur_bais,
                     self.task_candidat, self.task_recruteur_bais,
                     self.task_candidat, self.task_recruteur,
                     self.task_candidat, self.task_finale,
                     self.task_candidat_finale]
        crew = Crew(
                agents=[self.candidat, self.recruteur],
                tasks=list_task,
                process=Process.sequential,
                verbose=True,
                memory=True
            )
        result = crew.kickoff(inputs={'question': question})

        self.session_agentops.end_session("Success")

        self.terminer_entretien()

    def enregistrer_echange(self, role, message):
        # Enregistre l'échange dans la conversation
        self.conversation.append({"role": role, "message": message})

    def terminer_entretien(self):
        # Sauvegarde la conversation dans un fichier JSON
        with open(self.file_output, 'w', encoding='utf-8') as f:
            json.dump(self.conversation, f, ensure_ascii=False, indent=2)

        print("Fin entretien.")


# Exécuter le Flow
# python .\gen_full_crewai_conversation.py --fichier_db_candidats "candidats_generes_f_poste_1.json" --output_file "new_conversation_f_poste_1.json"
# python .\gen_full_crewai_conversation.py --fichier_db_candidats "candidats_generes_m_poste_1.json" --output_file "new_conversation_m_poste_1.json"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some parameters.")
    parser.add_argument('--fichier_db_postes', type=str, default="postes_generes_new_prompt_gpt4-o1.json",
                        help='Db postes file')
    parser.add_argument('--fichier_db_recruteurs', type=str, default="recruteurs_generes.json",
                        help='Db recruteurs file')
    parser.add_argument('--fichier_db_candidats', type=str, default="candidats_generes_f_poste_1.json",
                        help='Db candidats file')
    parser.add_argument('--output_file', type=str, default="conversation_f_poste_1.json", help='Output file')
    parser.add_argument('--index', type=str, default="0", help='Index number')

    args = parser.parse_args()

    fichier_db_postes = args.fichier_db_postes
    fichier_db_recruteurs = args.fichier_db_recruteurs
    fichier_db_candidats = args.fichier_db_candidats

    output_file = f"./output/{args.output_file}"
    index = args.index

    print("Initialisation ...")
    db_jobs = JobDataUtils(fichier_db_postes)
    db_recruteurs = RecruiterDataUtils(fichier_db_recruteurs)
    db_candidats = CandidateDataUtils(fichier_db_candidats)

    candidat = db_candidats.get_candidate_by_index(int(index))
    recruteur = db_recruteurs.get_recruiter_by_index(int(index))
    job = db_jobs.get_job_by_index(int(index))

    if job and candidat and recruteur:
        print(dedent(
            f"""
            Le recruteur {RecruiterDataUtils.get_recruiter_full_name(recruteur)} 
            recherche un candidat pour le poste de {JobDataUtils.get_job_title(job)}.
            Le candidat {CandidateDataUtils.get_candidate_full_name(candidat)} postule.
            """
        ))
        flow = EntretienFlow(max_echanges=7, profil_poste=job, profil_recruteur=recruteur,
                             profil_candidat=candidat, file_output=output_file)
        flow_result = flow.kickoff()

