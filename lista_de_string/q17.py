# Crie um programa que peça ao usuário para digitar uma senha. Depois, crie uma função chamada
#  validar_senha que receba essa senha e retorne True se ela for válida ou False se for inválida.

def validar_senha(senha):
    if len(senha) < 8 or " " in senha:
        return False
    if not any(c.isupper() for c in senha):
        return False
    if not any(c.islower() for c in senha):
        return False
    if not any(c.isdigit() for c in senha):
        return False
    return True

senha = input("Digite uma senha: ")
if validar_senha(senha):
    print("Senha válida.")

else:
    print("Senha inválida. A senha deve ter pelo menos 8 caracteres, conter letras maiúsculas, minúsculas e números, e não pode conter espaços.")