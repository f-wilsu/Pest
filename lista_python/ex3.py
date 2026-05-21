lista_produtos = ["bmw", "audi", "mercedes", "ferrari"]


# remover um item da lista
# existe mais de uma forma de remover um item da lista, a função pop() remove o item pelo índice, a função remove() remove o item pelo valor
# qual é a diferença entre as duas funções? a função pop() retorna o item removido, enquanto a função remove() não retorna nada

lista_produtos.remove("audi") # remove o item "audi" da lista
                              # se o item não existir na lista, a função remove() vai gerar um erro
print(lista_produtos)

print("-------------------------")

lista_produtos.pop(0) # remove o item da posição 0 da lista, ou seja, "bmw"
print(lista_produtos)

# eu támbem consigo armazenar o item removido em uma variável
item_removido = lista_produtos.pop(0) # remove o item da posição
print(item_removido) # imprime o item removido, ou seja, "mercedes"
print(lista_produtos) # imprime a lista atualizada, ou seja, ['ferrari']