'''5- Verificador de Número Primo
Enunciado:
Crie um programa que solicite um número inteiro positivo ao usuário e verifique se ele é um número primo. Um número primo só é divisível por 1 e por ele mesmo.'''

num = int(input("Digite um número inteiro positivo: "))
if num < 2:
    print(f"O número {num} não é primo.")
else:
    e_primo = True
    for i in range(2, num):
        if num % i == 0:
            e_primo = False
            break
    if e_primo:
        print(f"O número {num} é primo.")
    else:
        print(f"O número {num} não é primo.")