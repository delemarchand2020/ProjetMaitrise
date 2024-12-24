import json


def nettoyer_chaine(chaine, caracteres_a_enlever="{}"):
        """
        Cette fonction prend une chaîne, une liste de chaînes ou une liste de dictionnaires et une liste de caractères à enlever,
        et retourne la chaîne ou la liste nettoyée.

        :param chaine: La chaîne, la liste de chaînes ou la liste de dictionnaires à nettoyer.
        :param caracteres_a_enlever: Une chaîne contenant les caractères à enlever.
        :return: La chaîne ou la liste nettoyée.
        """

        def nettoyer_element(element, caracteres_a_enlever):
            if isinstance(element, str):
                for caractere in caracteres_a_enlever:
                    element = element.replace(caractere, '')
                return element
            elif isinstance(element, dict):
                element_str = json.dumps(element)
                for caractere in caracteres_a_enlever:
                    element_str = element_str.replace(caractere, '')
                return element_str
            else:
                return element

        if isinstance(chaine, str):
            return nettoyer_element(chaine, caracteres_a_enlever)
        elif isinstance(chaine, list):
            return [nettoyer_element(item, caracteres_a_enlever) for item in chaine]
        else:
            raise TypeError(
                "Le paramètre 'chaine' doit être une chaîne, une liste de chaînes ou une liste de dictionnaires.")


