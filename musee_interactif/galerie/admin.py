from django.contrib import admin
from .models import Artiste, Categorie, Oeuvre, Media, Exposition

# --- Configuration des modèles dans l'admin ---

@admin.register(Artiste)
class ArtisteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'nationalite', 'date_naissance')
    search_fields = ('nom', 'prenom', 'nationalite')
    list_filter = ('nationalite',)
    ordering = ('nom',)


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')
    search_fields = ('nom',)


class MediaInline(admin.TabularInline):
    model = Media
    extra = 1


@admin.register(Oeuvre)
class OeuvreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'artiste', 'categorie', 'annee_creation', 'date_ajout')
    list_filter = ('categorie', 'artiste')
    search_fields = ('titre', 'description')
    inlines = [MediaInline]
    date_hierarchy = 'date_ajout'
    ordering = ('-date_ajout',)


@admin.register(Exposition)
class ExpositionAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_debut', 'date_fin')
    list_filter = ('date_debut',)
    search_fields = ('titre', 'description')
    filter_horizontal = ('oeuvres',)
