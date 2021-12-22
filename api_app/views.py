from rest_framework.response import Response
from rest_framework import status, viewsets

from datetime import datetime

from drf_yasg.utils import swagger_auto_schema

from .models import User, Local, Reservation
from .serializers import UserSerializer, LocalSerializer, ReservationSerializer


class UserViewSet(viewsets.ViewSet):
    @swagger_auto_schema(tags=["User"], responses={200: UserSerializer(many=True)})
    def list(self, request):
        users_list = User.objects.all()
        users_serializer = UserSerializer(users_list, many=True)
        return Response(
            {"users": users_serializer.data},
            status=status.HTTP_200_OK,
            )

    @swagger_auto_schema(tags=["User"], request_body=UserSerializer)
    def create(self, request):
        name = request.data["name"]
        user = User(name=name)
        user.save()
        users_list = User.objects.all()
        users_serializer = UserSerializer(users_list, many=True)
        return Response(
            {"users": users_serializer.data},
            status=status.HTTP_200_OK
            )

    @swagger_auto_schema(tags=["User"])
    def destroy(self, request, pk):
        user = User.objects.filter(id=pk).first()
        user.delete()
        users_list = User.objects.all()
        users_serializer = UserSerializer(users_list, many=True)
        return Response(
            {"users": users_serializer.data},
            status=status.HTTP_200_OK
            )


class LocalViewSet(viewsets.ViewSet):
    @swagger_auto_schema(tags=["Local"], responses={200: LocalSerializer(many=True)})
    def list(self, request):
        locaux_list = Local.objects.all()
        locaux_serializer = LocalSerializer(locaux_list, many=True)
        return Response(
            {"locaux": locaux_serializer.data},
            status=status.HTTP_200_OK,
            )

    @swagger_auto_schema(tags=["Local"], request_body=LocalSerializer)
    def create(self, request):
        title = request.data["title"]
        capacity = request.data["capacity"]
        local = Local(title=title, capacity=capacity)
        local.save()
        locaux_list = Local.objects.all()
        locaux_serializer = LocalSerializer(locaux_list, many=True)
        return Response(
            {"locaux": locaux_serializer.data},
            status=status.HTTP_200_OK,
            )

    @swagger_auto_schema(tags=["Local"])
    def destroy(self, request, pk):
        local = Local.objects.filter(id=pk).first()
        local.delete()
        locaux_list = Local.objects.all()
        locaux_serializer = LocalSerializer(locaux_list, many=True)
        return Response(
            {"locaux": locaux_serializer.data},
            status=status.HTTP_200_OK,
            )


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
        local = Local.objects.filter(id=local_id).first()
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
