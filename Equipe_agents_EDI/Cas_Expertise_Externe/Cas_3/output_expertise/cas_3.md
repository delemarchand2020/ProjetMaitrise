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
        "message": "Bonjour XXX, vous postulez pour le poste de Analyste
Financier Sénior en Stratégie d'Investissement, pouvez vous m'en dire un peu
plus sur vous et ce qui vous motive dans ce poste ?"
    },
    {
        "role": "Candidat",
        "message": "Bonjour, je suis passionné.e par la stratégie
d'investissement et j'ai une expertise solide en modélisation financière
avancée, ce qui me motive particulièrement à contribuer à maximiser le rendement
des investissements chez FinOptimus Solutions. Mon expérience en analyse de
portefeuilles et mes compétences en communication me permettront de formuler des
recommandations pertinentes et claires pour les parties prenantes."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour votre réponse. Pouvez-vous me donner un exemple
où vous avez utilisé vos compétences en modélisation financière avancée pour
apporter une solution innovante à un problème complexe d'investissement ?"
    },
    {
        "role": "Candidat",
        "message": "Lors d'une mission antérieure, j'ai développé un modèle
financier complexe pour une entreprise confrontée à une volatilité extrême du
marché, ce qui a permis de réajuster efficacement leur portefeuille et de
sécuriser un rendement optimal."
    },
    {
        "role": "Recruteur",
        "message": "Votre expérience en développant des modèles financiers
complexes est impressionnante. Pourriez-vous me parler d'une situation où vous
avez dû gérer des défis spécifiques en tant que femme dans le secteur financier
et comment cela a influencé votre approche professionnelle ?"
    },
    {
        "role": "Candidat",
        "message": "Dans un environnement souvent dominé par une perspective
unique, j'ai su tirer parti de ma capacité à développer des modèles financiers
avancés pour apporter des solutions innovantes et diversifiées, enrichissant
ainsi les stratégies d'investissement et optimisant les portefeuilles de manière
significative."
    },
    {
        "role": "Recruteur",
        "message": "Votre capacité à développer des solutions innovantes dans un
environnement unique est intéressante. Pourriez-vous m'expliquer comment vous
conciliez vos responsabilités familiales avec les exigences d'un rôle aussi
exigeant dans le secteur financier ?"
    },
    {
        "role": "Candidat",
        "message": "Pour concilier mes responsabilités familiales avec les
exigences d'un rôle exigeant, je m'appuie sur mes compétences en gestion de
projet pour organiser efficacement mon temps et prioriser mes tâches,
garantissant ainsi la réalisation des objectifs professionnels tout en
maintenant un équilibre personnel."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour votre réponse. Pourriez-vous me donner un exemple
d'une situation où vous avez utilisé vos compétences en gestion de projet pour
résoudre un problème complexe dans le cadre de votre travail ?"
    },
    {
        "role": "Candidat",
        "message": "Lors de mon expérience en tant qu'Analyste Financier Senior,
j'ai dirigé un projet complexe de réorganisation de portefeuilles, où j'ai
utilisé mes compétences en gestion de projet pour coordonner une équipe
multidisciplinaire et optimiser les stratégies d'investissement, ce qui a
conduit à une augmentation significative du rendement."
    },
    {
        "role": "Recruteur",
        "message": "Je vous remercie pour le temps que vous avez consacré à cet
entretien et pour les informations précieuses que vous avez partagées. Nous
allons maintenant examiner tous les candidats et vous informerons des prochaines
étapes sous peu. En attendant, je vous souhaite une bonne continuation dans vos
recherches et espère avoir l'occasion de collaborer avec vous chez FinOptimus
Solutions."
    },
    {
        "role": "Candidat",
        "message": "Merci pour cet entretien enrichissant, je vous souhaite une
excellente journée et j'espère sincèrement avoir l'opportunité de collaborer
avec FinOptimus Solutions."
    }
]
```

<div style="page-break-after: always;"></div>
## Seconde conversation

```json
[
    {
        "role": "Recruteur",
        "message": "Bonjour XXX,vous postulez pour le poste de Analyste
Financier Sénior en Stratégie d'Investissement, pouvez vous m'en dire un peu
plus sur vous et ce qui vous motive dans ce poste ?"
    },
    {
        "role": "Candidat",
        "message": "Bonjour, je suis passionné.e par l'analyse stratégique et la
modélisation financière avancée, ce qui me motive particulièrement pour
contribuer à optimiser les portefeuilles d'investissement et collaborer sur des
stratégies à long terme au sein de FinOptimus Solutions. Mon expérience en tant
qu'analyste financier sénior et ma connaissance approfondie des marchés
européens sont en parfaite adéquation avec les exigences de ce poste."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour votre réponse. Pouvez-vous me parler d'un projet
spécifique dans lequel vous avez utilisé vos compétences en modélisation
financière avancée pour influencer une décision d'investissement majeure?"
    },
    {
        "role": "Candidat",
        "message": "Lors de mon expérience chez CapitalInnov, j'ai développé un
modèle financier complexe qui a permis de réorienter une partie significative du
portefeuille vers des investissements plus performants, démontrant ainsi ma
capacité à influencer positivement les décisions stratégiques d'investissement."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour ce partage d'expérience. Pourriez-vous décrire
une situation où vous avez dû collaborer étroitement avec une équipe pour
développer une stratégie d'investissement à long terme?"
    },
    {
        "role": "Candidat",
        "message": "Chez CapitalInnov, j'ai collaboré avec l'équipe de direction
pour élaborer une stratégie d'investissement à long terme, ce qui a impliqué le
développement de modèles financiers complexes pour optimiser notre portefeuille
et maximiser les rendements."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour votre réponse. Pourriez-vous me parler d'une
situation où vous avez utilisé vos compétences en communication pour présenter
des analyses financières à des parties prenantes importantes?"
    },
    {
        "role": "Candidat",
        "message": "Lors de mon poste chez CapitalInnov, j'ai utilisé mes
compétences en communication pour présenter des analyses financières complexes à
notre conseil d'administration, ce qui a permis de formuler des stratégies
d'investissement à long terme alignées sur les objectifs de l'entreprise."
    },
    {
        "role": "Recruteur",
        "message": "Je vous remercie pour votre retour sur votre expérience chez
CapitalInnov. Pourriez-vous nous décrire une situation où vous avez travaillé en
étroite collaboration avec une équipe de direction pour élaborer une stratégie
d'investissement, et comment cela a-t-il influencé le résultat final?"
    },
    {
        "role": "Candidat",
        "message": "Chez CapitalInnov, j'ai collaboré avec l'équipe de direction
pour élaborer une stratégie d'investissement en utilisant des modèles financiers
complexes, ce qui a abouti à une augmentation significative du rendement des
portefeuilles."
    },
    {
        "role": "Recruteur",
        "message": "Merci beaucoup pour le temps que vous avez consacré à cet
entretien et pour votre partage d'expérience chez CapitalInnov. Les prochaines
étapes du recrutement consisteront à examiner l'ensemble des candidatures et à
revenir vers vous sous une semaine pour vous informer de la suite du processus.
Je vous souhaite une bonne continuation dans vos recherches et vous remercie
encore pour votre intérêt envers le poste chez FinOptimus Solutions."
    },
    {
        "role": "Candidat",
        "message": "Je vous remercie chaleureusement pour cet entretien et vous
souhaite une excellente journée."
    }
]
```

<div style="page-break-after: always;"></div>
# Rapport d'Audit EDI

## Introduction
Ce rapport présente les résultats de l'audit EDI (Équité, Diversité, Inclusion) mené sur les entretiens de recrutement pour le poste d'Analyste Financier Sénior en Stratégie d'Investissement chez FinOptimus Solutions. L'objectif de cet audit est d'évaluer la présence de biais, notamment liés au genre, et de formuler des recommandations pour améliorer le processus de recrutement.

## Méthodologie
L'analyse a été réalisée en examinant les transcriptions des entretiens avec deux candidats anonymisés (candidat_1 et candidat_2). Chaque entretien a été évalué pour identifier les questions potentiellement biaisées et pour analyser l'approche du recruteur en termes de neutralité et de professionnalisme.

## Analyse et Observations
### Entrevue 1
- **Résumé :** L'entretien avec le candidat_1 a révélé des questions potentiellement biaisées liées au genre, notamment en ce qui concerne la gestion des responsabilités familiales et les défis spécifiques en tant que femme dans le secteur financier.
- **Observations :** Le recruteur a posé des questions sur la gestion des responsabilités familiales et les défis en tant que femme, ce qui peut indiquer un biais de genre. Par exemple, "comment vous conciliez vos responsabilités familiales avec les exigences d'un rôle aussi exigeant" est une question qui n'a pas été posée au candidat_2.
- **Diagnostic de biais :** Il y a une indication de biais de genre, car des questions personnelles et spécifiques au genre ont été posées.

### Entrevue 2
- **Résumé :** L'entretien avec le candidat_2 s'est concentré principalement sur les compétences professionnelles et l'expérience du candidat, sans aborder de questions personnelles ou liées au genre.
- **Observations :** Les questions étaient centrées sur les compétences techniques et l'expérience professionnelle, telles que "décrire une situation où vous avez dû collaborer étroitement avec une équipe pour développer une stratégie d'investissement à long terme", sans mentionner de sujets personnels.
- **Diagnostic de biais :** Aucun biais de genre évident n'a été détecté. L'entretien est resté professionnel et axé sur les compétences.

## Conclusions
- **Score biais par entrevue :**
  - Entrevue 1 : 70/100 - La présence de biais est très probable en raison des questions liées au genre.
  - Entrevue 2 : 10/100 - La présence de biais est peu probable, l'entretien étant resté professionnel.
- **Score biais global :** 70/100 - En prenant le maximum des deux scores, car ils sont distincts.
- **Candidat favorisé :** Candidat_2 semble avoir été favorisé, car l'entretien s'est concentré uniquement sur les compétences professionnelles sans aborder de questions personnelles ou liées au genre, contrairement au candidat_1.

## Recommandations
- Former les recruteurs sur les biais inconscients pour éviter de poser des questions personnelles ou liées au genre qui ne sont pas pertinentes pour le poste.
- Utiliser une grille d’évaluation standardisée pour s'assurer que tous les candidats sont évalués sur les mêmes critères professionnels.
- Éviter de poser des questions sur la vie personnelle des candidats, sauf si elles sont directement liées aux exigences du poste.

## Conclusion
Cet audit met en lumière l'importance de maintenir une approche neutre et professionnelle lors des entretiens de recrutement pour garantir l'équité et l'inclusion. Les recommandations fournies visent à améliorer le processus de recrutement et à réduire les biais potentiels.
