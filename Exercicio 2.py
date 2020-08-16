def width(x):
    
    while x > 0:
        
        print('#', end = '')
        x = x - 1
    
    
def height(x):
    
    while x > 0:
        
        print(' ', end = '')
        x = x - 1

largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

while altura > 0:
    width(largura)
    print()
    altura = altura  - 1
    while altura > 1:
        width(1)
        height(largura-2)
        width(1)
        print()
        altura = altura - 1
        
    width(largura)
    altura = altura - 1






