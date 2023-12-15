#Extra: realizar el programa para una cantidad indefinida de coches
import random
import pdb

class Coche():
    def __init__(self, nombre, caballos):
        self.nombre=nombre
        self.caballos=caballos

    def to_string(self):
        return "{marca:", self.nombre, "caballos: ", self.caballos, "}"
    '''Inicio extras'''
    def quienes_participante
    '''Fin extras'''
class Carrera():
    def __init__(self, coches):
        self.coches=coches
        self.resultado=[]

    def mostrar_parrilla_de_salida(self):
        aux = 1
        for coche in self.coches:
            print("El coche ", coche.nombre, "sale en [",aux,"] posicion")
            aux = aux+1
    
    def empieza_carrera(self):
        print("La carrera a empezado...")

    def finaliza_carrera(self):
        #Escoger resultados con random
        for i in self.resultado:
            posicion=random.randint(1,3)
            if self.resultado[posicion]!='':
                self.resultado[posicion]=self.coches[i]
            else:
                i=i-1

    def muestra_resultado(self):
        #Mostrar el ranking
        for coches in self.coches:
            print(coches.to_string())
    
    '''Inicio extras'''
    def cuantos_coches(self):
        cantidad_coches=input("cuantos coches van a participar en la carrera de hoy?")

    '''Fin extras'''
if __name__ == '__main__':
    c1 = Coche("Mercedes", "120hp")
    c2 = Coche("Ferrari", "200hp")
    c3 = Coche("Mustang", "200hp")
    coches=[c1, c2, c3]

    c = Carrera(coches)
    c.mostrar_parrilla_de_salida()
    c.empieza_carrera()
    c.finaliza_carrera()
    c.muestra_resultado()