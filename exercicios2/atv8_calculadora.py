'''8- Calculadora Simples
Enunciado:
Crie um programa que simule uma calculadora simples. O usuário deve informar dois números e a operação desejada (+, -, *, /) e o programa deve exibir o resultado da operação.'''

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação a ser realizada (+, -, *, /): ")

if operacao == "+":
    resul = num1 + num2
    print(f"O resultado de {num1} + {num2} é: {resul}")
elif operacao == "-":
    resul = num1 - num2
    print(f"O resultado de {num1} - {num2} é: {resul}")
elif operacao == "*":
    resul = num1 * num2
    print(f"O resultado de {num1} * {num2} é: {resul}")
elif operacao == "/":
    if num2 != 0:        
        resul = num1 / num2
        print(f"O resultado de {num1} + {num2} é: {resul}")
    else:
        print("Erro!!! divisão por zero não permitida.")
else:
    print("Operação inválida.")