cigarro_dia = int(input('Quantos Cigarros voce fuma por dia: '))
anos_fumante = int(input('Há quantos anos voce fuma? '))

dias_fumante = anos_fumante * 365
total_cigarros = dias_fumante * cigarro_dia
dias_perdidos = total_cigarros / 144

print('Voce perdeu', dias_perdidos,' dias')

##1 dia = 1440 minutos = 144 cigarros por dia
