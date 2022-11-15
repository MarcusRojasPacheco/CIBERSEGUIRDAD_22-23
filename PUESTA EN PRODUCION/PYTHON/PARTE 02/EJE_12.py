#Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y
#devuelva las palabras que tengan más de n caracteres.

def filtrar_palabra(lista,num):
    array = []
    for pala in lista:
        if len(pala) >= num:
            array.append(pala)
        if len(array) == 0:
            print("Ninguna palabra :(")
        else:
            print(array)

lista = ["sa", "sfsaf", "dsfds", "idsids"]
num = input("Escribe un numero: ")

filtrar_palabra(lista,num)