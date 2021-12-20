from django.db import models
from django.contrib.auth.models import User
# Create your models here. c72b9904-bbd6-45fd-91d1-1c32690501cc




class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.IntegerField(max_length=50)
    tenant = models.IntegerField(max_length=50)
    landlord = models.IntegerField(max_length=50)
    nbr_persons = models.IntegerField(max_length=50)
    in_date = models.DateTimeField(max_length=50)
    out_date =models.DateTimeField(max_length=50)
    total_price = models.FloatField(max_length=50)
    status = models.CharField(max_length=50)

class Utilisateur(models.Model):
    identifiant = models.AutoField(primary_key=True)
    first_name= models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mail_adresse = models.EmailField(max_length=50)
    birth_date = models.DateTimeField()
    gender = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)



class Chambre(models.Model):
    id = models.AutoField(primary_key=True)
    reservation = models.OneToOneField("Reservation",on_delete=models.CASCADE)
    town = models.DateTimeField()
    landlord = models.IntegerField()
    capacity = models.IntegerField()
    price = models.FloatField()


class locateur(Utilisateur):
    # id = models.AutoField(primary_key=True)
    chambre = models.ForeignKey("Chambre",on_delete=models.CASCADE)
    benefits = models.FloatField()


class locataire(Utilisateur):
    # id = models.AutoField(primary_key=True)
    reservation = models.ForeignKey("Reservation",on_delete=models.CASCADE)
    balance = models.FloatField()


class ville (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.FloatField()
    #chambre = models.ForeignKey("Chambre",on_delete=models.CASCADE)

   


   