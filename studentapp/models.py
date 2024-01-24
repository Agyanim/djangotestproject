from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=255)
    age=models.IntegerField()
    phone=models.CharField(max_length=100)
    Address=models.CharField(max_length=255)
    
    
class Users(models.Model):
    userName=models.CharField(max_length=255)
    password=models.CharField(max_length=255)