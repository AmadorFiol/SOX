def busqueda_while(arr,var_encontrar):
    encontrar=False
    while not encontrar:
        if arr==var_encontrar:
            print(arr)
            encontrar=True

def busqueda_for(arr,var_encontrar):
    i=0
    for i in arr:
        if "juan" == i:
            print(arr)
            break  

def recorrida_while(arr):
    i=0
    while i<len(arr):
        print(arr)
    
def recorrida_for(arr):
    for i in arr:
        print(arr)

if __name__=="__main__":
    arr=["macia","juan","jose","ernesto"]
    var_encontrar="juan"
    busqueda_for(arr,var_encontrar)
    busqueda_while(arr,var_encontrar)
    recorrida_for(arr)
    recorrida_while(arr)
