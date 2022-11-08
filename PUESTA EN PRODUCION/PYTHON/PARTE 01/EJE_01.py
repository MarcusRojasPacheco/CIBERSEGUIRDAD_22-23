### SISTEMA DE CLASIFICACIÓN
#Ejercicio 1.1
#El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
#El usuario proporcionará un valor entre 0 y 10.
#Si está entre 9 y 10: imprimir una A
#Si está entre 8 y menor a 9: imprimir una B
#Si está entre 7 y menor a 8: imprimir una C
#Si está entre 6 y menor a 7: imprimir una D
#Si está entre 0 y menor a 6: imprimir una F
#cualquier otro valor debe imprimir: Valor desconocido

def clasificacion(numero):
    int = numero
    if numero>=9:
        print("CALIFICACIÓN [A]")
    elif numero>=8 and numero<9:
        print("CALIFICACIÓN [B]")
    elif numero>=7 and numero<8:
        print("CALIFICACIÓN [C]")
    elif numero>=6 and numero<7:
        print("CALIFICACIÓN [D]")
    elif numero<6:
        print("CALIFICACIÓN [F]")
    else:
        print("VALOR DESCONOCIDO")

clasificacion(4)
