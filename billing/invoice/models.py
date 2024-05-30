from djongo import models


# Create your models here.
class Invoice(models.Model):
    patient_id = models.PositiveIntegerField()
    appointment_id = models.PositiveIntegerField()
    price = models.PositiveBigIntegerField()
    status = models.CharField(max_length=255)

    class Meta:
        db_table = 'invoice'
