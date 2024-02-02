from django.shortcuts import render
import os,time
# Create your views here.
def menu():
    verificado=False
    while verificado==False:
        print("1. Establecer contraseña")
        print("2. Cambiar contraseña")
        print("3. Borrar contraseña")
        print("4. Salir")
        eleccion=input("Eliga una de las opciones: ")            
        match(eleccion):
            case "1":
                verificado=True
                .nueva_contrasena()
            case "2":
                verificado=True
                .cambiar_crontrasena()
            case "3":
                verificado=True
                .eliminar_crontrasena()
            case "4":
                SystemExit
            case _:
                print("Asegurese que ha escrito solo el numero de una de las opciones de arriba")
                time.sleep(2)
                os.system("clear")

def nueva_contrasena(self):
    verificado=False
    while verificado==False:
        self.password=input("Inserte una contraseña: ")
        resguardo=input("Escribela de nuevo porfavor: ")
        if self.password==resguardo:
            print("Tu contraseña a sido establecida")
            verificado=True
        else:
            print("Las contraseñas no coinciden, intente denuevo")
            time.sleep(2)
            os.system("Clear")
    print("Va a ser devuelto al menu")
    time.sleep(2)
    .menu()

def cambiar_crontrasena(self):
    changed_password=input("Inserte la nueva contraseña: ")
    if changed_password==self.password:
        print("Esa es la contraseña actualmente establecida")
    else:
        self.password=changed_password
        print("Tu contraseña a sido cambiada con exito")
    print("Va a ser devuelto al menu")
    time.sleep(2)
    .menu()


def eliminar_crontrasena():
    print("Aun en proceso")
    print("Va a ser devuelto al menu")
    time.sleep(2)
    .menu()

def index(self):
    self.usuario=input("Username: ")
    self.password=input("Password: ")
    
def ShowPass():
    passw=Datos.objects("Select password From ")