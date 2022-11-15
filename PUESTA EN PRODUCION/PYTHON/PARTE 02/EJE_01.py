#Definir una función max() que tome como argumento dos números y devuelva el mayor
#de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla
#nosotros mismos es un muy buen ejercicio.
def mayor(n1, n2):
    if (n1 > n2):
        return n1
    if (n2 > n1):
        return n2

print(mayor(4,5))