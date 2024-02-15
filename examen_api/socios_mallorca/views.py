from django.shortcuts import render
from socios_mallorca.models import Socio
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def options(request):
    response="Las paginas disponibles son las siguiente: introducir,modificar,mostrar"
    return HttpResponse(response)

@csrf_exempt
def introducir(request):
    if request.method=='POST':
        my_json=json.loads(request.body.decode("UTF8").replace("*","*"))
        password=my_json['password']
        dni=my_json['dni']
        entry=Socio.objects.create(dni=dni, password=password)
        entry.save()
        response={"response": "New user created succesfully"}
        return JsonResponse(response)
    else:
        response="Comprueba que has insertado los datos via POST"
        return HttpResponse(response)
    
def show(request):
    response=serializers.serialize('json',Socio.objects.all())
    return JsonResponse(response, safe=False)

@csrf_exempt
def modificar(request):
    if request.method=='POST':
        my_json=json.loads(request.body.decode("UTF8").replace("*","*"))
        dni=my_json['dni']
        new_password=my_json['password']
        entry=Socio.objects.filter(dni=dni)
        entry.update(password=new_password)
        response={"response": "Password changed succesfully"}
        return JsonResponse(response)
    else:
        response="Comprueba que has insertado los datos via POST"
        return HttpResponse(response)