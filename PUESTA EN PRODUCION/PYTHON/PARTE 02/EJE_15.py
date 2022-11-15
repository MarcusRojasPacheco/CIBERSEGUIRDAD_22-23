#Definir una tupla con 10 edades de personas.
#Imprimir la cantidad de personas con edades superiores a 20.
#Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.

array = []

for i in range(1,11):
    array.append(int(input("ESCRIBE UNA EDAD: ")))

cant = 0

for j in array:
    if j >= 20:
        cant = cant + 1
    else:
        cant = cant

print("PERSONAS QUE TIENE O ES IGUAL A 20 "+ cant)