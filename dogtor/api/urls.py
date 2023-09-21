from django.urls import path, include
from rest_framework import routers

# Views
from .views import ListOwnersAPIView, RetrieveOwnersAPIView

# Router
# router = routers.DefaultRouter()
# router.register(r"owners", OwnersViewSet)
# router.register(r"pets", PetsViewSet)

# owners/ -> POST -> create owner
# owners/ -> GET -> list owners
# owners/id -> GET
# owners/id -> PUT
# owners/id -> DELETE
urlpatterns = [
    # path("", include(router.urls))
    path("owners/", ListOwnersAPIView.as_view(), name="owners_list"),
    path("owners/<int:pk>/", RetrieveOwnersAPIView.as_view(), name="owners_detail"),
]
