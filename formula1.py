class Coche():
    def __init__(self,marca,velocidad):
        self.marca=marca
        velocidad=None
        self.velocidad=velocidad

class Carrera():
    def __init__(self,coches):
        coches=[]
        self.coches=coches        

    def empieza_carrera(coches):
        print("Empieza la carrera, los competidores de hoy son")
        for i in coches:
            print(Coche.marca)

    def muestra_resultado(coches):
        pass
if __name__ == '__main__':
    c1=Coche("Mercedes","120hp")
    c2=Coche("Ferrari","200hp")
    c3=Coche("Aston Martin","480hp")
    coches=[c1, c2, c3]
    ''' lineas pruebas'''
    print(c1,c2,c3)
    '''fin lineas pruebas'''
    c = Carrera(coches)
    c.empieza_carrera()
    c.muestra_resultado()