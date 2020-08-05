number = int(input("Digite um numero: "))
x = 1

while number > 0:
    if x % 2 != 0:
        print(x)
        number = number - 1
    x = x + 1

