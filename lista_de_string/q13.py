# 1. **Crie uma função chamada `concatenar_fatiar` que receba duas strings como entrada.**
# A função deve retornar uma nova string formada por:
# Os três primeiros caracteres da primeira string
# Os três últimos caracteres da segunda string

def concatenar_fatiar(string1, string2):
    nova_string = string1[:3] + string2[-3:]
    return nova_string

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
resultado = concatenar_fatiar(string1, string2)
print(f"A nova string concatenada é: {resultado}")