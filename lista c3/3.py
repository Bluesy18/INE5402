### 3 ###

from random import randrange

# Define variáveis para verificar modo de operação e preenchimento, além de função para realizar a média
def verifica1(modo):
    while (modo != "M") and (modo != "S"):
        modo = input("Modo inexistente! Digite novamente: ").upper()
    return modo

def verifica2(n):
    while (n != "T") and (n != "R"):
        n = input("Opção inexistente! Digite novamente: ").upper()
    return n

def modoMedia(t, soma):
    media = soma/(((t**2)-t)/2)
    return media
    
# Cria variável de soma
soma = 0

# Usuário digita ordem da matriz
t = int(input("Digite a ordem da matriz: "))

# Cria matriz vazia
linha = [0] * t
matriz = [linha] * t

# Usuário digita como a matriz será preenchida
n = input("Escolha se os valores da matriz serão lidos do teclado (T) ou preenchidos aleatóriamente (R): ").upper()
n = verifica2(n)

# Se usuário deseja preencher com o teclado
if(n == "T"):
  for i in range (t):
    linha = []
    for j in range (t):
      numero = int(input(f"Digite o número {i}, {j}: "))
      # Se número da linha for maior do que o da coluna, soma número
      if (i > j):
        soma += numero
      linha.append(numero)

      matriz[i] = linha

# Se usuário deseja que o preenchimento seja aleatório
else:
  for i in range (t):
    linha = []
    for j in range (t):
      numero = randrange(0, 50)
      # Se número da linha for maior do que o da coluna, soma número
      if (i > j):
        soma += numero
      linha.append(numero)
  
      matriz[i] = linha

# Usuário digita a operação que será efetivada
modo = input("Se desejar a média, digite M. Se desejar a soma, digite S:").upper()
modo = verifica1(modo)

print()

# Mostra a matriz
for p in matriz:    
    print(*p, end="\n")

# Interpreta modo
if modo == "M":
    res = float(modoMedia(t,soma))
else:
    res = float(soma)

# Mostra o resultado 
print(f"\nO resultado da operação é {res}\n")

# Mostra matriz novamente
for p in matriz:    
    print(*p, end="\n")