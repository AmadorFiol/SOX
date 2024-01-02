import random
import time
import os
import getpass

class Menu():
    def __init__(self):
        opcion_elegida=None
        username=None

    def mostar_menu():
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
                #Tratamiento_fichero.lectura(self=Tratamiento_fichero)
                Ranking.mostrar_ranking(self=Ranking)
            case 3:
                os.system("clear")
                Tratamiento_fichero.escritura(self=Tratamiento_fichero)
                SystemExit
            case _:
                print("Por favor escoga una de las opciones del menu")
                time.sleep(1.25)
                os.system("clear")
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
        numeroplayer=input("Escoge un numero del 0 al 9: ")
        try:
                numeroplayer=int(numeroplayer)
                is_int=True
        except ValueError:
                is_int=False

        if is_int==False:
            print("Inserte denuevo el nombre de usuario y reintente escribiendo un numero")
            time.sleep(1)
            Partida.insertar_username(self=Partida)
        self.intentos=1
        while numeroplayer!=numerorandom:
            if numeroplayer!=numerorandom:
                print("Te has equivocado")
                print("Este es tu intento nº", self.intentos)
                self.intentos=self.intentos+1
                time.sleep(1)
                os.system ("clear")
            numeroplayer=input("Escoge un numero del 0 al 9: ")
            try:
                numeroplayer=int(numeroplayer)
                is_int=True
            except ValueError:
                is_int=False
            if is_int==False:
                print("Inserte denuevo el nombre de usuario y reintente escribiendo un numero")
                time.sleep(1)
                Partida.insertar_username(self=Partida)
        print("\n Has acertado! Te ha tomado", self.intentos,"intentos")
        time.sleep(1)
        Ranking.entrar_ranking(self=Ranking)

    def end():
        restart=None
        restart=input("Quieres jugar denuevo (s/n): ")
        match(restart):
            case "s":
                Partida.start(self=Partida)
            case "n":
                Menu.mostar_menu()

class Ranking():
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
        self.ranker=['']
        for i in range (0,10):
            self.intentos_ranker.append(int(99))
            self.ranker.append('No hay datos')

    def mostrar_ranking(self):
        os.system("clear")
        #Mostrar valores del ranking
        print("Rank, Username, Intentos")
        for i in range(0,11):
            print(self.posiciones[i],self.ranker[i],self.intentos_ranker[i])
        print("Pulse la tecla enter para volver al menu")
        getpass.getpass('')
        os.system("clear")
        Menu.mostar_menu()
        
    def entrar_ranking(self):
        if Partida.intentos<self.intentos_ranker[10]:
            self.intentos_ranker[10]=Partida.intentos
            self.ranker[10]=Partida.username
            Ranking.actualizar_ranking(self=Ranking)
        else: Partida.end()

    def actualizar_ranking(self):
        #Cambiar el valor y posiciones del ranking
        i=int(10)
        while self.intentos_ranker[i]<self.intentos_ranker[i-1] and i!=int(0):
            self.intentos_ranker[0]=self.intentos_ranker[i-1]
            self.ranker[0]=self.ranker[i-1]
            self.intentos_ranker[i-1]=self.intentos_ranker[i]
            self.ranker[i-1]=self.ranker[i]
            self.intentos_ranker[i]=self.intentos_ranker[0]
            self.ranker[i]=self.ranker[0]
            i=i-1
        self.intentos_ranker[0]=''
        self.ranker[0]=''
        os.system("clear")
        print("Enorabuena has entrado al ranking, que le gustaria hacer?")
        Menu.mostar_menu()

class Tratamiento_fichero():

    def __init__(self, nombre_fichero):
        self.nombre_fichero=nombre_fichero

    def lectura(self):
        f=open(self.nombre_fichero,"r")
        print(f.read())
        f.close()

    def escritura(self):
        f=open(self.nombre_fichero,"a")
        f.write("Rank, Username, Intentos\n")
        for i in range(0,11):
            f.write(Ranking.posiciones[i])
            f.write(" ")
            f.write(Ranking.ranker[i])
            f.write(" ")
            f.write(str(Ranking.intentos_ranker[i]))
            f.write("\n")
        f.close()

if __name__=="__main__":
    os.system("clear")
    Ranking.ranking_default(self=Ranking)
    Tratamiento_fichero.__init__(self=Tratamiento_fichero,nombre_fichero="ranking.txt")
    Menu.mostar_menu()