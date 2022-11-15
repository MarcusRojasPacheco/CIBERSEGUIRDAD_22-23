#Definir un histograma procedimiento() que tome una lista de números enteros e
#imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir
#lo siguiente:

a = [4, 9, 7]

def proce(a):
    lista = list(a)
    for i in lista:
        print("*"*int(i))

proce(a)