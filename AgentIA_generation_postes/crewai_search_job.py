from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool
import json
import yaml
from dotenv import load_dotenv
from pathlib import Path
from pydantic import BaseModel, ValidationError, Field
from typing import List
import agentops


# Charger les variables d'environnement
load_dotenv()

# Configuration du modèle de langage
llm = LLM(
    model="gpt-4o",
    temperature=0.9,
    top_p=0.9,
    frequency_penalty=0.2,
    presence_penalty=0.2,
)

# Chemins des fichiers de configuration
AGENTS_CONFIG_PATH = Path("config/agents.yaml")
TASKS_CONFIG_PATH = Path("config/tasks.yaml")

# Fonction utilitaire pour charger les fichiers YAML
def load_yaml_config(path: Path):
    if not path.exists():
        raise FileNotFoundError(f"Le fichier {path} est introuvable.")
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

# Charger la configuration de l'agent
def load_agent_config(agent_name: str):
    config = load_yaml_config(AGENTS_CONFIG_PATH)
    if agent_name not in config:
        raise KeyError(f"L'agent '{agent_name}' n'existe pas dans {AGENTS_CONFIG_PATH}.")
    return config[agent_name]

# Charger la configuration de la tâche
def load_task_config(task_name: str):
    config = load_yaml_config(TASKS_CONFIG_PATH)
    if task_name not in config:
        raise KeyError(f"La tâche '{task_name}' n'existe pas dans {TASKS_CONFIG_PATH}.")
    return config[task_name]

# Créer l'agent chercheur
def create_researcher_agent():
    config = load_agent_config('researcher')
    return Agent(
        role=config['role'],
        goal=config['goal'],
        backstory=config['backstory'],
        verbose=True,
        llm=llm,
        tools=[SerperDevTool()]
    )



class JobPosting(BaseModel):
    company_name: str
    job_title: str
    job_description: str
    responsibilities: List[str] = Field(default_factory=list)
    skills_required: List[str] = Field(default_factory=list)
    location: str
    experience_level: str
    education_required: str

def format_results(results):
    try:
        parsed = json.loads(results)
        if not isinstance(parsed, list):
            raise ValueError("Le JSON parsé n'est pas une liste.")

        jobs = []
        for entry in parsed:
            try:
                job = JobPosting(**entry)
                jobs.append(job.dict())
            except ValidationError as e:
                print(f"Erreur de validation pour une entrée :\n{e}\nEntrée ignorée.")
        return json.dumps(jobs, indent=2)

    except (json.JSONDecodeError, ValueError) as e:
        return f"[ERREUR] Le format n'était pas un JSON valide : {e}\n\nSortie brute :\n{results}"

# Lancer la recherche d'emploi
def run_job_search(job_title: str, location: str):
    agent = create_researcher_agent()
    task_config = load_task_config('job_search')

    task = Task(
        description=task_config['description'].format(job_title=job_title, location=location),
        agent=agent,
        expected_output=task_config['expected_output']
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True
    )

    crew_output = crew.kickoff()
    results = crew_output  # Extraire le texte (str)

    return format_results(results.raw)

# Point d'entrée
if __name__ == "__main__":
    session_agentops = agentops.init(default_tags=["recherche jobs"])
    results = run_job_search(job_title="Chef de projet IA", location="Paris")
    print(results)
