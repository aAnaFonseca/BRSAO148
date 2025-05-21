'''5 - Crie um programa com uma função que cadastre alunos e suas respectivas notas.
O sistema deve:
Solicitar o nome do aluno.
Solicitar 3 notas válidas (entre 0 e 10).
Armazenar os dados em um dicionário, onde a chave é o nome e o valor é uma lista de notas.
Permitir o cadastro de vários alunos até que o usuário digite "fim".
Exibir ao final:
A lista de alunos e suas médias.
O aluno com a maior média.
Use def para as funcionalidades e try/except para tratar entradas inválidas.'''

def obter_notas():
    notas = []
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Digite a {i}ª nota (0 a 10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida. Digite um valor entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
    return notas

def cadastrar_alunos():
    alunos = {}
    while True:
        nome = input("Digite o nome do aluno (ou 'fim' para encerrar): ").strip()
        if nome.lower() == "fim":
            break
        if nome == "":
            print("O nome do aluno não pode estar vazio.")
            continue
        if nome in alunos:
            print("Aluno já cadastrado. Use um nome diferente.")
            continue
        notas = obter_notas()
        alunos[nome] = notas
    return alunos

def calcular_medias(alunos):
    medias = {}
    for nome, notas in alunos.items():
        medias[nome] = sum(notas) / len(notas)
    return medias

def exibir_resultados(alunos):
    if not alunos:
        print("Nenhum aluno foi cadastrado.")
        return
    medias = calcular_medias(alunos)
    print("\nMédias dos alunos:")
    for nome, media in medias.items():
        print(f"{nome}: {media:.2f}")
    aluno_top = max(medias, key=medias.get)
    print(f"\nAluno com a maior média: {aluno_top} ({medias[aluno_top]:.2f})")

# Execução do programa
alunos_cadastrados = cadastrar_alunos()
exibir_resultados(alunos_cadastrados)
