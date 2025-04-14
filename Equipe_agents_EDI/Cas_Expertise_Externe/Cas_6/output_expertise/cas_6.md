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
        "message": "Bonjour XXX, vous postulez pour le poste de Ingénieur.e en
Conception de Structures Mécaniques Aéronautiques, pouvez vous m'en dire un peu
plus sur vous et ce qui vous motive dans ce poste ?"
    },
    {
        "role": "Candidat",
        "message": "Bonjour, je suis passionné.e par la conception de structures
mécaniques innovantes dans l'aéronautique, et avec mon expérience en CAO et FEA
ainsi que ma solide compréhension des matériaux composites, je suis enthousiaste
à l'idée de contribuer à des projets globaux chez TechnoStructure Innovators."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour votre enthousiasme. Pourriez-vous nous parler
d'un défi particulier que vous avez rencontré lors d'une collaboration
interdisciplinaire et comment vous l'avez surmonté?"
    },
    {
        "role": "Candidat",
        "message": "Lors d'un projet aéronautique majeur, nous avons dû intégrer
des solutions structurelles innovantes tout en assurant la conformité aux normes
de sécurité. J'ai collaboré étroitement avec des équipes de diverses disciplines
pour mener à bien des analyses FEA, garantissant ainsi la stabilité et la
résistance des structures développées."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour votre réponse détaillée. Pourriez-vous expliquer
comment vous abordez l'intégration de nouveaux matériaux dans les structures
aéronautiques tout en assurant leur conformité aux normes de sécurité?"
    },
    {
        "role": "Candidat",
        "message": "Pour intégrer de nouveaux matériaux dans les structures
aéronautiques, j'effectue des analyses par éléments finis (FEA) pour évaluer
leur résistance et stabilité, en collaboration avec des équipes
multidisciplinaires, afin d'assurer la conformité aux normes de sécurité."
    },
    {
        "role": "Recruteur",
        "message": "Je vous remercie pour cette précision. Pouvez-vous partager
une expérience où vous avez dû collaborer avec des équipes d'ingénierie
multidisciplinaires pour intégrer de nouvelles solutions structurelles dans un
projet aéronautique?"
    },
    {
        "role": "Candidat",
        "message": "Lors de ma mission en tant qu'ingénieur en conception
mécanique, j'ai collaboré avec des équipes d'ingénierie multidisciplinaires pour
intégrer de nouvelles solutions structurelles dans des projets aéronautiques,
assurant ainsi la conformité aux normes de sécurité et optimisant les
performances des structures."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour ce retour sur votre expérience en intégration de
solutions structurelles. Pourriez-vous nous parler de vos compétences en analyse
par éléments finis (FEA) et de la manière dont vous les avez appliquées dans un
projet aéronautique?"
    },
    {
        "role": "Candidat",
        "message": "Lors de mon expérience chez un grand constructeur
aéronautique, j'ai appliqué mes compétences en FEA pour réaliser des analyses
critiques de résistance sur des structures composites avancées, garantissant
ainsi leur conformité aux normes aéronautiques tout en optimisant leur
performance structurelle."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour votre temps et pour avoir partagé votre
expérience avec nous. Les prochaines étapes du processus de recrutement incluent
une évaluation plus approfondie de votre candidature par notre équipe. Nous
reviendrons vers vous sous peu pour vous informer de la suite. Je vous souhaite
une bonne continuation dans vos recherches."
    },
    {
        "role": "Candidat",
        "message": "Je vous remercie pour l'opportunité de cette entrevue et
vous souhaite une excellente journée."
    }
]
```

<div style="page-break-after: always;"></div>
## Seconde conversation

```json
[
    {
        "role": "Recruteur",
        "message": "Bonjour XXX, vous postulez pour le poste de Ingénieur.e en
Conception de Structures Mécaniques Aéronautiques, pouvez vous m'en dire un peu
plus sur vous et ce qui vous motive dans ce poste ?"
    },
    {
        "role": "Candidat",
        "message": "Bonjour, je suis passionné.e par la conception de structures
mécaniques et j'ai une solide expérience en CAO et FEA dans l'industrie
aéronautique, ce qui me motive à rejoindre TechnoStructure Innovators pour
innover et optimiser la sécurité des structures aériennes."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour votre réponse. Pourriez-vous partager une
expérience où vous avez collaboré avec une équipe multidisciplinaire pour
intégrer une solution structurelle dans un projet global ?"
    },
    {
        "role": "Candidat",
        "message": "Lors de mon expérience chez AeroDesign Solutions, j'ai
collaboré étroitement avec une équipe multidisciplinaire pour développer des
solutions structurelles innovantes, ce qui m'a permis de renforcer mes
compétences en intégration dans des projets globaux."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour votre retour sur votre expérience. Pourriez-vous
expliquer comment vous avez abordé une situation où vous deviez résoudre un
problème complexe lié à la résistance structurelle ?"
    },
    {
        "role": "Candidat",
        "message": "Lors de mon passage chez AviationTech Dynamics, j'ai dirigé
une équipe pour résoudre un problème complexe de résistance structurelle en
utilisant des analyses FEA avancées, garantissant ainsi la sécurité et la
conformité aux normes aéronautiques."
    },
    {
        "role": "Recruteur",
        "message": "C'est intéressant de savoir que vous avez déjà dirigé une
équipe pour résoudre des problèmes complexes de résistance structurelle.
Pourriez-vous me parler d'un défi particulier que vous avez rencontré dans votre
carrière et comment vous l'avez surmonté ?"
    },
    {
        "role": "Candidat",
        "message": "Un défi majeur a été d'optimiser la performance des
structures aériennes tout en garantissant la sécurité ; j'ai dirigé une équipe
pour effectuer des analyses FEA approfondies, ce qui nous a permis d'intégrer
des solutions innovantes et conformes aux normes aéronautiques."
    },
    {
        "role": "Recruteur",
        "message": "Votre expérience en dirigeant une équipe pour effectuer des
analyses FEA approfondies est précieuse pour le poste. Pouvez-vous partager une
situation où vous avez dû collaborer avec différents départements pour intégrer
des solutions structurelles dans un projet global ?"
    },
    {
        "role": "Candidat",
        "message": "Lors de mon expérience chez AviationTech Dynamics, j'ai
dirigé une équipe pour mener des analyses FEA avancées et collaboré avec
différents départements pour intégrer des solutions structurelles innovantes
dans des projets aéronautiques globaux, ce qui correspond parfaitement aux
responsabilités du poste chez TechnoStructure Innovators."
    },
    {
        "role": "Recruteur",
        "message": "Merci beaucoup pour votre temps et cet échange enrichissant.
Nous allons examiner votre candidature et vous recontacterons sous peu pour vous
informer des prochaines étapes. En attendant, je vous souhaite une bonne
continuation dans vos recherches."
    },
    {
        "role": "Candidat",
        "message": "Je vous remercie pour cette entrevue et vous souhaite une
excellente journée."
    }
]
```

<div style="page-break-after: always;"></div>
# Rapport d'Audit EDI

## Introduction
Ce rapport présente l'analyse de l'équité, de la diversité et de l'inclusion (EDI) dans le cadre des entrevues menées pour le poste d'Ingénieur.e en Conception de Structures Mécaniques Aéronautiques. L'objectif est de fournir aux gestionnaires une vue d'ensemble des pratiques de recrutement et de leur conformité aux principes d'EDI.

## Méthodologie
L'analyse a été réalisée en examinant les transcriptions des entrevues avec deux candidats anonymisés (candidat_1 et candidat_2). Chaque entrevue a été évaluée pour identifier la présence de biais de genre, en se concentrant sur le langage utilisé, la structure des questions, et l'équité du processus.

## Analyse et Observations
### Entrevue 1
- **Structure et Contenu :** L'entrevue avec le candidat_1 a été bien structurée, avec des questions techniques pertinentes axées sur l'expérience et les compétences en ingénierie aérospatiale.
- **Langage et Ton :** Le recruteur a maintenu un ton professionnel et neutre, sans indices de biais de genre.
- **Cohérence :** Les questions posées étaient ouvertes, permettant au candidat de démontrer ses compétences sans stéréotypes de genre.

### Entrevue 2
- **Structure et Contenu :** L'entrevue avec le candidat_2 a également été bien structurée, mettant l'accent sur l'expérience en gestion d'équipe et la résolution de problèmes complexes.
- **Langage et Ton :** Le recruteur a utilisé un langage neutre et a posé des questions similaires à celles de l'entrevue 1, assurant une cohérence dans le processus.

## Diagnostic de Biais
- **Entrevue 1 :** Aucun biais de genre évident n'a été détecté. Les questions étaient axées sur les compétences techniques et l'expérience.
- **Entrevue 2 :** De même, aucun biais de genre n'a été observé. Le recruteur a posé des questions similaires à celles de l'entrevue 1, indiquant une approche équitable.

## Recommandations
- Continuer à utiliser une grille d'évaluation standardisée pour garantir que toutes les questions posées sont pertinentes pour le poste et non influencées par des stéréotypes de genre.
- Former les recruteurs sur les biais inconscients pour s'assurer qu'ils restent neutres et objectifs tout au long du processus de recrutement.
- Encourager la diversité dans le panel de recruteurs pour apporter différentes perspectives et réduire les biais potentiels.

## Score de Biais
- **Entrevue 1 :** 5/100 - La présence de biais est très peu probable.
- **Entrevue 2 :** 5/100 - La présence de biais est très peu probable.
- **Score Biais Global :** 5/100 - La présence de biais chez ce recruteur est très peu probable.

## Conclusion
Aucun candidat ne semble avoir été favorisé. Les deux entrevues ont été menées de manière équitable, avec des questions similaires et un ton neutre. Le processus de recrutement respecte les principes d'équité, de diversité et d'inclusion, avec un score de biais global très faible.
