import os
import time
import getpass
import random

class General():
    def __init__(self):
        self=General
    def menu_general():
        print("Elige que clase quiere utilizar")
        print("1. Cuenta")
        print("2. Cancion")
        print("3. Persona")
        print("4. Salir")
        General.input_menu_general()

    def input_menu_general():
        general_input=input("Escriba solo el numero: ")
        match(general_input):
            case "1":
                Cuenta.crear_cuenta()
            case "2":
                Cancion.canciones_default(Cancion)
            case "3":
                print("Aun en proceso")
                General.menu_general
                #Persona.menu_persona()
            case "4":
                SystemExit
            case _:
                print("Seleccione una de las opciones en pantalla")
                time.sleep(1.5)
                os.system("clear")
                General.menu_general()

class Cuenta():
    def __init__(self):
        dni=None
        saldo=None
        numero_cuenta=None
        self.dni=dni
        self.saldo=saldo
        self.numero_cuenta=numero_cuenta

    def crear_cuenta():
        print("Bienvenido al banco de Amador, ¿que desea hacer?")
        print("1. Realizar pruebas con cuenta predeterminada")
        print("2. Realizar pruebas con cuenta personalizada")
        print("3. Volver al menu principal")
        Cuenta.eleccion_cuenta(Cuenta)
    
    def eleccion_cuenta(self):
        self.dni=""
        self.numero_cuenta=""
        self.saldo=""
        pruebas_con=input("(Escriba el numero de la opcion deseada)")
        match(pruebas_con):
            case "1":
                Cuenta.datos_default(Cuenta)
            case "2":
                Cuenta.obtener_datos(Cuenta)
            case "3":
                General.menu_general()
            case _:
                print("Escoga una de las opciones proporcionadas")
                time.sleep(1.25)
                os.system("clear")
                Cuenta.crear_cuenta()
    
    def obtener_datos(self):
        os.system("clear")
        print("Proporcione los datos de la cuenta porfavor (en caso de dejar un parametro vacio se le dara el valor predeterminado)")
        self.dni=input("Inserte el DNI: ")
        self.numero_cuenta=input("Inserte el numero de cuenta: ")
        self.saldo=input("Indiquenos su saldo porfavor: ")
        Cuenta.revision_datos_cuenta(Cuenta)

    def revision_datos_cuenta(self):
        try:
                self.saldo=float(self.saldo)
                is_int=True
        except ValueError:
                is_int=False

        if is_int==False:
            print("Por favor asegurese que el saldo es un valor numerico")
            time.sleep(1)
            os.system("clear")
            Cuenta.obtener_datos(Cuenta)
        Cuenta.datos_default(Cuenta)

    def datos_default(self):
        if self.dni=="":
            self.dni="45698420L"
        if self.numero_cuenta=="":
            self.numero_cuenta=123456
        if self.saldo=="":
            self.saldo=float(1000)
        Cuenta.mostrar_datos(Cuenta)

    def mostrar_datos(self):
        os.system("clear")
        print("DNI",self.dni)
        print("Saldo  disponible",self.saldo)
        print("Numero de a cuenta",self.numero_cuenta)
        print("")
        Cuenta.menu_banco()
    
    def menu_banco():
        print("Que desea realizar:")
        print("1. Ingresar dinero")
        print("2. Retirar dinero")
        print("3. Actualizar saldo")
        print("4. Volver al menu principal")
        Cuenta.eleccion_user(Cuenta)

    def eleccion_user(self):
        accion=input("(Escriba el numero de la opcion deseada)")
        match(accion):
            case "1":
                self.ingreso_retiro=1
                Cuenta.cantidad(Cuenta)
            case "2":
                self.ingreso_retiro=2
                Cuenta.cantidad(Cuenta)
            case "3":
                Cuenta.datos_interes(Cuenta)
            case  "4":
                General.menu_general()
            case _:
                print("Escoga una de las opciones proporcionadas")
                time.sleep(1.25)
                os.system("clear")
                Cuenta.menu_banco()

    def cantidad(self):
        if self.ingreso_retiro==1:
            self.cantidad_user=input("Escriba la cantiad a ingresar")
            Cuenta.revision_cantidad(Cuenta)
        elif self.ingreso_retiro==2:
            self.cantidad_user=input("Escriba la cantidad a retirar")
            Cuenta.revision_cantidad(Cuenta)

    def revision_cantidad(self):
        try:
            self.cantidad_user=float(self.cantidad_user)
            is_int=True
        except ValueError:
            is_int=False

        if is_int==False:
            print("Por favor asegurese que ha insertado un valor numerico")
            time.sleep(1)
            os.system("clear")
            Cuenta.cantidad(Cuenta)
        elif self.ingreso_retiro==1:
            self.saldo=self.saldo+self.cantidad_user
            os.system("clear")
            print("Tras el ingreso este es el estado de tu cuenta")
            Cuenta.cuenta_final(Cuenta)
        elif self.ingreso_retiro==2:
            if (self.saldo-self.cantidad_user)>0:
                self.saldo=self.saldo-self.cantidad_user
                os.system("clear")
                print("Tras el retiro este es el estado de tu cuenta:")
                Cuenta.cuenta_final(Cuenta)
            else:
                print("No hay saldo suficiente.")
                print("Tu saldo actual es de:",self.saldo)
                time.sleep(1.5)
                os.system("clear")
                Cuenta.menu_banco()

    def datos_interes(self):
        print("Ahora vamos a calcular las ganancias del interes")
        print("Necesitamos saber los siguientes parametros")
        self.ratio=input("Cual es el ratio/porcentaje del interes(basta con poner el numero)")
        self.tiempo=input("Durante cuanto tiempo ha estado afectando los intereses?(Escribelo en años)")
        self.tipo_interes=input("Que tipo interes estaba afectando(simple o compuesto)")
        Cuenta.interes_formulas(Cuenta)

    def revision_datos_interes(self):
        try:
            self.ratio=float(self.ratio)
            self.tiempo=float(self.tiempo)
            is_int=True
        except ValueError:
            is_int=False

        if is_int==False:
            print("Por favor asegurese que el ratio y el tiempo son valores numericos")
            time.sleep(1)
            os.system("clear")
            Cuenta.datos_interes(Cuenta)
        Cuenta.interes_formulas(Cuenta)

    def interes_formulas(self):
        match(self.tipo_interes):
            case "simple":
                Cuenta.formula_simple(Cuenta)
            case "compuesto":
                Cuenta.formula_compuesto(Cuenta)
            case _:
                print("Rellene denuvo los datos y escriba 'simple' o 'compuesto' dependiendo el tipo de interes")
                Cuenta.datos_interes(Cuenta)

    def formula_simple(self):
        ci=float(self.saldo)
        self.interes=(ci*float(self.ratio)*float(self.tiempo))/100.0
        self.saldo=ci+self.interes
        os.system("clear")
        print("Tras realizar los calculos correspondientes asi queda tu cuenta")
        Cuenta.cuenta_final(Cuenta)

    def formula_compuesto(self):
        ci=float(self.saldo)
        self.interes=ci*((1+(float(self.ratio)/100.0))**(float(self.tiempo)))
        self.saldo=self.interes
        os.system("clear")
        print("Tras realizar los calculos correspondientes asi queda tu cuenta")
        Cuenta.cuenta_final(Cuenta)

    def cuenta_final(self):
        print("DNI",self.dni)
        print("Saldo  disponible",self.saldo)
        print("Numero de a cuenta",self.numero_cuenta)
        print("Pulse la tecla enter para volver al menu")
        getpass.getpass('')
        os.system("clear")
        Cuenta.menu_banco()

