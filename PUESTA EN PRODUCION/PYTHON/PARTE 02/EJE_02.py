#Definir una función max_de_tres(), que tome tres números como argumentos y
#devuelva el mayor de ellos.
def mayor_de_tres(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    elif n3 > n1 and n3 > n2:
        return n3
    else:
        return print("TODOS SON IGUALES")

print(mayor_de_tres(6,7,8))
