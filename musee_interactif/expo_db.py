import os
import django

# Indique le fichier settings de ton projet
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musee_interactif.settings')

# Initialise Django
django.setup()

# Maintenant tu peux importer les modèles
from galerie.models import Artiste, Categorie, Oeuvre, Exposition

# Ton code de création d'expositions ici...

from datetime import date, timedelta


# === Nettoyage (optionnel si tu veux repartir propre) ===
# Exposition.objects.all().delete()
# Oeuvre.objects.all().delete()
# Artiste.objects.all().delete()
# Categorie.objects.all().delete()

print("=== Création de données d'exemple pour les expositions ===")

# === Catégories ===
categorie_peinture, _ = Categorie.objects.get_or_create(
    nom="Peinture", defaults={"description": "Œuvres réalisées à la peinture."}
)
categorie_sculpture, _ = Categorie.objects.get_or_create(
    nom="Sculpture", defaults={"description": "Œuvres sculptées à la main."}
)
categorie_photo, _ = Categorie.objects.get_or_create(
    nom="Photographie", defaults={"description": "Œuvres photographiques."}
)

# === Artistes ===
artiste1, _ = Artiste.objects.get_or_create(
    nom="Kaboré", prenom="Aïcha",
    defaults={"biographie": "Artiste peintre burkinabè passionnée par la nature.",
              "nationalite": "Burkina Faso"}
)

artiste2, _ = Artiste.objects.get_or_create(
    nom="Ouédraogo", prenom="Jean-Paul",
    defaults={"biographie": "Sculpteur et designer reconnu pour ses œuvres en bois.",
              "nationalite": "Burkina Faso"}
)

artiste3, _ = Artiste.objects.get_or_create(
    nom="Diallo", prenom="Fatoumata",
    defaults={"biographie": "Photographe contemporaine explorant la vie urbaine.",
              "nationalite": "Mali"}
)

# === Œuvres ===
oeuvre1, _ = Oeuvre.objects.get_or_create(
    titre="Forêt d’Espoir",
    artiste=artiste1,
    categorie=categorie_peinture,
    defaults={"description": "Tableau représentant la résilience de la nature.", "annee_creation": "2023"}
)

oeuvre2, _ = Oeuvre.objects.get_or_create(
    titre="L’Âme du Bois",
    artiste=artiste2,
    categorie=categorie_sculpture,
    defaults={"description": "Sculpture en bois d’ébène symbolisant la sagesse.", "annee_creation": "2022"}
)

oeuvre3, _ = Oeuvre.objects.get_or_create(
    titre="Regards d’Afrique",
    artiste=artiste3,
    categorie=categorie_photo,
    defaults={"description": "Série de clichés capturant la vie quotidienne à Ouagadougou.", "annee_creation": "2024"}
)

# === Dates de référence ===
today = date.today()

# Expositions EN COURS (date_fin dans le futur)
expo1, _ = Exposition.objects.get_or_create(
    titre="Couleurs d’Afrique",
    defaults={
        "description": "Une immersion dans la richesse visuelle du continent africain.",
        "date_debut": today - timedelta(days=5),
        "date_fin": today + timedelta(days=10),
    }
)
expo1.oeuvres.set([oeuvre1, oeuvre3])

expo2, _ = Exposition.objects.get_or_create(
    titre="Formes et Matières",
    defaults={
        "description": "Exploration des textures et volumes dans l’art contemporain.",
        "date_debut": today - timedelta(days=2),
        "date_fin": today + timedelta(days=20),
    }
)
expo2.oeuvres.set([oeuvre2])

# Expositions TERMINÉES (date_fin passée)
expo3, _ = Exposition.objects.get_or_create(
    titre="Lumières du Passé",
    defaults={
        "description": "Retour sur les œuvres emblématiques des années 2000.",
        "date_debut": today - timedelta(days=60),
        "date_fin": today - timedelta(days=30),
    }
)
expo3.oeuvres.set([oeuvre1, oeuvre2])

expo4, _ = Exposition.objects.get_or_create(
    titre="Visions Urbaines",
    defaults={
        "description": "Photographies modernes des villes africaines en pleine expansion.",
        "date_debut": today - timedelta(days=40),
        "date_fin": today - timedelta(days=5),
    }
)
expo4.oeuvres.set([oeuvre3])

print("=== Données créées avec succès ===")
print(f"Expositions en cours : {Exposition.objects.filter(date_fin__gte=today).count()}")
print(f"Expositions terminées : {Exposition.objects.filter(date_fin__lt=today).count()}")
