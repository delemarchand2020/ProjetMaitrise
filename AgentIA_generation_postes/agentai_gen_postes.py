import opik
import json
import argparse
import os
from opik.integrations.openai import track_openai
from openai import OpenAI, NOT_GIVEN

opik.configure()
client_opik = opik.Opik()
client = OpenAI()
openai_client = track_openai(client)

# paramètres pour un llm déterministe
model_llm_prompt_gen = "gpt-4o"
temperature_llm_prompt_gen = 0.0
top_p_llm_prompt_gen = 1.0
frequency_penalty_llm_prompt_gen = 0.0
presence_penalty_llm_prompt_gen = 0.0

# paramètres pour un llm créatif
model_llm_profil_gen = "gpt-4o"
temperature_llm_profil_gen = 0.8
top_p_llm_profil_gen = 0.9
frequency_penalty_llm_profil_gen = 0.2
presence_penalty_llm_profil_gen = 0.2


# création du méta prompt
def get_meta_prompt():
    with open("meta_prompt_gen_postes.txt", "r") as f:
        prompt_text = f.read()
    prompt = client_opik.create_prompt(name="meta_prompt_gen_postes", prompt=prompt_text)
    return prompt.prompt


# génération du prompt pour l'agent IA de génération de postes
def generate_prompt_from_meta(meta_prompt):
    completion = openai_client.chat.completions.create(
        model=model_llm_prompt_gen, messages=[{"role": "user", "content": meta_prompt}],
        temperature=temperature_llm_prompt_gen,
        top_p=top_p_llm_prompt_gen,
        frequency_penalty=frequency_penalty_llm_prompt_gen,
        presence_penalty=presence_penalty_llm_prompt_gen
    )
    return completion.choices[0].message.content


# création du prompt final pour l'agent ia de génération de postes
def register_prompt_gen_postes(prompt_text, nombre_postes="2", langue_de_travail="français",
                    metier="Ingénieur.e logiciel"):
    with open("prompt_gen_postes.txt", "w") as f:
        f.write(prompt_text)
    prompt = client_opik.create_prompt(name="prompt_gen_postes", prompt=prompt_text)
    return prompt.format(nombre_postes=nombre_postes, langue_de_travail=langue_de_travail, metier=metier)


# génération des postes
def generate_postes(prompt):
    completion = openai_client.chat.completions.create(
        model=model_llm_profil_gen, messages=[{"role": "user", "content": prompt}],
        temperature=temperature_llm_profil_gen,
        top_p=top_p_llm_profil_gen,
        frequency_penalty=frequency_penalty_llm_profil_gen,
        presence_penalty=presence_penalty_llm_profil_gen,
    )
    return completion.choices[0].message.content


# Fonction pour lire le contenu actuel du fichier JSON
def read_json_file(file_path):
    if os.path.getsize(file_path) == 0:
        return []
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


# Fonction pour écrire le contenu dans le fichier JSON
def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


# Fonction pour ajouter une nouvelle entrée JSON au fichier
def add_json_entry(file_path, new_entry):
    # Lire le contenu actuel du fichier
    data = read_json_file(file_path)

    # Si le fichier est vide ou contient un dictionnaire, convertir en liste
    if isinstance(data, dict):
        data = [data]
    elif isinstance(data, list):
        pass
    else:
        raise ValueError("Le fichier JSON ne contient pas une structure valide.")

    # Ajouter la nouvelle entrée
    data.append(new_entry)

    # Écrire le contenu mis à jour dans le fichier
    write_json_file(file_path, data)


def main():
    # Définir les arguments de ligne de commande avec des valeurs par défaut
    parser = argparse.ArgumentParser(description="Générer des postes.")
    parser.add_argument("--nombre_postes", type=str, default="2", help="nombre_postes")
    parser.add_argument("--langue_de_travail", type=str, default="français", help="La langue de travail.")
    parser.add_argument("--metier", type=str, default="Ingénieur.e logiciel", help="métier")
    parser.add_argument("--file_path", type=str, default="./output/2_postes_inge_logiciel.json",
                        help="Le chemin du fichier JSON de sortie.")

    # Parser les arguments
    args = parser.parse_args()

    # génération du prompt final à partir du meta prompt
    final_prompt_text = generate_prompt_from_meta(get_meta_prompt())
    # enregistrement du prompt final dans la librairie
    final_prompt_text = register_prompt_gen_postes(final_prompt_text, nombre_postes=args.nombre_postes,
                                                                  langue_de_travail=args.langue_de_travail,
                                                                  metier=args.metier)

    # generation des postes
    gen_profil_txt = generate_postes(final_prompt_text)

    # Enlever les balises ```json et ```
    json_string = gen_profil_txt.strip("```json").strip("```")

    # Convertir la chaîne JSON en dictionnaire Python
    data = json.loads(json_string)

    # Écrire dans le fichier
    write_json_file(args.file_path, data)


if __name__ == "__main__":
    main()

#python .\agentai_gen_postes.py --nombre_postes "3" --langue_de_travail "français" --metier "ingénieur.e infra cloud" --file_path "./output/3_postes_inge_infra_cloud.json"
