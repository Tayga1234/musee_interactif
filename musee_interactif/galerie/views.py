from django.shortcuts import get_object_or_404, render
from .models import *

def index(request):
    # Récupère les 6 œuvres les plus récentes
    oeuvres_recents = Oeuvre.objects.all().order_by('-date_ajout')[:8]
    artistes = Artiste.objects.all()[:6]
    return render(request, 'index.html', {'oeuvres_recents': oeuvres_recents, 'artistes':artistes})


from django.shortcuts import render
from .models import Exposition
from datetime import date

def expositions(request):
    today = date.today()
    expositions_courantes = Exposition.objects.filter(date_debut__lte=today, date_fin__gte=today)
    expositions_passees = Exposition.objects.filter(date_fin__lt=today)
    artistes = Artiste.objects.all()
    return render(request, 'expositions.html', {
        'expositions_courantes': expositions_courantes,
        'expositions_passees': expositions_passees,
        'artistes':artistes
    })
    
from datetime import date

def liste_expositions(request):
    today = date.today()

    expositions_en_cours = Exposition.objects.filter(date_fin__gte=today).order_by('-date_debut')
    expositions_passees = Exposition.objects.filter(date_fin__lt=today).order_by('-date_debut')
    
    artistes = Artiste.objects.all()
    context = {
        'expositions_en_cours': expositions_en_cours,
        'expositions_passees': expositions_passees,
        'today': today,
        'artistes':artistes
    }
    return render(request, 'expositions.html', context)


def detail_exposition(request, pk):
    """
    Affiche le détail d'une exposition, incluant toutes les œuvres associées.
    """
    exposition = get_object_or_404(Exposition, pk=pk)
    oeuvres = exposition.oeuvres.all()  # Toutes les œuvres liées
    # Vérifie si l'utilisateur a liké
    # Récupérer tous les commentaires liés aux oeuvres de cette exposition
    #commentaires = Commentaire.objects.filter(oeuvre__in=oeuvres).order_by('-date_creation')
    oeuvres_likes = {}
    if request.user.is_authenticated:
        for oeuvre in oeuvres:
            oeuvres_likes[oeuvre.id] = oeuvre.likes.filter(utilisateur=request.user).exists()
    contexte = {
        'exposition': exposition,
        'oeuvres': oeuvres,
        'oeuvres_likes': oeuvres_likes,
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
    
     # Vérifie si l'utilisateur a liké
    user_liked = False
    if request.user.is_authenticated:
        Like.objects.filter(utilisateur=request.user, oeuvre=oeuvre).exists()

    

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
        'user_liked': user_liked,
    }

    return render(request, 'oeuvre_detail.html', contexte)

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Nom d'utilisateur déjà utilisé.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        auth_login(request, user)
        return redirect('galerie:index')
    return render(request, 'index.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Vérification si les champs sont remplis
        if not username or not password:
            messages.error(request, "Veuillez remplir tous les champs.")
            return redirect('galerie:login')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Bienvenue, {user.username} 👋")
            return redirect('galerie:index')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
            return redirect('galerie:login')

    return render(request, 'login.html')

def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('galerie:index')


def profil(request):
    return render(request, 'profil.html')

def about(request):
    return render(request, 'about.html')

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def like_oeuvre(request, oeuvre_id):
    if request.method == "POST":
        oeuvre = get_object_or_404(Oeuvre, id=oeuvre_id)
        like, created = Like.objects.get_or_create(utilisateur=request.user, oeuvre=oeuvre)
        
        if not created:
            like.delete()
            liked = False
        else:
            liked = True

        # Nombre total de likes
        total_likes = oeuvre.likes.count()

        return JsonResponse({'liked': liked, 'total_likes': total_likes})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def about(request):
    return render(request, 'about.html')

def evenement(request):
    today = date.today()

    # Expositions en cours : déjà commencées mais pas encore terminées
    expositions_en_cours = Exposition.objects.filter(
        date_debut__lte=today,
        date_fin__gte=today
    ).order_by('-date_debut')

    # Expositions à venir : pas encore commencées
    expositions_a_venir = Exposition.objects.filter(
        date_debut__gt=today
    ).order_by('date_debut')

    # Expositions passées : déjà terminées
    expositions_passees = Exposition.objects.filter(
        date_fin__lt=today
    ).order_by('-date_debut')

    context = {
        'expositions_a_venir': expositions_a_venir,
        'expositions_en_cours': expositions_en_cours,
        'expositions_passees': expositions_passees,
        'today': today,
    }
    
    return render(request, 'evenement.html', context)