#Leia uma palavra digitada pelo usuário e mostre uma nova palavra 
# em que o último caractere seja substituído por #.

palavra = input("DIgite uma palavra: ")
nova_palavra = palavra[:-1] + '#'
print(f"Nova palavra: {nova_palavra}")
