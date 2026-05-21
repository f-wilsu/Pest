estoque = ["monitor", "teclado", "mouse", "headset"]
estoque.append("webcam")
posiçao_teclado = estoque.index("teclado")
estoque[posiçao_teclado] = "teclado mecânico"
print(estoque)

impressora_no_estoque = "impressora" in estoque
print(f"Impressora no estoque: {impressora_no_estoque}")


estoque.remove("mouse")
print(estoque)