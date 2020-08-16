import math

def soma_hipotenusas(x):

    k = 1
    soma = 0
    while k <= x :
        if é_hipotenusa(k) == True:
            soma = soma + k
            k = k + 1
        else:
            k = k + 1
    return soma

def é_hipotenusa(x):

    b = c = 1
    
    while x != math.sqrt(b**2+c**2) and b <= x:

        if b == c:
            b = b + 1
            c = 1
    
        else:
            c = c + 1
    
    if x == math.sqrt(b**2+c**2):
        return True
    else:
        return False
