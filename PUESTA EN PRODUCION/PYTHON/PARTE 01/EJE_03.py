# Iterar un rango de 0 a 10 e imprimir sólo los
# números divisibles entre 3
print("CON WHILE")
cont=0
while cont < 10:
    cont +=1
    if cont % 3 == 0:
        print(cont)
        continue
print("CON FOR")
for i in range(1,10):
    if i % 3 == 0:
        print(i)
        continue