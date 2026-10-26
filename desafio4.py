#criação de lista
alunos = []

aprovados = 0
recuperacao = 0
reprovados = 0
soma_medias = 0

quantidade = int(input("Quantos alunos serão cadastrados: "))

for i in range(quantidade):
    nome = input("Nome do Aluno: ")
    turma = input("Digite a turma: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2)/2

    soma_medias += media

    if media >= 7:
        situacao = "Aprovado"
        aprovados += 1
    elif media >= 5:
        situacao = "Recuperação"
        recuperacao += 1
    else:
        situacao = "Reprovado"
        reprovados += 1

    alunos.append([nome, turma, nota1, nota2, media, situacao])

   

if len(alunos) == 0:
    print("Nenhum aluno encontrado")
else:
    print("\n--- Boletim Escolar ---")
    for aluno in alunos:
        print("Nome do Aluno: ", aluno[0])
        print("Turma do Aluno: ", aluno[1])
        print("Nota 1: ", aluno[2])
        print("Nota 2: ", aluno[3])
        print("Média: ", aluno[4])
        print("Situação: ",aluno[5])

    media_geral = (soma_medias)/quantidade

    print("\n --- Situação dos Alunos --- ")
    print("Total de Alunos: ", quantidade)
    print("Aprovados: ", aprovados)
    print("Em Recuperação: ", recuperacao)
    print("Reprovados: ", reprovados)
    print("Média geral da Turma: ", round(media_geral, 2))
