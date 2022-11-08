#Solicitar al usuario dos valores:
#   ● numero1 (int)
#   ● numero2 (int)
#Se debe imprimir el mayor de los dos números

n1 = int(input("NUMERO UNO: "))
n2 = int(input("NUMERO DOS: "))

def Mayor_numero(n1,n2):

    if n1 > n2:
        print("EL NUMERO ",n1," ES EL MAYOR")
    else:
        print("EL NUMERO ",n2," ES EL MAYOR")
Mayor_numero(n1,n2)