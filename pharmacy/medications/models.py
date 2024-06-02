from djongo import models


# Create your models here.
class Medication(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.BigIntegerField()

    class Meta:
        db_table = 'medications'
