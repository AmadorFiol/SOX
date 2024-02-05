from django.db import models
import os,time

# Create your models here.
class Datos(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)