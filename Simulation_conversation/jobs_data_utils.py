import json


class JobDataUtils:
    def __init__(self, json_file):
        """
        Initialise l'utilitaire avec un fichier JSON contenant les informations des postes.
        :param json_file: Chemin vers le fichier JSON.
        """
        print(f"Initialisation de JobDataUtils avec le fichier : {json_file}")
        self.json_file = json_file
        self.data = self._load_json()
        self.filtered_jobs = None  # Stocke les résultats du dernier filtrage

    def _load_json(self):
        """
        Charge le fichier JSON en mémoire.
        :return: Données JSON sous forme de dictionnaire.
        """
        print(f"Chargement des données depuis le fichier : {self.json_file}")
        try:
            with open(self.json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                print("Chargement réussi.")
                return data
        except FileNotFoundError as e:
            print(f"Erreur : Fichier non trouvé ({e})")
            return None
        except json.JSONDecodeError as e:
            print(f"Erreur : Décodage JSON échoué ({e})")
            return None

    def get_job_by_index(self, index):
        """
        Récupère les informations d'un poste spécifique par son index.
        :param index: Index du poste dans la liste des postes.
        :return: Dictionnaire contenant les informations du poste ou None si l'index est invalide.
        """
        print(f"Récupération du poste à l'index : {index}")
        if not self.data or "postes" not in self.data:
            print("Les données JSON ne contiennent pas de liste 'postes'.")
            return None

        try:
            job = self.data["postes"][index]
            print(f"Poste trouvé : {job}")
            return job
        except IndexError:
            print(f"Index {index} hors limites. Nombre de postes disponibles : {len(self.data['postes'])}.")
            return None

    def get_jobs_by_filter(self, **filters):
        """
        Filtre les postes en fonction des critères donnés.
        Si un filtrage précédent existe, il est utilisé comme base. Sinon, la base complète est utilisée.
        :param filters: Paires clé-valeur représentant les critères de filtre.
        :return: Liste des postes correspondant aux critères.
        """
        print(f"Filtrage des postes avec les critères : {filters}")

        # Utilise les résultats filtrés précédents ou la base complète
        base_jobs = self.filtered_jobs if self.filtered_jobs else self.data.get("postes", [])
        if not base_jobs:
            print("Aucun poste disponible pour le filtrage.")
            return []

        filtered_jobs = base_jobs
        for key, value in filters.items():
            print(f"Application du filtre - {key}: {value}")
            filtered_jobs = [job for job in filtered_jobs if any(value.lower() in str(item).lower() for item in (job.get(key) if isinstance(job.get(key), list) else [job.get(key)]))]

        print(f"Nombre de postes trouvés : {len(filtered_jobs)}")
        self.filtered_jobs = filtered_jobs  # Met à jour le dernier résultat filtré
        return filtered_jobs

    def reset_filters(self):
        """
        Réinitialise les résultats filtrés pour repartir de la base complète.
        """
        print("Réinitialisation des filtres. Retour à la base complète.")
        self.filtered_jobs = None

    def list_all_jobs(self):
        """
        Liste tous les postes disponibles.
        :return: Liste des dictionnaires contenant les informations des postes.
        """
        print("Liste de tous les postes disponibles.")
        if not self.data or "postes" not in self.data:
            print("Les données JSON ne contiennent pas de liste 'postes'.")
            return []

        print(f"Nombre total de postes : {len(self.data['postes'])}")
        return self.data["postes"]

    # Helpers pour récupérer les parties d'un job
    @staticmethod
    def get_job_title(job):
        return job.get("job_title", "")

    @staticmethod
    def get_company_name(job):
        return job.get("company_name", "")

    @staticmethod
    def get_job_description(job):
        return job.get("job_description", "")

    @staticmethod
    def get_responsibilities(job):
        return job.get("responsibilities", [])

    @staticmethod
    def get_skills_required(job):
        return job.get("skills_required", [])

    @staticmethod
    def get_location(job):
        return job.get("location", "")

    @staticmethod
    def get_experience_level(job):
        return job.get("experience_level", "")

    @staticmethod
    def get_education_required(job):
        return job.get("education_required", "")


# Exemple d'utilisation
if __name__ == "__main__":
    # Remplacez 'jobs.json' par le chemin réel de votre fichier JSON
    print("Initialisation de l'exemple d'utilisation...")
    utils = JobDataUtils("../AgentIA_generation_postes/exemples/postes_generes_new_prompt_gpt4-o1.json")

    # Récupérer un poste par index
    print("Test : Récupération du poste à l'index 0")
    job = utils.get_job_by_index(0)
    if job:
        print("Poste 0 :", job)

        # Utilisation des helpers
        print("Titre du poste :", JobDataUtils.get_job_title(job))
        print("Nom de l'entreprise :", JobDataUtils.get_company_name(job))
        print("Description du poste :", JobDataUtils.get_job_description(job))
        print("Responsabilités :", JobDataUtils.get_responsibilities(job))
        print("Compétences requises :", JobDataUtils.get_skills_required(job))
        print("Localisation :", JobDataUtils.get_location(job))
        print("Niveau d'expérience :", JobDataUtils.get_experience_level(job))
        print("Éducation requise :", JobDataUtils.get_education_required(job))

    # Filtrer les postes par localisation
    print("Test : Filtrage des postes par localisation 'Paris, France'")
    jobs_in_paris = utils.get_jobs_by_filter(location="Paris, France")
    print("Postes à Paris :", jobs_in_paris)

    # Filtrer les postes par niveau d'expérience
    print("Test : Filtrage des postes par niveau d'expérience 'Junior' sur les résultats précédents")
    junior_jobs_in_paris = utils.get_jobs_by_filter(experience_level="Junior")
    print("Postes Junior à Paris :", junior_jobs_in_paris)

    # Réinitialiser les filtres et appliquer un nouveau filtrage
    print("Réinitialisation des filtres.")
    utils.reset_filters()

    # Filtrer les postes par compétence requise contenant un mot clé
    print("Test : Filtrage des postes par compétence contenant 'Java'")
    java_jobs = utils.get_jobs_by_filter(skills_required="Java")
    print("Postes contenant 'Java' dans les compétences requises :", java_jobs)

    # Lister tous les postes
    print("Test : Liste de tous les postes")
    all_jobs = utils.list_all_jobs()
    print("Tous les postes :", all_jobs)
