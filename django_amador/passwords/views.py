from django.shortcuts import render
from passwords.models import Datos
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import pdb,json


# Create your views here.

def show(self):
    response=serializers.serialize('json',Datos.objects.all())
    return JsonResponse(response, safe=False)

@csrf_exempt
def new(request):
    if request.method=='Post':
        pdb.set_trace
        my_json=json.loads(request.body.decode("UTF8").replace("*","*"))
        username=my_json['username']
        password=my_json['password']
        if not username or not password:
            response="Please, enter a username and a password"
            HttpResponseBadRequest(response)
        else:
            all_user=Datos.objects.values('username') #Insertamos una lista de todos los usernames 
            for username in all_user:   #Revisamos si el username esta en la lista de todos los usernames
                if all_user==username:  #Creamos boleano para controlar si el usuario existe
                    exists=True
                else:
                    exists=False
            if exists==True: #Si el usuario existe saltara un error debido a que en otras funciones se filtrara por el username asi que no puede haber mas de uno
                response="This username is already in use, please use another one"
                HttpResponseBadRequest(response)
            else:
                entry=Datos.objects.create(username=username, password=password)
                entry.save()
                response={"response": "New user created succesfully"}
                return JsonResponse(response)
    else:
        response="Be sure the method is POST"
        HttpResponseBadRequest(response)

@csrf_exempt
def change(request):
    if request.method=='Post':
        pdb.set_trace
        my_json=json.loads(request.body.decode("UTF8").replace("*","*"))
        username= my_json['username']
        new_password=my_json['password']
        if not username or not new_password:
            entry=Datos.objects.filter(username=username)
            entry.update(password=new_password)
            response={"response": "Password changed succesfully"}
            return JsonResponse(response)
        else:
            response="Please, enter a username and a new password"
            HttpResponseBadRequest(response)
    else:
        response="Be sure the method is POST"
        HttpResponseBadRequest(response)

'''
TODO: Terminar control de errores de la existencia del usuario
'''
@csrf_exempt
def delete(request):
    if request.method=='POST':
        pdb.set_trace
        my_json=json.loads(request.body.decode("UTF8").replace("*","*"))
        username=my_json['username']
        if not username:
            response="Please, enter a username"
            HttpResponseBadRequest(response)
        else:
            all_user=[]
            for i in Datos.objects.values('username'): #Insertamos una lista de todos los usernames
                all_user+=[Datos.objects.values('username')]
            for i in all_user:   #Revisamos si el username esta en la lista de todos los usernames
                if all_user==username:  #Creamos un boleano para controlar si el usuario existe
                    exists=True
                elif all_user==username:
                    exists=False
            print(exists)
            if exists==True:
                entry=Datos.objects.filter(username=username)
                entry.delete()
                response={"response": "The user have been deleted"}
                return HttpResponse(response)
            elif exists==False:
                response="This user doesn't exists"
                HttpResponseBadRequest(response)
    else:
        response="Be sure the method is POST"
        HttpResponseBadRequest(response)

def testing(request):
    response={"response": "working"}
    return JsonResponse(response)