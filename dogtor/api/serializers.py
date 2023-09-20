from rest_framework import serializers

# Modelos
from vet.models import PetOwner


# Serializadores -> Representacion de nuestra API
class OwnersSerializers(serializers.HyperlinkedModelSerializer):
    """Pet owners serializer."""

    class Meta:
        model = PetOwner
        fields = [
            "first_name",
            "last_name",
            "email",
            "address",
            "phone",
            "created_at",
        ]
