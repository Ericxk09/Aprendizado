def primo(number):

    primos = 1
    k = n = 2
    
    while k <= n and n <= number:

        if n % k == 0 and n != k:
            n = n + 1
            k = 2

        elif n == k:
            primos = n
            n = n + 1
            k = 2
        else:
            k = k + 1      

    print(primos)

print("Digite um numero inteiro maior ou igual a 2")
number = int(input("Digite um Numero: "))

while number < 2:
    number = int(input("Digite um Numero: "))
    
primo(number)
