---
layout: default
---

# UT1 PC01
## FUNDAMENTOS DE LA PROGRAMACIÓN
### 1º [CE. a] En primer lugar vamos a comprobar las características principales de los lenguajes de programación a través de los ejercicios prácticos que habéis realizado

#### EJERCICIO [PARTE 01]

##### EJERCICIO 1.3
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
variable = PHP;
```
> Pero tanto en PHP y C se necesita un **;** mientra que en el lenguaje de programación de python es indentado.

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
> 
> Datos primitivos
> - Python [int, float, bool, str]
> - C [char, shor int, int, long int, bool, float, double, long double]
> - PHP [boolean, integer, float, string, array, object, callable, iterable, resource, null]


#### EJERCICIO [PARTE 02]




[back](./)