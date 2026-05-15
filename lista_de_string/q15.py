# 1. **Uma loja usa códigos de produto com as seguintes regras:**
# Deve ter exatamente 6 caracteres
# Os 2 primeiros caracteres devem ser letras
# Os 4 últimos caracteres devem ser números
# Crie uma função chamada `validar_codigo` que receba um código e retorne se ele é válido ou inválido.


def validar_codigo(codigo):
    if len(codigo) == 6 and codigo[:2].isalpha() and codigo[2:].isdigit():
        return True
    else:
        return False

codigo = input("Digite o código do produto: ")
  
if validar_codigo(codigo):
    print("O código é válido.") 

else:    
     print("O código é inválido.")        