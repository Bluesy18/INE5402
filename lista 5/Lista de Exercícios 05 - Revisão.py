######## Fiz a 1, 2, 3, 4 e 14 com o André ########

### 1 ###

# Cria variável de resposta
r = "S"

# Cria variáveis dos jogadores
j1 = "pedra"
j2 = "papel"

while r=="S":
    # Jogadores decidem jogada
    j1 = input("Digite pedra, papel ou tesoura: ").lower()
    j2 = input("Digite pedra, papel ou tesoura: ").lower()
    
    # Verifica escolhas e mostra resultado
    if(j1 == j2):
        r = input("Empatou. Deseja continuar jogando? (S/N): ").upper()
        
    elif((j1 != "pedra") and (j1 != "papel") and (j1 != "tesoura")) or ((j2 != "pedra") and (j2 != "papel") and (j2 != "tesoura")):
        r = input("Opção inválida. Deseja tentar novamente? (S/N): ").upper()
        
    elif ((j1 == "pedra" and j2 == "papel") or (j1 == "papel" and j2 == "tesoura") or (j1 == "tesoura" and j2 == "pedra")):
        r = input("J2 ganhou. Deseja continuar jogando? (S/N): ").upper()
        
    elif ((j2 == "pedra" and j1 == "papel") or (j2 == "papel" and j1 == "tesoura") or (j2 == "tesoura" and j1 == "pedra")):
        r = input("J1 ganhou. Deseja continuar jogando? (S/N): ").upper()
        
### 2 ###

# Usuário digita 3 números inteiros
n1, n2, n3 = map(int, input("Digite três números inteiros separados por espaço: ").split())

# Organiza em ordem crescente
for i in range(2):
    if n1 > n2:
        n1, n2 = n2, n1
    if n2 > n3:
        n2, n3 = n3, n2
        
# Mostra os números em ordem
print(f"Primeiro: {n1}\nSegundo: {n2}\nTerceiro: {n3}")

### 3 ###

# Cria variável dos números
x = 0
y = 1

while (x != y):
    # Usuário informa os números
    x, y = map(int, input("Digite dois números inteiros separados por espaço: ").split())
    
    # Verifica e informa se números foram informados em ordem crescente os decrescente
    if (x < y):
        print("Crescente")
        
    elif (x > y):
        print("Decrescente")

### 4 ###

# Cria variável de soma de números ímpares
soma = 0

# Cria variável para contar vezes
v = 1

# Usuário digita quantos testes deseja realizar
n = int(input("Digite o número de testes que deseja fazer: "))

while (v != (1+n)):
    for i in range(n):
        # Acrescenta vezes
        v += 1
        # Usuário digita números
        x, y = map(int, input("Digite dois números inteiros separados por espaço: ").split())
        for j in range(x+1, y):
            # Verifica se número é ímpar
            if(j%2 != 0):
                # Aumenta contador de números ímpares
                soma += j                  
        
        # Mostra soma dos números ímpares
        print(soma)
        # Zera soma
        soma = 0

### 5 ###

# Usuário digita o valor
valor = round(float(input("Digite um valor: ")), 2)

# Calcula quantidade mínima de notas
n100 = valor/100
r100 = valor % 100
n50 = r100/50
r50 = r100 % 50
n20 = r50/20
r20 = r50 % 20
n10 = r20/10
r10 = r20 % 10
n5 = r10/5
r5 = r10 % 5
n2 = r5/2
r2 = r5 % 2

# Calcula quantidade mínima de moedas
valorC = int(valor*100)
rm100 = valorC % 100
m50 = rm100/50
rm50 = rm100 % 50
m25 = rm50/25
rm25 = rm50 % 25
m10 = rm25/10
rm10 = rm25 % 10
m5 = rm10/5
rm5 = rm10 % 5

# Mostra quantidade mínima de notas e moedas
print(f"NOTAS:\n{int(n100)} nota(s) de R$ 100.00\n{int(n50)} nota(s) de R$ 50.00\n{int(n20)} nota(s) de R$ 20.00\n{int(n10)} nota(s) de R$ 10.00\n{int(n5)} nota(s) de R$ 5.00\n{int(n2)} nota(s) de R$ 2.00\nMOEDAS:\n{int(r2)} moeda(s) de R$ 1.00\n{int(m50)} moeda(s) de R$ 0.50\n{int(m25)} moeda(s) de R$ 0.25\n{int(m10)} moeda(s) de R$ 0.10\n{int(m5)} moeda(s) de R$ 0.05\n{int(rm5)} moeda(s) de R$ 0.01")

### 6 ###

# Usuário digita distância e velocidades
d, vf, vg = map(int, input("Digite a distância entre os barcos, a velocidade do fugitivo e a velocidade da guarda costeira, repectivamente (separadas por espaço): ").split())

