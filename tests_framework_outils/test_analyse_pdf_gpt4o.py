import openai
import os
import base64
import tiktoken
from typing import List

openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialisation de l'encodeur pour GPT-4o
encoding = tiktoken.encoding_for_model("gpt-4o")
MAX_TOKENS = 128000000
SAFETY_MARGIN = 1000  # Marge de sécurité


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


def estimate_token_count(content: List[dict]) -> int:
    return len(encoding.encode(str(content)))


def ask_question_about_pdfs(pdf_paths: List[str], user_question: str) -> str:
    content = [{"type": "text", "text": user_question}]

    for path in pdf_paths:
        file_entry = encode_pdf_to_base64(path)
        temp_content = content + [file_entry]
        token_count = estimate_token_count(temp_content)

        if token_count > MAX_TOKENS - SAFETY_MARGIN:
            print(f"⚠️ Ajout de '{path}' annulé : trop de tokens ({token_count}).")
            break

        content.append(file_entry)
        print(f"✅ '{path}' ajouté (tokens estimés : {token_count})")

    # Envoi à GPT-4o
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": content}],
        temperature=0.3
    )

    return response.choices[0].message.content


# Exemple d'utilisation
pdf_files = ["document2.pdf", "document1.pdf"]
question = "Peux-tu me faire une synthèse de ces documents ? et combien de documents différents as-tu lu ?"

print(ask_question_about_pdfs(pdf_files, question))
