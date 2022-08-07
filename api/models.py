from django.db import models


class Gender(models.TextChoices):
    Male = 'male'
    Female = 'female'

# Create your models here.


class Auth(models.Model):
   authID = models.AutoField(primary_key=True)
   username = models.CharField(max_length=20)
   password = models.CharField(max_length=20)

class User(models.Model):
    userID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    gender = models.CharField(choices=Gender.choices, max_length=150)
    address = models.CharField(max_length=150)
    image = models.ImageField(upload_to="users/",blank=True)


class Record(models.Model):
    recordID = models.AutoField(primary_key=True)
    userID = models.ForeignKey("User", on_delete=models.CASCADE)
    disease = models.CharField(max_length=100)
    diagnosis = models.CharField(max_length=500)
    prescription = models.JSONField()
    date = models.DateField(auto_now=True)
    payment = models.BigIntegerField()
