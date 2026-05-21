preços = [100.0, 250.0, 500.0]
vinhos = ["Branco", "Tinto", "Champagne"]

vinho_escolhido = input("Digite o vinho a ser alterado: ")
novo_preço = input("Novo Preço: ")

novo_preço = novo_preço.replace("R$", "").replace(".", "").replace(",",".")
novo_preço = float(novo_preço)

posiçao_vinho = vinhos.index(vinho_escolhido)
preços[posiçao_vinho] = novo_preço

print(vinhos)
print(preços)

print(f"Preço do {vinho_escolhido}: {preços[posiçao_vinho]}") 