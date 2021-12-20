from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.conf.urls import url
from django_app.models import ville, locateur, Locataire
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.core import serializers

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from django.utils.timezone import get_current_timezone
from datetime import datetime

from drf_yasg.utils import swagger_auto_schema

#from .models import History
from .serializers import locateurSerializer, LoginSerializer

# Create your views here.

def home(request):
    return render(request, "django_app/home.html")

def users(request):
    if request.method == "POST":
        label = request.POST.get("input")
        categorieId = request.POST.get("categorieid")
        return render(request, "django_app/users.html")

    else:
        return render(request, "django_app/users.html")


def register(request):
    if request.method == "GET":
        return render(request, "django_app/register.html", {"status": False, "towns": ville.objects.all().values('name')})
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        gender = request.POST.get("gender")
        town = request.POST.get("town")
        profil = request.POST.get("profil")
        print(username + password + gender + town + profil)
        if (profil == "locataire"):
            user = User(username=username, password=make_password(password))
            user.save()
            locataire = Locataire(user.pk, gender=gender, town=town)
            locataire.save()
        if (profil == "locateur"):
            user = locateur(username=username, password=make_password(password), gender=gender, town=town)
            user.save()

        return render(request, "django_app/register.html", {"status": True})


@swagger_auto_schema(
    method="post", tags=["Authentication"], request_body=LoginSerializer
)
@api_view(["POST"])
def login(request):
    username = request.data["username"]
    password = request.data["password"]

    user = User.objects.filter(username=username)

    if user.exists():
        auth_success = check_password(password, user.first().password)

        if auth_success:
            token = Token.objects.filter(user=user.first())

            if token.exists():
                return Response(
                    {"token": "Token {}".format(token.first().key)},
                    status=status.HTTP_200_OK,
                )
            else:
                token = Token.objects.create(user=user.first())
                return Response(
                    {"token": "Token {}".format(token.key)}, status=status.HTTP_200_OK
                )
        else:
            return Response(
                {"message": "Mot de passe incorrect !"},
                status=status.HTTP_404_NOT_FOUND,
            )
    else:
        return Response(
            {"message": "L'utilisateur n'existe pas !"},
            status=status.HTTP_404_NOT_FOUND,
        )


@swagger_auto_schema(method="get", tags=["Authentication"])
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def logout(request):
    token_key = request.META["HTTP_AUTHORIZATION"].split(" ")[1]

    invalidated_token = Token.objects.filter(key=token_key).first()
    invalidated_token.delete()

    return Response(
        {"message": "Deconnexion effectuée avec succès !"}, status=status.HTTP_200_OK
    )

def statistics(request):
    return render(request, "django_app/statistics.html")


@swagger_auto_schema(method="get", tags=["Villes"])
@api_view(["GET"])
def towns(request):
    all_towns = ville.objects.all().values('name')
    return Response(
                    all_towns, status=status.HTTP_200_OK
                )


# class LocateurviewSet:
#     permission_classes = [IsAuthenticated]
    
#     token_key = request.META["HTTP_AUTHORIZATION"].split(" ")[1]
#     user = Token.objects.filter(key=token_key).first().user

#     def list(self,request):
#         locateurs = user.locateur_set.all()
#         locateur_serializer = locateurSerializer(locateurs , many=True)
