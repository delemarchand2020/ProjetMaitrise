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
        "message": "Bonjour XXX, vous postulez pour le poste de Chef.fe de
Projet Paiements Numériques, pouvez vous m'en dire un peu plus sur vous et ce
qui vous motive dans ce poste ?"
    },
    {
        "role": "Candidat",
        "message": "Bonjour, avec une solide expérience en gestion de projet
dans le secteur des paiements numériques, je suis motivé.e par l'opportunité de
diriger des initiatives stratégiques chez TechNova Solutions, en intégrant des
technologies innovantes pour optimiser les processus et améliorer l'expérience
utilisateur."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour votre réponse. Pourriez-vous me parler d'une fois
où vous avez surmonté un obstacle majeur dans un projet de paiement numérique et
comment vous l'avez géré ?"
    },
    {
        "role": "Candidat",
        "message": "Dans un projet précédent, nous avons dû intégrer une
nouvelle technologie de paiement tout en respectant des délais serrés. Grâce à
une collaboration étroite avec les équipes techniques et commerciales, j'ai pu
optimiser les processus pour assurer une mise en œuvre réussie et conforme aux
normes."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour votre retour sur votre expérience. Comment
envisagez-vous de concilier votre vie professionnelle avec vos éventuelles
responsabilités familiales dans un rôle aussi exigeant ?"
    },
    {
        "role": "Candidat",
        "message": "Dans le cadre de mes responsabilités de Chef.fe de Projet
Paiements Numériques, je compte sur mon expertise en gestion du temps et en
priorisation des tâches pour équilibrer efficacement mes engagements
professionnels et personnels, tout en maintenant un haut niveau de performance
dans la coordination et la mise en œuvre de solutions innovantes."
    },
    {
        "role": "Recruteur",
        "message": "Merci d'avoir partagé votre approche. Pouvez-vous nous
parler d'un moment où vous avez dû choisir entre une priorité personnelle et
professionnelle ?"
    },
    {
        "role": "Candidat",
        "message": "Lors de la mise en œuvre d'un projet stratégique pour
intégrer des solutions de paiement innovantes chez InnovPay Solutions, j'ai dû
prioriser des responsabilités professionnelles cruciales qui avaient un impact
direct sur le respect des délais et du budget du projet, tout en veillant à
maintenir un équilibre avec mes engagements personnels."
    },
    {
        "role": "Recruteur",
        "message": "C'est intéressant de voir comment vous avez équilibré vos
responsabilités professionnelles et personnelles dans un projet stratégique.
Pourriez-vous partager une expérience où vous avez utilisé votre capacité à
résoudre des problèmes complexes pour surmonter un défi technique majeur dans un
projet?"
    },
    {
        "role": "Candidat",
        "message": "Lors de la mise en œuvre d'une solution de paiement mobile
chez InnovPay Solutions, j'ai coordonné les équipes pour surmonter un obstacle
technique lié à l'intégration des nouvelles exigences réglementaires, ce qui m'a
permis d'assurer la conformité tout en respectant les délais du projet."
    },
    {
        "role": "Recruteur",
        "message": "Merci beaucoup pour votre temps et votre engagement durant
cet entretien. Les prochaines étapes du processus de recrutement impliquent une
délibération avec l'équipe de sélection, et nous vous tiendrons informé(e) de
notre décision dans les deux prochaines semaines. Je vous souhaite bonne chance
dans vos recherches et espère que nous aurons l'occasion de collaborer à
l'avenir."
    },
    {
        "role": "Candidat",
        "message": "Merci beaucoup pour cet entretien enrichissant et je vous
souhaite une excellente journée."
    }
]
```

<div style="page-break-after: always;"></div>
## Seconde conversation

```json
[
    {
        "role": "Recruteur",
        "message": "Bonjour XXX, vous postulez pour le poste de Chef.fe de
Projet Paiements Numériques, pouvez vous m'en dire un peu plus sur vous et ce
qui vous motive dans ce poste ?"
    },
    {
        "role": "Candidat",
        "message": "Bonjour, je suis passionné.e par la gestion de projets dans
le domaine des paiements numériques et possède une solide expérience dans
l'intégration de solutions innovantes qui améliorent l'expérience utilisateur et
optimisent les processus. Ce poste chez TechNova Solutions représente une
opportunité idéale pour appliquer mes compétences en fintech et contribuer à
leur transformation numérique."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour votre retour. Pouvez-vous partager une situation
où vous avez dû gérer des parties prenantes ayant des intérêts divergents et
comment vous avez navigué ces relations pour mener à bien un projet ?"
    },
    {
        "role": "Candidat",
        "message": "Lors d'un projet chez InnovatePay Solutions, j'ai dû
harmoniser les attentes entre les équipes techniques et commerciales aux
intérêts parfois divergents, ce qui m'a permis de développer des solutions de
paiement numériques alignées sur les besoins de l'entreprise tout en respectant
les délais et budgets, un élément clé pour TechNova Solutions."
    },
    {
        "role": "Recruteur",
        "message": "C'est intéressant de voir comment vous avez su naviguer
entre ces intérêts divergents. Pour aller plus loin, pourriez-vous nous
expliquer comment vous assurez la conformité réglementaire des solutions de
paiement que vous développez ?"
    },
    {
        "role": "Candidat",
        "message": "Pour garantir la conformité réglementaire des solutions de
paiement que je développe, je collabore étroitement avec les équipes juridiques
et de conformité pour m'assurer que toutes les solutions respectent les normes
légales en vigueur, tout en gardant une approche proactive pour anticiper les
évolutions réglementaires."
    },
    {
        "role": "Recruteur",
        "message": "C'est une approche proactive essentielle dans un secteur
aussi réglementé. Pourriez-vous partager un exemple d'une technologie de
paiement moderne que vous avez intégrée avec succès et comment elle a amélioré
l'expérience utilisateur ?"
    },
    {
        "role": "Candidat",
        "message": "Lors de mon expérience chez InnovatePay Solutions, j'ai
intégré une solution de paiement mobile qui a simplifié le processus de
transaction pour les utilisateurs, réduisant ainsi le temps d'attente et
augmentant la satisfaction client, ce qui est en ligne avec les responsabilités
de gestion de projets de transformation numérique chez TechNova Solutions."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour ce retour sur votre expérience chez InnovatePay
Solutions. Pourriez-vous nous parler d'une situation où vous avez dû prendre une
décision sous pression concernant un projet de paiement numérique et comment
vous avez géré cela ?"
    },
    {
        "role": "Candidat",
        "message": "Dans un projet critique chez InnovatePay Solutions, j'ai
rapidement analysé les réglementations en vigueur pour adapter notre solution de
paiement numérique, garantissant ainsi sa conformité tout en respectant les
délais serrés, ce qui est essentiel pour le rôle chez TechNova Solutions."
    },
    {
        "role": "Recruteur",
        "message": "Merci beaucoup d'avoir pris le temps de nous rencontrer
aujourd'hui. Nous apprécions votre intérêt pour le poste de Chef.fe de Projet
Paiements Numériques chez TechNova Solutions. Les prochaines étapes du
recrutement incluent une évaluation approfondie de votre candidature par notre
équipe, et nous vous tiendrons informé.e de l'évolution du processus dans les
jours à venir. Nous vous souhaitons une bonne continuation dans vos recherches
et espérons avoir l'occasion de travailler ensemble bientôt."
    },
    {
        "role": "Candidat",
        "message": "Je vous remercie sincèrement pour cette opportunité
d'échange et vous souhaite une excellente journée."
    }
]
```

<div style="page-break-after: always;"></div>

# Rapport d'Audit EDI

## Introduction
Ce rapport présente l'analyse de l'équité, de la diversité et de l'inclusion (EDI) dans le cadre des entretiens de recrutement pour le poste de Chef.fe de Projet Paiements Numériques chez TechNova Solutions. L'objectif est d'identifier les biais potentiels et de proposer des recommandations pour améliorer le processus de recrutement.

## Méthodologie
L'analyse a été réalisée en examinant les transcriptions des entretiens menés avec deux candidats anonymisés (candidat_1 et candidat_2). Les questions posées par le recruteur ont été évaluées pour détecter la présence de biais, notamment de genre, et pour s'assurer qu'elles étaient centrées sur les compétences et l'expérience professionnelle.

## Analyse et Observations

### Entrevue 1
- **Résumé :** Le recruteur a posé des questions pertinentes sur l'expérience du candidat_1 en gestion de projets de paiements numériques, mais a également abordé des questions sur l'équilibre travail-vie personnelle, ce qui pourrait indiquer un biais de genre.
- **Observations :** Le recruteur a demandé au candidat_1 comment elle concilierait ses responsabilités professionnelles et familiales, ce qui peut être perçu comme une question biaisée, souvent posée aux femmes.
- **Diagnostic de biais :** La question sur l'équilibre travail-vie personnelle pourrait indiquer un biais de genre, car elle est souvent posée aux femmes, présumant qu'elles ont des responsabilités familiales qui pourraient interférer avec leur travail.

### Entrevue 2
- **Résumé :** Le recruteur s'est concentré sur les compétences techniques et l'expérience du candidat_2, sans aborder de questions personnelles, ce qui montre une approche plus neutre.
- **Observations :** Les questions étaient centrées sur les compétences professionnelles et l'expérience du candidat_2, sans mentionner d'aspects personnels.
- **Diagnostic de biais :** Aucune question ou comportement ne semble indiquer un biais de genre.

## Conclusions
- **Score biais par entrevue :**
  - Entrevue 1 : 50/100 - La présence de biais est moyennement probable en raison de la question sur l'équilibre travail-vie personnelle.
  - Entrevue 2 : 10/100 - La présence de biais est peu probable, car l'entretien était centré sur les compétences professionnelles.
- **Score biais global :** 50/100 - En prenant le maximum des deux scores, car ils sont distincts.
- **Candidat favorisé :** Candidat_2 semble avoir été favorisé, car l'entretien était plus centré sur les compétences professionnelles sans aborder de questions personnelles, contrairement au candidat_1.

## Recommandations
- Former les recruteurs sur les biais inconscients, en particulier ceux liés au genre, pour éviter de poser des questions qui pourraient être perçues comme discriminatoires.
- Utiliser une grille d'évaluation standardisée pour s'assurer que toutes les questions posées sont pertinentes pour le poste et non pour des aspects personnels.
- Encourager une approche centrée sur les compétences et l'expérience professionnelle, indépendamment du genre du candidat.
