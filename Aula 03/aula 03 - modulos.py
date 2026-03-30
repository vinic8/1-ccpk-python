import math

#Testando
num = int(input("Digite um numero:"))
raiz = math.sqrt(num)
print(f"a raiz de {num} é {raiz:.2f}")

graus = 45
rad = graus / 180 * math.pi
sen = math.sin(rad)
print(sen)

import random

#Testando 2
num_random = random.random()
print(num_random*10)

num_random_int = random.randint(1,10)
print(num_random_int)
