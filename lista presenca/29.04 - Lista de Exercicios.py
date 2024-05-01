### 5 ###

# Verifica se n pertence ao limite informado
def verifica0(n):
  while ((n < 2) or (n > 100)):
    n = int(input("Valores inválidos! Digite novamente um inteiro: "))

  return n

# Verifica tamano da listaInc
def verifica1(listaInc):
  while (len(listaInc) != (n-1)):
    listaInc = [int(x) for x in (input(f"Valores inválidos! Digite {n-1} números da sequência novamente: ")).split()]

  return listaInc

# Usuário digita valor inteiro
n = int(input("Digite um inteiro: "))
n = verifica0(n)

# Cria lista de 1 até n
lista = list(range(1, n+1))

# Usuário digita números que formam lista incompleta
listaInc = [int(x) for x in (input(f"Digite {n-1} números da sequência: ")).split()]
listaInc = verifica1(listaInc)

# Remove elementos repetidos
for i in range (len(listaInc)):
  lista.remove(listaInc[i])

# Mosta elemento que falta na lista
print(*lista)

### 1471 ###

# Verifica se valores obedecem as restrições
def verifica0(n, r):
  while (((r > n) and (r!= 0) and (n != 0)) or (n < 1 and (n != 0)) or (r < 1 and r!= 0)):
    n, r = map(int, input("Valores inválidos! Digite novamente quantos mergulhadores mergulharam e quantos voltaram: ").split())

  return n, r

# Verifica tamanho da lista volt
def verifica1(volt):
  while (len(volt) != r):
    volt = [int(x) for x in (input(f"Valores inválidos! Digite novamente a identificação dos {r} mergulhadores que voltaram (separados por espaço): ")).split()]

  return volt

# Interpreta a lista merg e seleciona o resultado
def resultado(merg):
  if (len(merg) == 0):
    res = "*"

  else:
    res = merg

  return res

# Usuário digita quantos mergulhadores mergulharam e quantos voltaram
n, r = map(int, input("Digite quantos mergulhador(es) mergulharam e quantos voltaram: ").split())
n, r = verifica0(n, r)

while ((n != 0) and (r != 0)):

# Cria lista de mergulhadores
  merg = list(range(1, n+1))

# Usuário digita mergulhadores que voltaram e os adiciona à lista volt
  volt = [int(x) for x in (input(f"Digite a identificação dos {r} mergulhadores que voltaram (separados por espaço): ")).split()]
  volt = verifica1(volt)

# Remove mergulhadores que voltaram da lista merg
  for i in range (len(volt)):
    merg.remove(volt[i])

# Mostra quantos megulhadores não voltaram
  res = resultado(merg)
  print(*res)

# Continua o loop até n ou r ser 0
  n, r = map(int, input("Digite quantos mergulhadores mergulharam e quantos voltaram: ").split())
  n, r = verifica0(n, r)

### 1533 ###

# Verifica se n obedece às restrições
def verifica0(n):
  while (((n < 2) and (n != 0)) or (n > 1000)):
    n = int(input("Valor inválido! Digite novamente a quantidade de suspeitos: "))

  return n

# Usuário digita quantidade de suspeitos
n = int(input("Digite a quantidade de suspeitos: "))
n = verifica0(n)

while (n != 0):
    # Cria lista de susperitos e a ordena de menos suspeito até mais suspeito
    sus = [int(x) for x in (input("Digite quais são os suspeitos (separados por espaço): ")).split()]
    
    susOrd = sorted(sus)
    
    # Culpado é o segundo mais suspeito
    culpado = susOrd[len(susOrd) - 2]
    
    for i in range(len(sus)):
    
        if culpado == sus[i]:
          culpadoIndice = i + 1
    
    # Mostra o índice do culpado
    print(f" O índice do culpado é {culpadoIndice}")
    
    # Continua o loop até n ser 0
    n = int(input("Digite a quantidade de suspeitos: "))
    n = verifica0(n)

### 1961 ###

# Verifica se p e n obedecem aos limites
def verifica0(p, n):
  while ((p < 1) or (p > 5) or (n < 2) or (n > 100)):
    p, n = map(int, input("Valores inválidos! Digite a altura do pulo do sapo e a quantidade de canos (separados por espaço): ").split())

  return p, n

# Cria lista com as alturas dos canos digitadas pelo usuário
def verifica1(hcanos):
  while (len(hcanos) != n):
    hcanos = [int(x) for x in (input(f"Valores inválidos! Digite a altura de  {n} cano(s) (separados por espaço): ")).split()]

  return hcanos

# Interpreta variável gameover define resultado
def res(gameover):
  if (gameover == 0):
    res = "YOU WIN"

  else:
    res = "GAME OVER"

  return res

# Cria variável de controle "gameover"
gameover = 0

# Usuário digita altura do pulo do sapo e quantidade de canos
p, n = map(int, input("Digite a altura do pulo do sapo e a quantidade de canos (separados por espaço): ").split())
p, n = verifica0(p, n)

# Cria lista com alturas de canos digitadas pelo usuário
hcanos = [int(x) for x in (input(f"Digite a altura de  {n} cano(s) (separados por espaço): ")).split()]
hcanos = verifica1(hcanos)

# Verifica se diferença entre pulo e altura é letal ou não
for i in range (len(hcanos) - 1):
  dif = hcanos[i+1] - hcanos[i]

  if(dif < 0 ):
    dif = dif*-1

  if(dif > p):
    gameover = 1
    break

# Mostra resultado
print(res(gameover))

### 2060 ###

# Verifica se n obedece limites
def verificaN(n):
  while((n < 1) or (n > 1000)):
    n = int(input("Valor inválido! Digite a quantidade de números na lista novamente: "))

  return n

# Usuário digita a quantidade de números da lista
n = int(input("Digite a quantidade de números na lista: "))
n = verificaN(n)

# Cria lista com números digitados pelo usuário
lista = [int(x) for x in (input(f"Digite {n} números inteiros (separados por espaço): ")).split()]

# Cria lista de números que lista[i] podem ser múltiplos
num = [2, 3, 4, 5]

# Cria contador
cont = [0, 0, 0, 0]

# Verifica se números da lista são múltiplos dos números num
for i in range (n):

  for j in range (len(cont)):
    if(lista[i] % num[j] == 0):
      cont[j] += 1

# Mostra quantos números são múltipos dos números num
print(f"{cont[0]} Multiplo(s) de 2\n{cont[1]} Multiplo(s) de 3\n{cont[2]} Multiplo(s) de 4\n{cont[3]} Multiplo(s) de 5\n")

