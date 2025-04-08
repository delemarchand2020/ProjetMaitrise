import json
from utils import nettoyer_chaine


class CandidateDataUtils:
    def __init__(self, json_file):
        """
        Initialise l'utilitaire avec un fichier JSON contenant les informations des candidats.
        :param json_file: Chemin vers le fichier JSON.
        """
        print(f"Initialisation de CandidateDataUtils avec le fichier : {json_file}")
        self.json_file = json_file
        self.data = self._load_json()
        self.filtered_candidates = None  # Stocke les résultats du dernier filtrage

    def _load_json(self):
        """
        Charge le fichier JSON en mémoire et gère différents encodages.
        :return: Données JSON sous forme de liste ou dictionnaire.
        """
        print(f"Chargement des données depuis le fichier : {self.json_file}")
        for encoding in ["utf-8", "latin1"]:
            try:
                with open(self.json_file, 'r', encoding=encoding) as file:
                    data = json.load(file)
                    print(f"Chargement réussi avec l'encodage {encoding}.")
                    # Convertir un objet unique en liste pour une gestion uniforme
                    if isinstance(data, dict):
                        return [data]
                    return data
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Échec du chargement avec l'encodage {encoding} : {e}")
        print("Erreur : Impossible de charger le fichier avec les encodages pris en charge.")
        return None

    def get_candidate_by_index(self, index) -> dict | None :
        """
        Récupère les informations d'un candidat spécifique par son index.
        :param index: Index du candidat dans la liste des candidats.
        :return: Dictionnaire contenant les informations du candidat ou None si l'index est invalide.
        """
        print(f"Récupération du candidat à l'index : {index}")
        if not isinstance(self.data, list):
            print("Les données JSON ne contiennent pas de liste de candidats.")
            return None

        try:
            candidate = self.data[index]
            print(f"Candidat trouvé : {candidate}")
            return candidate
        except IndexError:
            print(f"Index {index} hors limites. Nombre de candidats disponibles : {len(self.data)}.")
            return None

    def get_candidates_by_filter(self, **filters):
        """
        Filtre les candidats en fonction des critères donnés.
        Si un filtrage précédent existe, il est utilisé comme base. Sinon, la base complète est utilisée.
        :param filters: Paires clé-valeur représentant les critères de filtre.
        :return: Liste des candidats correspondant aux critères.
        """
        print(f"Filtrage des candidats avec les critères : {filters}")

        # Utilise les résultats filtrés précédents ou la base complète
        base_candidates = self.filtered_candidates if self.filtered_candidates else self.data
        if not isinstance(base_candidates, list):
            print("Les données JSON ne contiennent pas de liste de candidats.")
            return []

        filtered_candidates = base_candidates
        for key, value in filters.items():
            print(f"Application du filtre - {key}: {value}")
            filtered_candidates = [
                cand for cand in filtered_candidates if any(
                    value.lower() in str(item).lower()
                    for item in (cand.get(key) if isinstance(cand.get(key), list) else [cand.get(key)])
                )
            ]

        print(f"Nombre de candidats trouvés : {len(filtered_candidates)}")
        self.filtered_candidates = filtered_candidates  # Met à jour le dernier résultat filtré
        return filtered_candidates

    def reset_filters(self):
        """
        Réinitialise les résultats filtrés pour repartir de la base complète.
        """
        print("Réinitialisation des filtres. Retour à la base complète.")
        self.filtered_candidates = None

    def list_all_candidates(self):
        """
        Liste tous les candidats disponibles.
        :return: Liste des dictionnaires contenant les informations des candidats.
        """
        print("Liste de tous les candidats disponibles.")
        if not isinstance(self.data, list):
            print("Les données JSON ne contiennent pas de liste de candidats.")
            return []

        print(f"Nombre total de candidats : {len(self.data)}")
        return self.data

    # Helpers pour récupérer les parties d'un candidat
    @staticmethod
    def get_candidate_full_name(candidate):
        return nettoyer_chaine(candidate.get("candidate_full_name", ""))

    @staticmethod
    def get_candidate_first_name(candidate):
        return CandidateDataUtils.get_candidate_full_name(candidate).split()[0]

    @staticmethod
    def get_company_name(candidate):
        return nettoyer_chaine(candidate.get("company_name", ""))

    @staticmethod
    def get_job_title(candidate):
        return nettoyer_chaine(candidate.get("job_title", ""))

    @staticmethod
    def get_passions_hobbies(candidate):
        return nettoyer_chaine(candidate.get("passions_hobbies", []))

    @staticmethod
    def get_why_is_a_good_fit(candidate):
        return nettoyer_chaine(candidate.get("why_is_a_good_fit", []))

    @staticmethod
    def get_academic_background_certifications(candidate):
        return nettoyer_chaine(candidate.get("academic_background_certifications", []))

    @staticmethod
    def get_technical_professional_skills(candidate):
        return nettoyer_chaine(candidate.get("technical_professional_skills", []))

    @staticmethod
    def get_interpersonal_soft_skills(candidate):
        return nettoyer_chaine(candidate.get("interpersonal_soft_skills", []))

    @staticmethod
    def get_professional_experiences(candidate):
        return nettoyer_chaine(candidate.get("professional_experiences", []))


# Exemple d'utilisation
if __name__ == "__main__":
    # Remplacez 'candidates.json' par le chemin réel de votre fichier JSON
    print("Initialisation de l'exemple d'utilisation...")
    utils = CandidateDataUtils("../CrewAI_equipe_creation_BD_candidats/output/candidats_generes_a1ec09c6-22ab-4b9f-9b84-5fc727d5d095.json")

    # Récupérer un candidat par index
    print("Test : Récupération du candidat à l'index 0")
    candidate = utils.get_candidate_by_index(0)
    if candidate:
        print("Candidat 0 :", candidate)

        # Utilisation des helpers
        print("Nom complet :", CandidateDataUtils.get_candidate_full_name(candidate))
        print("Nom de l'entreprise :", CandidateDataUtils.get_company_name(candidate))
        print("Titre du poste :", CandidateDataUtils.get_job_title(candidate))
        print("Passions et hobbies :", CandidateDataUtils.get_passions_hobbies(candidate))
        print("Pourquoi un bon choix :", CandidateDataUtils.get_why_is_a_good_fit(candidate))
        print("Formation et certifications :", CandidateDataUtils.get_academic_background_certifications(candidate))
        print("Compétences techniques et professionnelles :", CandidateDataUtils.get_technical_professional_skills(candidate))
        print("Compétences interpersonnelles :", CandidateDataUtils.get_interpersonal_soft_skills(candidate))
        print("Expériences professionnelles :", CandidateDataUtils.get_professional_experiences(candidate))

    # Lister tous les candidats
    print("Test : Liste de tous les candidats")
    all_candidates = utils.list_all_candidates()
    print("Tous les candidats :", all_candidates)

    # Filtrer les candidats par un critère
    print("Test : Filtrage des candidats avec 'lecture' dans les passions et hobbies")
    filtered_candidates = utils.get_candidates_by_filter(passions_hobbies="lecture")
    print("Candidats filtrés :", filtered_candidates)

    # Réinitialiser les filtres
    print("Réinitialisation des filtres.")
    utils.reset_filters()