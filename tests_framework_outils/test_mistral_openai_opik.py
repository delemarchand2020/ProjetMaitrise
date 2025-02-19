import opik
import json
import os
from opik.integrations.openai import track_openai
from openai import OpenAI

opik.configure()
client_opik = opik.Opik()


def load_api_keys(file_path):
    """Charge les clés API à partir d'un fichier JSON."""
    with open(file_path, 'r') as file:
        return json.load(file)


def set_environment(api_keys):
    """Configure les variables d'environnement nécessaires."""
    for key, value in api_keys.items():
        os.environ[key] = value


# Charger les clés API
api_keys = load_api_keys("api_keys.json")
set_environment(api_keys)

# Instanciation du client OpenAI pointant vers l'API de Mistral
client = OpenAI(
    base_url="https://api.mistral.ai/v1",  # Remplacez par l'URL appropriée si nécessaire
    api_key=os.environ["MISTRAL_API_KEY"],               # La clé d'API, si requise (sinon, c'est ignoré)
)

openai_client = track_openai(client)

# Appel d'une complétion via l'API
completion = openai_client.chat.completions.create(
    model="mistral-large-latest", messages=[{"role": "user", "content": "quel est la capitale de la france ?"}],
)

print(completion.choices[0].message.content)
