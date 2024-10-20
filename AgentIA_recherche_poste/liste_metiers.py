from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


# On définit un Pydantic model pour les métiers
class Metier(BaseModel):
    id: int
    description: str


metiers = [
    Metier(id=1, description="Ingénieur(e) logiciel"),
    Metier(id=2, description="Médecin"),
    Metier(id=3, description="Avocat(e)"),
    Metier(id=4, description="Enseignant(e)"),
    Metier(id=5, description="Infirmier(e)"),
    Metier(id=6, description="Comptable"),
    Metier(id=7, description="Architecte"),
    Metier(id=8, description="Pharmacien(ne)"),
    Metier(id=9, description="Ingénieur(e) en mécanique"),
    Metier(id=10, description="Ingénieur(e) électricien"),
    Metier(id=11, description="Ingénieur(e) civil"),
    Metier(id=12, description="Économiste"),
    Metier(id=13, description="Psychologue"),
    Metier(id=14, description="Vétérinaire"),
    Metier(id=15, description="Chimiste"),
    Metier(id=16, description="Biologiste"),
    Metier(id=17, description="Physicien(ne)"),
    Metier(id=18, description="Mathématicien(ne)"),
    Metier(id=19, description="Statisticien(ne)"),
    Metier(id=20, description="Designer graphique"),
    Metier(id=21, description="Rédacteur(e) technique"),
    Metier(id=22, description="Traducteur(e)"),
    Metier(id=23, description="Chef cuisinier(ière)"),
    Metier(id=24, description="Boulanger(ère)"),
    Metier(id=25, description="Pâtissier(ière)"),
    Metier(id=26, description="Barman(Barmaid)"),
    Metier(id=27, description="Serveur(euse)"),
    Metier(id=28, description="Hôte(sse) de l'air"),
    Metier(id=29, description="Steward"),
    Metier(id=30, description="Pilote"),
    Metier(id=31, description="Contrôleur(e) aérien"),
    Metier(id=32, description="Agent(e) de bord"),
    Metier(id=33, description="Mécanicien(ne) automobile"),
    Metier(id=34, description="Électricien(ne)"),
    Metier(id=35, description="Plombier(ière)"),
    Metier(id=36, description="Charpentier(ière)"),
    Metier(id=37, description="Peintre en bâtiment"),
    Metier(id=38, description="Maçon"),
    Metier(id=39, description="Paysagiste"),
    Metier(id=40, description="Coiffeur(euse)"),
    Metier(id=41, description="Esthéticien(ne)"),
    Metier(id=42, description="Journaliste"),
    Metier(id=43, description="Éditeur(e)"),
    Metier(id=44, description="Photographe"),
    Metier(id=45, description="Vidéaste"),
    Metier(id=46, description="Animateur(e) radio"),
    Metier(id=47, description="Producteur(trice) de musique"),
    Metier(id=48, description="Artiste")
]


@app.get("/tasks", response_model=List[Metier])
async def get_metiers():
    """
    Retourne la liste des métiers
    """
    return metiers

