# encontrar um elemenyto na lista (a posição do elemwnto)

lista_produtos = ["bmw", "audi", "mercedes", "ferrari"]
print("bugati" in lista_produtos) # verificar se um elemento existe na lista
print("bmw" in lista_produtos) # verificar se um elemento existe na lista
print("BMW" in lista_produtos) # verificar se um elemento existe na lista

posiçao = lista_produtos.index("mercedes") # encontrar a posição de um elemento na lista
print(posiçao)

pedaço_lista = lista_produtos[posiçao:] # pegar a posição da mercedes e vai até o final da lista
print(pedaço_lista)

# edita um idtem da lsta
lista_preço = [55000, 21000, 21600, 265000]
novo_preço = round(lista_preço[0] * 1.1, 2)  # aumentar o preço do primeiro item da lista em 10%, esse round é para arredondar o valor para 2 casas decimais
lista_preço[0] = novo_preço        # atualizar o preço do primeiro item da lista
print(lista_preço)


# remover um item da lista
# existe mais de uma forma de remover um item da lista, a função pop() remove o item pelo índice, a função remove() remove o item pelo valor
# qual é a diferença entre as duas funções? a função pop() retorna o item removido, enquanto a função remove() não retorna nada

lista_produtos.remove("audi") # remove o item "audi" da lista
                              # se o item não existir na lista, a função remove() vai gerar um erro
print(lista_produtos)                           

