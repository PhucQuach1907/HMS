from djongo import models


# Create your models here.
class MedicalRecord(models.Model):
    patient_id = models.PositiveIntegerField()
    doctor_id = models.PositiveIntegerField()
    appointment_id = models.PositiveIntegerField()
    details = models.TextField()
    prescription_id = models.PositiveIntegerField(null=True, blank=True)
    medical_supplies_id = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'medical_record'
