# Documentation : Orchestration des Scripts EDI

Ce projet vise à automatiser l'exécution de plusieurs scripts pour générer un rapport EDI (Équité, Diversité, Inclusion) basé sur des données simulées. Le script principal orchestre toutes les étapes nécessaires, en respectant un ordre spécifique.

## Prérequis

1. **Environnement Python** : Assurez-vous que Python est installé (version 3.8 ou ultérieure).
2. **Clés API** : Un fichier `api_keys.json` contenant les clés API nécessaires doit être présent.

### Exemple de fichier `api_keys.json`

```json
{
    "OPENAI_API_KEY": "votre_clé_openai",
    "OPENAI_ORG_ID": "votre_org_id",
    "AGENTOPS_API_KEY": "votre_clé_agentops"
}
```

Placez ce fichier dans le même répertoire que le script principal ou spécifiez son chemin avec l'argument `--api_keys_file`.

## Structure du Projet

- `AgentIA_generation_postes` : Contient le script pour générer des postes.
- `CrewAI_equipe_creation_BD_candidats` : Contient le script pour générer des candidats.
- `AgentAI_creation_BD_recruteurs` : Contient le script pour générer des recruteurs.
- `Simulation_conversation` : Contient le script pour générer des conversations.
- `Equipe_agents_EDI` : Contient le script pour générer le rapport final.

## Utilisation

### Commande de Base

```bash
python main.py
```

### Options

- `--metier` : Spécifie le métier à utiliser pour la génération des postes. Par défaut, "ingénieur.e infra cloud".
- `--api_keys_file` : Spécifie le chemin du fichier JSON contenant les clés API. Par défaut, `api_keys.json`.

### Exemple

```bash
python main.py --metier "chef de projets IA" --api_keys_file .\\api_keys.json
```

## Fonctionnement

1. **Étape 1** : Génération des postes.
   - Appelle le script `agentai_gen_postes.py`.
2. **Étape 2** : Génération des candidates féminines.
   - Appelle le script `crewai_gen_candidats.py`.
3. **Étape 3** : Génération des recruteurs.
   - Appelle le script `agentai_gen_recruteurs.py`.
4. **Étape 4** : Génération de la première conversation.
   - Appelle le script `gen_full_crewai_conversation.py`.
5. **Étape 5** : Génération des candidats masculins.
   - Appelle à nouveau `crewai_gen_candidats.py`.
6. **Étape 6** : Génération de la deuxième conversation.
   - Appelle `gen_full_crewai_conversation.py`.
7. **Étape 7** : Génération du rapport EDI.
   - Appelle le script `gen_rapport_EDI.py`.

## Gestion des Erreurs

Si une étape échoue, le script s'arrête et affiche un message d'erreur clair. Corrigez le problème avant de relancer le script.

## Licence
This project is licensed under the [Apache 2.0 License](../LICENSE) - see the LICENSE file for details.


