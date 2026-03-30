#logica E (and)

verifica_email = False
verifica_senha = False

verifica_login = verifica_email and verifica_senha
print(verifica_login)

if verifica_login:
    print("Entra no programa")

#logica ou (or)

logica_ou = False or False
print(logica_ou)

#negação

negacao = not False
print(negacao)
if not verifica_login:
    print(verifica_login)