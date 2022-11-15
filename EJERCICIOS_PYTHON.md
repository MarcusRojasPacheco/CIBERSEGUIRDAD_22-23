---
layout: default
---

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

> Pero tanto en PHP y C se necesita un **;** mientra que en el lenguaje de programación de python es indentado.

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
> Para poder comentar en Python seria **#**, mientra que en C seria **/* */** y en PHP seria **//**.

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
#### ¿Qué diferencias existen entre los dos lenguajes?
#### ¿Para qué tipo de programa puede servir cada lenguaje?
#### ¿Cómo sería el proceso de lectura del código fuente de cada programa?



[VOLVER PAGINA PRINCIPAL](./)