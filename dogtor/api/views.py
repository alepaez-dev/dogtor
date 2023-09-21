from django.shortcuts import render
from rest_framework import viewsets

# Models
from vet.models import PetOwner

# Serializers
from .serializers import OwnersSerializers

# Create your views here.


# LIST -> GET - check
# RETRIEVE -> GET
# UPDATE -> PUT
# CREATE -> POST
# DELETE -> DELETE


# TODOS LOS ENDPOINTS DE PETS
# TODOS LOS ENDPOINTS DE PETDATES


class OwnersViewSet(viewsets.ModelViewSet):
    """ViewSet del modelo PetOwner."""

    # 1. queryset que se va a realizar -> ORM
    # 2. El serializador

    # Obtener todos los owners -> PetOwners.objects.all()
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializers
