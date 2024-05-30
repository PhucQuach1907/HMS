from django.db import models


# Create your models here.
class Patient(models.Model):
    user_id = models.PositiveIntegerField()

    class Meta:
        db_table = 'patient'
