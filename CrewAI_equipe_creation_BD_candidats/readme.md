# Équipe d'agents IA de création de la base de données des candidats
Créer une base de données de candidats "fictifs" pour répondre à des offres d'emplois "fictives".

L'équipe se compose des agents suivants :

- Agent chef d'équipe : cet agent choisit un poste dans la base fournie (fichier JSON) 
et demande à son équipe de produire une description complète du candidat "fictif" 
idéal pour répondre à ce poste. 
Il continuera ces demandes pour atteindre son quota de candidats à fournir.


- Agent de description du poste : cet agent produit un descriptif
de poste selon les informations qui lui sont transmises par le chef d'équipe. 
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