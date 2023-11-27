import random
import time
import os
import getpass
'''
Juego de adivinar numero:
    Menu:
        1) Iniciar Partida
            $Numero=random(0-9)
            "Introduce username":$Nombre
            -Cambio pantalla-
            "Elige un numero del 0 al 9"
                if $NumeroPlayer!=$Numero:
                    Has fallado, vuelve a intentar
                    $Intentos=$Intentos+1
                if $NumeroPlayer==$Numero:
                    Correcto el numero era $NumeroPlayer
            -END-
        2) Ver ranking
            Print($Posicion=>$Nombre=>$Intentos
        3) Salir

    Clases Partida,Menu
'''

class Menu():
    def __init__(self):
        opcion_elegida=None

    def mostar_menu():
        os.system ("clear")
        print("1) Iniciar partida")
        print("2) Ver ranking")
        print("3) Salir")
        Menu.seleccionar()


    def seleccionar():
        opcion_elegida=input()
        try:
                opcion_elegida=int(opcion_elegida)
                is_int=True
        except ValueError:
                is_int=False

        if is_int==False:
            print("Escriba solo el numero de las opciones de arriba")
            time.sleep(1)
            Menu.mostar_menu()

        match(opcion_elegida):
            case 1:
                Partida.start()
            case 2:
                Menu.mostrar_ranking()
            case 3:
                SystemExit
            case _:
                print("Por favor escoga una de las opciones del menu")
                time.sleep(1.25)
                Menu.mostar_menu()
    
    def mostrar_ranking():
        os.system("clear")
        print("De momento no hay nada")
        #TODO
        print("Pulse la tecla enter para volver al menu")
        getpass.getpass('')
        Menu.mostar_menu()

class Partida():
    def __init__(self):
        intentos=None
    def start():
        os.system ("clear")
        numerorandom=random.randint(0,9)
        numeroplayer=int(input("Escoge un numero del 0 al 9: "))
        intentos=1
        while numeroplayer!=numerorandom:
            if numeroplayer!=numerorandom:
                print("Te has equivocado")
                print("Este es tu intento nº", intentos)
                intentos=intentos+1
                time.sleep(0.5)
                os.system ("clear")
            numeroplayer=int(input("Escoge un numero del 0 al 9: "))
        print("Has acertado! Te ha tomado", intentos,"intentos")
        Partida.end()
    def end():
        restart=None
        restart=input("Quieres jugar denuevo (s/n): ")
        match(restart):
            case "s":
                Partida.start()
            case "n":
                Menu.mostar_menu()
                Menu.seleccionar()

if __name__=="__main__":
    Menu.mostar_menu()