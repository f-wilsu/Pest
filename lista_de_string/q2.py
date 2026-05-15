#Leia uma palavra digitada pelo usuário e mostre 
# seus caracteres do último até o primeiro.

palavra = input("Digite uma palavra: ")
for letra in palavra[::-1]:
    print(letra)