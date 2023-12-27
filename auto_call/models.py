from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Patient(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    emergancy = models.BooleanField(default= False)
    log_date = models.DateTimeField("date logged")


    
