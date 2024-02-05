from django.shortcuts import render
from passwords.models import Datos
# Create your views here.

def ShowPass(self):
    username_busqueda=input('Cual es tu username: ')
    show=Datos.objects(f"SELECT password FROM password_datos WHERE username={username_busqueda}")
    return(show)

def new(self):
    self.usuario=input("Username: ")
    self.password=input("Password: ")
    add=Datos.objects(f"INSERT INTO password_datos('username','password') VALUES ('{self.password}','{self.username}')")
    return(add)

def change(self):
    username_busqueda=input('Cual es tu username: ')
    ch=Datos.objects(f"UPDATE password_datos SET {self.password} WHERE {username_busqueda}")
    return(ch)

def delete(self):
    username_busqueda=input('Cual es tu username: ')
    dele=Datos.objects(f"DELETE password AND username FROM password_datos WHERE username={username_busqueda}")
    return(dele)