import os
import openai

# Assure-toi que ta clé est bien définie ici ou dans ton environnement
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_top_k_initial_tokens(prompt, k=3):
    """Étape 1 – Obtenir les top-k tokens initiaux avec leurs logprobs."""
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1,
        temperature=0,
        logprobs=True,
        top_logprobs=k
    )

    # Récupère le 1er token généré (objet ChatCompletionTokenLogprob)
    token_logprob = response.choices[0].logprobs.content[0]

    # Liste de (token, logprob) pour les top-k candidats
    top_k_tokens = [(t.token, t.logprob) for t in token_logprob.top_logprobs]
    return top_k_tokens


def generate_continuation(prompt, initial_token, max_tokens=100):
    """Étape 2–4 – Générer la suite d’un prompt + token, et calculer le score logprob total."""
    new_prompt = f"{prompt} {initial_token}"
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": new_prompt}],
        max_tokens=max_tokens,
        temperature=0.7,
        logprobs=True,
        top_logprobs=1
    )

    content = response.choices[0].message.content.strip()
    token_logprobs = [t for t in response.choices[0].logprobs.content]
    total_score = sum(t.logprob for t in token_logprobs)
    average_score = total_score / len(token_logprobs) if token_logprobs else float('-inf')
    return content, average_score, new_prompt


def decoding_cot_pipeline(prompt, k=3, max_tokens=100):

    top_k = get_top_k_initial_tokens(prompt, k=k)
    completions = []

    for i, (token, _) in enumerate(top_k):
        content, score, full_prompt = generate_continuation(prompt, token, max_tokens)
        completions.append((content, score, full_prompt))
        print(f"\n--- Option {i + 1} ---")
        print(f"Score logprobs : {score:.2f}")

    best = max(completions, key=lambda x: x[1])

    return best[0]


# Exemple
if __name__ == "__main__":
    decoding_cot_pipeline("Combien de R dans le mot Strawberry ?", k=3)

