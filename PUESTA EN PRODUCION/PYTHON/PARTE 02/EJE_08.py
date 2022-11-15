#Definir una función generar_n_caracteres() que tome un entero n y devuelva el
#caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver
#"xxxxx"

def Generar_numero_caracter(a,b):
    c = b
    for i in range(a):
        b = b + c
    return print(b)

Generar_numero_caracter(5,"*")