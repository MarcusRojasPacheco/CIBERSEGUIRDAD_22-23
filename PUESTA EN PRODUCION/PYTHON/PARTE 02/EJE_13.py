#Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene
#que evaluar la cadena y decir cuantas letras mayúsculas tiene.

frase = "HolA Como Estas JoNatan"
cant = 0
for letra in frase:
    minuscula = letra.lower()
    if letra == minuscula:
        cant = cant
    else:
        cant = cant + 1
print(cant)