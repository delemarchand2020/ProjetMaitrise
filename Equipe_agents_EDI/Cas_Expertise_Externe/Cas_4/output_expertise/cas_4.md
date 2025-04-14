# Demande d'évaluation de cas pour l'étude des biais de genre


**Votre mission :**

1. **Lecture des entrevues :** pour chaque cas sélectionné, lisez dans l'ordre les deux transcriptions d'entrevues.
2. **Observations :** notez sur un papier vos observations concernant la présence ou l'absence de manifestations de biais de type stéréotype pour chaque conversation anonymisée.
3. **Score de biais :** attribuez un score de présence de biais pour chaque conversation en utilisant le même barème que celui utilisé par notre agent IA EDI.
4. **Lecture du rapport EDI :** lisez le rapport EDI fourni, à lire après avoir fait vos propres observations et attribution de scores.
5. **Comparaison et évaluation :** comparez vos résultats avec ceux du rapport EDI et notez qualitativement vos observations sur le rapport.

**Points importants :**

- Vous n'avez pas à évaluer le réalisme ou la pertinence des conversations.
- Vous n'avez pas accès aux profils des protagonistes ni à la description du poste.
- Nous vous demandons uniquement de nous indiquer si, face à ces transcriptions d'entrevues (réelles ou non), vous feriez les mêmes observations que notre agent EDI.

**Barème :**

| **Score de biais** | **Interprétation**                                                 |
|---------------------|---------------------------------------------------------------------|
| 100 sur 100        | La présence de biais est confirmée sans aucun doute.               |
| 0 sur 100          | La présence de biais est inexistante sans aucun doute.            |
| 5 à 10 sur 100     | La présence de biais est très peu probable.                         |
| 10 à 30 sur 100    | La présence de biais est peu probable.                             |
| 30 à 50 sur 100    | La présence de biais est probable.                                |
| 50 à 70 sur 100    | La présence de biais est moyennement probable.                     |
| 70 à 90 sur 100    | La présence de biais est très probable.                            |
| 90 à 100 sur 100   | La présence de biais est très fortement probable.                  |

Je vous remercie par avance pour votre collaboration et votre expertise. Vos retours me seront précieux pour améliorer l'approche en IA dans ce domaine.

<div style="page-break-after: always;"></div>
## Première conversation

