def width(x):
    
    while x > 0:
        
        print('#', end = '')
        x = x - 1
    
    
def height():
    print()



largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

while altura > 0:
    width(largura)
    height()
    altura = altura - 1






