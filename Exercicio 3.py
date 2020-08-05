number = int(input("Digite um numero: "))
soma = 0
while number > 0:
    soma = soma + (number % 10)
    number = number//10
print(soma)
