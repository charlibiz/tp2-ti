from django.urls import path, include
from rest_framework import routers

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import user, rooms

schema_view = get_schema_view( 
    openapi.Info(
        title="Swagger TP2",
        default_version="v1.0",
        description="Application pour l'api du TP2",
    ),
    public=True,
)

router = routers.DefaultRouter()
# compléter ...
#router.register("user", UserViewSet, basename="user")

urlpatterns = [
    path("user/", user, name="user"),
    path("rooms", rooms, name="rooms"),
    path(
        "swagger",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
