from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=40)
    log_date = models.DateTimeField("date logged")

class Patient(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    log_date = models.DateTimeField("date logged")
