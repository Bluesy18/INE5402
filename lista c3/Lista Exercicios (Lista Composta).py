### 1 ###

# Cria listas vazias e variável de resposta
res = "S"
pessoas = []
info = []
pesados = []
leves = []
velhos = []

# Enquanto resposta for "S"
while res == "S":
    # Usuário digita quantas pessoas serão cadastradas
    n = int(input("Quantas pessoas serão cadastradas: "))
    
    for i in range (n):
        # Usuário digita as informações
        info = input("Digite o nome, idade e peso (separado por espaço): ").split()

        # Interpreta e define o maior e o menor peso
        if(i == 0):
            menorPeso = info[2]
            maiorPeso = info[2]
        else:
            if(info[2] >= maiorPeso):
                maiorPeso = info[2]
        
            if(info[2] <= menorPeso):
                menorPeso = info[2]
                
        pessoas.append(info[:])
    
    
    # Transforma em inteiros
    for p in pessoas:
        int(p[1])
        int(p[2])
        
        # Interpreta qual(quais) pessoa(s) tem o maior e o menor peso, além de quais têm mais de 20 anos
        if (p[2] == maiorPeso):
            pesados.append(p[0])
            
        if (p[2] == menorPeso):
            leves.append(p[0])
            
        if (p[1] > "20"):
            velhos.append(p[1])

    # Mostra resultado para o usuário
    print(f"{n} pessoas foram cadastradas.\nO(s) dono(s) do maior peso é/são: {pesados}\nO(s) dono(s) do menor peso é/são: {leves}\nAs pessoas acima de vinte anos são: {velhos}")
    
    # Continua (ou não) loop
    res = input("Deseja continuar?(s ou n): ").upper()
    
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

### 4 ###

# Cria lista vazia de quadrados pretos e de letras
preto = []
letras = ["A", "B", "C", "D", "E"]

# Usuário digita número de questões
n = int(input("Digite o número de questões: "))

# Enquanto n for diferente de 0
while (n != 0):
  # Usuário digita valor referente ao nível de cinza das opções da questão
  for i in range (n):
    questao = [int(x) for x in (input(f"Digite um número de 0 a 255: ")).split()]

    # Se for menor ou igual a 127, é considerado preto
    for p in questao:
      if (p <= 127):
        preto.append(p)

    # Se não houver exatamente 1 opção preenchida, mostra "*"
    if (len(preto) != 1):
      print("*")
      preto.clear()
      
    # Traduz a opção marcada para uma das letras
    else:
      letra = questao.index(preto[0])
      print(letras[letra])
      preto.clear()
      
  # Continua (ou não) o loop
  n = int(input("Digite o número de questões: "))

### Exercico do slide ###

# Cria lista de pares, ímpares e do resultado
par = []
impar = []
resultado = []

# Usuário digita 10 inteiros
for i in range(10):
    n = int(input("Digite um número inteiro: "))
    # Separa os pares e os ímpares
    if (n%2) == 0 :
        par.append(n)
    
    else:
        impar.append(n)
    
# Ordena as listas de maneira crescente
par.sort()
impar.sort()

# Junta os pares e ímpares em uma só lista
resultado.append(par)
resultado.append(impar)

# Mostra o resultado
print(resultado)
        
      
    
        
        
         