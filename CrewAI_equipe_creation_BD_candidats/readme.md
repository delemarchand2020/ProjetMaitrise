# Équipe d'agents IA de création de la base de données des candidats
Créer une base de données de candidats "fictifs" pour répondre à des offres d'emplois "fictives".

L'équipe se compose des agents suivants :

- Agent préparateur : cet agent choisit un poste dans la base fournie (fichier JSON) 
et demande au rédacteur de produire une description complète du poste. 


- Agent de description du poste : cet agent produit un descriptif
de poste selon les informations qui lui sont transmises par le préparateur. 
Il doit extraire les informations du poste, les mettre en forme selon une spécification qui lui
sera fournie et transmettre cette information à son collègue de création du profil de candidat idéal. 


- Agent de création du profil de candidat idéal : cet agent génère un
profil de candidats idéal basé sur la description du poste à pourvoir.
Il collabore avec l'agent de création de personna pour compléter le profil.
Un profil contient les informations suivantes :
  * Formations académiques et certifications.
  * Compétences techniques/métiers.
  * Compétences humaines et relationnelles.
  * Personna (qui sera complété par l’agent de rédaction de personna).
  * Expériences professionnelles.
  

- Agent de rédaction de personna : cet agent génère la description
  du personna pour le candidat afin de compléter son profil.

## Préalables
Il vous faut un compte sur https://platform.openai.com/ pour utiliser les LLM nécessaires via API.

Il vous faut également un compte sur https://app.agentops.ai/ 
pour suivre les sessions de conversation de l'équipe CrewAI. C'est optionnel mais néanmoins très utile
pour le débogage.

Créer un environnement virtuel :
```bash
python -m venv .venv_crewai  
```
Activer l'environnement : 
```bash
.\.venv_crewai\Scripts\activate
```
Installer les dépendances avec la commande suivante :
```bash
pip install -r requirements.txt
 ``` 
Créer les variables suivantes qui contiennent vos clés pour les API OpenAI et AgentOps :
```bash
${env:OPENAI_API_KEY} = "VOTRE CLE OPEN AI"
${env:OPENAI_ORG_ID} = "VOTRE ID ORG OPEN AI"
${env:AGENTOPS_API_KEY} = "VOTRE CLE AGENTOPS"
```
## Génération des profils de candidats
```bash
cd .\CrewAI_equipe_creation_BD_candidats\ 
python .\crewai_gen_candidats.py 
 ``` 
## Apprentissages
* points positifs :
  * L'utilisation de agentops est vraiment bénéfique pour déboguer et effectuer les réglages sur les tâches.
  * L'utilisation du framework CrewAI est simple, facile et efficace pour le développeur.
    * La documentation est riche et bien faite.
* Points négatifs :
  * Coûts GPT-4o bien inférieur à GPT-4 (0.04$ contre 0.5$ pour un profil candidat, donc un rapport de 10 minimum)
    * GPT-4o a été conçu pour être deux fois plus rapide que GPT-4 Turbo, ce qui réduit les ressources nécessaires par requête.
    * Les améliorations apportées à GPT-4o permettent de diminuer les dépenses opérationnelles, permettant ainsi à OpenAI de proposer des tarifs plus compétitifs.
    * En réduisant les coûts, OpenAI vise à rendre GPT-4o accessible à un plus large public, y compris aux utilisateurs gratuits, tout en maintenant des limites d'utilisation raisonnables. 
  * GPT-4o bien plus rapide !
  * Le réglage des instructions à mettre dans les tâches est un processus itératif : beaucoup de variabilité dans la qualité des résultats dépend de cela.
  * L'utilisation de l'outil FileWriterTool par les agents n'est pas simple : il faut guider l'agent à bien l'utiliser (essais/erreurs).
    * Il n'est pas capable d'ajouter des lignes à un fichier existant.
  * Non mesuré, mais des biais semblent ressortir : 
    * Beaucoup plus de candidats masculins que féminins générés.
    * Beaucoup plus de jeunes que de vieux (non prise en compte de la consigne sénior lorsque demandée dans le poste)
  * Difficulté à respecter les consignes : exemple mettre les dates sur les diplômes et les expériences.
    * Soit mettre un agent qui contrôle cela, soit raffiner les instructions des tâches (ou mettre ceci dans les attentes de l'agent).
  * Faible variabilité dans la génération inventive de prénom, nom, écoles, loisirs (on dirait un biais aussi), ...

## License
This project is licensed under the [Apache 2.0 License](../LICENSE) - see the LICENSE file for details.
