### 5 ###

def verifica0(n):
  while ((n < 2) or (n > 100)):
    n = int(input("Valores inválidos! Digite novamente um inteiro: "))

  return n

def verifica1(listaInc):
  while (len(listaInc) != (n-1)):
    listaInc = [int(x) for x in (input(f"Valores inválidos! Digite {n-1} números da sequência novamente: ")).split()]

  return listaInc

n = int(input("Digite um inteiro: "))
n = verifica0(n)

lista = list(range(1, n+1))

listaInc = [int(x) for x in (input(f"Digite {n-1} números da sequência: ")).split()]
listaInc = verifica1(listaInc)

for i in range (len(listaInc)):
  lista.remove(listaInc[i])

print(*lista)



     
