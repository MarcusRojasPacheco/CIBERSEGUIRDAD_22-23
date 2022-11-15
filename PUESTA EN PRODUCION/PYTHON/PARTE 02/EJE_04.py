#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo
#contrario devuelve False.
def ES_UN_NUMERO(a):
    try:
        int(a)
    except:
        return False;
    return True;

def ES_UN_CARACTER(b):
    if(len(b)>1):
        return False
    if(len(b)==1):
        return True

def ES_VOCAL(c):
    vocales = "aeiouáéíóú"
    if not (ES_UN_NUMERO(c)) and (ES_UN_CARACTER(c)):
        for i in range(len(vocales)):
            for j in range(len(c)):
                if (vocales[i] == c):
                    return True
                else:
                    return False
    elif(ES_UN_NUMERO(c)):
        print("ES UN NUMERO")
    elif not(ES_UN_CARACTER(c)):
        print("NO ES SOLO UN CARACTER")

ES_VOCAL("as")
