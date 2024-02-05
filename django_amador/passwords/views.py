from django.shortcuts import render
from passwords.models import Datos
from django.http import HttpResponse, JsonResponse
import json

# Create your views here.

def show(self):
    Datos.objects.serialize(username='Username: ', password='Password: ')

def new(request,self=Datos):
    Datos.objects.create(username='Username: ', password='New password: ')
    return HttpResponse("New user created")

def change(self):
    Datos.objects.filter(username='Username: ').update(password='New password: ')
    return HttpResponse("Password changed succesfully")

def delete(self):
    Datos.objects.filter(username='Username: ').delete()
    return HttpResponse("The user have been deleted")

def to_json(request):
    response={
        "response": "working"
    }
    return JsonResponse(response)