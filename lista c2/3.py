### 3 ###

def verifica0(lista, n):
  while (len(lista) != n):
    lista = [int(x) for x in (input("Digite 5 valores inteiros: ")).split()]

  return lista

n = int(input("Digite o tamanho de sua lista: "))

lista = [int(x) for x in (input(f"Digite {n} valores inteiros: ")).split()]
lista = verifica0(lista, n)

repetidos = []

for i in range (len(lista)):
  cont = lista.count(lista[i])
  if (cont > 1):
    if lista[i] not in repetidos:
      repetidos.append(lista[i])

if (len(repetidos) == 0):
  print("Não exitem números repetidos.")

else:
  print(*repetidos)