# Verifica se os valores são válidos
if ((1 <= d <= 100) and (1 <= vf <= 100) and (1 <= vg <= 100)):
  
  # Calcula distância da guarda e o tempo de ambos
  dg = (144 + (d**2))**0.5
  tf = 12/vf
  tg = dg/vg

  # Verifica se a guarda chega a tempo e mostra o resultado
  if (tg <= tf):
    print("S")
  
  else:
    print("N")

else:
  print("Valores inválidos!")

### 7 ###

# Usuário digita os tempos
l, r = map(int, input("Digite o tempo do líder e do retardatário, respectivamente (separados por espaço): ").split())

# Calcula a volta em que se tornará retardatário
d = r-l
v = r/d

# Arredonda para cima
va = int(-(-v // 1))

# Mostra volta em que o líder ultrapassará o último colocado
print(va)

### 8 ###

# Usuário digita as notas
n1a, n2a, n3a, n4a, n5a = map(float, input("Digite as cinco notas separados por espaço: ").split())

# Arredondamento das notas
n1 = round(n1a, 1)
n2 = round(n2a, 1)
n3 = round(n3a, 1)
n4 = round(n4a, 1)
n5 = round(n5a, 1)

# Verifica a qual a menor e a maior nota
for i in range(4):
    if n1 > n2:
        n1, n2 = n2, n1
    if n2 > n3:
        n2, n3 = n3, n2
    if n3 > n4:
        n3, n4 = n4, n3
    if n4 > n5:
        n4, n5 = n5, n4

# Calcula nota final
nf = round(n2+n3+n4, 1)

# Mostra a nota final
print(nf)

### 9 ###

# Variável de contagem de teste
t = 1

# Variável de resposta
r = "S"

# Variável de débito
d = 0

while (r == "S"):
  # Usuário digita o númerod e depósitos
  n = int(input("Digite o número de depósitos: "))

  for i in range (n):

    # Usuário digita os valores dos depósitos
    j, z = map(int, input("Digite o valor depositado para Joãozinho e para Zezinho, respectivamente (separado por espaço): ").split())
    
    # Calcula débito
    d = j - z + d

    # Mostra qual o teste
    if (i == 0):
      print(f"Teste {t}")
    
    # Mostra o débito
    print(d)

    # Ao fim, pergunta se o usuário gostaria de testar novamente
    if (i == n-1):
      t += 1
      r = input("Deseja testar novamente? (S/N): ").upper()

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

### 11 ###

# Cria variável z
z = -1

# Cria variável de contagem
cont = 1

# Cria variável de soma
soma = 0

# Usuário digita valores de x e de z
x = int(input("Digite um número inteiro: "))
z = int(input("Digite outro número inteiro: "))

# Se valor for negativo, fecha o programa
if (x < 0):
  print("Tente novamente")

else:

  # Enquanto valor de z for menor ou igual a x, pede outro valor para z
  while (z <= x):
    z = int(input("Digite outro número inteiro: "))
  
  # Enquanto a soma dos valores for menor ou igual a z, acrescenta o próximo número da sequência
  while (soma <= z):
   cont += 1
   x += 1
   soma += x
  
  # Mostra quantos números foram necessários somar
  print(cont)

### 12 ###

# Usuário digita coordenada da bola
x, y = map(int, input("Digite as coordenadas da bola (separados por espaço): ").split())

# Verifica e informa se bola está dentro ou fora
if((0 <= x <= 432) and (0 <= y <= 468)):
  print("dentro")

else:
  print("fora")

### 13 ###

# Cria variável caminho
caminho = ""

# Cria variável dos flippers
p = 2
r = 3

# Verifica se valores são compatíveis com 1 e 0
while ((p != 1) and (p != 0)) or ((r != 1) and (r != 0)):
  # Usuário digita estado do flipper
  p, r = map(int, input("Digite o valor de P e de R (separados por espaço): ").split())

# Verifica os valores dos flippers e seleciona o caminho
if (p == 0):
  caminho = "C"
  
elif((p == 1) and (r == 0)):
  caminho = "B"

elif((p == 1) and (r == 1)):
  caminho = "A"
  
# Informa o caminho
print(caminho)

### 14 ###

# Cria variável de contagem
cont = 0

# Usuário digita quantas bandejas foram usadas
n = int(input("Digite quantas bandejas foram usadas: "))

for i in range(n):
    # Usuário digita quantidade de latas e de copos
    l, c = map(int, input("Digite quantas latas e copos, respectivamente, foram usados (separados por espaço): ").split())
    
    # Verifica se existem mais latas que copos
    if l>c :
        # Aumenta contagem de copos derrubados
        cont += c

# Mostra quantos copos foram derrubados
print(cont)

### 15 ###

# Usuário digita os valores
a, g, rA, rG = map(float, input("Digite preço do álcool, preço da gasolina, rendimento do álcool e rendimento da gasolina (separados por espaço): ").split())

# Verifica o custo-benefício, depois informa qual combustível mais vale a pena
if(rA/a <= rG/g):
  print("G")

else:
  print("A")








    



