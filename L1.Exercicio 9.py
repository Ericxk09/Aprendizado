distancia_km = float(input('Distancia percorrida em KM:'))
quantdias_alugado = int(input('Quantidade de dias que o carro ficou alugado: '))

valor_dia = quantdias_alugado * 60
valor_distancia = distancia_km * 0.15
valor_final = valor_dia + valor_distancia

print('Preço a pagar: $', valor_final)
