def metodo1():
    print ("Hello World")


array = ["pepito", "juanjo", "salvador"]
def printarray():
    for i in array[i]:
        print (array[i])


if  __name__ == "__main__":
    metodo1()
    def metodo2():
        x = float(input("Escriba un numero: "))
        y = float(input("Escriba otro numero: "))
        operacion = str(input("Que operacion quiere realizar? (suma,resta,multiplicacion,division): "))
        if (operacion == "suma"):
            suma = (x+y)
            print (suma)
        elif (operacion == "resta"):
            resta = (x-y)
            print (resta)
        elif (operacion == "multiplicacion"):
            multiplicacion = (x * y)
            print (multiplicacion)

        elif (operacion == "division"):
            division = (x//y)
            print (division)
        else:
            print("Escriba una operacion valida")
    metodo2()
    printarray()