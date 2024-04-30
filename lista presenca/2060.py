### 2060 ###

def verificaN(n):
  while((n < 1) or (n > 1000)):
    n = int(input("Valor inválido! Digite a quantidade de números na lista novamente: "))

  return n

n = int(input("Digite a quantidade de números na lista: "))
n = verificaN(n)

lista = [int(x) for x in (input(f"Digite {n} números inteiros (separados por espaço): ")).split()]
num = [2, 3, 4, 5]
cont = [0, 0, 0, 0]

for i in range (n):

  for j in range (len(cont)):
    if(lista[i] % num[j] == 0):
      cont[j] += 1

print(f"{cont[0]} Multiplo(s) de 2\n{cont[1]} Multiplo(s) de 3\n{cont[2]} Multiplo(s) de 4\n{cont[3]} Multiplo(s) de 5\n")

