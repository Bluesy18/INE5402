### 3 ###

from random import randrange

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
    
soma = 0

t = int(input("Digite a ordem da matriz: "))

linha = [0] * t
matriz = [linha] * t

n = input("Escolha se os valores da matriz serão lidos do teclado (T) ou preenchidos aleatóriamente (R): ").upper()
n = verifica2(n)

if(n == "T"):
  for i in range (t):
    linha = []
    for j in range (t):
      numero = int(input(f"Digite o número {i}, {j}: "))
      if (i > j):
        soma += numero
      linha.append(numero)

      matriz[i] = linha
    
else:
  for i in range (t):
    linha = []
    for j in range (t):
      numero = randrange(0, 50)
      if (i > j):
        soma += numero
      linha.append(numero)
  
      matriz[i] = linha

modo = input("Se desejar a média, digite M. Se desejar a soma, digite S:").upper()
modo = verifica1(modo)

print()

for p in matriz:    
    print(*p, end="\n")

if modo == "M":
    res = float(modoMedia(t,soma))
else:
    res = float(soma)
    
print(f"\nO resultado da operação é {res}\n")

for p in matriz:    
    print(*p, end="\n")