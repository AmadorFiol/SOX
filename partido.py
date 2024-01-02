import random
import time
class Equipos():
    def __init__(jugadores,nombre,self):
        self.jugadores = []
        self.nombre = nombre
        self.esgol = 0

        def ocasion_gol():
            self.esgol= random.randint(0,1)
            if self.esgol==1:
                return 1
            elif self.esgol==1:
                return 0
        
class Partido():
    def __init__(E1,E2,ocasiones,self):
        self.goles1 = 0
        self.goles2 = 0
        self.forwhogol = 0
        self.E1=E1
        self.E2=E2
        self.ocasiones=ocasiones
    
    def marcador(self):
        print(self.goles1,":",self.goles2)

    def jugar_partido(self):
        for i in range(self.ocasiones):
            self.forwhogol = random.randint(1,2)
        #print(forwhogol) #Linea de pruebas
            if self.forwhogol==1:
                print("E1 tiene la oportunidad para hacer un gol y...")
                esgol = random.randint(0,1)
                #print(esgol) #Linea de pruebas
                self.E1.ocasion_gol()
            elif self.forwhogol==2:
                print("E2 tiene tiene la oportunidad para hacer un gol y...")
                self.E2.ocasion_gol()

if __name__=="__main__":
    equipo1=Equipos([P1,AA,AB,AC,AD],"Equipo1")
    equipo2=Equipos([P2,BA,BB,BC,BD],"Equipo2")
    partido=Partido(equipo1,equipo2,10)
    partido.jugar_partido