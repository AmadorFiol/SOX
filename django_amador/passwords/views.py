from django.shortcuts import render
from passwords.models import Datos
# Create your views here.

def ShowPass(self):
    show=Datos.objects(f"SELECT {self.password} FROM ")

def new(self):
    self.usuario=input("Username: ")
    self.password=input("Password: ")

def change(self):
    ch=Datos.objects(f"UPDATE {{{'''TODO tabla'''}}} SET {self.password} WHERE {self.username}")

def delete(self):
    dele=Datos.objects(f"DELETE {self.password} FROM {{{'''TODO tabla'''}}} WHERE {self.username}")