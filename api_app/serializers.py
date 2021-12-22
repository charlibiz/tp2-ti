from rest_framework import fields, serializers

from .models import User, Local, Reservation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name")

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ("id", "title", "capacity")

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ("id", "user_id", "local_id", "time")