import math

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

delta = (b**2)-4*a*c

if delta > 0:
    delta = math.isqrt(((b**2)-4*a*c))
    x1 =(-b + delta)/(2*a)
    x2 =(-b - delta)/(2*a)
    print("Possui duas Raizes Reais!")
    print("X':",x1)
    print("X'':",x2)

elif delta == 0:
    print("Possui uma Raiz Real!")
    print("Delta =",delta)

else:
    print("Não possui Raizes Reais!")
    