class Cancion:
    def __init__(self):
        self.titulos=[]
        self.autores=[]

    def canciones_default(self):
        self.titulos=[]
        self.autores=[]
        self.titulos+=["Toxic","Enemy"]
        self.autores+=["BoyWithUke","ImagineDragons"]
        Cancion.menu_cancion()

    def menu_cancion():
        print("Escoga una de las siguientes opciones")
        print("1. Dame la informacion de una cancion aleatoria")
        print("2. Inserta una cancion nueva")
        print("3. Buscar una cancion")
        print("4. Volver al menu principal")
        Cancion.eleccion_menu_canción()

    def eleccion_menu_canción():
        match(input("Escribe el numero de una de las opciones de arriba ")):
            case "1":
                Cancion.dame_cancion(Cancion)
            case "2":
                Cancion.nueva_cancion(Cancion)
            case "3":
                Cancion.busqueda_por()
            case "4":
                General.menu_general()
            case _:
                print("funciono")
    
    def dame_cancion(self):
        id_random=random.randint(0,(len(self.titulos)-1))
        print("Nombre de la cancion", self.titulos[id_random])
        print("Autor de la cancion", self.autores[id_random])
        Cancion.menu_cancion()

    def nueva_cancion(self):
        self.nuevo_titulo=input("Escriba el nombre de la cancion: ")
        self.nuevo_autor=input("Escriba el nombre del autor o grupo de la cancion (si no conoce el autor deje el espacio en blanco)")
        if self.nuevo_autor=="":
            self.nuevo_autor="Desconocido"
        print(self.nuevo_titulo," de ",self.nuevo_autor,". Los datos son correctos?")
        Cancion.verificacion_nueva_cancion(Cancion)
    
    def verificacion_nueva_cancion(self):
        verificado=False
        while verificado==False:
            match(input("Escriba Y/n: ")):
                case "Y" | "y" | "yes":
                    self.titulos+=[self.nuevo_titulo]
                    self.autores+=[self.nuevo_autor]
                    verificado=True
                case "N" | "n" | "no":
                    verificado=True
                    Cancion.nueva_cancion(Cancion)
        Cancion.menu_cancion()

    def busqueda_por():
        verificado=False
        while verificado==False:
            match(input("Por que quieres buscar? (Autor o titulo) ")):
                case "autor"|"autores"|"grupo"|"Autor"|"Autores"|"Grupo":
                    verificado=True
                    Cancion.busqueda_autor(Cancion)
                case "titulo"|"nombre"|"cancion"|"Titulo"|"Nombre"|"Cancion":
                    verificado=True
                    Cancion.busqueda_titulo(Cancion)
                case _:
                    print("Reintente escribiendo autor o titulo")

    def busqueda_autor(self):
        parametro_busqueda=input("Escriba el nombre del autor o grupo: ")
        print("------------")
        print("Canciones registradas en el programa de: ", parametro_busqueda)
        j=0
        for i in self.autores:
            if self.autores[j]==parametro_busqueda:
                print(self.titulos[j])
            j=j+1
        


    def busqueda_titulo(self):
        parametro_busqueda=input("Escriba el titulo de la cancion completo: ")
        print("------------")
        print("Resultados de la busqueda de: ", parametro_busqueda)
        j=0
        for i in self.titulos:
            print(j)
            if self.titulos[j]==parametro_busqueda:
                print(self.titulos[j]," de ",self.autores[j])
    
if __name__=="__main__":
    General.menu_general()