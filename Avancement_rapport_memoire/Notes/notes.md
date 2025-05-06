# Notes
# 🧠 Concepts et Méthodologies Clés

## NLP et Vision par Ordinateur

* **ViT (Vision Transformers)** : Utiliser les questions posées par le recruteur pour générer une représentation visuelle du candidat, permettant ainsi de détecter visuellement les biais potentiels.

## Génération de Conversations

* **Qualité des datasets** : Assurer que les conversations générées sans biais sont réellement neutres, en utilisant des méthodes comme SEAT.

* **Variété des conversations** : Diversifier les postes, profils de candidats et recruteurs grâce à des techniques comme le RAG (Retrieval-Augmented Generation).

## Biais des Modèles de Langage

* **Utilisation des biais des LLMs** : Les biais présents dans les LLMs peuvent être exploités pour simuler des recruteurs biaisés de manière plus réaliste.

## Évaluation des Échanges

* **Théorie de l'aversion aux risques** : Appliquer des concepts comme le paradoxe d'Allais pour modéliser la perception des biais en termes de gains ou pertes.

* **Paradoxe de Simpson** : Prendre en compte les facteurs de confusion dans l'analyse statistique des biais.

---

# 🧪 Techniques d'Apprentissage et d'Évaluation

## Distillation et Optimisation de Prompts (OPRO)

* **Stratégie Enseignant-Élève** : Utiliser un LLM pour générer des données annotées, former un SLM (Small Language Model) sur ces données, et évaluer les performances avec un LLM juge.

* **Réduction des coûts** : Cette approche permet de limiter les besoins en fine-tuning coûteux tout en maintenant une performance acceptable.

## Modèles de Langage de Petite Taille (SLM)

* **Avantages des SLMs** : Moins gourmands en ressources, plus faciles à déployer et à adapter à des tâches spécifiques.

---

# 🧰 Outils et Protocoles

## Mémoire pour Agents IA

* **Types de mémoire** :

  * *Mémoire de travail* : Contexte immédiat de la conversation.
  * *Mémoire épisodique* : Historique des interactions passées.
  * *Mémoire sémantique* : Connaissances factuelles et conceptuelles.
  * *Mémoire procédurale* : Compétences et routines apprises.([ABC News][1], [The Court Manager][2])

* **Implémentation** : Utiliser des fichiers TXT comme base de stockage avec une approche RAG.

## Protocoles et Standards

* **MCP (Model Context Protocol)** : Standard ouvert développé par Anthropic pour connecter les assistants IA aux systèmes de données externes.([Home][3])

---

# 📚 Ressources et Références

* **OPRO** : Technique d'optimisation de prompts développée par Google DeepMind. ([TechTalks][4])

* **SLM** : Modèles de langage de petite taille, optimisés pour des tâches spécifiques.&#x20;

* **RAG** : Technique combinant récupération d'information et génération pour améliorer la précision des modèles IA. ([NVIDIA Blog][5])

* **MCP** : Protocole standardisé pour connecter les modèles IA aux sources de données externes. ([Reddit][6])

---

# 🧪 Cas d'Utilisation

* **Comparaison de Conversations** : Générer deux conversations pour un même poste, l'une avec un recruteur biaisé, l'autre non, et analyser les différences perçues.

* **Évaluation de Candidatures** : Présenter deux candidats avec des caractéristiques différentes à un recruteur non biaisé, avant et après un audit de biais, pour observer les changements de décision.

---

# 📝 Notes Supplémentaires

* **Importance de l'EDI** : Intégrer systématiquement une expertise en Équité, Diversité et Inclusion dans la conception et l'évaluation des systèmes IA.

* **Évolution vers ESG** : Bien que l'EDI reste pertinent, certaines entreprises intègrent ces objectifs dans des stratégies ESG plus larges.

* **Fine-tuning** : Envisager le fine-tuning des modèles sur des datasets nettoyés pour améliorer la détection des biais.

---

N'hésitez pas à me solliciter pour approfondir l'une de ces sections ou pour obtenir des exemples concrets.

[1]: https://abcnews.go.com/US/dei-programs/story?id=97004455&utm_source=chatgpt.com "A look at what DEI means amid Trump executive orders - ABC News"
[2]: https://thecourtmanager.org/articles/what-does-the-acronym-dei-mean-to-you/?utm_source=chatgpt.com "What Does the Acronym DEI Mean to You? - NACM – Court Manager"
[3]: https://www.anthropic.com/news/model-context-protocol?utm_source=chatgpt.com "Introducing the Model Context Protocol - Anthropic"
[4]: https://bdtechtalks.com/2023/11/20/deepmind-opro-llm-optimization/?utm_source=chatgpt.com "Optimize your ChatGPT prompts with DeepMind's OPRO technique"
[5]: https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/?utm_source=chatgpt.com "What Is Retrieval-Augmented Generation aka RAG - NVIDIA Blog"
[6]: https://www.reddit.com/r/ClaudeAI/comments/1gzv8b9/anthropics_model_context_protocol_mcp_is_way/?utm_source=chatgpt.com "Anthropic's Model Context Protocol (MCP) is way bigger than most ..."
