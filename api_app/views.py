from rest_framework.response import Response
from rest_framework import status, viewsets

from datetime import datetime

from drf_yasg.utils import swagger_auto_schema

from ui_app.models import  Chambre, Reservation
from django.contrib.auth.models import User
from ui_app.models import ville, Locateur, Locataire
from .serializers import UserSerializer, RoomSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token



@swagger_auto_schema(method="get", tags=["Utilisateur"])
@swagger_auto_schema(method="put", tags=["Utilisateur"])
@api_view(["GET", "PUT"])
def user(request):
    token_key = request.META["HTTP_AUTHORIZATION"].split(" ")[1]
    id = Token.objects.filter(key=token_key).first().user_id
    user = User.objects.filter(id=id)
    if (Locataire.objects.filter(user_id=id)):
        profil = Locataire.objects.filter(user_id=id).profil
    if (Locateur.objects.filter(user_id=id)):
        profil = Locateur.objects.filter(user_id=id).profil
    return Response(
                    user, profil, status=status.HTTP_200_OK
                )



@swagger_auto_schema(method="get", tags=["Rooms"])
@api_view(["GET"])
def rooms(request):
    rooms_list = Chambre.objects.all()
    return Response(
        {"rooms": rooms_list.values()},
        status=status.HTTP_200_OK,
        )

@swagger_auto_schema(tags=["Room"], request_body=RoomSerializer)
def room(self, request):
    if request.method == "GET":
        room_id = request.data["room_id"]
        room = Chambre.objects.filter(id=room_id).first()
        return Response(
            {"room": room.values()},
            status=status.HTTP_200_OK,
            )
    if request.method == "POST":
        town = request.data["town"]
        capacity = request.data["capacity"]
        price = request.data["price"]
        landlord_id = request.data["landlord_id"]
        landlord = Locateur.objects.filter(id=landlord_id).first()
        room = Chambre(town=town, capacity=capacity, price=price, landlord=landlord)
        room.save()
        rooms_list = Chambre.objects.all()
        return Response(
        {"rooms": rooms_list.values()},
        status=status.HTTP_200_OK,
        )
    if request.method == "DELETE":
        rooms_list = Chambre.objects.all()
        return Response(
        {"rooms": rooms_list.values()},
        status=status.HTTP_200_OK,
        )

    @swagger_auto_schema(tags=["Room"])
    def destroy(self, request, pk):
        room = Chambre.objects.filter(id=pk).first()
        room.delete()
        rooms_list = Chambre.objects.all()
        rooms_serializer = RoomSerializer(rooms_list, many=True)
        return Response(
            {"rooms": rooms_serializer.data},
            status=status.HTTP_200_OK,
            )

"""
class ReservationViewSet(viewsets.ViewSet):
    @swagger_auto_schema(
        tags=["Reservation"], responses={200: ReservationSerializer(many=True)}
    )
    def list(self, request):
        reservations_list = Reservation.objects.all()
        reservations_serializer = ReservationSerializer(reservations_list, many=True)
        return Response(
            {"reservations": reservations_serializer.data},
            status=status.HTTP_200_OK,
            )

    @swagger_auto_schema(tags=["Reservation"], request_body=ReservationSerializer)
    def create(self, request):
        user_id = request.data["user_id"]
        user = User.objects.filter(id=user_id).first()
        local_id = request.data["local_id"]
        local = Room.objects.filter(id=local_id).first()
        time = datetime.now()
        reservation = Reservation(user_id=user, local_id=local, time=time)
        reservation.save()
        reservations_list = Reservation.objects.all()
        reservations_serializer = ReservationSerializer(reservations_list, many=True)
        return Response(
            {"reservations": reservations_serializer.data},
            status=status.HTTP_200_OK,
            )

    @swagger_auto_schema(tags=["Reservation"])
    def destroy(self, request, pk):
        reservation = Reservation.objects.filter(id=pk).first()
        reservation.delete()
        reservations_list = Reservation.objects.all()
        reservations_serializer = ReservationSerializer(reservations_list, many=True)
        return Response(
            {"reservations": reservations_serializer.data},
            status=status.HTTP_200_OK,
            )

@swagger_auto_schema(method="get", tags=["Villes"])
@api_view(["GET"])
def towns(request):
    all_towns = ville.objects.all().values('name')
    return Response(
                    all_towns, status=status.HTTP_200_OK
                )

"""

