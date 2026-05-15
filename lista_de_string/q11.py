# Crie uma função chamada inverter_texto que receba uma 
# string como parâmetro e retorne essa string invertida.

def inverter_texto(texto):
    texto = texto[ : :-1]
    return texto

palavra = input("Digite uma palavra: ")
texto_invertido = inverter_texto(palavra)
print(f"O texto invertido é: {texto_invertido}")