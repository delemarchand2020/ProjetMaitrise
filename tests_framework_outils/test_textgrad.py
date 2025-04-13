# Importation des bibliothèques nécessaires
import textgrad as tg

# Spécification du modèle de langage à utiliser pour évaluer la réponse du modèle cible + prompt
tg.set_backward_engine("gpt-4o", override=True)

# Initialisation du prompt
initial_prompt = tg.Variable(
    "Vous êtes un assistant qui répond aux questions sur la géographie. Fournissez des réponses détaillées.",
    requires_grad=True,
    role_description="system prompt pour le modèle de langage cible"
)

# Spécification du modèle de langage cible dont on veut optimiser le prompt
model = tg.BlackboxLLM("gpt-4o", system_prompt=initial_prompt)

query = tg.Variable(
    "Quelle est la capitale de la France ?",
    requires_grad=False,
    role_description="question to the LLM"
)
response = model(query)

print("Prompt initial :", initial_prompt.value)
print("Réponse initiale :", response.value)

# Fonction de perte pour évaluer la réponse
def loss_function(prediction, ground_truth_answer):
    eval_instruction = tg.Variable(
        "Analyse l'écart entre la prediction et  ground_truth_answer",
        requires_grad=False,
        role_description="eval system prompt"
    )
    eval_fn = tg.loss.MultiFieldEvaluation(eval_instruction,["prediction", "ground_truth_answer"])
    eval_output_variable = eval_fn(inputs=[prediction, ground_truth_answer])
    return eval_output_variable


# Initialisation de l'optimiseur et du paramètre à optimiser
optimizer = tg.TextualGradientDescent(parameters=[initial_prompt])

# Boucle d'optimisation : identique à ce que lon ferait avec PyTorch
max_iterations = 10
response = None
for iteration in range(max_iterations):
    # Réinitialiser les gradients
    optimizer.zero_grad()

    # Générer une réponse avec le modèle de langage
    query = tg.Variable(
        "Quelle est la capitale de la France ?",
        requires_grad=False,
        role_description="question to the LLM"
    )
    response = model(query)

    # Vérité terrain pour la question posée
    ground_truth = tg.Variable(
        """Réponse courte : Paris.
        Réponse détaillée : La Constitution de la Ve République ne définit pas la capitale de la France. 
        Cependant, le statut hors-norme de Paris, son importance tant sur le plan politique que culturel 
        et sa valeur de symbole la désignent de manière incontestable comme capitale depuis le XIIe siècle.""",
        requires_grad=False,
        role_description="ground truth"
    )

    # Calculer la perte
    loss = loss_function(response, ground_truth)

    # Rétropropagation pour calculer les gradients
    loss.backward()

    # Mettre à jour le prompt
    optimizer.step()

# Afficher le prompt optimisé et la réponse découlant
print("---------------------------------------------------------")
print("Prompt optimisé :", initial_prompt.value)
print("Réponse avec prompt optimisé :", response.value)
