import openai
import os
import base64
import tiktoken
from typing import List

openai.api_key = os.getenv("OPENAI_API_KEY")

MODEL = "gpt-4.1"
MAX_TOKENS = 1_000_000
SAFETY_MARGIN = 2000

encoding = tiktoken.encoding_for_model("gpt-4o")

def encode_pdf_to_base64(path: str) -> dict:
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    return {
        "type": "file",
        "file": {
            "filename": os.path.basename(path),
            "file_data": f"data:application/pdf;base64,{encoded}"
        }
    }

def estimate_total_tokens(messages: List[dict]) -> int:
    return len(encoding.encode(str(messages)))

def ask_question_about_multiple_pdfs(pdf_paths: List[str], user_question: str) -> str:
    messages = []

    for path in pdf_paths:
        # Ajoute un message user par fichier
        base = os.path.basename(path)
        messages.append({
            "role": "user",
            "content": [{"type": "text", "text": f"Voici le document : {base}"}]
        })
        messages.append({
            "role": "user",
            "content": [encode_pdf_to_base64(path)]
        })

        # Vérification de tokens
        total = estimate_total_tokens(messages)
        if total > MAX_TOKENS - SAFETY_MARGIN:
            print(f"⛔️ Trop de contenu, on s'arrête avant d'ajouter {base}")
            break

        print(f"✅ {base} ajouté (tokens estimés : {total})")

    # Ajoute la question finale
    messages.append({
        "role": "user",
        "content": [
            {"type": "text", "text": (
                "Merci d’analyser tous les documents précédents. "
                + user_question)}
        ]
    })

    print(f"🧠 Nombre total estimé de tokens : {estimate_total_tokens(messages)}")

    response = openai.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.3
    )

    return response.choices[0].message.content

# Exemple d’utilisation
pdf_files = ["document1.pdf", "document2.pdf"]
question = "Fais une synthèse globale de tous ces documents. Combien en as-tu lu ? Combien de pages ?"

résultat = ask_question_about_multiple_pdfs(pdf_files, question)
print("📝 Réponse :\n", résultat)
