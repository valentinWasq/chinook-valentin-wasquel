from django import forms

# forms pour la recherche
class RechercheForm(forms.Form):
    recherche = forms.CharField()