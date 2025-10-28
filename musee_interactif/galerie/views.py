from django.shortcuts import get_object_or_404, render
from .models import Oeuvre

def index(request):
    # Récupère les 6 œuvres les plus récentes
    oeuvres_recents = Oeuvre.objects.all().order_by('-date_ajout')[:6]
    return render(request, 'index.html', {'oeuvres_recents': oeuvres_recents})


from django.shortcuts import render
from .models import Exposition
from datetime import date

def expositions(request):
    today = date.today()
    expositions_courantes = Exposition.objects.filter(date_debut__lte=today, date_fin__gte=today)
    expositions_passees = Exposition.objects.filter(date_fin__lt=today)
    return render(request, 'expositions.html', {
        'expositions_courantes': expositions_courantes,
        'expositions_passees': expositions_passees
    })
    
from datetime import date

def liste_expositions(request):
    today = date.today()

    expositions_en_cours = Exposition.objects.filter(date_fin__gte=today).order_by('-date_debut')
    expositions_passees = Exposition.objects.filter(date_fin__lt=today).order_by('-date_debut')

    context = {
        'expositions_en_cours': expositions_en_cours,
        'expositions_passees': expositions_passees,
        'today': today,
    }
    return render(request, 'expositions.html', context)


def detail_exposition(request, pk):
    """
    Affiche le détail d'une exposition, incluant toutes les œuvres associées.
    """
    exposition = get_object_or_404(Exposition, pk=pk)
    oeuvres = exposition.oeuvres.all()  # Toutes les œuvres liées
    contexte = {
        'exposition': exposition,
        'oeuvres': oeuvres,
    }
    return render(request, 'exposition_detail.html', contexte)



from django.shortcuts import render, get_object_or_404
from .models import Oeuvre, Media

def detail_oeuvre(request, oeuvre_id):
    """
    Affiche le détail d'une œuvre, incluant images, vidéos, audio et fichiers 3D.
    """

    # Récupérer l'œuvre ou renvoyer 404
    oeuvre = get_object_or_404(Oeuvre, id=oeuvre_id)

    # Récupérer tous les médias associés
    medias = oeuvre.medias.all()

    # Séparer les médias par type pour un affichage structuré
    images = medias.filter(type='image')
    videos = medias.filter(type='video')
    audios = medias.filter(type='audio')
    fichiers_3d = medias.filter(type='3d')

    contexte = {
        'oeuvre': oeuvre,
        'images': images,
        'videos': videos,
        'audios': audios,
        'fichiers_3d': fichiers_3d,
    }

    return render(request, 'oeuvre_detail.html', contexte)
