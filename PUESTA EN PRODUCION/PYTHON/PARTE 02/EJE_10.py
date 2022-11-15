#La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio
#2 (primera parte), solo van a funcionar para 2 o 3 números. Supongamos que tenemos
#más de 3 números o no sabemos cuántos números son. Escribir una función
#max_in_list() que tome una lista de números y devuelva el más grande
lista = [0,7,3,1,5,6,3,2,4,8,10]

def maximo_en_lista(lista):
    num_mayor = lista[0]

    for i in lista:
        if num_mayor <= i:
            num_mayor = i
        else:
            num_mayor = num_mayor
    print(num_mayor)

maximo_en_lista(lista)