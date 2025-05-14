'''6 - Crie um programa que receba um número do usuário e diga se ele é positivo, negativo ou igual a zero.'''

num = float(input("Digite um número: "))
if num > 0:
    print("O número é positivo")
elif num < 0:
    print("O número é negativo")
else:
    print("O número é zero.")