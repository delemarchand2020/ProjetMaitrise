# Agent IA de génération de postes
Cet agent génère automatiquement des descriptifs de postes selon la liste des métiers qu'on lui fournit.
Il doit générer des descriptions de postes, 
les mettre en forme selon une spécification qui lui sera fournie et écrire le résultat dans un fichier JSON des descriptions de poste à pourvoir.

## Préalables
Installer les dépendances avec la commande suivante :
```bash
pip install -r requirements.txt
 ``` 
Avoir un compte ChatGPT+ et accéder à la console de création des assistants GPT : https://chatgpt.com/gpts/mine
## Implémentation
Cet agent est créé avec la plateforme ChatGPT+ (my GPT) et utilise une API externe qui retourne la liste des métiers envisagés.

### Instructions pour l'agent 
#### (à placer dans la console de création ChatGPT+)
Tu es un assistant qui génère des descriptifs de postes réalistes.

Étape préliminaire : demande à l'utilisateur combien de postes il faut générer par métier et combien de métier il veut traiter.

Étape 1 : tu dois choisir un métier parmi la liste retournée par tes outils disponibles. Ne demande pas à l'utilisateur de choisir. Choisis par toi-même.

Étape 2 : générer un nom de compagnie, une description du poste, le rôle et les responsabilités du poste, les compétences requises pour occuper ce poste.

Étape 3 : formatter ces informations au format JSON selon le format suivant sans afficher ce contenu à l'utilisateur :
 ```json   
 {
        "company_name": "",
        "job_title": "",
        "job_description": "",
        "responsibilities": [],
        "skills_required": [],
        "location": "",
        "experience_level": "",
        "education_required": ""
    }
 ```

Étape 4 : recommence à l'étape 1 tant que la quantité demandée n'est pas complétée.

Étape finale : prend tous ces JSON, regroupe les dans un JSON liste des postes et met le dans un fichier .json que l'utilisateur pourra télécharger.

### Action pour récupérer la liste des métiers 
#### (à placer dans la console de création ChatGPT+)

```json 
{
  "openapi": "3.1.0",
  "info": {
    "title": "FastAPI",
    "version": "0.1.0"
  },
  "servers": [
    {
      "url": "https://ec25-24-200-146-112.ngrok-free.app"
    }
  ],
  "paths": {
    "/metiers": {
      "get": {
        "summary": "Get Metiers",
        "description": "Retourne la liste des métiers",
        "operationId": "get_metiers_metiers_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "items": {
                    "$ref": "#/components/schemas/Metier"
                  },
                  "type": "array",
                  "title": "Response Get Metiers Metiers Get"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "Metier": {
        "properties": {
          "id": {
            "type": "integer",
            "title": "Id"
          },
          "description": {
            "type": "string",
            "title": "Description"
          }
        },
        "type": "object",
        "required": [
          "id",
          "description"
        ],
        "title": "Metier"
      }
    }
  }
}
```
L'Api doit être lancé avant l'utilisation de l'agent via la commande :
```bash
uvicorn liste_metiers_api:app 
 ```
Ensuite elle doit être exposée publiquement avec la commande :
```bash
./Outils/ngrok.exe http 8000
 ```  
Après exécution, cette commande va générer une url de ce type : https://ec25-24-200-146-112.ngrok-free.app que l'on peut consulter via la console :
https://dashboard.ngrok.com/endpoints

Cette URL est à placer dans la description JSON ci-dessus avant de la copier dans la console ChatGPT+.

## Version programmatique
```bash
cd .\AgentIA_generation_postes
python .\agentai_gen_postes.py --nombre_postes "2" --metier "ingénieur.e infra cloud" --file_path "./output/2_postes_inge_infra_cloud.json"
 ``` 

## License
This project is licensed under the [Apache 2.0 License](../LICENSE) - see the LICENSE file for details.
