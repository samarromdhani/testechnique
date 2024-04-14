from .views import list_produit,miseAJourProduit
from django.urls import path

urlpatterns = [
        path('list/',list_produit),
                path('update/',miseAJourProduit),


]