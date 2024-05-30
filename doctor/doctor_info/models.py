from django.db import models


# Create your models here.
class Doctor(models.Model):
    user_id = models.PositiveIntegerField()
    specialty = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)

    class Meta:
        db_table = 'doctor'
