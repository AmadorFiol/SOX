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
                Persona.menu_crear_persona()
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

class Persona():
    def __init__():
        pass

    def menu_crear_persona():
        verificado=False
        while verificado==False:
            #Cambiar mensaje bienvenida
            print("---Mensaje de bienvenida---")
            print("1. Realizar pruebas con datos predeterminados")
            print("2. Realizar pruebas con datos personalizados")
            print("3. Volver al menu principal")
            match(input("Esriba solo el numero porfavor: ")):
                case "1":
                    verificado=True
                    Persona.datos_predeterminados(Persona)
                case "2":
                    verificado=True
                    Persona.datos_personalizados(Persona)
                case "3":
                    verificado=True
                    General.menu_general()
                case _:
                    print("Reintente denuevo")
                    time.sleep(1.5)
                    os.system("clear")

    def datos_personalizados(self):
        verificado_edad=False
        while verificado_edad==False:
            self.edad=input("Cuantos años tienes? ")
            try:
                self.edad=int(self.edad)
                verificado_edad=True
            except ValueError:
                print("La edad debe ser un valor numerico")
                time.sleep(2.5)
                os.system("clear")
        if self.edad<18:
            self.mayor_edad=False
        else:
            self.mayor_edad=True
        verificado_sexo=False
        while verificado_sexo==False:
            print("Eres hombre o mujer? (M o F)")
            self.sexo=input("(Si no te identificas con ninguno deja el espacio en blanco) ")
            match(self.sexo):
                case "m"|"M"|"hombre"|"Hombre"|"macho"|"Macho":
                    self.sexo="M"
                    verificado_sexo=True
                case "f"|"F"|"mujer"|"Mujer"|"hembra"|"Hembra":
                    self.sexo="F"
                    verificado_sexo=True
                case "":
                    self.sexo="H"
                case _:
                    print("Sino se siente identificado con ninguno de los dos recuerde dejar el espacio en blanco")
                    time.sleep(4)
                    os.system("clear")
        Persona.generar_dni(Persona)

    def datos_predeterminados(self):
        self.edad=random.randint(1,60)
        if self.edad<18:
            self.mayor_edad=False
        else:
            self.mayor_edad=True
        self.sexo="M"
        Persona.generar_dni(Persona)

    def generar_dni(self):
        dni_valido=False
        while dni_valido==False:
            numeros_dni=[]
            i=0
            sumatorio_dni=0
            while i<8:
                numeros_dni+=[random.randint(0,9)]
                sumatorio_dni=numeros_dni[i]+sumatorio_dni
                i=i+1
            match(sumatorio_dni%23):
                case 0:
                    letra_dni="T"
                    dni_valido=True
                case 1:
                    letra_dni="R"
                    dni_valido=True
                case 2:
                    letra_dni="W"
                    dni_valido=True
                case 3:
                    letra_dni="A"
                    dni_valido=True
                case 4:
                    letra_dni="G"
                    dni_valido=True
                case 5:
                    letra_dni="M"
                    dni_valido=True
                case 6:
                    letra_dni="Y"
                    dni_valido=True
                case 7:
                    letra_dni="F"
                    dni_valido=True
                case 8:
                    letra_dni="P"
                    dni_valido=True
                case 9:
                    letra_dni="D"
                    dni_valido=True
                case 10:
                    letra_dni="X"
                    dni_valido=True
                case 11:
                    letra_dni="B"
                    dni_valido=True
                case 12:
                    letra_dni="N"
                    dni_valido=True
                case 13:
                    letra_dni="J"
                    dni_valido=True
                case 14:
                    letra_dni="Z"
                    dni_valido=True
                case 15:
                    letra_dni="S"
                    dni_valido=True
                case 16:
                    letra_dni="Q"
                    dni_valido=True
                case 17:
                    letra_dni="V"
                    dni_valido=True
                case 18:
                    letra_dni="H"
                    dni_valido=True
                case 19:
                    letra_dni="L"
                    dni_valido=True
                case 20:
                    letra_dni="C"
                    dni_valido=True
                case 21:
                    letra_dni="K"
                    dni_valido=True
                case 22:
                    letra_dni="E"
                    dni_valido=True
                case _:
                    dni_valido=False
        i=0
        self.dni=[]
        while i<8:
            self.dni.append(numeros_dni[i])
            i=i+1
        self.dni.append(letra_dni)
        Persona.mostrar_datos(Persona)

    def mostrar_datos(self):
        print("Tu humano: ")
        print("Genero: ", self.sexo)
        print("DNI: ", self.dni)
        print("Y tiene +18? ",self.mayor_edad)
    

if __name__=="__main__":
    General.menu_general()

    '''
    Menus en una clase distinta
    Poner los datos en constructor es ponerlo por defecto
    Revisar algunos while y cambiar por foreachs
    Clases helper
    '''