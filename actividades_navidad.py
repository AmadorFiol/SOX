class Cuenta():
    def __init__(self):
        DNI=int()
        saldo=int()
        numero_cuenta=str()
        self.DNI= DNI
        self.saldo= saldo
        self.numero_cuenta= numero_cuenta

    def mostrar_datos(self):
        print("DNI",self.DNI)
        print("Saldo  disponible",self.saldo)
        print("Numero de a cuenta",self.numero_cuenta)

if __name__=="__main__":
    Cuenta.mostrar_datos(Cuenta)