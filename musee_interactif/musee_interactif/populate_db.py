import os
import django
from datetime import date
import random

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musee_interactif.settings')
django.setup()

from galerie.models import Artiste, Categorie, Oeuvre, Exposition

from museum.models import Artiste, Categorie, Oeuvre

# Créer un artiste "Anonyme"
artiste, created = Artiste.objects.get_or_create(
    nom="Inconnu",
    prenom="Artiste",
    defaults={
        "biographie": "Artiste contemporain africain fictif pour le musée.",
        "nationalite": "Africaine"
    }
)

# Créer la catégorie "Masques"
categorie, created = Categorie.objects.get_or_create(
    nom="Masques",
    defaults={"description": "Collection de masques africains contemporains."}
)

# Liste des masques avec infos de base
masques_info = [
    {"titre": "Masque du Soleil", "description": "Symbole de lumière et de renouveau.", "annee": "2023"},
    {"titre": "Visage des Ancêtres", "description": "Rend hommage aux ancêtres et à la mémoire collective.", "annee": "2024"},
    {"titre": "Masque de l’Esprit du Baobab", "description": "Représente la sagesse et la longévité.", "annee": "2022"},
    {"titre": "Masque des Quatre Vents", "description": "Évoque l’union des éléments et des directions.", "annee": "2023"},
    {"titre": "Gardiens du Royaume", "description": "Protège le patrimoine et la culture locale.", "annee": "2025"},
    {"titre": "Masque de la Mémoire", "description": "Symbole de l’histoire et du souvenir.", "annee": "2024"},
    {"titre": "Masque de l’Abondance", "description": "Célèbre la richesse et la prospérité.", "annee": "2023"},
    {"titre": "Sourire du Village", "description": "Exprime la joie et l’hospitalité africaine.", "annee": "2025"},
    {"titre": "Masque du Fleuve Sacré", "description": "Inspire respect pour la nature et les ressources d’eau.", "annee": "2022"},
    {"titre": "Masque de la Sagesse", "description": "Représente la connaissance et l’équilibre.", "annee": "2023"},
]

# Créer les oeuvres
for info in masques_info:
    oeuvre, created = Oeuvre.objects.get_or_create(
        titre=info["titre"],
        artiste=artiste,
        categorie=categorie,
        defaults={
            "description": info["description"],
            "annee_creation": info["annee"]
        }
    )
    if created:
        print(f"Oeuvre '{info['titre']}' créée avec succès")
    else:
        print(f"Oeuvre '{info['titre']}' existait déjà")
