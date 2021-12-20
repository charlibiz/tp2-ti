from django.db import models
from django.contrib.auth.models import User
# Create your models here. c72b9904-bbd6-45fd-91d1-1c32690501cc




class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.IntegerField()
    tenant = models.IntegerField()
    landlord = models.IntegerField()
    nbr_persons = models.IntegerField()
    in_date = models.DateField()
    out_date =models.DateField()
    total_price = models.FloatField()
    status = models.CharField(max_length=50)

# class Utilisateur(models.Model):
#     identifiant = models.AutoField(primary_key=True)
#     first_name= models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     mail_adresse = models.EmailField(max_length=50)
#     birth_date = models.DateTimeField()
#     gender = models.CharField(max_length=50)
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)



class Chambre(models.Model):
    id = models.AutoField(primary_key=True)
    reservation = models.OneToOneField("Reservation",on_delete=models.CASCADE)
    town = models.CharField(max_length=50)
    landlord = models.IntegerField()
    capacity = models.IntegerField()
    price = models.FloatField()


class locateur(User):
    chambre = models.ForeignKey("Chambre",on_delete=models.CASCADE)
    benefits = models.FloatField()
    birth_date = models.DateField()
    gender = models.CharField(max_length=50)


class locataire(User):
    reservation = models.ForeignKey("Reservation",on_delete=models.CASCADE)
    balance = models.FloatField()
    birth_date = models.DateField()
    gender = models.CharField(max_length=50)


class ville (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.FloatField()
    #chambre = models.ForeignKey("Chambre",on_delete=models.CASCADE)

   


   