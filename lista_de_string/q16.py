# 1. **Crie uma função chamada `limpar_frase` que receba uma frase e retorne
#  uma nova frase contendo apenas letras e espaços.**
# Caracteres como números, pontos, vírgulas, exclamações e símbolos devem ser removidos.

def limpa_frase(frase):
    nova_frase = ''
    for caractere in frase:
        if caractere.isalpha() or caractere == ' ':
            nova_frase += caractere
    return nova_frase

frase = input("Digite uma frase: ")
frase_limpa = limpa_frase(frase)
print(f"Frase limpa: {frase_limpa}")
