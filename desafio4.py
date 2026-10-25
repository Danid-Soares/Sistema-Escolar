#criação de lista#
alunos = []

quantidade = int(input("Quantos alunos serão cadastrados"))

for i in range(quantidade):
    nome = input("Nome do Aluno: ")
    turma = input("Digite a turma: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2)/2

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    alunos.append([nome, turma, nota1, nota2, media, situacao])

if len(alunos) == 0:
    print("Nenhum aluno encontrado")
else:
    print("\n--- Boletim Escolar ---")

    for aluno in alunos:
        print("Nome do Aluno: ", aluno[0])
        print("Turma do Aluno", aluno[1])
        print("Nota 1: ", aluno[2])
        print("Nota 2: ", aluno[3])
        print("Média", aluno[4])
        print("Situação",aluno[5])
    