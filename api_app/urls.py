from django.urls import path, include
from rest_framework import routers

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import UserViewSet, LocalViewSet, ReservationViewSet

schema_view = get_schema_view( 
    openapi.Info(
        title="Réservation de salles de réunion",
        default_version="v1.0",
        description="Application pour l'examen",
    ),
    public=True,
)

router = routers.DefaultRouter()
# compléter ...
router.register("user", UserViewSet, basename="user")
router.register("local", LocalViewSet, basename="local")
router.register("reservation", ReservationViewSet, basename="reservation")

urlpatterns = [
    path("", include(router.urls), name="api"),
    path(
        "swagger",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
