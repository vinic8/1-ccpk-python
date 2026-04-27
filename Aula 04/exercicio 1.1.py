def validar_nota(nota):
    while nota < 0 or nota > 10:
        print("A nota é de 0 a 10")
        nota = float(input("Digite a nota 1: "))
    return nota

nota1 = float(input("Digite a nota 1: "))
nota1 = validar_nota(nota1)

nota2 = float(input("Digite a nota 2: "))
nota2 = validar_nota(nota2)

media = (nota2 + nota1) / 2
print(media)