'''Crie uma função chamada converter_temperatura que receba uma temperatura em graus Celsius e a converta para Fahrenheit ou Kelvin o usuário deverá escolher para qual temperatura será feita a conversão. O programa deve solicitar ao usuário a temperatura em Celsius, usar a função para converter e exibir o valor correspondente em Fahrenheit ou Kelvin. O usuário poderá realizar essa operação repetidamente até informar um valor negativo.
Fórmula para conversão Fahrenheit: f = (9/5) * celsius + 32
Fórmula para conversão Kelvin: k = celsius + 273.15'''

def converter_temperatura(celsius, escala):
    if escala == 'f':
        return (9/5) * celsius + 32
    elif escala == 'k':
        return celsius + 273.15

def menu_temperatura():
    while True:
        celsius = float(input("Digite a temperatura em Celsius (ou um número negativo para sair): "))
        if celsius < 0:
            break
        escala = input("Para qual escala você deseja converter? (f - Fahrenheit / k - Kelvin): ").strip().lower()
        temperatura_convertida = converter_temperatura(celsius, escala)
        if escala == 'f':
            print(f"{celsius:.2f} °C é igual a {temperatura_convertida:.2f} °F")
        elif escala == 'k':
            print(f"{celsius:.2f} °C é igual a {temperatura_convertida:.2f} K")
        else:
            print("Escala inválida.")

menu_temperatura()