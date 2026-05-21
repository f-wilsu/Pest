# adicionar um item na lista
# append() é a função para adicionar um item no final da lista 
# insert() é a função para adicionar um item em uma posição específica da lista, ele não substitui o item da posição, ele empurra os itens para a direita
# extend() é a função para adicionar uma lista em outra lista


lista_preço = [55000, 21000, 21600, 265000]
lista_produtos = ["bmw", "audi", "mercedes", "ferrari"]
lista_produtos.append("bugatti") # adiciona o item "bugatti" no final da lista

lista2_produtos = ["m4", "preto", "carro"]
lista_produtos.extend(lista2_produtos) # adiciona a lista2_produtos como um item na lista_produtos
print(lista_produtos)


# inserir um item em uma posição específica da lista
lista_produtos.insert(1, "batman") # insere o item "batman" na posição
print(lista_produtos)


# contar quantas vezes um item aparece na lista
print(lista_produtos.count("bmw")) # conta quantas vezes o item "bmw" aparece na lista

# ordenar uma lista
lista_produtos.sort() # quando ele está vazio ele ordena em ordem alfabética, quando tem números ele ordena do menor para o maior
print(lista_produtos)

# quando tiver números e letras na lista, ele vai ordenar os números primeiro e depois as letras, porque os números tem um valor ASCII menor do que as letras
# quando tiver letras maiúsculas e minúsculas na lista, ele vai ordenar as letras maiúsculas primeiro, porque as letras maiúsculas tem um valor ASCII menor do que as letras minúsculas
lista_produtos.append("BMW") # adiciona o item "BMW" no final da lista
print(lista_produtos)
lista_produtos.sort() 
print(lista_produtos)

lista_preço.sort(reverse=True) # ordena a lista de preços do menor para o maior
print(lista_preço)

