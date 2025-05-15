import getpass

class Login:
    def __init__(self, nome_usuario, senha_usuario):
        self.nome_usuario = nome_usuario
        self.senha_usuario = senha_usuario

    def login(self):
        return self.nome_usuario == "camila" and self.senha_usuario == "123457"

if __name__ == "__main__":
    nome_usuario = input("Nome: ")
    senha_usuario = getpass.getpass("Senha: ")

    entrada = Login(nome_usuario, senha_usuario)
    if entrada.login():
        print("Login bem sucedido!")
    else:
        print("Falha no login.")
   
