nome_correto = "admin"
senha_correta = "123"
tentativas = 0

while tentativas < 3:
        nome_usuario = input("Digite o nome do Usuario")
        senha = input("Digite sua senha")

        if nome_usuario == nome_correto and senha == senha_correta:
            print("Acesso autorizado")
            break
        else:
            tentativas += 1
            print("senha incorreta tente novamente")

else:
    print("Acesso bloqueado! Você excedeu o limite de tentativas.")

    


