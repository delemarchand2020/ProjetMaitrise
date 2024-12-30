import opik
import json
import base64
import os
import argparse

from opik.integrations.openai import track_openai
from openai import OpenAI

# Configuration Opik et OpenAI
opik.configure()
client_opik = opik.Opik()
client = OpenAI()
openai_client = track_openai(client)

# Paramètres LLM
model_llm = "gpt-4o"
temperature_llm = 0.8
top_p_llm = 0.9
frequency_penalty_llm = 0.2
presence_penalty_llm = 0.2

def encode_file(file_path):
    try:
        with open(file_path, "rb") as file:
            return base64.b64encode(file.read()).decode('utf-8')
    except FileNotFoundError:
        raise ValueError(f"File not found: {file_path}")
    except Exception as e:
        raise RuntimeError(f"An error occurred while encoding the file: {e}")

def escape_json_content(file_path):
    with open(file_path, "r") as file:
        json_content = json.load(file)
    return json.dumps(json_content, indent=2, ensure_ascii=False)

def get_prompt(file_name):
    if not os.path.exists(file_name):
        raise ValueError(f"Prompt file does not exist: {file_name}")
    with open(file_name, "r") as f:
        prompt_text = f.read()
    try:
        prompt = client_opik.create_prompt(name=file_name, prompt=prompt_text)
        return prompt.format()
    except Exception as e:
        raise RuntimeError(f"An error occurred while creating the prompt: {e}")

def generate_eval_1_conv(prompt, file_conv_1):
    file_content = escape_json_content(file_conv_1)
    messages = [
        {"role": "user", "content": [{"type": "text", "text": f"{prompt}"}]},
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": (
                        "Voici la conversation au format JSON. Analyse la et répond au prompt:\n\n"
                        "```json\n"
                        f"{file_content}\n"
                        "```"
                    ),
                }
            ],
        },
    ]
    try:
        completion = openai_client.chat.completions.create(
            model=model_llm,
            messages=messages,
            temperature=temperature_llm,
            top_p=top_p_llm,
            frequency_penalty=frequency_penalty_llm,
            presence_penalty=presence_penalty_llm,
        )
        return completion.choices[0].message.content
    except Exception as e:
        raise RuntimeError(f"An error occurred while generating the evaluation: {e}")

def generate_eval_2_conv(prompt, file_conv_1, file_conv_2):
    file_content_1 = escape_json_content(file_conv_1)
    file_content_2 = escape_json_content(file_conv_2)
    messages = [
        {"role": "user", "content": [{"type": "text", "text": f"{prompt}"}]},
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": (
                        "Voici les deux conversations au format JSON. Analyse-les et répond au prompt:\n\n"
                        "Conversation 1:\n"
                        "```json\n"
                        f"{file_content_1}\n"
                        "```\n"
                        "Conversation 2:\n"
                        "```json\n"
                        f"{file_content_2}\n"
                        "```"
                    ),
                }
            ],
        },
    ]
    try:
        completion = openai_client.chat.completions.create(
            model=model_llm,
            messages=messages,
            temperature=temperature_llm,
            top_p=top_p_llm,
            frequency_penalty=frequency_penalty_llm,
            presence_penalty=presence_penalty_llm,
        )
        return completion.choices[0].message.content
    except Exception as e:
        raise RuntimeError(f"An error occurred while generating the evaluation: {e}")

def main():
    # Configuration de l'interface de ligne de commande
    parser = argparse.ArgumentParser(description="Génération d'un rapport Markdown à partir d'un ou deux fichiers JSON.")
    parser.add_argument(
        "--file1", required=True, help="Chemin du premier fichier JSON à traiter."
    )
    parser.add_argument(
        "--file2", required=False, help="Chemin du second fichier JSON à traiter, optionnel."
    )
    parser.add_argument(
        "--output-dir", required=True, help="Répertoire où le rapport Markdown sera enregistré."
    )

    args = parser.parse_args()

    # Vérification des chemins
    input_file1 = args.file1
    input_file2 = args.file2
    output_dir = args.output_dir

    if not os.path.exists(input_file1):
        raise ValueError(f"Le fichier spécifié n'existe pas : {input_file1}")

    if not os.path.isfile(input_file1):
        raise ValueError(f"Le chemin spécifié n'est pas un fichier : {input_file1}")

    if input_file2:
        if not os.path.exists(input_file2):
            raise ValueError(f"Le fichier spécifié n'existe pas : {input_file2}")

        if not os.path.isfile(input_file2):
            raise ValueError(f"Le chemin spécifié n'est pas un fichier : {input_file2}")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Nom du fichier de sortie
    if input_file2:
        report_name = "evaluation_report_2_files.md"
    else:
        report_name = os.path.splitext(os.path.basename(input_file1))[0] + "_report.md"
    output_file = os.path.join(output_dir, report_name)

    # Récupération du prompt
    prompt = get_prompt("prompt_evaluation_EDI_comparative_2_entrevues.txt" if input_file2 else "prompt_evaluation_EDI_1_entrevue.txt")

    # Génération du rapport
    try:
        if input_file2:
            report_content = generate_eval_2_conv(prompt, input_file1, input_file2)
        else:
            report_content = generate_eval_1_conv(prompt, input_file1)
    except Exception as e:
        raise RuntimeError(f"Erreur lors de la génération du rapport : {e}")

    # Écriture du rapport au format Markdown
    try:
        with open(output_file, "w") as f:
            f.write(report_content)
        print(f"Rapport généré avec succès : {output_file}")
    except Exception as e:
        raise RuntimeError(f"Erreur lors de l'écriture du rapport : {e}")

if __name__ == "__main__":
    main()
