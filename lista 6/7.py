### 7 ###

# Define a função que verifica se a capacidade foi excedida
def capacidade(c, n):

  # Cria variável de controle
  exce = 0

  # Verifica n vezes quantas pessoas entraram e quantas saíram
  for i in range (n):
    s, e = map(int, input("Digite quantas pessoas saíram e quantas entraram, respectivamente (separadas por espaço): ").split())

    if(i == 0):
      a = e - s

    elif(i != 0):
      saldo = e - s
      a = a + saldo

    if (a > c):
      exce = 1

  # Mostra se a capacidade foi excedida ou não
  if (exce == 1):
      print("S")

  else:
    print("N")

# Usuário digita quantidade de leituras e capacidade do elevador
n, c = map(int, input("Digite a quantidade de leituras e a capacidade do elevador (separadas por espaço): ").split())

# Chama função para verificar capacidade
capacidade(c, n)



