import math

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

def valordelta(a,b,c):
    delta = (b**2)-4*a*c
    return delta

def raizdelta(delta,a,b):
    raiz_delta = math.sqrt(delta)
    x =(-b + raiz_delta)/(2*a)
    y =(-b - raiz_delta)/(2*a)
    return x,y

delta = valordelta(a,b,c)

if delta > 0:
    raizes = raizdelta(delta,a,b)
    print("Possui duas raizes, sendo ",raizes[0],"e",raizes[1])
    
elif delta == 0:
    raizes = raizdelta(delta,a,b)
    print("So possui uma raiz",raizes[0])

else:
    print("Não possui raizes reais")
