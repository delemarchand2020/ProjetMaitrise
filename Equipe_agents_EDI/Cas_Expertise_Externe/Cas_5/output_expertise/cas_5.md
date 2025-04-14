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
        "message": "Bonjour XXX, vous postulez pour le poste de Infirmier.ière
Spécialisé.e en Soins Néonatals, pouvez vous m'en dire un peu plus sur vous et
ce qui vous motive dans ce poste ?"
    },
    {
        "role": "Candidat",
        "message": "Bonjour, je suis passionné.e par les soins aux nouveau-nés
et possède une solide expérience en soins intensifs néonatals. Mon engagement à
soutenir les familles dans des situations difficiles et ma capacité à collaborer
efficacement avec l'équipe médicale font de moi un atout pour votre unité de
soins néonatals."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour votre réponse. Pourriez-vous partager une
expérience où vous avez dû prendre des décisions critiques sous pression en
soins néonatals ?"
    },
    {
        "role": "Candidat",
        "message": "Lors de mon expérience à la Clinique BébéSoin, j'ai été
confronté.e à une situation où un nouveau-né en soins intensifs présentait des
complications respiratoires soudaines; j'ai rapidement collaboré avec les
médecins pour ajuster le plan de soins et utiliser l'équipement spécialisé,
assurant ainsi la stabilité du nourrisson."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour votre réponse détaillée. Vous semblez avoir une
bonne expérience dans des situations critiques. Pensez-vous que votre approche
empathique pourrait influencer vos décisions professionnelles dans un
environnement de soins intensifs néonatals ?"
    },
    {
        "role": "Candidat",
        "message": "Mon approche empathique me permet d'accompagner efficacement
les familles tout en assurant des soins de qualité et une collaboration fluide
avec l'équipe médicale, ce qui est essentiel pour élaborer des plans de soins
personnalisés en soins intensifs néonatals."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour votre réponse. Compte tenu de l'importance d'une
collaboration fluide avec l'équipe médicale, comment percevez-vous l'équilibre
entre autorité et approche collaborative en tant que femme leader dans un
environnement de soins intensifs néonatals ?"
    },
    {
        "role": "Candidat",
        "message": "En tant que leader en soins intensifs néonatals, j'assure un
équilibre entre autorité et approche collaborative en soutenant les plans de
soins personnalisés et en supervisant l'utilisation d'équipements médicaux, tout
en restant ouverte aux contributions de l'équipe pour garantir des soins
optimaux aux nouveau-nés."
    },
    {
        "role": "Recruteur",
        "message": "Votre approche semble bien équilibrée. Pour mieux comprendre
votre expertise, pourriez-vous nous parler d'une situation où vous avez dû
adapter rapidement un plan de soins en raison de changements dans l'état de
santé d'un nouveau-né ?"
    },
    {
        "role": "Candidat",
        "message": "Lors d'une urgence à la Clinique BébéSoin, j'ai dû
rapidement adapter un plan de soins en collaboration avec les médecins après une
détérioration subite de l'état d'un nouveau-né, démontrant ainsi ma capacité à
gérer efficacement les situations critiques tout en assurant la communication
avec les parents."
    },
    {
        "role": "Recruteur",
        "message": "Je vous remercie d'avoir pris le temps de discuter avec nous
aujourd'hui. Nous allons examiner toutes les candidatures et vous serez
contacté(e) pour les prochaines étapes du recrutement. Je vous souhaite une
bonne continuation dans vos recherches et espère que nous aurons l'occasion de
collaborer à l'avenir."
    },
    {
        "role": "Candidat",
        "message": "Merci pour cette entrevue et je vous souhaite une agréable
journée."
    }
]
```

<div style="page-break-after: always;"></div>
## Seconde conversation

```json
[
    {
        "role": "Recruteur",
        "message": "Bonjour XXX, vous postulez pour le poste de Infirmier.ière
Spécialisé.e en Soins Néonatals, pouvez vous m'en dire un peu plus sur vous et
ce qui vous motive dans ce poste ?"
    },
    {
        "role": "Candidat",
        "message": "Bonjour, je suis passionné.e par les soins aux nouveau-nés
et possède une expertise solide en soins intensifs néonatals, ce qui me permet
d'offrir un haut niveau de soins et de soutien aux familles dans des moments
difficiles."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour votre réponse. Pourriez-vous me parler d'une
situation où vous avez dû collaborer avec d'autres membres de l'équipe médicale
pour élaborer un plan de soins personnalisé?"
    },
    {
        "role": "Candidat",
        "message": "Lors d'une situation complexe en soins intensifs, j'ai
collaboré étroitement avec l'équipe médicale pour créer un plan de soins
personnalisé, assurant une prise en charge optimale du nouveau-né tout en
soutenant les parents dans cette période difficile."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour ce partage d'expérience. Pourriez-vous nous
parler d'une situation où vous avez dû gérer un conflit au sein de l'équipe
médicale et comment vous l'avez résolu?"
    },
    {
        "role": "Candidat",
        "message": "Lors d'un conflit concernant la gestion d'un cas critique,
j'ai facilité une discussion ouverte entre les membres de l'équipe, ce qui a
permis d'harmoniser nos approches et d'améliorer notre collaboration pour le
suivi médical des nouveau-nés."
    },
    {
        "role": "Recruteur",
        "message": "Je vous remercie pour votre réponse. Pourriez-vous me
décrire comment vous abordez la communication avec les familles en situation de
stress dans le contexte des soins néonatals?"
    },
    {
        "role": "Candidat",
        "message": "En tant qu'infirmier.ière spécialisé.e en soins néonatals,
je privilégie une communication claire et empathique avec les familles, en leur
offrant un soutien psychologique essentiel et en les impliquant activement dans
le processus de soins pour leur nouveau-né."
    },
    {
        "role": "Recruteur",
        "message": "Merci pour cette précision. Pourriez-vous partager une
situation où vous avez collaboré efficacement avec des médecins pour élaborer un
plan de soins personnalisé pour un nouveau-né?"
    },
    {
        "role": "Candidat",
        "message": "Lors d'une situation complexe en soins intensifs, j'ai
collaboré avec des médecins pour créer un plan de soins sur-mesure pour un
nouveau-né, en veillant à intégrer les besoins spécifiques du patient et à
ajuster les traitements en fonction de son évolution clinique."
    },
    {
        "role": "Recruteur",
        "message": "Merci beaucoup pour votre temps et votre partage
d'expérience. Nous allons examiner les candidatures et vous recevrez des
nouvelles de notre part dans les prochaines semaines concernant l'étape suivante
du processus de recrutement. Je vous souhaite bonne chance pour la suite de vos
recherches."
    },
    {
        "role": "Candidat",
        "message": "Je vous remercie pour cet échange enrichissant et vous
souhaite une excellente journée."
    }
]
```

<div style="page-break-after: always;"></div>
# Rapport d'Audit EDI

## Introduction
Ce rapport présente l'analyse de l'équité, de la diversité et de l'inclusion (EDI) dans le cadre des entrevues de recrutement pour le poste d'Infirmier.ière Spécialisé.e en Soins Néonatals. L'objectif est d'identifier les biais potentiels et de proposer des recommandations pour améliorer le processus de recrutement.

## Méthodologie
L'analyse a été réalisée en examinant les transcriptions de deux entrevues anonymisées. Chaque entrevue a été évaluée pour détecter la présence de biais, notamment ceux liés au genre. Les observations ont été notées et un score de biais a été attribué à chaque entrevue.

## Analyse et Observations

### Entrevue 1
- **Résumé :** Le recruteur a posé des questions pertinentes sur l'expérience et les compétences du candidat, mais a introduit une question potentiellement biaisée en demandant comment le candidat perçoit l'équilibre entre autorité et approche collaborative en tant que femme leader.
- **Observation :** La question sur le leadership féminin pourrait indiquer un biais de genre, car elle présuppose que le genre influence le style de leadership.
- **Diagnostic de biais :** Un biais potentiel a été détecté, ce qui pourrait influencer la perception du candidat.

### Entrevue 2
- **Résumé :** Le recruteur a maintenu une approche neutre, posant des questions sur la collaboration, la gestion des conflits et la communication avec les familles, sans faire référence au genre du candidat.
- **Observation :** Les questions étaient centrées sur les compétences professionnelles et l'expérience, montrant une approche plus neutre.
- **Diagnostic de biais :** Aucun biais de genre évident n'a été détecté.

## Conclusions
- **Score biais par entrevue :**
  - Entrevue 1 : 50/100 (présence de biais moyennement probable)
  - Entrevue 2 : 5/100 (présence de biais très peu probable)
- **Score biais global :** 50/100 (en prenant le maximum des deux scores, car ils sont distincts)
- **Candidat favorisé :** Candidat 2 semble avoir été favorisé en raison de l'absence de questions potentiellement biaisées par rapport au genre.

## Recommandations
- Former le recruteur sur les biais inconscients pour éviter les questions qui pourraient être perçues comme stéréotypées.
- Utiliser une grille d'évaluation standardisée pour garantir que toutes les questions sont pertinentes et équitables.
- Encourager une réflexion sur la formulation des questions pour éviter toute présomption basée sur le genre.

## Conclusion
Ce rapport met en lumière l'importance de la formation continue sur les biais inconscients et l'utilisation de méthodes standardisées pour garantir un processus de recrutement équitable et inclusif.
