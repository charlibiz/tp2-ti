from rest_framework import fields, serializers

from django.contrib.auth.models import User
from .models import locateur, ville

class locateurSerializer(serializers.ModelSerializer):
    class Meta:
       model = locateur
       fields = {"username", "password", "first_name", "last_name", "email", "birth_date", "gender", "chambre", "balance"}


class villeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ville
        fields = ("id", "name")

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")