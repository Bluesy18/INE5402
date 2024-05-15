### 1 (1796) ###

# Define funções para verificar o valor de q, o tamanho da lista "pesquisa" e se seu itens estão de acordo com as limitações
def verifica0 (q):
  while ((q < 4) or (q > 233000)):
    q = int(input("Número inválido! Digite novamente quantas pessoas fizeram parte da pesquisa: "))

def verifica1 (pesquisa):
  while (len(pesquisa) != q):
    pesquisa = [int(x) for x in (input(f"Número inválido de opiniões! Digite novamente {q} opiniões que variam entre satisfatório (0) e não satisfatório (1) (separadas por espaço): ")).split()]
  for p in pesquisa:
      if((p != 0) and (p != 1)):
        certo = 0
        break
      else:
        certo = 1
  while (certo == 0):
    pesquisa = [int(x) for x in (input(f"Número inválido para opiniões! Digite novamente {q} opiniões que variam entre satisfatório (0) e não satisfatório (1) (separadas por espaço): ")).split()]
    for p in pesquisa:
      if((p != 0) and (p != 1)):
        certo = 0
        break
      else:
        certo = 1
  return pesquisa

# Verifica se 0 é maioria ou não
def maioria(pesquisa):
  soma = 0
  res = ""
  for l in pesquisa:
    soma += l

  if (soma < len(pesquisa)/2):
    res = "S"

  else:
    res = "N"

  return res  

# Usuário digita quantas pessoas fizeram parte da pesquisa
q = int(input("Digite quantas pessoas fizeram parte da pesquisa: "))

# Usuário digita as opiniões das pessoas
pesquisa = [int(x) for x in (input(f"Digite {q} opiniões que variam entre satisfatório (0) e não satisfatório (1) (separadas por espaço): ")).split()]
pesquisa = verifica1(pesquisa)
res = maioria(pesquisa)

# Mostra se a maioria acha a situação atual satisfatória (ou não)
print(res)

### 2 (1164) ###

# Verifica valor de x de acordo com as limitações
def verifica0 (x):
  while ((x < 1) or (x > 20)):
    x = int(input("Número inválido! Digite novamente um número inteiro entre 1 e 20"))

  return x

# Usuário digita quantos casos deseja testar
n = int(input("Digite quantos casos você deseja testar: "))

# Cria lista de divisores
divisores = []

# Usuário digita números inteiros de 1 a 20
for i in range (n):
  x = int(input("Digite um número inteiro entre 1 e 20: "))
  x = verifica0(x)
  # Se for divisor, adiciona à lista de divisores
  for j in range(x):
    if(j != 0):
      if(x % j == 0):
        divisores.append(j)
  soma = 0
  for p in divisores:
    soma += p

  # Se soma dos divisores for igual a x, x é perfeito, caso contrário, não é
  if (soma == x):
    print(f"{x} eh perfeito")
  
  else:
    print(f"{x} não eh perfeito")

  # Limpa lista de divisores
  divisores = []

### 2 (1164) ###

# Verifica valor de x de acordo com as limitações
def verifica0 (x):
  while ((x < 1) or (x > 20)):
    x = int(input("Número inválido! Digite novamente um número inteiro entre 1 e 20"))

  return x

# Usuário digita quantos casos deseja testar
n = int(input("Digite quantos casos você deseja testar: "))

# Cria lista de divisores
divisores = []

# Usuário digita números inteiros de 1 a 20
for i in range (n):
  x = int(input("Digite um número inteiro entre 1 e 20: "))
  x = verifica0(x)
  # Se for divisor, adiciona à lista de divisores
  for j in range(x):
    if(j != 0):
      if(x % j == 0):
        divisores.append(j)
  soma = 0
  for p in divisores:
    soma += p

  # Se soma dos divisores for igual a x, x é perfeito, caso contrário, não é
  if (soma == x):
    print(f"{x} eh perfeito")
  
  else:
    print(f"{x} não eh perfeito")

  # Limpa lista de divisores
  divisores = []

### 5  ###

# Cria variáveis para operação
somaTop = 0
somaPar = 0
somaPrin = 0
somaUlt = 0
medPrin = 0
prodSec = 1 
                
