#Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a"
#tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
#Se puede hacer que el usuario sea quien elija la palabra.

def cont_vocal(palabra):
    palabra_min = palabra.lower()
    cant_a = 0
    cant_e = 0
    cant_i = 0
    cant_o = 0
    cant_u = 0
    for i in palabra_min:
        if i == "a":
            cant_a = cant_a + 1
        elif i == "e":
            cant_e = cant_e + 1
        elif i == "i":
            cant_i = cant_i + 1
        elif i == "o":
            cant_o = cant_o + 1
        elif i == "u":
            cant_u = cant_u + 1
    print("HAY "+ str(cant_a)+ " a")
    print("HAY " + str(cant_e) + " e")
    print("HAY " + str(cant_i) + " i")
    print("HAY " + str(cant_o) + " o")
    print("HAY " + str(cant_u) + " u")

palabra = input("ESCRIBE UNA PALABRA: ")
cont_vocal(palabra)
