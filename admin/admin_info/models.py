from django.db import models


# Create your models here.
class Admin(models.Model):
    user_id = models.PositiveIntegerField()

    class Meta:
        db_table = 'admin_info'
