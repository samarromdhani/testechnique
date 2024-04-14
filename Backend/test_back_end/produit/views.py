from produit.produit_serializer import ProduitSerializer
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from .models import Produit,Categories
import logging
logger=logging.getLogger(__name__)

#Récupérer la liste de tout les produits
@csrf_exempt
@api_view(['GET'])
@permission_classes((AllowAny,))
def list_produit(request):
    produit_data=Produit.objects.all()
    mesure_serializer=ProduitSerializer(produit_data,many=True)
    return JsonResponse(mesure_serializer.data,safe=False, status=status.HTTP_200_OK)
#Mettre a jour uniquement le champs 
@csrf_exempt
@api_view(['PUT'])
@permission_classes((AllowAny,))
def miseAJourProduit(request):
    logger.info("Nouvelle request de mise à ajour de utilisateur ...")

    try:
        produit_data=Produit.objects.get(produit_Id=request.data['produit_id'])
        categorie=request.data['categories_Produit']
        #Vérifier la catégories exacte
        if categorie=='VIANDE':
             produit_data.categories_Produit=Categories.VIANDE
        elif categorie=='FRUIT':
             produit_data.categories_Produit=Categories.FRUIT
        elif categorie=='LEGUME':
            produit_data.categories_Produit=Categories.lEGUME
        produit_data.save()
        return JsonResponse("Modifier avec succés",safe=False, status=status.HTTP_200_OK)

    except Exception as e:#Relever tous les exceptions
        logger.error('error'+str(e))
        return JsonResponse("error lors de mise a jour",safe=False,status=status.HTTP_500)
