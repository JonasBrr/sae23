from django.db import models
from datetime import datetime


# Create your models here.
class Machine(models.Model):

    TYPE = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('MAc - Run MacOS')),
        ('Serveur',('Serveur - Simple Server to deploy virtual machines')),
        ('Switch', ('Switch - To maintains and connect servers')),
    )

    id = models.AutoField(
        primary_key=True,
        editable=False
    )
    nom = models.CharField(
        max_length=50
    )
    maintenanceDate = models.DateField( 
        default=datetime.now()
    )
    mach = models.CharField(
        max_length=32,
        choices=TYPE,
        default='PC'
    )

    def __str__(self):
        return str(self.id) + " -> " + self.nom

    def get_name(self): 
        return str(self.id) + " " + self.nom

class Personnel(models.Model):
    num_secu =models.CharField(
        primary_key=True,
        editable=True,
        max_length = 15
    )
    nom = models.CharField(
        max_length=50
    )
    prenom = models.CharField(
        max_length=20
    )

    def __str__(self):
        return str(self.num_secu) + " -> " + self.nom + " " + self.prenom
