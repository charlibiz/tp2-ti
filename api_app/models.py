from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class Local(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    capacity = models.IntegerField()

class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("User",on_delete=models.CASCADE)
    local_id = models.ForeignKey("Local",on_delete=models.CASCADE)
    time = models.DateTimeField()