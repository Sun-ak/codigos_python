horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor por hora: "))

horas_normais = 40

if horas_trabalhadas > horas_normais:
    horas_extras = horas_trabalhadas - horas_normais
    pagamento_normal = horas_normais * valor_por_hora
    pagamento_extras = horas_extras * valor_por_hora * 1.5
    salario_total = pagamento_normal + pagamento_extras
else:
    salario_total = horas_trabalhadas * valor_por_hora

print(f"O salário total é: R$ {salario_total:.2f}")