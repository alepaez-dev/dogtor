# 1. path
# 2. urlpatterns

from django.urls import path

# Views
# PascalCase -> clases -> modelos o vistas clase
# snake_case -> para todo lo demas
from .views import list_pet_owners, Test, OwnersList, OwnerDetail


urlpatterns = [
    path("owners/", OwnersList.as_view()),
    path("owners/<int:pk>/", OwnerDetail.as_view()),
    path("test/", Test.as_view()),
]
