from django.shortcuts import render
from passwords.models import Datos
# Create your views here.

def ShowPass(self):
    show=Datos.objects(f"SELECT password FROM password_datos WHERE username={self.username}")

def new(self):
    self.usuario=input("Username: ")
    self.password=input("Password: ")
    add=Datos.objects(f"INSERT INTO password_datos('username','password') VALUES ('{self.password}','{self.username}')")

def change(self):
    ch=Datos.objects(f"UPDATE password_datos SET {self.password} WHERE {self.username}")

def delete(self):
    dele=Datos.objects(f"DELETE {self.password} FROM password_datos WHERE {self.username}")