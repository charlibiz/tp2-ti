from django.urls import path
from .views import home, users, members, order, purchase

urlpatterns = [
    path("", home, name="home"),
    path("users", users, name="users"),
    path("members", members, name="members"),
    path("order", order, name="order"),
    path("purchase", purchase, name="purchase")
]