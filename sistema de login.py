usuario_lista = ["admin"]
senha_lista = ["admin"]
while True:
    usuario = input("Insira um novo usuario:")
    senha = input("Insira uma nova senha:")
    senha_confirmacao = (input("Confirme a sua senha:"))
    if(senha == senha_confirmacao):
        usuario_lista.append(usuario)
        senha_lista.append(senha)
        print("Novo usuario e senha cadastrados.")
        break
    else:
        print("As senhas nao correspondem.")

print(usuario_lista, senha_lista)

while True:
    usuario = input("Digite o nome de usurario:")
    senha = input("Digite a senha:")
    if (usuario != usuario_lista and senha != senha_lista):
        print("Usuario ou senha incorretos.")
    else:
        print("Usuario Logado.")
        break
