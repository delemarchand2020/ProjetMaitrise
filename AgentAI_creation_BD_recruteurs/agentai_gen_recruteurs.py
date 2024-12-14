import opik

# Read the prompt from a file
with open("meta_prompt_gen_profil_recruteur.txt", "r") as f:
    prompt_text = f.read()

opik.configure()
client = opik.Opik()

# Create a new prompt
prompt = client.create_prompt(name="meta_prompt_gen_profil_recruteur", prompt=prompt_text)

# Print the prompt text
print(prompt.prompt)

# Build the prompt
print(prompt.format(biais="stéréotype sur le genre"))
