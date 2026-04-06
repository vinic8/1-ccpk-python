#exercicio 2
num = int(input("digite um numero:"))
if num % 2 == 0:
    print("seu numero e par")
else:
    print("seu numero e impar")

#exercicio 3
num1 = float(input("digite um numero:"))
num2 = float(input("digite um segundo numero:"))
if num1 > num2:
    print(f"O numero {num1} é maior")
elif num2 > num1:
    print(f"O numero {num2} é maior")
elif num1 == num2:
    print(f"{num1} e {num2} são iguais")
else:
    print("numero invalido")

#exercicio 4
print("digite suas notas")
nota1 = float(input("qual foi sua nota do 1:"))
nota2 = float(input("qual foi sua nota do 2:"))
nota3 = float(input("qual foi sua nota do 3:"))
nota4 = float(input("qual foi sua nota do 4:"))
media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 7:
  print(f"sua media e de {media} e voce esta aprovado")
elif media >= 5:
  print(f"sua media e de {media} e voce esta de recuperação")
else:
  print(f"sua media e de {media} e voce esta reprovado")

#exercicio 5
num3 = int(input("digite um numero:"))
num4 = int(input("digite um numero:"))
if num4 % num3 == 0:
    print(f"O {num4} é multiplo do {num3}")
else:
    print("Eles nao são multiplos")

#exercicio 6
num5 = float(input("digite um numero:"))
num6 = float(input("digite outro numero:"))
operacao = input("Digite a operação (+, -, *, /): ")
if operacao == '+':
    soma = num5 + num6
    print(f'a soma de{num5} e {num6} é {soma}')
elif operacao == '-':
    sub = num5 - num6
    print(f'a diferença de{num5} e {num6} é {sub}')
elif operacao == '*':
    mult = num5 * num6
    print(f'O produto de{num5} e {num6} é {mult}')
elif operacao == '/':
    if num6 != 0:
        div = num5 / num6
        print(f'O quociente de{num5} e {num6} é {div}')
    else:
        print("Erro: divisão por zero")
        exit()
else:
    print("Operação inválida")
    exit()

#exercicio 7
idade = int(input("Digite sua idade:"))

if idade < 18:
    print("seu voto é opcional")
elif idade > 70:
    print("seu voto é opcional")
else:
    print("seu voto é obrigatório")

#exercicio 8
salario = float(input("Digite o salário do colaborador: R$ "))
if salario <= 280:
    percentual = 20
elif salario <= 700:
    percentual = 15
elif salario <= 1500:
    percentual = 10
else:
    percentual = 5
aumento = salario * (percentual / 100)
novo_salario = salario + aumento
print(f"Salário antes do reajuste: R$ {salario:.2f}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")

#exercicio 9
