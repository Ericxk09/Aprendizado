number = int(input("Digite um numero: "))

primo = 2
divisores = 0
while primo < number:
    if number % primo == 0:
        print("Não primo")
        divisores = 1
        break
    primo = primo + 1
if divisores == 0 and number > 0:
    print("Primo")
elif number == 0:
    print("Não primo")
