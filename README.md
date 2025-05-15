# Atividade de engenharia de software 
`Aluna: Camila Ferreira de Almeida` `-` `BSI 5` `-` `Código disponivel na branch (dev)`

### Atividade que poderia utilizar (i) TDD, (ii) Refatoração, (iii) Integração.
Escrever um código em  JavaScript, __Python__ ou outra linguagem de conhecimento

---
Foi usado o Sigaa (Sistema Integrado de Gestão de Atividades Acadêmicas) como cénario. Para a resolução dessa atividade foi usado TDD (Test-Driven Development) em uma aplicação muito simples em python: a tela de login.

Foi criado um teste chamado *__test.login.py__*. Foram definidos três testes para verificar se o login está funcionando corretamente:

```
from login_sigaa import Login

def teste_login():
    assert Login("camila", "123457").login() == True
    assert Login("julia", "134567").login() == False
    assert Login("andre", "123456").login() == False
```

Depois foi criado um arquivo *__login_sigaa.py__* com a seguinte função:

```
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

```

Somente se __nome_usuario__ e __senha_usuario__ for igual a __camila__ e __'123457'__ o código ira passar no teste.
