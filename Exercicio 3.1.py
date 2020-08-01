s = input("Digite uma palavra: ")

def right_justify(s):
    x = " "
    space = len(s)
    while space < 70:
        space = space + 1
        s = x+s
    
    return print(s)
right_justify(s)

            
