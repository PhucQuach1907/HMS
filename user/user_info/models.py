import uuid
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('user_type', 'patient')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_doctor(self, username, password=None, **extra_fields):
        extra_fields.setdefault('user_type', 'doctor')

        return self.create_user(username, password, **extra_fields)

    def create_admin(self, username, password=None, **extra_fields):
        extra_fields.setdefault('user_type', 'admin')

        return self.create_user(username, password, **extra_fields)


class Fullname(models.Model):
    first_name = models.CharField(max_length=255)
    mid_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'user_fullname'


class Address(models.Model):
    noHouse = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        db_table = 'user_address'


class User(AbstractBaseUser):
    login_id = models.CharField(max_length=25, unique=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    fullname = models.OneToOneField(to=Fullname, on_delete=models.CASCADE)
    address = models.OneToOneField(to=Address, on_delete=models.CASCADE)
    gender = models.CharField(max_length=255)
    dob = models.DateField()
    phone_number = models.CharField(max_length=10)
    user_type = models.CharField(max_length=255)

    objects = UserManager()

    USERNAME_FIELD = 'login_id'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'user_info'

    def save(self, *args, **kwargs):
        if not self.login_id:
            self.login_id = self.generate_login_id()
        super(User, self).save(*args, **kwargs)

    def generate_login_id(self):
        prefix = self.user_type[:3].upper()
        unique_id = uuid.uuid4().hex[:8].upper()
        return f"{prefix}{unique_id}"

    def __str__(self):
        return self.username
