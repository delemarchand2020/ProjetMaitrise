import json
from utils import nettoyer_chaine


class RecruiterDataUtils:
    def __init__(self, json_file):
        """
        Initialise l'utilitaire avec un fichier JSON contenant les informations des recruteurs.
        :param json_file: Chemin vers le fichier JSON.
        """
        print(f"Initialisation de RecruiterDataUtils avec le fichier : {json_file}")
        self.json_file = json_file
        self.data = self._load_json()
        self.filtered_recruiters = None  # Stocke les résultats du dernier filtrage

    def _load_json(self):
        """
        Charge le fichier JSON en mémoire.
        :return: Données JSON sous forme de liste.
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

    def get_recruiter_by_index(self, index):
        """
        Récupère les informations d'un recruteur spécifique par son index.
        :param index: Index du recruteur dans la liste des recruteurs.
        :return: Dictionnaire contenant les informations du recruteur ou None si l'index est invalide.
        """
        print(f"Récupération du recruteur à l'index : {index}")
        if not self.data:
            print("Les données JSON ne contiennent pas de recruteurs.")
            return None

        try:
            recruiter = self.data[index]
            print(f"Recruteur trouvé : {recruiter}")
            return recruiter
        except IndexError:
            print(f"Index {index} hors limites. Nombre de recruteurs disponibles : {len(self.data)}.")
            return None

    def get_recruiters_by_filter(self, **filters):
        """
        Filtre les recruteurs en fonction des critères donnés.
        Si un filtrage précédent existe, il est utilisé comme base. Sinon, la base complète est utilisée.
        :param filters: Paires clé-valeur représentant les critères de filtre.
        :return: Liste des recruteurs correspondant aux critères.
        """
        print(f"Filtrage des recruteurs avec les critères : {filters}")

        # Utilise les résultats filtrés précédents ou la base complète
        base_recruiters = self.filtered_recruiters if self.filtered_recruiters else self.data
        if not base_recruiters:
            print("Aucun recruteur disponible pour le filtrage.")
            return []

        filtered_recruiters = base_recruiters
        for key, value in filters.items():
            print(f"Application du filtre - {key}: {value}")
            filtered_recruiters = [rec for rec in filtered_recruiters if any(value.lower() in str(item).lower() for item in (rec.get(key) if isinstance(rec.get(key), list) else [rec.get(key)]))]

        print(f"Nombre de recruteurs trouvés : {len(filtered_recruiters)}")
        self.filtered_recruiters = filtered_recruiters  # Met à jour le dernier résultat filtré
        return filtered_recruiters

    def reset_filters(self):
        """
        Réinitialise les résultats filtrés pour repartir de la base complète.
        """
        print("Réinitialisation des filtres. Retour à la base complète.")
        self.filtered_recruiters = None

    def list_all_recruiters(self):
        """
        Liste tous les recruteurs disponibles.
        :return: Liste des dictionnaires contenant les informations des recruteurs.
        """
        print("Liste de tous les recruteurs disponibles.")
        if not self.data:
            print("Les données JSON ne contiennent pas de recruteurs.")
            return []

        print(f"Nombre total de recruteurs : {len(self.data)}")
        return self.data

    # Helpers pour récupérer les parties d'un recruteur
    @staticmethod
    def get_recruiter_full_name(recruiter):
        return nettoyer_chaine(recruiter.get("recruiter_full_name", ""))

    @staticmethod
    def get_role_description(recruiter):
        return nettoyer_chaine(recruiter.get("role_description", ""))

    @staticmethod
    def get_responsibilities(recruiter):
        return nettoyer_chaine(recruiter.get("responsibilities", []))

    @staticmethod
    def get_passions_hobbies(recruiter):
        return nettoyer_chaine(recruiter.get("passions_hobbies", []))

    @staticmethod
    def get_bias(recruiter):
        return nettoyer_chaine(recruiter.get("bias", ""))

    @staticmethod
    def get_bias_hints(recruiter):
        return nettoyer_chaine(recruiter.get("bias_hints", []))


# Exemple d'utilisation
if __name__ == "__main__":
    # Remplacez 'recruiters.json' par le chemin réel de votre fichier JSON
    print("Initialisation de l'exemple d'utilisation...")
    utils = RecruiterDataUtils("../AgentAI_creation_BD_recruteurs/output/recruteurs_generes.json")

    # Récupérer un recruteur par index
    print("Test : Récupération du recruteur à l'index 0")
    recruiter = utils.get_recruiter_by_index(0)
    if recruiter:
        print("Recruteur 0 :", recruiter)

        # Utilisation des helpers
        print("Nom complet :", RecruiterDataUtils.get_recruiter_full_name(recruiter))
        print("Description du rôle :", RecruiterDataUtils.get_role_description(recruiter))
        print("Responsabilités :", RecruiterDataUtils.get_responsibilities(recruiter))
        print("Passions et hobbies :", RecruiterDataUtils.get_passions_hobbies(recruiter))
        print("Biais :", RecruiterDataUtils.get_bias(recruiter))
        print("Indicateurs de biais :", RecruiterDataUtils.get_bias_hints(recruiter))

    # Filtrer les recruteurs par un critère
    print("Test : Filtrage des recruteurs avec 'technologie' dans la description du rôle")
    tech_recruiters = utils.get_recruiters_by_filter(role_description="technologie")
    print("Recruteurs trouvés :", tech_recruiters)

    # Réinitialiser les filtres
    print("Réinitialisation des filtres.")
    utils.reset_filters()

    # Lister tous les recruteurs
    print("Test : Liste de tous les recruteurs")
    all_recruiters = utils.list_all_recruiters()
    print("Tous les recruteurs :", all_recruiters)
