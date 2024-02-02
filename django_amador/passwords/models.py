from django.db import models

# Create your models here.
class Datos(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(blank=True)
    password=models.CharField()