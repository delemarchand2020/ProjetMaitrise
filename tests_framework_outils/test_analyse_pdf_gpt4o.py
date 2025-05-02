import openai
import os
import base64
import tiktoken
from typing import List
from PyPDF2 import PdfMerger
import tempfile

# Configuration OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

MODEL = "gpt-4.1"
MAX_TOKENS = 1_000_000
SAFETY_MARGIN = 2000
encoding = tiktoken.encoding_for_model("gpt-4o")  # GPT-4.1 non encore supporté explicitement

# 🔧 Fusionne plusieurs fichiers PDF en un seul
def merge_pdfs(input_paths: List[str]) -> str:
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    merger = PdfMerger()
    for pdf in input_paths:
        merger.append(pdf)
    merger.write(temp_file.name)
    merger.close()
    return temp_file.name  # renvoie le chemin du fichier fusionné

# 🔧 Encode le PDF fusionné en base64
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

# 🔧 Estime le nombre de tokens utilisés
def estimate_total_tokens(messages: List[dict]) -> int:
    return len(encoding.encode(str(messages)))

# 🔁 Fonction principale
def ask_question_about_merged_pdfs(pdf_paths: List[str], user_question: str) -> str:
    # Étape 1 : fusion
    merged_pdf_path = merge_pdfs(pdf_paths)
    print(f"📎 Fichier fusionné créé : {merged_pdf_path}")

    # Étape 2 : construction du prompt
    prompt_intro = (
        f"Les documents suivants ont été fusionnés : {', '.join(os.path.basename(p) for p in pdf_paths)}.\n"
        "Lis le document fusionné et réponds à la question suivante :\n\n" + user_question
    )

    content = [{"type": "text", "text": prompt_intro}, encode_pdf_to_base64(merged_pdf_path)]
    messages = [{"role": "user", "content": content}]

    # Étape 3 : estimation des tokens
    total_tokens = estimate_total_tokens(messages)
    print(f"🧠 Nombre total estimé de tokens : {total_tokens}")
    if total_tokens > MAX_TOKENS - SAFETY_MARGIN:
        raise ValueError("❌ Trop de contenu pour la fenêtre de contexte de GPT-4.1")

    # Étape 4 : appel API
    response = openai.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.3
    )

    # Nettoyage temporaire
    os.remove(merged_pdf_path)

    return response.choices[0].message.content

# === Exemple d'utilisation ===
pdf_files = ["document1.pdf", "document2.pdf"]
question = "Fais une synthèse globale de tous ces documents. Combien de pages ? Quels sont les points communs et différences ?"

résultat = ask_question_about_merged_pdfs(pdf_files, question)
print("📝 Réponse :\n", résultat)
