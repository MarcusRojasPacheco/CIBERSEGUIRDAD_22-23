#Escribir una función sum() y una función multip() que sumen y multipliquen
#respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería
#devolver 10 y multip([1,2,3,4]) debería devolver 24.

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