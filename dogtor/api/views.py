from django.shortcuts import render
from rest_framework import viewsets

# Models
from vet.models import PetOwner

# Create your views here.


class OwnersViewSet(viewsets.ModelViewSet):
    """ViewSet del modelo PetOwner."""

    # 1. queryset que se va a realizar -> ORM
    # 2. El serializador

    # Obtener todos los owners -> PetOwners.objects.all()
    queryset = PetOwner.objects.all()
