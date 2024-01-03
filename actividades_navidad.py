import os
import time

class Cuenta():
    def __init__(self):
        dni=None
        saldo=None
        numero_cuenta=None
        self.dni=dni
        self.saldo=saldo
        self.numero_cuenta=numero_cuenta

    def menu_banco():
        print("Bienvenido al banco de Amador, ¿que desea hacer?")
        print("1. Realizar pruebas con cuenta predeterminada")
        print("2. Realizar pruebas con cuenta personalizada")
        Cuenta.eleccion_user(Cuenta)
    
    def eleccion_user(self):
        self.dni=""
        self.numero_cuenta=""
        self.saldo=""
        pruebas_con=input("(Escriba el numero de la opcion deseada)")
        match(pruebas_con):
            case "1":
                Cuenta.datos_default(Cuenta)
            case "2":
                Cuenta.obtener_datos(Cuenta)
            case _:
                print("Escoga una de las opciones proporcionadas")
                time.sleep(1.25)
                os.system("clear")
                Cuenta.menu_banco()
    
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
        Cuenta.datos_interes(Cuenta)
    
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
        ci=self.saldo
        self.interes=(ci*self.ratio*self.tiempo)/100
        self.saldo=ci+self.interes
        print("Tras realizar los calculos correspondientes asi queda tu cuenta")
        Cuenta.cuenta_final(Cuenta)

    def formula_compuesto(self):
        ci=self.saldo
        self.interes=ci*((1+(self.ratio/100))**(self.tiempo))
        self.saldo=self.interes
        print("Tras realizar los calculos correspondientes asi queda tu cuenta")
        Cuenta.cuenta_final(Cuenta)

    def cuenta_final(self):
        print("DNI",self.dni)
        print("Saldo  disponible",self.saldo)
        print("Numero de a cuenta",self.numero_cuenta)

if __name__=="__main__":
    Cuenta.menu_banco()