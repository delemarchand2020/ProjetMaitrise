import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import argparse

def lire_fichiers_csv(repertoire, filtre=None):
    fichiers_csv = [f for f in os.listdir(repertoire) if f.endswith('.csv')]
    if filtre:
        fichiers_csv = [f for f in fichiers_csv if filtre not in f]
    return fichiers_csv

def lire_csv(fichier):
    return pd.read_csv(fichier)

def generer_rapport_statistique(df):
    rapport = {}

    # Convertir les colonnes numériques en float, en ignorant les valeurs non numériques
    df['Note pertinence question'] = pd.to_numeric(df['Note pertinence question'], errors='coerce')
    df['Note pertinence réponse'] = pd.to_numeric(df['Note pertinence réponse'], errors='coerce')

    # Statistiques pour chaque échange (1 à 5)
    for echange in range(1, 6):
        df_echange = df[df['Numéro échange'] == echange]

        rapport[f'Échange {echange}'] = {
            'Note pertinence question': {
                'Moyenne': df_echange['Note pertinence question'].mean(),
                'Médiane': df_echange['Note pertinence question'].median(),
                'Écart-type': df_echange['Note pertinence question'].std(),
                'Min': df_echange['Note pertinence question'].min(),
                'Max': df_echange['Note pertinence question'].max(),
                'Nombre de valeurs': df_echange['Note pertinence question'].count()
            },
            'Note pertinence réponse': {
                'Moyenne': df_echange['Note pertinence réponse'].mean(),
                'Médiane': df_echange['Note pertinence réponse'].median(),
                'Écart-type': df_echange['Note pertinence réponse'].std(),
                'Min': df_echange['Note pertinence réponse'].min(),
                'Max': df_echange['Note pertinence réponse'].max(),
                'Nombre de valeurs': df_echange['Note pertinence réponse'].count()
            },
            'Réalisme interaction': df_echange['Réalisme interaction'].value_counts(normalize=True).mul(100).round(2).to_dict()
        }

    # Statistiques globales pour tous les échanges
    rapport['Global'] = {
        'Note pertinence question': {
            'Moyenne': df['Note pertinence question'].mean(),
            'Médiane': df['Note pertinence question'].median(),
            'Écart-type': df['Note pertinence question'].std(),
            'Min': df['Note pertinence question'].min(),
            'Max': df['Note pertinence question'].max(),
            'Nombre de valeurs': df['Note pertinence question'].count()
        },
        'Note pertinence réponse': {
            'Moyenne': df['Note pertinence réponse'].mean(),
            'Médiane': df['Note pertinence réponse'].median(),
            'Écart-type': df['Note pertinence réponse'].std(),
            'Min': df['Note pertinence réponse'].min(),
            'Max': df['Note pertinence réponse'].max(),
            'Nombre de valeurs': df['Note pertinence réponse'].count()
        },
        'Réalisme interaction': df['Réalisme interaction'].value_counts(normalize=True).mul(100).round(2).to_dict()
    }

    # Conversations les plus mal notées
    df['Moyenne pertinence'] = df[['Note pertinence question', 'Note pertinence réponse']].mean(axis=1)
    df['Réalisme moyen'] = df['Réalisme interaction'].apply(lambda x: 1 if x == 'Oui' else 0)
    conversation_moins_pertinente = df.groupby('Nom du fichier JSON')['Moyenne pertinence'].mean().idxmin()
    conversation_moins_réaliste = df.groupby('Nom du fichier JSON')['Réalisme moyen'].mean().idxmin()

    # Conversations les mieux notées
    conversation_plus_pertinente = df.groupby('Nom du fichier JSON')['Moyenne pertinence'].mean().idxmax()
    conversation_plus_réaliste = df.groupby('Nom du fichier JSON')['Réalisme moyen'].mean().idxmax()

    # Scores des conversations les plus mal et les mieux notées
    score_moins_pertinente = df[df['Nom du fichier JSON'] == conversation_moins_pertinente]['Moyenne pertinence'].mean()
    score_moins_réaliste = df[df['Nom du fichier JSON'] == conversation_moins_réaliste]['Réalisme moyen'].mean() * 100
    score_plus_pertinente = df[df['Nom du fichier JSON'] == conversation_plus_pertinente]['Moyenne pertinence'].mean()
    score_plus_réaliste = df[df['Nom du fichier JSON'] == conversation_plus_réaliste]['Réalisme moyen'].mean() * 100

    # Liste de toutes les conversations évaluées et leur nombre d'évaluations reçues
    conversations_évaluées = df.groupby('Nom du fichier JSON').size()/5
    conversations_évaluées = conversations_évaluées.to_dict()

    # Scores moyens des échanges pour chaque conversation
    scores_moyens = df.groupby('Nom du fichier JSON')[['Moyenne pertinence', 'Réalisme moyen']].mean().round(2)
    scores_moyens['Réalisme moyen'] = scores_moyens['Réalisme moyen'].round(2) * 100

    rapport['Conversations les plus mal notées'] = {
        'Moins pertinente': {
            'Nom': os.path.splitext(conversation_moins_pertinente)[0],
            'Score': score_moins_pertinente
        },
        'Moins réaliste': {
            'Nom': os.path.splitext(conversation_moins_réaliste)[0],
            'Score': score_moins_réaliste
        }
    }

    rapport['Conversations les mieux notées'] = {
        'Plus pertinente': {
            'Nom': os.path.splitext(conversation_plus_pertinente)[0],
            'Score': score_plus_pertinente
        },
        'Plus réaliste': {
            'Nom': os.path.splitext(conversation_plus_réaliste)[0],
            'Score': score_plus_réaliste
        }
    }

    rapport['Liste des conversations évaluées'] = {
        'Nombre d\'évaluations': conversations_évaluées,
        'Scores moyens': scores_moyens.to_dict(orient='index')
    }

    return rapport

