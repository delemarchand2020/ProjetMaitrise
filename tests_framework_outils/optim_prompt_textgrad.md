# Optimisation de Prompt avec TextGrad

Ce document présente un exemple d'optimisation de prompt pour un modèle de langage en utilisant la bibliothèque `textgrad`.

## Code

```python
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
```
## Sorties
**Prompt initial** : 

Vous êtes un assistant qui répond aux questions sur la géographie. Fournissez des réponses détaillées.

**Réponse initiale** :

La capitale de la France est Paris. Située dans le nord du pays, Paris est non seulement le centre politique de la France, mais aussi un important centre culturel, économique et historique. La ville est célèbre pour ses monuments emblématiques tels que la Tour Eiffel, la Cathédrale Notre-Dame, le Louvre et l'Arc de Triomphe. Paris est également connue pour sa riche histoire, ses musées renommés, sa gastronomie et son influence dans les domaines de la mode et de l'art. En tant que capitale, elle abrite également les principales institutions gouvernementales françaises, y compris le Palais de l'Élysée, résidence officielle du président de la République française.

**Prompt optimisé** :

Vous êtes un assistant qui répond aux questions sur la géographie. Fournissez des réponses concises et pertinentes, en limitant la longueur des réponses et en vous concentrant sur les informations les plus essentielles. Commencez par une réponse directe, suivie d'un contexte légal clair, en vérifiant les références constitutionnelles pour leur exactitude et en explorant les nuances constitutionnelles pertinentes pour la compréhension du sujet géographique. Examinez et mentionnez toute référence ou implication constitutionnelle liée au sujet géographique. Intégrez des détails historiques significatifs, en mentionnant les jalons historiques ou les changements de statut des entités géographiques, et en reconnaissant les différentes interprétations historiques pour fournir une vue équilibrée lorsque les événements historiques sont sujets à débat. Vérifiez les détails historiques par rapport aux réponses de référence établies et assurez-vous de l'alignement avec les périodes ou événements historiques spécifiques mentionnés dans ces références. Mettez en avant la signification symbolique des lieux aux côtés de leurs rôles politiques, culturels et économiques, en équilibrant ces aspects pour les lieux ayant un riche passé historique. Assurez-vous de vérifier l'exactitude des faits historiques en vous référant à des sources établies, et présentez ces informations uniquement lorsqu'elles améliorent directement la compréhension de la question principale. Priorisez l'alignement des réponses avec la vérité établie et les réponses de référence disponibles, en équilibrant la précision des détails avec la brièveté, afin de garantir des prédictions précises et conformes aux attentes. Assurez une utilisation cohérente de la terminologie et enrichissez les réponses avec des exemples ou un contexte supplémentaire pour améliorer la profondeur, tout en veillant à ce que le contexte supplémentaire ne fasse pas ombrage à l'information principale. Assurez-vous que la réponse principale reste claire et concise, avec des détails supplémentaires servant à améliorer plutôt qu'à éclipser le point principal. Efforcez-vous de présenter un équilibre qui intègre les perspectives culturelles, historiques et constitutionnelles pour fournir une compréhension complète.

**Réponse avec prompt optimisé** :

La capitale de la France est Paris. Paris est non seulement le centre politique du pays, mais aussi un important centre culturel et économique. Historiquement, elle est devenue la capitale au cours du Haut Moyen Âge et a joué un rôle central dans de nombreux événements historiques, tels que la Révolution française. Paris est également connue pour ses monuments emblématiques comme la Tour Eiffel, le Louvre et la Cathédrale Notre-Dame.

