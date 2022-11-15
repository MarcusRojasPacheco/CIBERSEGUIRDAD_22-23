#Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto
#que python tiene la función len() incorporada, pero escribirla por nosotros mismos
#resulta un muy buen ejercicio

def ES_UN_NUMERO(a):
    try:
        int(a)
    except:
        return False;
    return True;
def longitud(a):
    i=0
    if not (ES_UN_NUMERO(a)):
        for i in range(len(a)):
            i = i + 1
    elif(ES_UN_NUMERO(a)):
        return (a)
    return (i)
print(longitud("hola"))
print(longitud(["1","2","3"]))
