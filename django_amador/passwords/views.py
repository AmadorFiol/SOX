from django.shortcuts import render
from passwords.models import Datos
from django.http import HttpResponse, JsonResponse
from django.core import serializers


# Create your views here.

def show(self):
    response=serializers.serialize('json',Datos.objects.all())
    return JsonResponse(response, safe=False)

def new(request):
    username= request.GET.get("username", "")
    password= request.GET.get("password", "")
    Datos.objects.create(username=username, password=password)
    response={
        "response": "New user created"
    }
    return JsonResponse(response)

def change(request):
    username=request.GET.get("username","")
    new_password=request.GET.get("new_password","")
    Datos.objects.filter(username=username).update(password=new_password)
    response={
        "response": "Password changed succesfully"
    }
    return JsonResponse(response)

def delete(request):
    username=request.GET.get("username","")
    Datos.objects.filter(username=username).delete()
    response={
        "response": "The user have been deleted"
    }
    return JsonResponse(response)

def to_json(request):
    response={
        "response": "working"
    }
    return JsonResponse(response)