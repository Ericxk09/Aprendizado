def factorial(x):
    fat_x = 1
    while x > 1:
        fat_x = fat_x * x
        x = x -1
    return fat_x
def binominal(a,b):
    fat_a = factorial(a)
    fat_b = factorial(b)
    fat_ab = factorial(a - b)
    cal_binominal = (fat_a/fat_b*fat_ab)
    return print(cal_binominal)

print("(A!)/(B!*(A-B)!)")
a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))

binominal(a,b)
