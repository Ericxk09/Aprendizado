vlr_mercadoria = float(input('Valor da Mercadoria: $ '))
desconto = float(input('Valor do desconto em %: '))

desconto_final = vlr_mercadoria * (desconto / 100)
vlr_mercadoria_final = vlr_mercadoria - desconto_final

print('Valor do Desconto: $', desconto_final)
print('Valor da Mercadoria: $', vlr_mercadoria_final)
