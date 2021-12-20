from rest_framework import fields, serializers

from django.contrib.auth.models import User
#from .models import History

from .models import locateur

class locateurSerializer(serializers.ModelSerializer):
    class Meta:
       model = locateur
       fields = {"username", "password", "first_name", "last_name", "email", "birth_date", "gender", "chambre", "balance"}


class ConvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = "History"
        fields = ("initial_val", "initial_met")

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = "History"
        fields = ("time", "initial_val", "initial_met", "final_val", "final_met")

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")