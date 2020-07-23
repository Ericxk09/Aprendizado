salario_hora = float(input("Salario hora: "))
hora_mensal = float(input("Horas Trabalhadas: "))

salario_bruto = salario_hora * hora_mensal
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato

print("Salario bruto: $",salario_bruto)
print("IR(11%): $",ir)
print("INSS(8%): $", inss)
print("Sindicato(5%): $",sindicato)
print("Salario Liquido: $",salario_liquido)
