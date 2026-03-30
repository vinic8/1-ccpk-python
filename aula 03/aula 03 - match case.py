escolha_user = 0

match escolha_user:
    case 0:
        status = "sair do programa"
    case 1:
        staus = "entrar no programa"
    case _:
        status = "erro"
print(status)