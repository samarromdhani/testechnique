from django.db import models
from django.utils import timezone
from django_enumfield import enum

#Enumeration pour le type categories
class Categories(enum.Enum):
    FRUIT=0
    lEGUME=1
    VIANDE=2
    
    
#Déclaration de la classe produit
class Produit(models.Model):
    produit_Id=models.AutoField(primary_key=True)
    code_Produit=models.CharField(max_length=32,unique=True)
    designation=models.CharField(max_length=25)
    date_Creation=models.DateTimeField(default=timezone.now)
    date_Miseajour=models.DateTimeField(default=None)

    prix=models.FloatField(default=None)
    categories_Produit=enum.EnumField(Categories)
    image=models.CharField(max_length=255)

    class Meta:
        db_table = 'produit'
        verbose_name= "produit"