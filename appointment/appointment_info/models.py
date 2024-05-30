from djongo import models


# Create your models here.
class Appointment(models.Model):
    patient_id = models.PositiveIntegerField()
    doctor_id = models.PositiveIntegerField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=255)

    class Meta:
        db_table = 'appointment'
