area_pintar = int(input("Tamanho da area a ser pintada: "))

if area_pintar > 54:
    if area_pintar % 54 == 0:
        latas = int(area_pintar / 54)
        preco = latas * 18

        print("Latas: ",latas)
        print("Preço: $",preco)
        
    else:
        latas = int(area_pintar / 54)+1
        preco = latas * 18
        print("Latas: ",latas)
        print("Preço: $",preco)
        
else:
    print("Latas: 1")
    print("Preço: $18,00")