# Usuário digita ordem da matriz
t = int(input("Digite a ordem da matriz: "))

# Cria matriz
linha = [0] * t
matriz = [linha] * t

# Usuário insere números na matriz
for i in range (t):
    linha = []
    for j in range (t):
        nume = int(input(f"Digite o número {i}, {j}: "))

        # Interpreta se casos solicitados ocorreram
        if (nume%2 == 0):
            somaPar += nume
        
        if (i == j):
            somaPrin += nume
            medPrin = somaPrin/t
            
        if (i+j == t):
            prodSec = nume*prodSec
            
        if (j-i == 1):
            somaTop += nume
            mediaTop = somaTop/(t-1)
            
        if (j == t):
            somaUlt += nume
        
        linha.append(nume)
        
    matriz[i] = linha

# Verifica qual o menor número    
for k in range(t):
    if (k == 0):
        menor = matriz[0][k]
        
    elif (matriz[0][k] < menor):
        menor = matriz[0][k]
        
for p in matriz:    
    print(*p, end="\n")
    
# Mostra resultados solicitados
print(f"a) {somaPar}\nb) {medPrin}\nc) {prodSec}\nd) {mediaTop}\ne) {somaUlt}\nf) {menor}")

### 6 ###
from random import randrange

# Cria listas de jogo e resultado
jogo = []
resultado = []

# Usuário digita quantos jogos deseja fazer
n = int(input("Quantos jogos você deseja?: "))

# Cria jogos
for i in range(n):
    for j in range(6):
        jogo.append(randrange(60))
    resultado.append(jogo[:])
    jogo.clear()

# Mostra jogos        
for p in range(n):
    print(f"Jogo {p+1}: {resultado[p]}") 

### 7 ###

# Define função para calcular a média
def calcMedia(info):
  soma = 0
  for p in info:
    soma += p

  media = round((soma/3), 2)

  return soma, media

# Define funções para verificar listas "info" e "consulta"
def verifica0 (info):
  for n in info:
      if((n < 0) or (n > 10)):
        certo = 0
        break
      else:
        certo = 1
  while (certo == 0):
    info = [float(x) for x in (input(f"Notas inválidas! Digite novamente as 3 notas do aluno {nome}: ")).split()]
    for n in info:
      if((n < 0) or (n > 10)):
        certo = 0
        break
      else:
        certo = 1

  return info

def verifica1(consulta):
  for l in boletim:
      if(consulta == l[1]):
        igual = 1
        break
      else:
        igual = 0
  while (igual == 0):
    consulta = input("Nome inválido! Digite novamente o nome do aluno que desejas consultar: ")
    for l in boletim:
      if(consulta == l[1]):
        igual = 1
        break

  return consulta

# Cria listas de alunos, infos e boletim
alunos = []
info = []
boletim = []

# Usuário digita quantos alunos irá informar
n = int(input("Digite quantos alunos deseja informar: "))

# Usuário digita nome do aluno e suas 3 notas e a partir disso, separa informações em seus devidos lugares
for i in range (n):
  nome = input(f"Digite o nome do {i+1}º aluno: ")
  info = [float(x) for x in (input(f"Digite as 3 notas do aluno {nome}: ")).split()]
  soma, media = calcMedia(info)
  info = verifica0(info)
  info.append(media)
  info.append(nome)
  alunos.append(info)
  boletim.append([media, nome])
  info = []

# Mostra boletim
print(boletim)

# Usuário digita se deseja consultar notas individuais
res = input("Deseja consultar as notas individuais? (S/N): ").upper()

# Se sim...
while (res == "S"):

  # Usuário digita nome do aluno que deseja consultar
  consulta = input("Digite o nome do aluno que desejas consultar: ")
  consulta = verifica1(consulta)
  
  # Consulta e mostra notas individuais
  for m in alunos:
    if(consulta in m):
      print(f"Notas individuais: {m[0]}, {m[1]} e {m[2]}")

  # Continua loop
  res = input("Deseja consultar as notas individuais? (S/N): ").upper()
  
      
 


        
    

