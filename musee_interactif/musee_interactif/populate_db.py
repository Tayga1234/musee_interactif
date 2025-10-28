import os
import django
from datetime import date
import random

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musee_interactif.settings')
django.setup()

from galerie.models import Artiste, Categorie, Oeuvre, Exposition

# === Catégories ===
categories = [
    ("Peinture", "Œuvres réalisées à la peinture à huile, acrylique, aquarelle..."),
    ("Sculpture", "Œuvres modelées, taillées ou moulées."),
    ("Photographie", "Captures artistiques contemporaines."),
    ("Installation", "Créations immersives ou expérimentales."),
]

for nom, desc in categories:
    Categorie.objects.get_or_create(nom=nom, defaults={'description': desc})

print("✅ Catégories créées avec succès !")

# === Artistes ===
artistes_data = [
    ("Kouassi", "Adama", "Artiste ivoirien passionné par l'abstraction et la couleur.", "Côte d'Ivoire", "1985-03-21"),
    ("Ouédraogo", "Mariam", "Sculptrice burkinabè explorant les formes traditionnelles revisitées.", "Burkina Faso", "1990-11-10"),
    ("Diallo", "Moussa", "Photographe malien documentant la vie urbaine africaine.", "Mali", "1988-06-05"),
]

for nom, prenom, bio, nat, dob in artistes_data:
    Artiste.objects.get_or_create(
        nom=nom,
        prenom=prenom,
        defaults={'biographie': bio, 'nationalite': nat, 'date_naissance': dob}
    )

print("✅ Artistes créés avec succès !")

# === Œuvres ===
oeuvres_data = [
    ("Reflets d'Abidjan", "Peinture", "Une vision abstraite de la capitale ivoirienne.", 2018),
    ("La Force des Femmes", "Sculpture", "Hommage à la résilience féminine.", 2020),
    ("Lumières de Bamako", "Photographie", "Jeux de lumière dans la ville de Bamako.", 2021),
]

for titre, cat_nom, desc, annee in oeuvres_data:
    categorie = Categorie.objects.get(nom=cat_nom)
    artiste = random.choice(Artiste.objects.all())
    Oeuvre.objects.get_or_create(
        titre=titre,
        artiste=artiste,
        categorie=categorie,
        defaults={'description': desc, 'annee_creation': annee}
    )

print("✅ Œuvres créées avec succès !")

# === Expositions ===
expo_data = [
    ("Abstractions Africaines", "Un voyage à travers les formes et couleurs d'Afrique.", date(2025, 5, 10), date(2025, 7, 30)),
    ("Femmes et Matières", "Exploration de la féminité à travers la sculpture.", date(2025, 8, 15), date(2025, 10, 20)),
]

for titre, desc, debut, fin in expo_data:
    expo, created = Exposition.objects.get_or_create(
        titre=titre,
        defaults={'description': desc, 'date_debut': debut, 'date_fin': fin}
    )
    oeuvres = list(Oeuvre.objects.all())
    expo.oeuvres.set(random.sample(oeuvres, min(3, len(oeuvres))))
    expo.save()

print("✅ Expositions créées avec succès !")
