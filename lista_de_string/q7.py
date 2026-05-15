# Leia uma string digitada pelo usuário e informe:
# Quantas letras ela possui
# Quantos números ela possui
# Quantos outros caracteres ela possui


string = input("Digite uma string: ")
letras = 0
numeros = 0     
outros = 0
for caractere in string:
    if (caractere >= 'a' and caractere <= 'z') or (caractere >= 'A' and caractere <= 'Z'):
        letras += 1
    elif caractere >= '0' and caractere <= '9':
        numeros += 1
    else:
        outros += 1
print(f"Quantidade de letras: {letras}")
print(f"Quantidade de números: {numeros}")
print(f"Quantidade de outros caracteres: {outros}")