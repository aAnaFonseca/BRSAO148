'''5 - Crie um programa em Python que peça dois números e uma operação matemática (+, -, * ou /), e mostre o resultado de acordo com a operação escolhida.'''
# Solicita que o usuário digite o primeiro número
num1 = float(input("Digite o primeiro número: "))
# Solicita que o usuário digite o segundo número
num2 = float(input("Digite o segundo número: "))
# Solicita que o usuário digite a operação
operacao = input("Digite a operação (+, -, * ou /): ")
# Verifica a operação que o usuário digitou
if operacao == "+":
    # Soma os 2 números
    resul = num1 + num2
    print("O resultado da soma é: ", resul)

elif operacao == "-":
    resul = num1 - num2
    print("O resultado da subtração é: ", resul)

elif operacao == "*":
    resul = num1 * num2
    print("O resultado da multiplicação é: ", resul)

elif operacao == "/":
    # Verifica se o segundo número é diferente de zero
    if num2 != 0:
        resul = num1 / num2
        print("O resultado da divisão é: ", resul)
    else:
        print("Erro: divisão por ZERO não é permitida")
else:
    print("Operação inválida!")