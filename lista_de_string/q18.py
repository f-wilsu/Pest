# Crie um programa que simule um pequeno cadastro de usuário.

def validar_nome(nome):
    return len(nome) >= 3 and nome.replace(" ", "").isalpha()

def validar_email(email):
    return "@" in email and "." in email and " " not in email

def validar_senha(senha):
    tem_letra = any(c.isalpha() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    return len(senha) >= 8 and tem_letra and tem_numero

nome  = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
senha = input("Digite sua senha: ")

if validar_nome(nome) and validar_email(email) and validar_senha(senha):
    print("Cadastro aceito! ")
else:
    print("Cadastro recusado! ")
    if not validar_nome(nome):
        print(" Nome inválido!")
    if not validar_email(email):
        print("E-mail inválido!")
    if not validar_senha(senha):
        print("Senha inválida!")