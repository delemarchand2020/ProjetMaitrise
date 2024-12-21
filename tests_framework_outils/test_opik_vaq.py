import openai
import base64
import opik
from opik.integrations.openai import track_openai
from openai import OpenAI

opik.configure()
client_opik = opik.Opik()
client = OpenAI()
openai_client = track_openai(client)

# Fonction pour encoder l'image en base64


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


# Chemin vers votre image locale
image_path = "test.jpg"
base64_image = encode_image(image_path)

# Définissez le modèle et le message utilisateur
model = "gpt-4o"
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "Décrire ce que contient cette image ? et répondre à la question : "
                                     "est-ce que l'on y trouve un animal?"},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
        ]
    }
]


# Effectuez la requête à l'API
response = openai_client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    max_tokens=300
)

# Affichez la réponse
print(response.choices[0].message.content)
