### 1 ###

# Verifica se lista tem o comprimento correto
def verifica0(lista):
  while (len(lista) != 5):
    lista = [int(x) for x in (input("Digite 5 valores inteiros: ")).split()]

  return lista

# Conta a quantidade de noves
def nove(lista):
  cont = lista.count(9)
  return cont

# Mostra (se existir) a posição do primeiro 3
def tres(lista):
  if 3 in lista:
    pos = lista.index(3)
    return pos
  
  else:
    return "NaN"

# Conta quantos pares existem na lista
def par(lista):
  parc = 0
  for i in range(len(lista)):
    if (lista[i] % 2 == 0):
      parc += 1
  return parc

# Cria lista com os 5 valores inteiros digitados
lista = [int(x) for x in (input("Digite 5 valores inteiros: ")).split()]
lista = verifica0(lista)
cont = nove(lista)
pos = tres(lista)
parc = par(lista)

# Mostra o que foi solicitado na questão
print(f"O número 9 apareceu {cont} vez(es), o primeiro 3 foi digitado na posição {pos} e existe(m) {parc} par(es)")

### 2 ###

# Importa a biblioteca random
import random

# Cria lista
lista = []

# Adiciona 5 números pseudo-aleatórios (1-50) na lista OBS: o range de 50 foi aleatório 
for i in range (5):
  lista.append(random.randint(1, 50))

# Organiza do menor para o maior
for i in range (4):
        if lista[0] > lista[1]:
            lista[0], lista[1] = lista[1], lista[0]
        if lista[1] > lista[2]:
            lista[1], lista[2] = lista[2], lista[1]
        if lista[2] > lista[3]:
            lista[2], lista[3] = lista[3], lista[2]
        if lista[3] > lista[4]:
            lista[3], lista[4] = lista[4], lista[3]

# Mostra qual o maior e qual o menor número da lista
print(f"Lista: {lista}\nO maior número é o {lista[4]} e o menor é o {lista[0]}")

### 3 ###

# Verifica o tamanho da lista
def verifica0(lista, n):
  while (len(lista) != n):
    lista = [int(x) for x in (input("Digite 5 valores inteiros: ")).split()]

  return lista

# Digita o tamanho da lista
n = int(input("Digite o tamanho de sua lista: "))

# Adiciona n inteiros à lista
lista = [int(x) for x in (input(f"Digite {n} valores inteiros: ")).split()]
lista = verifica0(lista, n)

# Cria lista de repetidos
repetidos = []

# Verifica se há repetidos, se sim, os adiciona à lista de repetidos
for i in range (len(lista)):
  cont = lista.count(lista[i])
  if (cont > 1):
    if lista[i] not in repetidos:
      repetidos.append(lista[i])

# Mostra se existem (e quais) números repetidos ou não
if (len(repetidos) == 0):
  print("Não exitem números repetidos.")

else:
  print(*repetidos)

### 1172 ###

# Digita um número inteiro
for i in range (10):
  x = int(input("Digite um valor do vetor: "))

# Se ele for menor ou igual a zero, substitui o valor por 1
  if (x <= 0):
    x = 1

# Mosta o valor i do vetor X
  print(f"X[{i}] = {x}")

### 1173 ###

# Digita um valor para o i0 do vetor
x = int(input("Digite um valor para N[0]: "))

for i in range (10):

# Se for a primeira iteração, n0 = x
  if (i == 0):
    print (f"N[{i}] = {x}")
    xPassado = x

# Se não for a primerira iteração ni = xpassado*2
  else:
    print(f"N[{i}] = {xPassado*2}")
    xPassado = xPassado*2
         
### 1547 ###

# Verifica se valores obedecem os limites
def verifica0(qt, s):
  while ((qt < 4) or (qt > 10) or (s < 1) or (s > 100)):
    qt, s = map(int, input("Valores incorretos! Digite novamente a quantidade de alunos no grupo e qual o número a ser descoberto: ").split())

  return qt, s

# Verifica tamanho do grupo
def verifica1(grupo, qt):
  while (len(grupo) != qt):
    grupo = [int(x) for x in (input(f"Quantidade incorreta de alunos! Digite os valores de {qt} alunos: ")).split()]

  return grupo

# Cria variáveis para guardar qual aluno chegou mais próximo do número e qual a menor diferença entre o número escolhido e o número secreto
melhorAluno = ""
melhorDiferenca = 0

# Digita quantidade de camisetas a serem sorteadas
n = int(input("Digite quantas camisetas serão sorteadas: "))


for i in range(n):

  # Digita quantos alunos tem no grupo e qual o número secreto
  qt, s = map(int, input("Digite a quantidade de alunos no grupo e qual o número a ser descoberto: ").split())
  qt, s = verifica0(qt, s)

  # Cria lista com números escolhidos por cada aluno
  grupo = [int(x) for x in (input(f"Digite os valores de {qt} alunos: ")).split()]
  grupo = verifica1(grupo, qt)

  # Calcula a diferença entre o número escolhido e o número secreto
  for j in range (qt):
    dif = s - grupo[j]

    if (dif < 0):
      dif = dif*-1

    # Se for a primeira iteração, só guarda os valores
    if (j == 0):
      melhorAluno = j+1
      melhorDiferenca = dif

    # Se não for a primeira iteração, compara a diferença j com a melhor diferença, se for menor, se torna a melhor diferença
    if (j != 0):
      if(dif < melhorDiferenca):
        melhorDiferenca = dif
        melhorAluno = j+1

  # Mostra qual aluno disse o valor mais próximo do número secreto
  print(f"O valor mais próximo do número foi do aluno {melhorAluno}")

### 1743 ###

# Verifica tamanho da lista
def verifica0(conectores1):
  while (len(conectores1) != 5):
    conectores1 = [int(x) for x in (input(f"Quantidade errada! Digite novamente 5 números (0 ou 1): ")).split()]

  return conectores1

# Cria variável de resposta
res = "Y"

# Cria listas com os valores inteiros digitados
conectores1 = [int(x) for x in (input(f"Digite 5 números (0 ou 1): ")).split()]
conectores1 = verifica0(conectores1)

conectores2 = [int(x) for x in (input(f"Digite 5 números (0 ou 1): ")).split()]
conectores2 = verifica0(conectores2)

# Se a diferença entre os dois conectores for 0, não são compatíveis
for i in range (5):
  if((conectores1[i] - conectores2[i]) == 0):
    res = "N"
    break

# Mostra compatibilidade
print(res)

### 2399 ###

# Verifica se valores são 0 ou 1
def verifica0(x):
  while ((x != 0) and (x != 1)):
    x = int(input(f"Valor inválido! Digite novamente se existe (1) ou não existe (0) mina na célula {i}: "))

  return x

# Digita quantas células existem no campo minado
n = int(input("Digite quantas células existem no campo minado: "))

# Cria listas do campo e de varredura
campo = []
varredura = []

# Usuário digita se existe mina na célula n
for i in range (n):
  x = int(input(f"Digite se existe (1) ou não existe (0) mina na célula {i}: "))
  x = verifica0(x)
  campo.append(x)

# Soma as casas vizinhas para dar o número de minas vizinhas e adiciona na lista de varredura
for j in range (n):
  
  if (j == 0):
    varredura.append((campo[j]+campo[j+1]))

  elif (j == n-1):
    varredura.append((campo[j]+campo[j-1]))

  else:
    varredura.append((campo[j-1]+campo[j]+campo[j+1]))

# Mostra a lista de varredura, elemento por elemento
for k in range (len(varredura)):
  print(varredura[k])


