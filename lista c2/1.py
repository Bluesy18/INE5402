### 1 ###

def verifica0(lista):
  while (len(lista) != 5):
    lista = [int(x) for x in (input("Digite 5 valores inteiros: ")).split()]

  return lista

def nove(lista):
  cont = lista.count(9)
  return cont

def tres(lista):
  if 3 in lista:
    pos = lista.index(3)
    return pos
  
  else:
    return "NaN"

def par(lista):
  parc = 0
  for i in range(len(lista)):
    if (lista[i] % 2 == 0):
      parc += 1
  return parc

lista = [int(x) for x in (input("Digite 5 valores inteiros: ")).split()]
lista = verifica0(lista)
cont = nove(lista)
pos = tres(lista)
parc = par(lista)

print(f"O número 9 apareceu {cont} vez(es), o primeiro 3 foi digitado na posição {pos} e existe(m) {parc} par(es)")

