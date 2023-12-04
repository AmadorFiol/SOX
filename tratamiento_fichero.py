class Tratamiento_fichero():

    def __init__(self, nombre_fichero):
        self.nombre_fichero=nombre_fichero

    def lectura():
        f=open(self.nombre_fichero,"r")
        print(f.read())
        f.close

    def escritura():
        f=open(self.nombre_fichero,"a")
        f.write("Hola")
        f.write("\n")
        f.close

if __name__=="__main__":
    f=Tratamiento_fichero("ranking.txt")
    f.escritura
    f.lectura