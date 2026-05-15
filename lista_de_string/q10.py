# Crie uma função chamada contar_caracteres que receba uma string como parâmetro
#  e retorne a quantidade de caracteres dessa string sem usar a função len(). Depois, leia uma palavra do usuário, chame a função e mostre o resultado.

def contar_caracteres(string):
    contador = 0 
    for caractere in string:
        contador += 1 
    return contador 
    
palavra = input("Digite uma palavra: ")
quantidade = contar_caracteres(palavra)
print(f"A quantidade de caractere é: {quantidade}")

