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
                Partida.insertar_username(self=Partida)
            case 2:
                Ranking.ranking_default(self=Ranking)
            case 3:
                os.system("clear")
                SystemExit
            case _:
                print("Por favor escoga una de las opciones del menu")
                time.sleep(1.25)
                Menu.mostar_menu()

class Partida():
    def __init__(self):
        intentos=None
        self.intentos=intentos
        username=None
        self.username=username

    def insertar_username(self):
        os.system("clear")
        self.username=input("Inserte un nombre de usuario: ")
        Partida.start(self)

    def start(self):
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
        print("\n Has acertado! Te ha tomado", self.intentos,"intentos")
        Partida.end()
    def end():
        restart=None
        restart=input("Quieres jugar denuevo (s/n): ")
        match(restart):
            case "s":
                Partida.start(self=Partida)
            case "n":
                Menu.mostar_menu()

class Ranking():
    '''
        TODO:
        Como funcionara el ranking:
        Las posiciones serian del TOP 10, TOP 25 o TOP 50 (de momento vamos a hacer top10 por facilidad)
        Y hay que mostrar lo siguiente: posicion    Nombre ranker    Cantidad intentos ranker

        Como se decide si alguien entra al ranking
        Si intentos<intentos_ranker[10] cambiar datos de intentos_ranker[10] por intentos y cambiar ranker[10] por username
        
        Como se deciden las posiciones?
        Si intentos_ranker[10]<intentos_ranker[9] pasar los datos de intentos_ranker[9]=>intentos_ranker[0] y ranker[9]=>ranker[0]
        intentos_ranker[10]=>intentos_ranker[9] y ranker[10]=>ranker[9], intentos_ranking[0]=>intentos_ranking[10] y ranker[0]=>ranker[10]
        ademas de repetir iteracion para cada ranking superior
    '''

    def __init__(self):
        posiciones=None
        self.posiciones=posiciones
        intentos_ranker=None
        self.intentos_ranker=intentos_ranker
        ranker=None
        self.ranker=ranker
    
    def ranking_default(self):
        self.posiciones=['',' 1º',' 2º',' 3º',' 4º',' 5º',' 6º',' 7º',' 8º',' 9º','10º']
        self.intentos_ranker=['']
        self.ranker=['',]
        for i in range (0,10):
            self.intentos_ranker.append('Sin datos')
            self.ranker.append('')
        Ranking.mostrar_ranking(self=Ranking)

    def mostrar_ranking(self):
        os.system("clear")
        #Mostrar valores del ranking
        print("Rank, Username, Intentos")
        for i in range(0,11):
            print(self.posiciones[i],self.intentos_ranker[i],self.ranker[i])
        print("Pulse la tecla enter para volver al menu")
        irmenu=getpass.getpass('')
        Menu.mostar_menu()

    def actualizar_ranking(self):
        #Cambiar el valor y posiciones del ranking
        if Partida.intentos<self.intentos_ranker[11]:
            pass

class Tratamiento_fichero():

    def __init__(self, nombre_fichero):
        self.nombre_fichero=nombre_fichero

    def lectura(self):
        f=open(self.nombre_fichero,"r")
        print(f.read())
        f.close()

    def escritura(self):
        f=open(self.nombre_fichero,"a")
        f.write("Ranking mensual ('''mm/AAAA''')")
        f.write("\n")
        f.close()

if __name__=="__main__":
    Menu.mostar_menu()