def generer_visualisations(df, repertoire_sortie):
    # Créer des graphiques pour les notes de pertinence des questions et réponses côte à côte
    plt.figure(figsize=(14, 7))

    # Fondre les données pour avoir une colonne 'Type' indiquant si c'est une question ou une réponse
    df_melted = pd.melt(df, id_vars=['Numéro échange'], value_vars=['Note pertinence question', 'Note pertinence réponse'],
                         var_name='Type', value_name='Note')

    sns.boxplot(x='Numéro échange', y='Note', hue='Type', data=df_melted)
    plt.title('Notes de pertinence des questions et réponses par échange')
    plt.legend(title='Type')
    plt.tight_layout()
    plt.savefig(os.path.join(repertoire_sortie, 'notes_pertinence.png'))
    plt.close()

    # Créer un graphique en camembert pour le réalisme des interactions
    plt.figure(figsize=(10, 7))
    réalisme_counts = df['Réalisme interaction'].value_counts(normalize=True).mul(100).round(2)
    réalisme_counts.plot.pie(autopct='%1.1f%%', startangle=140)
    plt.title('Réalisme des interactions')
    plt.ylabel('')  # Supprimer l'étiquette de l'axe y
    plt.savefig(os.path.join(repertoire_sortie, 'realisme_interaction.png'))
    plt.close()

def ecrire_rapport_markdown(rapport, repertoire_sortie, nb_conversations, nb_échanges):
    fichier_sortie = os.path.join(repertoire_sortie, 'rapport_statistique.md')
    with open(fichier_sortie, 'w', encoding='utf-8') as f:
        f.write("# Rapport Statistique\n\n")
        f.write(f"## Nombre total de conversations : {nb_conversations}\n")
        f.write(f"## Nombre total d'échanges : {nb_échanges}\n\n")

        # Inclure les graphiques
        f.write("## Graphiques\n\n")
        f.write("### Notes de pertinence des questions et réponses par échange\n\n")
        f.write(f"![Notes de pertinence](notes_pertinence.png)\n\n")
        f.write("### Réalisme des interactions\n\n")
        f.write(f"![Réalisme des interactions](realisme_interaction.png)\n\n")

        # Inclure les statistiques
        for échange, stats in rapport.items():
            if échange == 'Conversations les plus mal notées' or échange == 'Conversations les mieux notées':
                f.write(f"## {échange}\n")
                for stat, valeur in stats.items():
                    f.write(f"- **{stat}** : {valeur['Nom']} (Score: {valeur['Score']})\n")
            elif échange == 'Liste des conversations évaluées':
                f.write(f"## {échange}\n")
                f.write("### Nombre d'évaluations\n")
                for nom, nb_évaluations in stats['Nombre d\'évaluations'].items():
                    f.write(f"- **{os.path.splitext(nom)[0]}** : {nb_évaluations} évaluations\n")
                f.write("### Scores moyens\n")
                for nom, scores in stats['Scores moyens'].items():
                    f.write(f"- **{os.path.splitext(nom)[0]}** : Moyenne pertinence: {scores['Moyenne pertinence']}, Réalisme moyen: {scores['Réalisme moyen']}%\n")
            else:
                f.write(f"## Statistiques pour {échange}\n")
                for colonne, valeurs in stats.items():
                    f.write(f"### {colonne}\n")
                    if isinstance(valeurs, dict):
                        for stat, valeur in valeurs.items():
                            if colonne == 'Réalisme interaction':
                                f.write(f"- **{stat}**: {valeur}%\n")
                            else:
                                f.write(f"- **{stat}**: {valeur}\n")
                    else:
                        f.write(f"- {valeurs}\n")
                f.write("\n")

def main():
    parser = argparse.ArgumentParser(description='Générer un rapport statistique à partir de fichiers CSV.')
    parser.add_argument('--filter', type=str, help='Filtre pour exclure certains fichiers en fonction de leur nom.')
    args = parser.parse_args()

    repertoire = './evaluations/'
    fichiers_csv = lire_fichiers_csv(repertoire, args.filter)

    df_global = pd.DataFrame()

    for fichier in fichiers_csv:
        chemin_fichier = os.path.join(repertoire, fichier)
        df = lire_csv(chemin_fichier)
        df_global = pd.concat([df_global, df], ignore_index=True)

    rapport_global = generer_rapport_statistique(df_global)

    # Nombre total de conversations et d'échanges
    nb_conversations = len(fichiers_csv)
    nb_échanges = nb_conversations * df_global['Numéro échange'].nunique()

    # Créer le répertoire de sortie s'il n'existe pas
    repertoire_sortie = './output/'
    os.makedirs(repertoire_sortie, exist_ok=True)

    # Générer les visualisations
    generer_visualisations(df_global, repertoire_sortie)

    # Écrire le rapport dans un fichier Markdown
    ecrire_rapport_markdown(rapport_global, repertoire_sortie, nb_conversations, nb_échanges)

    print(f"Rapport généré dans {repertoire_sortie}/rapport_statistique.md")
    print(f"Visualisations générées dans {repertoire_sortie}")

if __name__ == "__main__":
    main()
