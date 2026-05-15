# Crie um programa que leia o nome e o sobrenome de uma pessoa. Depois, 
# crie uma função chamada gerar_usuario que retorne um nome de usuário formado por:
# As três primeiras letras do nome
# As três últimas letras do sobrenome
# Tudo em letras minúsculas

def gerar_usuario(nome, sobrenome):
    nome_usuario = nome[:3].lower() + sobrenome[-3:].lower()
    return nome_usuario

nome = input("Digite o nome: ")
sobrenome = input("Digite o sobrenome: ")
usuario = gerar_usuario(nome, sobrenome)
print(f"O nome de usuário gerado é: {usuario}")

