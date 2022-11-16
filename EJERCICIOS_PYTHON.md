---
layout: default
---
<!-- https://marcusrojaspacheco.github.io/CIBERSEGUIRDAD_22-23/EJERCICIOS_PYTHON.html -->
# UT1 PC01
## FUNDAMENTOS DE LA PROGRAMACIÓN
[VOLVER PAGINA PRINCIPAL](./)
### 1º [CE. a] En primer lugar vamos a comprobar las características principales de los lenguajes de programación a través de los ejercicios prácticos que habéis realizado

#### EJERCICIO [PARTE 01]

```python
# PYTHON EJERCICIO 1.3
cont=0
while cont < 10:
    cont +=1
    if cont % 3 == 0:
        print(cont)
        continue
```
> La manera de definir la variable es de la siguiente forma.

```markdown
variable = python
variable = C;
$variable = PHP;
```

> Pero tanto en PHP y C se necesita un** ;** mi entra que en el lenguaje de programación de python es indentado.

#### EJERCICIO [PARTE 02]

```python
# PYTHON EJERCICIO 2.5
def sum(a):
    total = 0
    for i in range(len(a)):
        total += a[i]
    return  total
def multip(b):
    total = 1
    for i in range(len(b)):
        total *= b[i]
    return total

print(sum([1,2,3,4]))
print(multip([1,2,3,4]))
```
> Para poder comentar en Python seria **#**, mientras que en C seria **/* */** y en PHP seria **//**.

Datos primitivos

> - **Python**: [int, float, bool, str]
> - **C**: [char, shor int, int, long int, bool, float, double, long double]
> - **PHP**: [boolean, integer, float, string, array, object, callable, iterable, resource, null]

```python
# PYTHON EJERCICIO 2.10
lista = [0,7,3,1,5,6,3,2,4,8,10]

def maximo_en_lista(lista):
    num_mayor = lista[0]

    for i in lista:
        if num_mayor <= i:
            num_mayor = i
        else:
            num_mayor = num_mayor
    print(num_mayor)

maximo_en_lista(lista)
```

> - **Python**: Las tuplas es este lenguaje es una estructura parecida a una lista pero esta inmutable, por lo que no puede ser modificado durante la ejercución del mismo programa.
> - **C**: Tiene tener una cabecera de la función, que tiene indicar el nomnbre y una lista de argumentos cerrada con parentesis, tambien una lista de declaración de argumentos si en este caso incluye estos en la cabecera y por ultimo la función a realizar.
> - **PHP**: La estructura es parecida con el lenguaje C, lo unico que tiene diferente son en los arrays.

Bucles en **for** en los diferentes lenguajes.

> - **Python**: La palabra clave es **for** seguida con el nombre de la variable del ciclo, la palabra **in** y una llamada a la función **range()** que se especifica los parametros que se necesita seguido con **:**.
> - **C**: Se empieza como **Python** con la palabra **for** pero en este caso la sentencia seria **_(variable = 0; sentencia; sumatorio);_**.
> - **PHP**: Es como el C pero en las variables y sentencias se debe poner **$**.

### 2º [CE. b] En esta actividad vamos a realizar una comparación entre Python y C, es por ello que debes elegir tres de los ejercicios de los realizados en clase y contestar a las siguientes preguntas.

```python
# PYTHON EJERCICIO 1.01
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
```

#### ¿Qué diferencias habría en el desarrollo del programa?

> Con las variables en **C** se tiene que declarar su tipo, pero con **Python** no es necesario y no te obligar a declararlo, ya que en **C** se tendria declarar la variable y la estructura de control.

#### ¿Qué diferencias existen entre los dos lenguajes?

> En **C** es un lenguaje compilado y en python es un lenguaje interpretado.
> En el ejercicio anterior el IF en **C** es diferentes en comparación con Python, ahora se pondra un ejemplo del mismo.
 
```c
/* EJEMPLO EN C */
#include <stdio.h>
    int main()
    {
        int a,b;
        if(a > b){
            printf("Mayor es %d",a);
        }else if(a == b){
            printf("son igules %d y %d"a,b);
        }else{
            printf("Mayor es %d",b);
        }
    }
```
#### ¿Para qué tipo de programa puede servir cada lenguaje?

```python
# PYTHON EJERCICIO 2.07
ddef ES_UN_NUMERO(a):
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

def ES_POLINDROMO(a):
    inv=inver(a)
    if(inv == a):
        return True
    else:
        return False
print(ES_POLINDROMO("radar"))
```

> - **Python**: Normalmente utilizado para un aprendizaje que puede ser automatico o que puede usarse para desarrollo web o en aplicacciones.
>
> - **C**: Se suele utilizar para un desarrollo de aplicaciones que suele ser relacionadas con hardware, S.O, etc..., ya que cuando compila da tambien el lenguaje codigo maquina que es como se comunica nuestro ordenador.

#### ¿Cómo sería el proceso de lectura del código fuente de cada programa?

