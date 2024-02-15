from django.db import models

# Create your models here.
class Socio(models.Model):
    numero_socio=models.AutoField(primary_key=True)
    password=models.CharField(max_length=30)
    dni=models.CharField(max_length=9)