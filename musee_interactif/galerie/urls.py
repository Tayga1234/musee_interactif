from django.urls import path
from . import views

app_name = 'galerie'

urlpatterns = [
    path('', views.index, name='index'),  # Page d’accueil
    #path('artistes/', views.artistes, name='artistes'),
    #path('oeuvres/', views.oeuvres, name='oeuvres'),
    #path('contact/', views.contact, name='contact'),
    path('exposition/', views.liste_expositions, name='liste_expositions'),
    path('oeuvre/<int:pk>/', views.detail_oeuvre, name='detail_oeuvre'),
    path('exposition/<int:pk>/', views.detail_exposition, name='detail_exposition'),

]