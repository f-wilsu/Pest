rota = ["São Paulo", "Campinas", "Jundiai", "Sorocaba"]
novas_cidades = ["Itu", "Ceará"]

rota.extend(novas_cidades)
print(rota)
posiçao_sorocaba = rota.index("Sorocaba") + 1
print(f"Sorocaba é a {posiçao_sorocaba}ª cidade da rota:")