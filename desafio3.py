nomeAluno = input("Digite o nome do Aluno: ")
turma = input("Digite a Turma: ")

nota1 = float(input("Digite sua 1 nota: "))
nota2 = float(input("Digite sua 2 nota: "))
nota3 = float(input("Digite sua 3 nota: "))

media = (nota1 + nota2 + nota3)/3

if len(nomeAluno.strip()) == 0:
    print("Nenhum aluno encontrado")
else:
    print("Nome do Aluno: ", nomeAluno)
    print("Turma do Aluno", turma)
    print("Nota 1: ", nota1)
    print("Nota 2: ", nota2)
    print("Nota 3: ", nota3)
    print("Média", media)

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")


