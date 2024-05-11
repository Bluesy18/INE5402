### 2 ###

from random import randrange

# Define funções para verificar se escolha está dentro dos limites, se o modo digitado existe e para calcular a média
def verifica(t,escolha):
    while ((0 >= escolha) or (escolha > t)):
        escolha = int(input("Número incorreto!! Digite novamente: "))
    return escolha 

def verifica2(modo):
    while (modo != "M") and (modo != "S"):
        modo = input("Modo inexistente! Digite novamente: ").upper()
    return modo

def modoMedia(escolha,t,soma):
    media= soma/t
    return media
    
# Cria variável de soma
soma = 0

# Usuário digita ordem da matriz
t = int(input("Digite a ordem da matriz: "))

# Cria matriz vazia
linha = [0] * t
matriz = [linha] * t
    
# Preenche a matriz com números aleatórios (até 50)
for i in range (t):
    linha = []
    for j in range (t):
        linha.append(randrange(0, 50))
        
    matriz[i] = linha

# Usário escolhe a linha que vai operar    
escolha = int(input("Digite a linha que você deseja fazer a operação: "))
escolha = verifica(t,escolha)

# Soma números da linha
for p in matriz[escolha-1]:
    soma += p

# Usuário digita qual operação será realizada
modo = input("Se desejar a média, digite M. Se desejar a soma, digite S: ").upper()
modo = verifica2(modo)

print()

# Mostra a matriz
for p in matriz:    
    print(*p, end="\n")

# Interpreta modo
if modo == "M":
    res = modoMedia(escolha,t,soma)
else:
    res = soma
    
# Mostra o resutado
print(f"\nO resultado da operação é {res}")


