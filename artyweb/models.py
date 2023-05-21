# Create your models here.
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




class Service(models.Model):
    TYPE_CHOICES = [
        ('Design Graphique', 'Design Graphique'),
        ('Design Web', 'Design Web'),
        ('SC', 'Scénarisation'),
    ]
    
    nom = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    image = models.ImageField( null=True, blank=True)
   
    def __str__(self):
        return self.nom


class Projet(models.Model):
    libelle = models.CharField(max_length=50)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    acheve = models.BooleanField(default=False)
    image= models.ImageField(upload_to='media/', blank=True)
    service = models.ForeignKey('Service', on_delete=models.CASCADE, null=True, blank=True)
    equipe = models.ForeignKey('Equipe', on_delete=models.CASCADE, null=True, blank=True)

    

    def __str__(self):
        return self.libelle
    
class Personnel(models.Model):
    nom = models.CharField(max_length=50)
    cv = models.TextField()
    photo = models.ImageField()
    lien_fb = models.URLField(null=True, blank=True)
    equipe = models.ForeignKey('Equipe', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nom
class Equipe(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    image= models.ImageField( blank=True)
   
    
    def __str__(self):
        return self.nom
