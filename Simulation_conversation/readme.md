# Génération des conversations d'entrevue
Créer une base de données de conversations synthétiques d'entrevue de recrutement.
### L'équipe se compose des agents IA suivants :

#### Agent recruteur

Cet agent est chargé de poser des questions pertinentes au candidat et de réagir à ses réponses. Il a en permanence accès à l'historique de la conversation. Le profil du recruteur contient les informations suivantes (issues de la base de données des recruteurs) :

- **Son rôle, ses responsabilités, ses passions et loisirs.**  
- **Ses convictions personnelles (biais), s'il en a.**  
- **La description du poste pour atteindre son objectif : trouver un bon candidat pour ce poste.**  

#### Agent candidat

Cet agent est chargé de répondre aux questions du recruteur en mettant en avant ses compétences et son expérience. Il a en permanence accès à l'historique de la conversation. Le profil du candidat contient les informations suivantes (issues de la base de données des candidats) :

- **Son CV incluant ses formations, ses compétences et expériences passées, ses passions et loisirs.**  
- **Ses atouts : pourquoi il pense être un bon candidat pour le poste.**  
- **La description du poste pour atteindre son objectif : obtenir ce poste.**  

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
## Génération d'une conversation
```bash
cd .\Simulation_conversation\   
python .\gen_conversation.py  --fichier_db_postes "postes_generes_new_prompt_gpt4-o1.json" 
                              --fichier_db_recruteurs "recruteurs_generes.json" 
                              --fichier_db_candidats "candidats_generes_f_poste_1.json" 
                              --output_file "conversation_f_poste_1.json" 
                              --index "0"

 ``` 
## Évaluation d'une conversation
```bash
cd .\Simulation_conversation\   
python .\eval_conversation.py --file1 "./output/conversation_f_poste_1.json" --output-dir "./output"

 ``` 
## Évaluation de 2 conversations 
```bash
cd .\Simulation_conversation\   
python .\eval_conversation.py --file1 "./output/conversation_f_poste_1.json" --file2 "./output/conversation_m_poste_1.json" --output-dir "./output"

 ``` 
## Apprentissages
* points positifs :
  * L'utilisation de agentops est vraiment bénéfique pour déboguer et effectuer les réglages sur les tâches.
  * L'utilisation du framework CrewAI est simple, facile et efficace pour le développeur.
    * La documentation est riche et bien faite.
* Points négatifs :
  * Le réglage des "prompts" (goal, backstory et task) est un processus itératif : beaucoup de variabilité dans la qualité des résultats dépend de cela.
  * Ne pas oublier de nettoyer la mémoire CrewAI lors des changements de tâches et d'agents (cela semble mélanger les agents et leurs tâches) :
  ```bash 
     crewai reset-memories -a 
  ```
  Voire supprimer tous les fichiers ici : C:\Users\USER_NAME\AppData\Local\CrewAI\Equipe_agents_EDI
  ```bash 
  Remove-Item -Path "C:\Users\delem\AppData\Local\CrewAI\Simulation_conversation" -Recurse -Force
  ``` 

## License
This project is licensed under the [Apache 2.0 License](../LICENSE) - see the LICENSE file for details.
