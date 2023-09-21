from rest_framework import serializers

# Modelos
from vet.models import PetOwner, Pet


# HTTP -> body
# Serializadores -> Representacion de nuestra API
class OwnersSerializers(serializers.HyperlinkedModelSerializer):
    """Pet owners serializer."""

    class Meta:
        model = PetOwner
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "phone",
            "created_at",
        ]


class PetsSerializer(serializers.HyperlinkedModelSerializer):
    """Pet serializer."""

    owner = serializers.PrimaryKeyRelatedField(
        queryset=PetOwner.objects.all(), many=False
    )

    class Meta:
        model = Pet
        fields = [
            "name",
            "type",
            "created_at",
            "owner",  # foreign key
        ]
