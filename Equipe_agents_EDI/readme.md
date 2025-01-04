# Équipe d'agents IA EDI pour détecter les bais dans les recrutements
Fournir un rapport complet pour évaluer les biais chez les recruteurs

L'équipe se compose des agents suivants :

- Agent préparateur des dossiers : récupère les informations (conversations, rapports de recrutement), 
éventuellement fait un pré-traitement (anonymisation, changer les prénoms ...), monte le dossier et le transmet à l'auditeur EDI.  
- Agent auditeur EDI : réalise l'audit selon les stratégies demandées (analyse des échanges seuls, des rapports seuls, ou des échanges et des rapports)
- Agent rédacteur d'audit : rédige le rapport d'audit selon les analyses de l'auditeur dans le format spécifié. 

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
## Génération du rapport EDI
```bash
cd .\Equipe_agents_EDI\   
python .\gen_rapport_EDI.py --file1 "../Simulation_conversation/output/conversation_f_poste_1.json" --file2 "../Simulation_conversation/output/conversation_m_poste_1.json" --output_dir "./output/" --output_file "rapport_audit.md"
 ``` 
## Apprentissages
* points positifs :
  * 
* Points négatifs :
  * 
## License
This project is licensed under the [Apache 2.0 License](../LICENSE) - see the LICENSE file for details.
