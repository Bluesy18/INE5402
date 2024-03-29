### 10 ###

# Cria variável de valor
valor = 1

while (valor != 0):
  # Usuário digita o valor
  valor = int(input("Digite um valor: "))

  # Calcula quantidade mínima de notas
  n50 = valor//50
  r50 = valor % 50
  n10 = r50//10
  r10 = r50 % 10
  n5 = r10//5
  r5 = r10 % 5

  if(valor != 0):
    # Mostra quantidade necessária de cada nota
    print(n50, n10, n5, r5)