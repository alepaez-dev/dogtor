from django import forms

# Importamos los modelos
from .models import PetOwner

# Los formularios se tienen que vincular con los modelos.


# Los formularios -> CLASES
class OwnerForm(forms.ModelForm):
    # 1. Modelo de nuestro formulario
    # 2. fields que van a estar en nuestro formulario

    class Meta:
        model = PetOwner  # 1
        fields = ("first_name", "last_name", "address", "email", "phone")  # 2
