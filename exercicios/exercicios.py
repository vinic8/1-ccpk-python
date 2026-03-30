# EXERCÍCIO 1 - Área do círculo
raio = 5
pi = 3.14159
area = pi * raio**2
print(f"Área do círculo: {area:.2f}")

print()  # pular linha

# EXERCÍCIO 2 - Fahrenheit para Celsius
fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"Temperatura em Celsius: {celsius:.2f}")

print()

# EXERCÍCIO 4 - Total gasto
livros = 3 * 25
canetas = 2 * 5
total = livros + canetas
print(f"Total gasto: R$ {total:.2f}")

print()

# EXERCÍCIO 5 - Tempo de viagem
distancia = 150
velocidade = 60
tempo = distancia / velocidade
print(f"Tempo da viagem: {tempo:.2f} horas")

print()

# EXERCÍCIO 6 - Média simples
A = float(input("Digite a nota A: "))
B = float(input("Digite a nota B: "))
media = (A + B) / 2
print(f"Média aritmética: {media:.2f}")

print()

# EXERCÍCIO 7 - Média ponderada
A = float(input("Digite a nota A: "))
B = float(input("Digite a nota B: "))
media_ponderada = (A * 4 + B * 6) / 10
print(f"Média ponderada: {media_ponderada:.2f}")

print()

# EXERCÍCIO 8 - Peças
peca1 = input("Nome da peça 1: ")
qtd1 = int(input("Quantidade da peça 1: "))
valor1 = float(input("Valor unitário da peça 1: "))

peca2 = input("Nome da peça 2: ")
qtd2 = int(input("Quantidade da peça 2: "))
valor2 = float(input("Valor unitário da peça 2: "))

total = (qtd1 * valor1) + (qtd2 * valor2)
print(f"Valor total a pagar: R$ {total:.2f}")

print()

# EXERCÍCIO 9 - Troco
valor_produto = float(input("Valor do produto: "))
valor_pago = float(input("Valor pago: "))

troco = valor_pago - valor_produto
print(f"Troco: R$ {troco:.2f}")