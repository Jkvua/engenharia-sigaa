from login_sigaa import Login

def teste_login():
    assert Login("camila", "123457").login() == True
    assert Login("julia", "134567").login() == False
    assert Login("andre", "123456").login() == False