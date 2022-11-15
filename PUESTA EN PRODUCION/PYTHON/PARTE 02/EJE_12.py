#Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y
#devuelva las palabras que tengan más de n caracteres.

def filtrar_pala(lista, numero):
    array = []
    for pala in lista:
        if len(pala) <= numero :
            array.append(pala)
    if len(array) == 0:
        print("NINGUA PALABRA :(")
    else:
        print(array)
lista = ["sa", "sdssdsd", "sdsdsdsdd", "rrtrdgdv"]
numero = int(input("ESCRIBE UN NUMERO: "))

filtrar_pala(lista,numero)