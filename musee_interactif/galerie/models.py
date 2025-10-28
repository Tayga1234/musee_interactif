from django.db import models

# Create your models here.
from django.db import models

class Artiste(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, blank=True, null=True)
    biographie = models.TextField(blank=True)
    photo = models.ImageField(upload_to='artistes/', blank=True, null=True)
    nationalite = models.CharField(max_length=100, blank=True, null=True)
    date_naissance = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom


class Oeuvre(models.Model):
    titre = models.CharField(max_length=200)
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE, related_name='oeuvres')
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)
    annee_creation = models.CharField(max_length=20, blank=True)
    image_principale = models.ImageField(upload_to='oeuvres/', blank=True, null=True)
    fichier_3d = models.FileField(upload_to='oeuvres/3d/', blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre


class Media(models.Model):
    oeuvre = models.ForeignKey(Oeuvre, on_delete=models.CASCADE, related_name='medias')
    type = models.CharField(max_length=50, choices=[
        ('image', 'Image'),
        ('video', 'Vidéo'),
        ('audio', 'Audio'),
        ('3d', '3D'),
    ])
    fichier = models.FileField(upload_to='fich')
    legende = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.type} - {self.oeuvre.titre}"


class Exposition(models.Model):
    titre = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField(blank=True, null=True)
    oeuvres = models.ManyToManyField(Oeuvre, related_name='expositions')
    image_affiche = models.ImageField(upload_to='expositions/', blank=True, null=True)

    def __str__(self):
        return self.titre
