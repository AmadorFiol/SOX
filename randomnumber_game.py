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
            Print($Posicion=>$Nombre=>$Intentos)
        3) Salir

    Clases Partida,Menu
'''

class Menu():
    def __init__(self):
        opcion_elegida=None
        username=None

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
                Partida.insertar_username()
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
        ranker=None
        intentos_ranker=None
        posicion=int()
        Partida.username=ranker
        Partida.intentos=intentos_ranker
        '''
        Como funcionara el ranking:
        Las posiciones serian del TOP 10, TOP 25 o TOP 50 (de momento vamos a hacer top10 por facilidad)
        Mostrar posicion    Nombre ranker    Cantidad intentos ranker

        Como se deciden las posiciones?
        Si intentos<intentos_ranker[10] cambiar datos de intentos_ranker[10] por intentos y cambiar ranker[10] por username
        
        Si intentos_ranker[10]<intentos_ranker[9] pasar los datos de intentos_ranker[9]=>intentos_ranker[0] y ranker[9]=>ranker[0]
        intentos_ranker[10]=>intentos_ranker[9] y ranker[10]=>ranker[9], intentos_ranking[0]=>intentos_ranking[10] y ranker[0]=>ranker[10]
        ademas de repetir iteracion para cada ranking superior
        
        '''
        

        print("Pulse la tecla enter para volver al menu")
        getpass.getpass('')
        Menu.mostar_menu()

class Partida():
    def __init__(self):
        intentos=None
        self.intentos=intentos
        username=None
        self.username=username

    def insertar_username():
        os.system("clear")
        self.username=input("Inserte un nombre de usuario: ")
        Partida.start()

    def start():
        os.system ("clear")
        numerorandom=random.randint(0,9)
        numeroplayer=int(input("Escoge un numero del 0 al 9: "))
        self.intentos=1
        while numeroplayer!=numerorandom:
            if numeroplayer!=numerorandom:
                print("Te has equivocado")
                print("Este es tu intento nº", self.intentos)
                self.intentos=self.intentos+1
                time.sleep(0.5)
                os.system ("clear")
            numeroplayer=int(input("Escoge un numero del 0 al 9: "))
        print("Has acertado! Te ha tomado", self.intentos,"intentos")
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

class Tratamiento_fichero():

    def __init__(self, nombre_fichero):
        self.nombre_fichero=nombre_fichero

    def lectura():
        f=open(self.nombre_fichero,"r")
        print(f.read())
        f.close

    def escritura():
        f=open(self.nombre_fichero,"a")
        f.write('''Texto ranking''')
        f.write("\n")
        f.close

if __name__=="__main__":
    Menu.mostar_menu()