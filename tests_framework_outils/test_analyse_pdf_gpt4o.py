import openai
import os
import base64

# Clé API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Chemin vers votre fichier PDF
pdf_path = "document.pdf"

# Lecture et encodage du fichier PDF en base64
with open(pdf_path, "rb") as f:
    pdf_bytes = f.read()
    base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

# Construction du message avec le fichier PDF encodé
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Veuillez lire ce PDF et en fournir un résumé en français."
            },
            {
                "type": "file",
                "file": {
                    "filename": "document.pdf",
                    "file_data": f"data:application/pdf;base64,{base64_pdf}"
                }
            }
        ]
    }
]

# Envoi de la requête à l'API GPT-4o
response = openai.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    temperature=0.7
)

# Affichage de la réponse
print(response.choices[0].message.content)
