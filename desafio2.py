usuario = []

nome_cadastro = input("Digite o seu nome de usuario para cadastro: ")
senha_cadastro = input("Digite sua Senha para cadastro: ")

usuario.append([nome_cadastro, senha_cadastro]) 

tentativas = 0 
acesso_autorizado = False

while tentativas < 3 and not acesso_autorizado:

    for cadastrado in usuario:
            nome_usuario = input("Digite o nome do Usuario: ")
            senha = input("Digite sua senha: ")

            if nome_usuario == usuario[0][0] and senha == usuario[0][1]:
                print("Acesso autorizado")
                acesso_autorizado = True
                break
            else:
                tentativas += 1
                print("Usuario ou senha incorretos")
                
else:
    print("Acesso bloqueado! Você excedeu o limite de tentativas.")

    


