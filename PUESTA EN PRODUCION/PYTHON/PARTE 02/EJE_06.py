#Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la
#cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
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

def inver(c):
    transformar = ""
    if(ES_UN_NUMERO(c)):
        print("ES UN NUMERO")
        return "ERROR"
    elif not(ES_UN_CARACTER(c) and ES_UN_NUMERO(c)):
        for i in range(len(c)):
            transformar = transformar + c[(len(c)-1)-i]
        return transformar
    else:
        print("NO DEBE SER UN NUMERO O UNA SOLA LETRA")

print(inver("odnaborp yotse"))