```json
[
    {
        "role": "Recruteur",
        "message": "Bonjour XXX, vous postulez pour le poste de Spécialiste en
Recrutement d'Ouvriers Techniques, pouvez vous m'en dire un peu plus sur vous et
ce qui vous motive dans ce poste ?"
    },
    {
        "role": "Candidat",
        "message": "Bonjour, je suis passionné.e par le recrutement dans le
secteur technique et je possède une solide expérience en développement de
réseaux de candidats qualifiés, ce qui me motive particulièrement à contribuer
au succès de TechnoCraft Recruitment Solutions."
    },
    {
        "role": "Recruteur",
        "message": "C'est formidable que vous soyez motivé à contribuer au
succès de TechnoCraft Recruitment Solutions. Pourriez-vous me parler d'une
situation où vous avez dû utiliser des tests techniques pour évaluer les
compétences d'un candidat ?"
    },
    {
        "role": "Candidat",
        "message": "Lors de ma précédente expérience chez Talent Bridge
Solutions, j'ai organisé des campagnes de recrutement où j'ai systématiquement
intégré des tests techniques pour évaluer les compétences des candidats,
garantissant ainsi l'identification de talents en adéquation avec les besoins de
nos clients."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour votre réponse. Avez-vous déjà rencontré des défis
spécifiques liés à l'intégration dans une équipe technique principalement
masculine, et comment les avez-vous surmontés ?"
    },
    {
        "role": "Candidat",
        "message": "Ayant travaillé dans des environnements similaires, j'ai
développé des compétences interpersonnelles fortes qui m'ont permis de
collaborer efficacement avec divers profils et de m'adapter aux dynamiques
d'équipe, ce qui est essentiel pour mener à bien les responsabilités liées au
développement d'un réseau de candidats qualifiés chez TechnoCraft Recruitment
Solutions."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour votre réponse. Comment envisagez-vous votre
progression de carrière dans un secteur dominé par les hommes, et quelles
stratégies comptez-vous adopter pour atteindre vos objectifs professionnels ?"
    },
    {
        "role": "Candidat",
        "message": "Pour progresser dans un secteur dominé par les hommes, je
compte tirer parti de mon expertise dans la rédaction d'annonces ciblées et
l'évaluation des compétences pour développer un réseau solide de candidats
qualifiés, tout en collaborant étroitement avec les gestionnaires pour répondre
aux besoins spécifiques en recrutement."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour votre réponse. Pouvez-vous me décrire une
situation où vous avez réussi à établir une relation de confiance avec un
candidat difficile, et comment cela a influencé le processus de recrutement ?"
    },
    {
        "role": "Candidat",
        "message": "Dans une de mes expériences précédentes, j'ai réussi à
établir une relation de confiance avec un candidat difficile en utilisant
l'écoute active et une approche personnalisée, ce qui a facilité son intégration
dans le processus de recrutement et a permis d'aligner ses compétences sur les
attentes spécifiques des gestionnaires de recrutement."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour votre temps et d'avoir partagé vos expériences
avec nous. Les prochaines étapes incluent une évaluation approfondie de tous les
candidats, et nous vous tiendrons informé de la suite du processus sous peu. En
attendant, je vous souhaite une bonne continuation dans vos recherches
professionnelles."
    },
    {
        "role": "Candidat",
        "message": "Merci beaucoup pour cette entrevue et je vous souhaite une
excellente journée."
    }
]
```

<div style="page-break-after: always;"></div>
## Seconde conversation

```json
[
    {
        "role": "Recruteur",
        "message": "Bonjour XXX, vous postulez pour le poste de Spécialiste en
Recrutement d'Ouvriers Techniques, pouvez vous m'en dire un peu plus sur vous et
ce qui vous motive dans ce poste ?"
    },
    {
        "role": "Candidat",
        "message": "Bonjour, j'ai une expérience significative en recrutement
technique, ce qui me permet de développer efficacement des réseaux de candidats
qualifiés. Ma maîtrise des outils de sourcing en ligne et des logiciels ATS me
motive particulièrement pour ce rôle où je pourrais collaborer étroitement avec
les gestionnaires pour répondre aux besoins spécifiques d'embauche."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour votre réponse. Pourriez-vous partager une
expérience où vous avez utilisé vos compétences en communication
interpersonnelle pour surmonter un défi dans le recrutement?"
    },
    {
        "role": "Candidat",
        "message": "Lors d'un projet de recrutement complexe pour un client dans
l'industrie manufacturière, j'ai utilisé mes compétences en communication
interpersonnelle pour comprendre en profondeur leurs besoins spécifiques et
créer une stratégie de recrutement sur mesure, ce qui a permis de placer
plusieurs candidats qualifiés avec succès."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour votre réponse. Comment gérez-vous le stress lié à
la gestion simultanée de plusieurs recrutements tout en respectant les délais?"
    },
    {
        "role": "Candidat",
        "message": "Grâce à mon aptitude à gérer plusieurs projets de
recrutement simultanément, j'ai développé des stratégies efficaces pour
prioriser les tâches et maintenir un haut niveau de qualité, ce qui est
essentiel pour respecter les délais tout en répondant aux besoins spécifiques
des clients."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour cette précision. Pourriez-vous décrire une
situation où vous avez dû adapter vos stratégies de recrutement en réponse à un
changement soudain des besoins d'un client?"
    },
    {
        "role": "Candidat",
        "message": "Lors d'une mission avec un client de l'industrie
manufacturière, un changement soudain dans leurs besoins m'a poussé à adapter
rapidement ma stratégie en augmentant notre vivier de talents techniques via de
nouvelles plateformes de sourcing, ce qui a permis de répondre efficacement à
leurs attentes en temps voulu."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour cette information. Pourriez-vous nous parler de
vos compétences interpersonnelles et comment elles vous aident dans votre rôle
de recruteur, notamment lors des entretiens avec les candidats?"
    },
    {
        "role": "Candidat",
        "message": "Lors des entretiens avec les candidats, mes compétences
interpersonnelles, comme l'écoute active et la communication claire, me
permettent de comprendre en profondeur leurs attentes et d'évaluer efficacement
leur adéquation avec les besoins techniques spécifiques de nos clients."
    },
    {
        "role": "Recruteur",
        "message": "Merci beaucoup pour votre temps et pour avoir partagé vos
expériences avec nous aujourd'hui. Les prochaines étapes consistent à évaluer
toutes les candidatures, et nous reviendrons vers vous sous une semaine avec une
mise à jour. En attendant, je vous souhaite bonne chance dans vos recherches et
espère que nos chemins se croiseront à nouveau bientôt."
    },
    {
        "role": "Candidat",
        "message": "Je vous remercie pour cet entretien enrichissant et vous
souhaite une excellente journée."
    }
]
```

