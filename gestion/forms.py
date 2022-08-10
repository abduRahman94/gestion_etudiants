from django.forms import ModelForm
from django.db import models
from .models import Etudiant


class EtudiantForm(ModelForm):
    class Meta:
        model = Etudiant
        fields = ('nom', 'prenom', 'age', 'parcours')