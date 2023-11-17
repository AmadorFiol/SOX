import time
class Car():
    def __init__(self, motor, ruedas, puertas, velocidad_actal, velocidad_max):
        self.motor = motor
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad_actual = 10
        self.velocidad_max = 100
    
    def autoarrancar(self):
        print("aceleremos")
        while self.velocidad_actual!=self.velocidad_max:
            time.sleep(0.25)
            print(self.velocidad_actual,"km/h")
            self.velocidad_actual=self.velocidad_actual+1
        print("comencemos a frenar")
        while self.velocidad_actual>0:
            time.sleep(0.50)
            self.velocidad_actual=self.velocidad_actual-2
            print(self.velocidad_actual,"km/h")

    def arrancar(self):
        print("arranco")
        print("*vroom*")

    def acelerar(self):
       print("acelero")
       time.sleep(1)
       while self.velocidad!=50:
            time.sleep(1)
            print(self.velocidad,"km/h")
            self.velocidad=self.velocidad+1

    def cambiarmarcha(self):
        print("Aceleremos más")
        while self.velocidad!=100:
            time.sleep(0.50)
            self.velocidad=self.velocidad+2
            print(self.velocidad,"km/h")
        print("Aun mas rapido")
        while self.velocidad!=150:
            time.sleep(0.25)
            self.velocidad=self.velocidad+5
            print(self.velocidad,"km/h")

    def frenar(self):
        if self.velocidad==150:
            print("vamos a frenar")
            while self.velocidad>0:
                time.sleep(0.25)
                print(self.velocidad,"km/h")
                self.velocidad=self.velocidad-5

if __name__ =="__main__":    
    c1 = Car("V8", "rayomcqueen", "5", 30, 100)
    c1.autoarrancar()