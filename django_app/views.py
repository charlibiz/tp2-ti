from django.shortcuts import render, redirect
from django.conf.urls import url
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from django.utils.timezone import get_current_timezone
from datetime import datetime

from drf_yasg.utils import swagger_auto_schema

#from .models import History
from .serializers import locateurSerializer, ResultSerializer, LoginSerializer

# Create your views here.
user_key = "721aebe0-0232-4326-9e21-1967ad98fff1"

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
    if request.method == "POST":
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        address = request.POST.get("address")
        city = request.POST.get("city")
        phone = request.POST.get("phone")
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        password = request.POST.get("password")
        login = request.POST.get("login")

        user = {
            "id": "",
            "statut": "1",
            "employee": "0",
            "gender": gender,
            "email": email,
            "address": address,
            "town": city,
            "user_mobile": phone,
            "login": login,
            "country_code": "CA",
            "lastname": lastName,
            "firstname": firstName,
            "date_creation": "today",
            "note_private": password
            }
        req = 'requests.post("http://34.95.8.244/api/index.php/users?DOLAPIKEY="+ dolapikey, user)'
        if req.status_code == 200:
            return render(request, "django_app/register.html", {"success":1, "id":req.json()})
        else: 
            return render(request, "django_app/register.html", {"success":0})
    return render(request, "django_app/register.html")




def register(request):
    if request.method == "GET":
        return render(request, "django_app/register.html", {"status": False})
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User(username=username, password=make_password(password))
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



# class LocateurviewSet:
#     permission_classes = [IsAuthenticated]
    
#     token_key = request.META["HTTP_AUTHORIZATION"].split(" ")[1]
#     user = Token.objects.filter(key=token_key).first().user

#     def list(self,request):
#         locateurs = user.locateur_set.all()
#         locateur_serializer = locateurSerializer(locateurs , many=True)
