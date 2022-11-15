#Escriba una función es_bisiesto() que determine si un año determinado es un año
#bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400

def ES_BISIESTO(ano):
    if ano%4 == 0:
        if ano%100 != 0:
            print("ES BISIESTO")
        else:
            print("NO ES BISIESTO")

ano = int(input("ESCRIBE UN AÑO PARA SABER SI ES BISIESTO: "))
ES_BISIESTO(ano)