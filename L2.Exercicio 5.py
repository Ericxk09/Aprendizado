numero1 = float(input("Numero 1: "))
numero2 = float(input("Numero 2: "))
numero3 = float(input("Numero 3: "))

if numero1 > numero2 and numero1 > numero3:
    print("Maior numero: ",numero1)
    if numero2 > numero3:
        print("Menor numero: ",numero3)
        
    elif numero2 < numero3:
        print("Menor numero: ",numero2)

    else:
        print("Os outros numeros são iguais!")
        
elif numero2 > numero1 and numero2 > numero3:
    print("Maior numero: ",numero2)
    if numero1 > numero3:
        print("Menor numero: ",numero3)
        
    elif numero1 < numero3:
        print("Menor numero: ",numero1)

    else:
        print("Os outros numeros são iguais!")
    
elif numero3 > numero1 and numero3 > numero2:
    print("Maior numero: ",numero3)
    if numero2 > numero1:
        print("Menor numero: ",numero1)
        
    elif numero2 < numero1:
        print("Menor numero: ",numero2)

    else:
        print("Os outros numeros são iguais!")
    
elif numero1 == numero2 and numero2 == numero3:
    print("Todos os numeros são iguais ")
    
