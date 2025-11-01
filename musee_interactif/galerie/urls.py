from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'galerie'

urlpatterns = [
    path('', views.index, name='index'),  # Page d’accueil
    #path('artistes/', views.artistes, name='artistes'),
    #path('oeuvres/', views.oeuvres, name='oeuvres'),
    #path('contact/', views.contact, name='contact'),
    path('exposition/', views.liste_expositions, name='liste_expositions'),
    path('oeuvre/<int:oeuvre_id>/', views.detail_oeuvre, name='detail_oeuvre'),

    #path('oeuvres/', views.liste_oeuvres, name='liste_oeuvres'),
    path('exposition/<int:pk>/', views.detail_exposition, name='detail_exposition'),
    
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profil/', views.profil, name='profil'),
    path('register/', views.register, name='register'),

    path('oeuvre/<int:oeuvre_id>/like/', views.like_oeuvre, name='like_oeuvre'),
    path('about/', views.about, name='about'),
    path('evenement/', views.evenement, name='evenement'),

]