from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Etudiant

# Create your views here.

class EtudiantsView(View):
    
    def get(self, request):
        etat = True
        etudiants = Etudiant.objects.all()
        return render(request, 'gestion/etudiants.html', {'etudiants': etudiants, 'etat': etat})
    
    def post(self, request):
        return HttpResponse('<p>Ceci est une liste d\'etudiants</p>')

def etudiant(request, id=None):
    if id is None:
        return HttpResponse('<p> Ceci est un étudiant</p>')
    
    return HttpResponse(f'<p> Ceci est l\'etudiant numéro {id} </p>')

def display_base(request):
    return render(request, 'gestion/base.html')

def display_child(request):
    return render(request, 'gestion/child.html')

def detail(request, id):
    etudiant = Etudiant.objects.get(pk=id)
    
    return render(request, 'gestion/detail.html', {'etudiant': etudiant})
            
