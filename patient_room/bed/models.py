from django.db import models

from room.models import Room


# Create your models here.
class Bed(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    bed_number = models.IntegerField()
    status = models.CharField(max_length=255)
    patient_id = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'patient_bed'
