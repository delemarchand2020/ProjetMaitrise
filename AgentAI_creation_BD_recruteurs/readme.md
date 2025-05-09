# Agent IA de génération de profils de recruteur
Cet agent génère automatiquement des profils de recruteurs selon une liste de biais
cognitifs fournie. Il doit générer ces profils de recruteurs, les mettre en forme selon une
spécification qui lui sera fournie et écrire le résultat dans un fichier JSON. Chacun de ces
profils servira à créer un agent IA devant incarner le recruteur impliqué dans le processus
de recrutement pour un poste. Le but ultime est de générer une conversation réaliste entre
un candidat et un recruteur lors d’une entrevue fictive.

## Préalables
Il vous faut un compte sur https://www.comet.com/opik
pour suivre les expérimentations d'ingénierie de prompts. 
C'est très utile pour le débogage et l'amélioration continue.

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
Créer les variables suivantes qui contiennent votre clé pour l'API OpenAI et le nom de votre projet OPIK :
```bash
${env:OPENAI_API_KEY} = "VOTRE CLE OPEN AI"
${env:OPIK_PROJECT_NAME} = "VOTRE NOM DE PROJET SUR OPIK"
```
La clé OPIK_API_KEY vous sera demandée à la première utilisation et sera stockée.

Exemple :
```bash
python .\agentai_gen_recruteurs.py
OPIK: Your Opik API key is available in your account settings, can be found at https://www.comet.com/api/my/settings/ for Opik cloud
Please enter your Opik API key:
Do you want to use "delemarchand" workspace? (Y/n)Y
OPIK: Configuration saved to file: C:\Users\delem\.opik.config
```
## Génération des profils de recruteur
```bash
python .\agentai_gen_recruteurs.py  --biais "stéréotype sur le genre féminin" 
        --langue_de_travail "français" 
        --genre "masculin" --secteur "informatique" 
        --file_path "./output/recruteurs_generes.json"
```
Pour générer un profil sans biais mettre ceci :
```bash
--biais "aucun biais"
```
## Apprentissages
* points positifs :
  * L'utilisation de Opik est vraiment bénéfique pour déboguer et effectuer des réglages sur les prompts.
    * Cela permet également une gestion des versions des prompts.
    * Et d'avoir une trace des appels LLM incluant les métadonnées (modèle utilisé et ses paramètres, nb tokens utilisés, temps de réponse, coût approximatif, ...).
    * D'autres fonctionnalités Opik sont à creuser, notamment la gestion des datasets et des expérimentations : utilisation des métriques d'évaluation "LLM as a judge" inclut dans le framework semble prometteur.
  * Utiliser un meta-prompt pour générer le prompt du générateur de profil de recruteur est efficace : les LLM sont vraiment de bons prompt engineer !
* Points négatifs :
  * Probablement refaire l'agent IA de génération de postes avec la même approche "programmatique" que celle-ci !
## License
This project is licensed under the [Apache 2.0 License](../LICENSE) - see the LICENSE file for details.
