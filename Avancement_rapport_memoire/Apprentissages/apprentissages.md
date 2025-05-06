# Apprentissages

## Agent IA de génération de postes

**Points positifs :**
    
- L'utilisation est simple et conviviale (identique à une conversation en langage naturel avec ChatGPT).
- Possibilité de compléter les spécifications au début de la session : en plus des consignes de base inscrites lors de la configuration, on peut spécifier par exemple un nom de fichier particulier, une quantité de postes, filtrer certains métiers, ..., le tout en langage naturel. Par exemple : 5 postes par métier et 5 métiers de préférence non scientifique ou technique.
- Possibilité de raffiner la demande après la génération du fichier : après révision de la génération, on peut demander des ajustements et des corrections. Par exemple : tu as juste copié 5 fois le même poste par métier. Je veux à chaque fois un poste différent (un nom d'entreprise différent, des compétences différentes, des expériences différentes, ...).
    
**Points de vigilance :**
    
- Limitations sur la créativité : très rapidement, la génération arrive à bout de souffle quand il s'agit d'imaginer des noms, des lieux, des expériences, ..., pour un nombre total de postes supérieur à 10 ou pour des métiers sous représentés sur le Web (on peut supposer un lien avec ce que le LLM sous jacent a ingurgité durant son apprentissage). 
- Un contrôle qualité humain est nécessaire pour valider la pertinence et le réalisme des postes générés : parfois, il faut plusieurs itérations pour arriver à générer des descriptions adéquates. 
- Compléter les spécifications au début de la session vient parfois contredire les consignes originales et donc la qualité de la sortie.
- La qualité des prompts en entrée est primordiale pour assurer une bonne qualité de génération en sortie : un récent article de Cameron Wolfe https://cameronrwolfe.substack.com/p/automatic-prompt-optimizationAutomatic Prompt Optimization indique que l'une des principales conclusions des articles scientifiques sur l'optimisation des prompts est que les LLM excellent dans l'écriture de prompts. Il précise dans son article « En supposant que nous fournissions les bonnes informations en contexte, il est possible de créer des algorithmes d'optimisation de prompts étonnamment puissants en demandant simplement, de manière itérative, à un LLM de critiquer et d'améliorer un prompt. Les LLMs plus grands (et plus performants) ont tendance à être meilleurs dans cette tâche ».

## Agent IA de génération de profils de recruteur

**Points positifs :**
    
- L'utilisation d'Opik est vraiment bénéfique pour déboguer et effectuer des réglages sur les prompts (voir la figure fig:opik_console).
- Opik permet une gestion simple et efficace des prompts (gestion des versions). 
- Opik permet de voir la trace des appels LLM incluant toutes les métadonnées (modèle utilisé et ses paramètres, quantité de tokens utilisés, temps de réponse, coût approximatif, ...).
- Utiliser un meta-prompt pour générer le prompt du générateur de profil de recruteur semble très efficace : à ce stade, il apparaît que les LLM sont vraiment de bons « prompt engineer », contrairement à ce que soutient l'article de Ruotian et al., « Are Large Language Models Good Prompt Optimizers? » ma2024largelanguagemodelsgood. En effet l'article conclut que les LLM ne sont pas des « prompt engineer » parfaits. Ils rencontrent des difficultés à identifier les véritables causes des erreurs et à générer des prompts optimaux. Cependant, des approche comme l'Optimisation Comportementale Automatique (ABO) montrent un potentiel prometteur pour améliorer l'efficacité de l'optimisation des prompts en se concentrant sur le comportement des modèles cibles (ici notre générateur de profil). Il conviendrait de poursuivre cette analyse en mesurant la performance de l'agent recruteur qui utilisera le profil généré à cette étape.
    
**Points d'amélioration :**
    
- D'autres fonctionnalités Opik sont à creuser, notamment la gestion des datasets et des expérimentations : l'utilisation des métriques d'évaluation "LLM as a judge" inclut dans le framework semble prometteur.
- Probablement qu'il faudrait refaire l'agent IA de génération de postes avec la même approche "programmatique" que celle-ci !
    

## Équipe d'agents IA de création des profils candidats

**Points positifs :**
    
- L'utilisation du framework AgentOPS est vraiment bénéfique pour déboguer et effectuer les réglages sur les tâches.
- L'utilisation du framework CrewAI est simple, facile et efficace pour le développeur.
  - En outre, la documentation est riche et très bien faite.
- Les coûts GPT-4o sont bien inférieurs à ceux de GPT-4 (0.04\` pour GPT-4o contre 0.5\` pour GPT-4, pour la génération d'un profil candidat), lors de la sortie de ce modèle, OpenAI communiquait ceci :
  - GPT-4o a été conçu pour être deux fois plus rapide que GPT-4 Turbo, ce qui réduit les ressources nécessaires par requête.
  - Les améliorations apportées à GPT-4o permettent de diminuer les dépenses opérationnelles, permettant ainsi à OpenAI de proposer des tarifs plus compétitifs.
  - En réduisant les coûts, OpenAI vise à rendre GPT-4o accessible à un plus large public, y compris aux utilisateurs gratuits, tout en maintenant des limites d'utilisation raisonnables. 
- GPT-4o est bien plus rapide que GPT-4 (40s à 50 secondes pour GPT-4o contre 120 secondes et plus pour GPT-4)
    
**Points de vigilance :**
    
- Il faut faire très attention au choix du modèle LLM et de son paramétrage utilisé par un agent. Selon les besoins, il convient de les adapter : notamment la température qui influence directement la créativité des sorties mais aussi le nombre de tokens générés et donc le coût. Pour certaines tâches simples, on peut se permettre d'utiliser un modèle moindre (GPT-3.5 par exemple). L'article « RouteLLM: Learning to Route LLMs with Preference Data » ong2024routellmlearningroutellms aborde le défi de choisir entre des LLM de grande taille, plus puissants mais coûteux, et des modèles plus petit mais plus économiques. Les auteurs proposent des techniques de routage qui, lors de l'inférence, sélectionnent dynamiquement entre un LLM plus fort et un LLM plus faible, assurant ainsi l'équilibre entre le coût et la qualité des réponses. 
- Le réglage des instructions à mettre dans les tâches est un processus itératif : beaucoup de variabilité dans la qualité des résultats dépend des instructions qui sont des prompts. Comme évoqué dans le chapitre sur les LLM, l'effet papillon (Butterfly effect) salinas2024butterflyeffectalteringprompts se manifeste depuis l'initialisation puis à chaque étape de la conversation avec un agent IA.
- L'utilisation de l'outil FileWriterTool (fourni par CrewAI) par les agents n'est pas simple : il faut guider l'agent à bien l'utiliser (quelques essais/erreurs ont été nécessaires pour le faire fonctionner correctement).
  - Néanmoins, après correction du prompt, cet outil n'est toujours pas capable d'ajouter des lignes à un fichier existant ! Il faudrait en développer un spécifique. Néanmoins ceci est assez simple à faire avec CrewAI.
- Non mesuré, mais les biais des données d'apprentissage semblent ressortir : 
  - Beaucoup plus de candidats masculins que féminins ont été générés. Le genre a donc été explicitement spécifié dans les instructions pour palier ce biais.
  - Beaucoup plus de générations d'expériences de juniors que de seniors. Malgré le niveau d'expérience requis demandé dans le poste, la consigne n'a pas été prise en compte par l'agent en charge de créer le profil. La demande de prise en compte de cette consigne a donc été ajouté dans les instructions. L'instruction a été complétée et précise désormais une correspondance entre les années d'expériences requises et le niveau demandé (junior, intermédiaire ou senior). C'est tout l'intérêt des exemples à mettre dans un prompt et constitue ce que l'on appelle l'apprentissage en contexte pour le LLM.
- Quelques difficultés à respecter systématiquement certaines consignes simples : par exemple mettre les dates d'obtention des diplômes et des expériences.
- Nous pourrions ajouter à l'équipe un agent qui contrôle le formatage mais cela viendrait ajouter un temps de traitement et un coût supplémentaires. Il serait également possible de préciser avec des exemples les instructions.
- Faible variabilité dans la génération des prénoms, noms, écoles et loisirs (cela s'apparente à un biais des données d'apprentissage).

## Équipe d'agents IA pour la génération des conversations

**Points positifs :**
- L'utilisation du framework AgentOPS est vraiment bénéfique pour déboguer et effectuer les réglages sur les tâches.
- L'utilisation du framework CrewAI est simple, facile et efficace pour le développeur.
  - En outre, la documentation est riche et très bien faite.
        
**Points de vigilance :**
- Le réglage des "prompts" (goal, backstory et task) est un processus itératif : beaucoup de variabilité dans la qualité des résultats dépend de cela.
- Il est très difficile d'évaluer si la conversation est biaisée ou pas lorsque l'on souhaite qu'elle le soit ou pas !\\

## Agents EDI, analyse des conversations d'entrevue

**Points positifs :**
    
- Les éléments mentionnés dans le rapport sont souvent pertinents et bien écrits.
- L'essentiel des entrevues semble bien capté. Cela semble bien résumer les échanges et les potentiels "biais".
- Cela ressemble à un vrai rapport professionnel d'audit !
    
**Points de vigilance :**
    
- Cependant, il repère parfois des "biais" qui n'en sont pas au sens des stéréotypes visés : il faudrait lui "apprendre" à détecter les biais de type stéréotype (c'est à dire lui fournir des exemples et des indices dans le prompt).
- Il est assez difficile de comprendre et suivre le fonctionnement du mode hiérarchique de CrewAI https://docs.crewai.com/how-to/hierarchical-processMode hiérarchique dans CrewAI. De plus, ce mode est très gourmand en ressources LLM (le framework introduit la planification et l'orchestration des tâches) : jusqu'à 50 LLM mis en jeu contre 18 en mode séquentiel https://docs.crewai.com/how-to/sequential-processMode séquentiel dans CrewAI.
- Il ne pas oublier de nettoyer la mémoire CrewAI lors des différentes exécutions d'équipes (cela semble mélanger les agents et leurs tâches) : par exemple si nous lançons 2 fois la génération du rapport EDI sur 2 jeux de conversations différentes, la mémoire court terme (permanente tout de même sur une fenêtre de temps courte) utilisée par les agents vient parfois confondre les candidats et leurs conversations pourtant distinctes. 
- Le cumul des tâches d'analyse paraît mal adapté à un mode de traitement séquentiel. Une structure où chaque tâche d'analyse est traitée indépendamment semble plus prometteuse : soit analyser une conversation à la fois puis produire un rapport, soit analyser les deux conversations simultanément avant de générer le rapport. Cependant, enchaîner les deux analyses dans le même flux de travail crée des interférences avec la mémoire de l'équipe, ce qui risque de mélanger les informations. Cela semble conduire également à des résumés ou à des suppressions partielles d'informations dans l'historique.
- On a pu noter que selon les prompts, l'analyste EDI loupe des petits détails de conversation (pourtant important pour la détection d'un biais).
- Le choix du modèle de langage (LLM) peut avoir un impact significatif. Par exemple, un test utilisant le modèle d'OpenAI o1-mini comme LLM pour l'auditeur EDI a donné les résultats suivants : l'auditeur indique initialement que le candidat 2 pourrait être favorisé, avec un biais global estimé à 10 \%. Cependant, un retournement de situation se produit lorsque le rédacteur de l'audit conclut avec un biais global de 62,5 \%, cette fois en faveur du candidat 1. Cela soulève une question importante : pourquoi le rédacteur refait-il l'analyse déjà effectuée dans le flux de travail ? Il est probable que le mode de raisonnement du modèle o1-mini vienne compléter ou être influencé par celui produit par des prompts évolués dans le framework CrewAI. Dans ce cas, il serait judicieux d'envisager d'utiliser o1-mini seul pour éviter toute interférence.

## Orchestrateur de scenario

**Points positifs :**
    
- En une seule commande, il est possible de générer un scénario complet de bout en bout.
- Cette approche a permis de déboguer toutes les autres parties en obligeant à écrire des scripts dédiés pour chacune d'elles et en enregistrant toutes les informations dans un seul projet agentops, facilitant ainsi le suivi des étapes et des appels aux LLM sous-jacents.
- La centralisation et l'orchestration ont également conduit à finaliser la documentation du code.
    
**Points de vigilance :** 
- Le processus complet permet d'évaluer le temps et le coût d'exécution : chaque génération de scénario coûte environ 0,32 \$ et prend environ 9 minutes, ce qui peut devenir onéreux pour une exploration intensive.
- Il est nécessaire d'améliorer l'orchestrateur pour permettre de lancer uniquement certaines étapes du processus (par exemple, éviter de régénérer un poste pour le même métier si l'objectif est de tester uniquement avec d'autres candidats).
- Les expérimentations ont révélé des limites dans les résultats : les rapports montrent que la génération des conversations biaisées et leur détection sont loin d'être parfaites, nécessitant un travail approfondi sur les prompts et les configurations.


