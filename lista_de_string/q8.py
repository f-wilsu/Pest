# Leia o nome completo de uma pessoa e mostre:
# O nome todo em letras maiúsculas
# O nome todo em letras minúsculas
# A quantidade total de caracteres, sem contar espaços
# A primeira letra do nome

nome_completo = input("Digite seu nome completo: ")
print(f"Nome em letras maiúsculas: {nome_completo.upper()}")
print(f"Nome em letras minúsculas: {nome_completo.lower()}")
print(f"Quantidade de caracteres (sem espaços): {len(nome_completo.replace(' ', ''))}")
print(f"Primeira letra do nome: {nome_completo[0]}")