from djongo import models

from medications.models import Medication


# Create your models here.
class Prescription(models.Model):
    doctor_id = models.PositiveBigIntegerField()
    medication_id = models.ManyToManyField(Medication)
    dosage = models.CharField(max_length=255)
    frequency = models.CharField(max_length=255)

    class Meta:
        db_table = 'prescription'