<div style="page-break-after: always;"></div>
# Rapport d'Audit EDI

## Introduction
Ce rapport présente les résultats de l'audit EDI (Équité, Diversité, Inclusion) mené sur deux entrevues de recrutement. L'objectif est d'évaluer la présence de biais, notamment de genre, et de proposer des recommandations pour améliorer l'équité dans le processus de recrutement.

## Méthodologie
L'analyse a été réalisée en examinant les questions posées lors des entrevues et en identifiant les éléments potentiellement biaisés. Chaque entrevue a été évaluée individuellement pour détecter la présence de stéréotypes de genre.

## Analyse et Observations

### Entrevue 1
- **Questions posées :**
  - Intégration dans une équipe technique principalement masculine : "Avez-vous déjà rencontré des défis spécifiques liés à l'intégration dans une équipe technique principalement masculine, et comment les avez-vous surmontés ?"
  - Progression de carrière dans un secteur dominé par les hommes : "Comment envisagez-vous votre progression de carrière dans un secteur dominé par les hommes, et quelles stratégies comptez-vous adopter pour atteindre vos objectifs professionnels ?"
- **Diagnostic de biais :**
  - La présence de questions orientées vers le genre indique un biais potentiel. Ces questions peuvent refléter des stéréotypes de genre.

### Entrevue 2
- **Questions posées :**
  - Les questions étaient centrées sur les compétences et les expériences du candidat, sans mentionner de stéréotypes de genre.
- **Diagnostic de biais :**
  - Aucun biais de genre évident n'a été détecté. Les questions étaient neutres et axées sur les compétences professionnelles.

## Conclusions
- **Score biais par entrevue :**
  - Entrevue 1 : 60/100 (La présence de biais est moyennement probable en raison des questions orientées vers le genre)
  - Entrevue 2 : 10/100 (La présence de biais est peu probable, les questions étaient neutres)
- **Score biais global :** 60/100 (En prenant le maximum des deux scores, car ils sont distincts)
- **Candidat favorisé :** Candidat 2 semble avoir été favorisé en raison de l'absence de questions biaisées et d'une approche plus neutre et professionnelle de la part du recruteur.

## Recommandations
- Formation sur les biais inconscients pour le recruteur afin de sensibiliser aux stéréotypes de genre.
- Utilisation d'une grille d'évaluation standardisée pour garantir que toutes les questions posées sont pertinentes et équitables.
- Éviter les questions qui pourraient suggérer des stéréotypes de genre et se concentrer sur les compétences et les expériences professionnelles.

## Conclusion
Ce rapport met en lumière l'importance de maintenir une approche neutre et équitable lors des entrevues de recrutement. En suivant les recommandations proposées, l'organisation peut améliorer son processus de recrutement et promouvoir un environnement plus inclusif.
