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
    exposition = get_object_or_404(Exposition, pk=pk)
    # récupérer toutes les oeuvres de cette exposition
    oeuvres = exposition.oeuvres.all()
    return render(request, 'exposition_detail.html', {
        'exposition': exposition,
        'oeuvres': oeuvres
    })

def detail_oeuvre(request, pk):
    oeuvre = get_object_or_404(Oeuvre, pk=pk)
    return render(request, 'detail_oeuvre.html', {'oeuvre': oeuvre})
