from django import template

register = template.Library()

@register.filter
def dict_key(d, key):
    """Retourne la valeur d'un dictionnaire pour une clé donnée"""
    return d.get(key)
