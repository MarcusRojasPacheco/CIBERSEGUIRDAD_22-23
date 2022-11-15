#Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la
#letra a.
#También se puede hacer elegir al usuario la letra a buscar. (Un poco mas emocionante)

nomb = []
for i in range(0,10):
    nomb.append(input("ESCRIBE UN NOMBRE: ").lower())

letra_busc = int(input("¿QUE LETRA BUSCAS?: "))
cant = 0

for j in nomb:
    for k in nomb:
        if k == letra_busc:
            cant = cant + 1
            break
        else:
            cant = cant
print(cant)