```python
# PYTHON EJERCICIO 2.18
def ES_BISIESTO(ano):
    if ano%4 == 0:
        if ano%100 != 0:
            print("ES BISIESTO")
        else:
            print("NO ES BISIESTO")

ano = int(input("ESCRIBE UN AÑO PARA SABER SI ES BISIESTO: "))
ES_BISIESTO(ano)
```
> - **Python**: Se compila con un codigo de **bytes** lo que luego es interpretado por un programa.
> - **C**: Se compila directamente en el codigo maquina que es ejecutado por la **CPU**, ya que al compilar nos da un archivo que es codigo maquina que solo entiende nuestro ordenador y puede iterpretar.

### 3º [CE. c] Teniendo todos los ejercicios realizados y entregado. Sobre el código fuente creado en la relación de ejercicios de las actividades 0 y 1 de la unidad, realiza en un documento los comentarios sobre todos los ejercicios indicando que elementos del código fuente has utilizado y qué función tienen.

> Ahora vamos a ver las diferentes elementos usados en los ejercicios.

#### EJERCICIOS CREADO CON EL ELEMENTO FOR

> Ahora vamos a ver que ejercicio ha usado la siguiente elemento en los ejercicios creado.

```python
# EJEMPLO PYTHON DE FOR
    for VARIABLE in VARIABLE_ANTE_CREADA:
        SENTENCIA
```

> Como vemos en esta tabla con todos los ejercicios creados, se ve como se usa de diferente forma el **FOR** para lo que pida el ejercicio y lo que vayamos a hacer en él.
> 
> También vemos que algunos ejercicios se necesita de algunos anteriores para poder hacerlo, empleando las mismas sentencia y condición de él.
> 
> Los bubcles son lo más utilizado al hacer una acción repetida.

| PARTE | EJERCICIO                                                                                                                                 | 
|:-----:|:------------------------------------------------------------------------------------------------------------------------------------------|
|   1   | [EJERCICIO1.3](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2001/EJE_03.py)  |
|   2   | [EJERCICIO2.3](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_03.py)  |
|   2   | [EJERCICIO2.4](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_04.py)  |
|   2   | [EJERCICIO2.5](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_05.py)  |
|   2   | [EJERCICIO2.6](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_06.py)  |
|   2   | [EJERCICIO2.7](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_07.py)  |
|   2   | [EJERCICIO2.8](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_08.py)  |
|   2   | [EJERCICIO2.9](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_09.py)  |
|   2   | [EJERCICIO2.10](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_10.py) |
|   2   | [EJERCICIO2.11](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_11.py) |
|   2   | [EJERCICIO2.12](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_12.py) |
|   2   | [EJERCICIO2.13](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_13.py) |
|   2   | [EJERCICIO2.15](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_15.py) |
|   2   | [EJERCICIO2.16](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_16.py) |
|   2   | [EJERCICIO2.17](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_17.py) |


#### EJERCICIOS CREADO CON EL ELEMENTO IF

> Vamos a ver los elementos usado en los ejercicios creados.

```python
# EJEMPLO PYTHON DE IF
    IF CONDICION:
        SENTENCIA
    ELIF CONDICION:
        SENTENCIA
    ELSE:
        SENTENCIA
```

> Con esta sentencia es muy usada para decir **SI** la condición puede ser verdadera o **SI NO** si la condición es diferente a la anterior usada.
> Es la más utilizada en cualquiera programa de cualquier lenguaje.

| PARTE | EJERCICIO                                                                                                                                 | 
|:-----:|:------------------------------------------------------------------------------------------------------------------------------------------|
|   1   | [EJERCICIO1.1](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2001/EJE_01.py)  |
|   1   | [EJERCICIO1.2](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2001/EJE_02.py)  |
|   2   | [EJERCICIO2.1](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_01.py)  |
|   2   | [EJERCICIO2.2](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_02.py)  |
|   2   | [EJERCICIO2.3](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_03.py)  |
|   2   | [EJERCICIO2.4](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_04.py)  |
|   2   | [EJERCICIO2.6](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_06.py)  |
|   2   | [EJERCICIO2.7](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_07.py)  |
|   2   | [EJERCICIO2.10](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_10.py) |
|   2   | [EJERCICIO2.11](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_11.py) |
|   2   | [EJERCICIO2.12](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_12.py) |
|   2   | [EJERCICIO2.13](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_13.py) |
|   2   | [EJERCICIO2.15](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_15.py) |
|   2   | [EJERCICIO2.16](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_16.py) |
|   2   | [EJERCICIO2.17](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_17.py) |
|   2   | [EJERCICIO2.18](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002/EJE_18.py) |


#### EJERCICIOS CREADO CON EL ELEMENTO VARIABLES

> Las variables que se usan en los ejercicios son diferentes en el cual a veces se usa en cadena o se una número entero o en algún caso se usa un array.

| PARTE | EJERCICIO                                                                                                                    | 
|:-----:|:-----------------------------------------------------------------------------------------------------------------------------|
|   1   | [EJERCICIO1](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2001) |
|   2   | [EJERCICIO2](https://github.com/MarcusRojasPacheco/CIBERSEGUIRDAD_22-23/blob/main/PUESTA%20EN%20PRODUCION/PYTHON/PARTE%2002) |


[VOLVER PAGINA PRINCIPAL](./)