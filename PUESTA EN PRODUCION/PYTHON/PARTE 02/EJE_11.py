#Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga.
def mas_larga(lista):
    pala_mayor = len(lista[0])
    pala_mostrar = lista[0]

    for pala in lista:
        if pala_mayor <= len(pala):
            pala_mostrar = pala
            pala_mayor = len(pala)
        else:
            pala_mostrar = pala_mostrar
    print(pala_mostrar)

lista = ["a", "afgdfgfdb", "dsfdsfdsfsdfsdfsd"]
mas_larga(lista)
