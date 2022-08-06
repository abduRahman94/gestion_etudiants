from django.db import models

# Create your models here.

class Etudiant(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    age = models.IntegerField()

