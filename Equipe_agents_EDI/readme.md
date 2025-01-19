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
  * Les points mentionnés dans le rapport sont souvent pertinents et bien écrits.
  * L'essentiel des entrevues est bien capté. Cela résume bien les échanges et les potentiels "biais". 
  * Cela semble être un vrai rapport professionnel !
* Points de vigilance :
  * Cependant il repère parfois des biais qui n'en sont pas au sens des stéréotypes visés : il faut lui apprendre à détecter les biais de type stéréotype (exemples, indices, ...) ! 
  * Assez difficile de comprendre comment fonctionne le mode hierarchique
  * Le mode hierarchique est très gourmand en ressources LLM (planification et orchestration) :  jusqu'à 50 LLM mis en jeu contre 18 en mode séquentiel.
  * Ne pas oublier de nettoyer la mémoire CrewAI lors des changements d'équipes (cela semble mélanger les agents et leurs tâches) :
  ```bash 
     crewai reset-memories -a 
  ```
  Voire supprimer tous les fichiers ici : C:\Users\USER_NAME\AppData\Local\CrewAI\Equipe_agents_EDI
  ```bash 
  Remove-Item -Path "C:\Users\delem\AppData\Local\CrewAI\Equipe_agents_EDI" -Recurse -Force
  ```
  * Le choix des LLM (créatif ou pas) pour les agents est important : 
    * On peut noter que selon les prompts, l'analyste loupe des petits détails de conversation (pourtant important pour la détection d'un biais).
    * Voir la session 33336c9d-0f8a-43c2-8942-fdc79163cbb9 avec o1-mini, auditeur EDI dit que c'est le candidat 2 qui pourrait être favori (biais global de 10%) puis retournement lorsque c'est le rédacteur de l'audit qui conclue (biais global de 62.5% et candidat 1 favorisé). Pourquoi le rédacteur refait une analyse !
  * Beaucoup de variabilité dans la production du rapport (manque de respect des consignes)
    * Lancer plusieurs fois sur les mêmes intrants pour mesurer la dispersion.
      * Vérifier la note finale du score de biais : structure pydantic à mettre en place !
      * Faire ces tests avec et sans nettoyage de la mémoire CrewAI !
  * Parfois une entrevue n'est pas analysée !
    * Attention aux verrous qu'un éditeur de fichiers pourrait mettre sur un des fichiers d'entrevue
  * La structure des tâches ne semble pas adaptée non plus au mode séquentiel !
      * Une structure tâche par tâche me semble plus prometteur (analyser une conversation à la fois puis produire le rapport, ou bien analyser les 2 conversations puis produire le rapport, mais ne pas enchainer les 2 car cela se répercute dans la mémoire de l'équipe et cela peut tout mélanger)
      * Ou bien c'est un pb de respect_context_window=True (il résume ou coupe certaines informations dans l'historique)
## License
This project is licensed under the [Apache 2.0 License](../LICENSE) - see the LICENSE file for details.
