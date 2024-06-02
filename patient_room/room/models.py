from djongo import models


# Create your models here.
class Room(models.Model):
    room_number = models.PositiveIntegerField()

    class Meta:
        db_table = 'patient_room'

