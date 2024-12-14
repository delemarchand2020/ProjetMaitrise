import opik
from opik.integrations.openai import track_openai
from openai import OpenAI

opik.configure()
client_opik = opik.Opik()
client = OpenAI()
openai_client = track_openai(client)

model_llm_prompt_gen = "gpt-4o"
temperature = 0.9
top_p = 0.9
frequency_penalty = 0.2
presence_penalty = 0.2

# création du méta prompt


def get_meta_prompt(biais="stéréotype sur le genre féminin", langue_de_travail="français"):
    with open("meta_prompt_gen_profil_recruteur.txt", "r") as f:
        prompt_text = f.read()
    prompt = client_opik.create_prompt(name="meta_prompt_gen_profil_recruteur", prompt=prompt_text)
    return prompt.format(biais=biais, langue_de_travail=langue_de_travail)

# génération du prompt pour l'agent IA de génération de profil recruteurs


def generate_prompt_from_meta(meta_prompt):
    completion = openai_client.chat.completions.create(
        model=model_llm_prompt_gen, messages=[{"role": "user", "content": meta_prompt}],
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )
    return completion.choices[0].message.content

# création du prompt final pour l'agent ia de génération de profil


def register_prompt_gen_profil_recruteur(prompt_text):
    with open("prompt_gen_profil_recruteur.txt", "w") as f:
        f.write(prompt_text)
    prompt = client_opik.create_prompt(name="prompt_gen_profil_recruteur", prompt=prompt_text)
    return prompt.prompt

# génération du prompt final et enregistrement dans la librairie


final_prompt_text = generate_prompt_from_meta(get_meta_prompt())
final_prompt_text = register_prompt_gen_profil_recruteur(final_prompt_text)
