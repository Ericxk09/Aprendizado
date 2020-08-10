def vogal(x):

    vogais = 'a e i o u'.split( )
    k = 0
    for k in range(5):
        if x == vogais[k]:
            break
            
    print(x==vogais[k])
            
x = input('Digite um caracter: ')

while len(x) != 1:
    x = input('Digite um caracter: ')
vogal(x)
