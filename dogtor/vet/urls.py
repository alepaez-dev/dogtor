# 1. path
# 2. urlpatterns

from django.urls import path

# Views
# PascalCase -> clases -> modelos o vistas clase
# snake_case -> para todo lo demas
from .views import list_pet_owners, Test, OwnersList, OwnerDetail, PetsList, PetsDetail

# alias (reversed urls) -> rutas de una app en especifico
# alias (reversed urls) -> rutas del proyecto

# si no tienes include -> reversed url se pone como 3er parametro ejemplo -> name="owners_list"
# si SI tienes include -> reversed url se pone como 2do parametro DENTRO del include() -> include(("vet.urls", "vet"))

# SINTAXIS de como acceder
# "vet:owners_list"
# "vet:owners_detail"
# "reversed_url_app: reversed_url_singular"
urlpatterns = [
    path("owners/", OwnersList.as_view(), name="owners_list"),
    path("owners/<int:pk>/", OwnerDetail.as_view(), name="owners_detail"),
    path("pets/", PetsList.as_view()),
    path("pets/<int:pk>/", PetsDetail.as_view()),
    path("test/", Test.as_view()),
]
