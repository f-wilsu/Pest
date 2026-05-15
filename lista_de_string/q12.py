# 1. **Crie uma função chamada `eh_palindromo` que receba uma palavra e
#  retorne `True` se ela for um palíndromo ou `False` caso contrário.**

#OBS: Uma palavra é palíndromo quando pode ser lida da mesma forma de trás para frente.

def eh_palindromo(palavra):
    palavra = palavra.lower() 

    if palavra == palavra[ : :-1]:
        return True
    else:
        return False

palavra = input("Digite uma palavra: ")
if eh_palindromo(palavra):
    print(f"A palavra '{palavra}' é um palíndromo.")

else:
    print(f"A palavra '{palavra}' não é um palíndromo.")        