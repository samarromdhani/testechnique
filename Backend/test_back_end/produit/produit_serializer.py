from .models import Produit,Categories
from rest_framework import serializers

class ProduitSerializer(serializers.ModelSerializer):
   categories_Produit=serializers.ChoiceField(choices=dict(map(lambda item: (item.name, item.value), Categories)))
   class Meta:
       model=Produit
       fields = '__all__'