'''3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.'''

val = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F, K): ").upper()
destino = input("Digite a unidade de destino (C, F, K): ").upper()
if origem == "C":
    if destino == "F":
        resul = (val * 9/5) + 32
    elif destino == "K":
        resul = val + 273.15
    else:
        resul = val
elif origem == "F":
    if destino == "C":
        resul = (val -32) * 5/9
    elif destino == "K":
        resul = (val - 32) * 5/9 + 273.15
    else:
        resul = val
elif origem == "K":
    if destino == "C":
        resul = val - 273.15
    elif destino == "F":
        resul = (val - 273.15) * 9/5 + 32
    else:
        resul = val
else:
    resul = None
if resul is not None:
    print(f"Temperatura convertida: {resul:.2f} {destino}")
else:
    print("Unidade inválida informada.")