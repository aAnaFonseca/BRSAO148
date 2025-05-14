'''7 - Crie um programa que contenha uma lista com números e calcule a soma total desses números usando um laço for.'''

# Definição de números em uma lista [] - lista
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
soma = 0
for num in nums:
    soma += num
print("A soma dos números é: ", soma)