### 2 ###

import random

lista = []
for i in range (5):
  lista.append(random.randint(1, 50))

for i in range (4):
        if lista[0] > lista[1]:
            lista[0], lista[1] = lista[1], lista[0]
        if lista[1] > lista[2]:
            lista[1], lista[2] = lista[2], lista[1]
        if lista[2] > lista[3]:
            lista[2], lista[3] = lista[3], lista[2]
        if lista[3] > lista[4]:
            lista[3], lista[4] = lista[4], lista[3]

print(f"Lista: {lista}\nO maior número é o {lista[4]} e o menor é o {lista[0]}")