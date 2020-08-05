soma = number = int(input("Digite um numero: "))
x = number - 1

if number == 0:
    soma = 1
    print(soma)

else:
    while x > 1:
        soma = soma * x
        x = x - 1 
        
    print(soma)
