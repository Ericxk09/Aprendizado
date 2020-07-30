import random

numero = random.sample(range(100),20)
par = []
impar = []
k = 0
while k < 20:
    if numero[k]%2 == 0:
        par.append(numero[k])
    else:
        impar.append(numero[k])
    k = k + 1
print("Numeros sorteados: ",numero)
print("Numeros Pares: ",par)
print("Numeros Impares: ",impar)

    
