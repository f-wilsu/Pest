#  Leia uma palavra digitada pelo usuário e mostre apenas os caracteres que
#  estão em posições pares.

palavra = input("DIgite uma palavra: ")

for i in range(len(palavra)):
    if i % 2 == 0:
        print(palavra[i])

#outra maneira de fazer mais simples

palavra = input("Digite uma palavra: ")
nova_palavra = palavra[ : :2]
print(f"Nova palavra: {nova_palavra}")