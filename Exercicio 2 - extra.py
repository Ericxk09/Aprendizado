number = int(input("Digite um numero: "))

n1 = number % 10
adjacente = False
while number > 0:
    n2 = n1
    number = number // 10
    n1 = number % 10
    if n2 == n1:
        adjacente = True
        break
    else:
        adjacente = False
if adjacente == True:
    print("sim")
else:
    print("Não")
    
