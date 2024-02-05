from django.shortcuts import render
from passwords.models import Datos
from django.http import JsonResponse
import json

# Create your views here.

def ShowPass(self):
    username_busqueda=input('Cual es tu username: ')
    show=Datos.objects(f"SELECT password FROM password_datos WHERE username={username_busqueda}")
    return(show)

def new(request,self=Datos):
    self.username=json.loads(request.POST.get('username'))
    self.password=input("Password: ")
    add=Datos.objects(f"INSERT INTO password_datos('username','password') VALUES ('{self.password}','{self.username}')")
    response={
        add
    }
    return JsonResponse(response)

def change(self):
    username_busqueda=input('Cual es tu username: ')
    ch=Datos.objects(f"UPDATE password_datos SET {self.password} WHERE {username_busqueda}")
    response={
        ch
    }
    return JsonResponse(response)

def delete(self):
    username_busqueda=input('Cual es tu username: ')
    dele=Datos.objects(f"DELETE password AND username FROM password_datos WHERE username={username_busqueda}")
    response={
        dele
    }
    return JsonResponse(response)

def to_json(request):
    response={
        "response": "working"
    }
    return JsonResponse(response)