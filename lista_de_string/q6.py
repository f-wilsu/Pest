# Leia uma frase digitada pelo usuário e conte quantas vogais ela possui. 
# O programa deve funcionar mesmo se o usuário digitar letras maiúsculas.

frase = input("Digite uma frase: ")
vogais = 'aeiouAEIOU'
contador_vogais = 0
for caractere in frase:
    if caractere in vogais:
        contador_vogais += 1
print(f"Quantidade de vogais: {contador_vogais}")