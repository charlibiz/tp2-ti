from rest_framework import fields, serializers

from ui_app.models import Chambre
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "town", "lanlord", )

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chambre
        fields = ("id", "title", "capacity")
 
