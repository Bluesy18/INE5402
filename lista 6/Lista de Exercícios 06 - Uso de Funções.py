### 1 ###

# Define função de contador
def contador(i,f,p):
    
    # Mostra os parâmetros da contagem
    print(f"Contagem de {i} até {f} de {p} em {p}.")
    
    # Se passo for negativo, transforma-o em positivo
    if (p < 0) :
        p *= -1
    
    # Se passo for nulo, assume-se passo 1
    if (p==0):
        p=1
        
    # Se início da contagem for menor, começa a contagem
    if i<f:
        cont = i
        while (cont <= f):
            print(f"{cont}",end=" ")
            cont += p
        print(" Fim! ")
    else:
        cont = i
        while (cont >= f):
            print(f"{cont}",end=" ")
            cont -= p
        print(" Fim! ")
 
# Passa parâmetros pra função contador
contador(1,10,1)

contador(10,0,2)

print("Contagem personalizada: ")

# Usuário digita quais devem ser os parâmetros para uma contagem personalizada
ini,fim, pas = [int(x) for x in input("Digite inicio, fim e passo: ").split()]
contador(ini,fim,pas)

### 2 ###

# Calcula e mostra área de um quadrilátero
def area(l, c):
    areac = l*c
    print(areac)

# Usuário digita largura e comprimento, em seguida passa esses valores como parâmetros para a função área()
l, c = map(float, input("Digite a largura e comprimento: ").split())
area(l, c)

### 3 ###

# Função calcula novo salário e diferença do atual com o anterior e mostra pro usuário além desses valores, o acréscimo em percentual
def salario(sal, acre, per):
    sala = acre*sal
    dif = sala - sal
        
    print(f"Novo salario: {sala}\nReajuste ganho: {dif}\nEm percentual : {per}")
    
sal = -1

# Enquanto salário for negativo, continua pedindo para usuário digitar o salário
while (sal < 0):
    sal = float(input("Digite seu salário: "))

# Interpreta qual será o valor do acréscimo, baseado no salário digitado
if (sal <= 400.00):
        acre = 1.15
        per = "15%"
    
elif (sal <= 800.00):
        acre = 1.12
        per = "12%"
        
elif (sal <= 1200.00):
        acre = 1.10
        per = "10%"
        
elif (sal <= 2000.00):
        acre = 1.07
        per = "7%"
        
elif (sal > 2000.00):
        acre = 1.04
        per = "4%"

# Chama função para calcular salário        
if (sal >= 0):
    salario(sal, acre, per)

### 4 ### 

# Função verifica se valores estão dentro dos limites, caso não estiverem, pede novo input
def verificaG (saida, tempo, fuso):
    while ((0 > saida) or (saida > 23) or (1 > tempo) or (tempo > 12) or (-5 > fuso) or (fuso > 5)):
        saida, tempo, fuso = map(int,input("Valores incorretos! Digite novamente: ").split())

# Função calcula tempo de chegada
def app(saida, tempo, fuso):
    soma = saida+tempo+fuso
    while (soma >= 24):
        soma -= 24
    print(soma)

# Usuário digita hora de saída, tempo de viagem e o fuso horário
saida, tempo, fuso = map(int,input("Digite a hora de saida, o tempo de viagem e o fuso: ").split())

# Chama funções para verificar valores e horário de chegada
verificaG(saida, tempo, fuso)
app(saida, tempo, fuso)

### 5 ###

# Define função para somar sucessor até ultrapassar z
def soma(x, xini, z):
  soma = 0

  while soma <= z:
      soma += x
      x += 1

  # Mostra quantos números foram necessários ser somados para ultrapassar z
  print(x - xini)


# Usuário digita um número inteiro
x = int(input("Digite um número inteiro: "))

# Armazena x inicial
xini = x

while True:
    # Usuário digita outro número inteiro
    z = int(input("Digite um outro número inteiro: "))
    
    # Quando z for maior que x, interrompe o loop
    if z > x:
        break
    
# Chama a função de soma
soma(x, xini, z)

### 6 ###

# Define função que localiza ponto no plano cartesiano
def local(x, y):
  if ((x > 0) and (y > 0)):
    print("primeiro")

  elif ((x < 0) and (y > 0)):
    print("segundo")

  elif ((x < 0) and (y < 0)):
    print("terceiro")

  elif ((x > 0) and (y < 0)):
    print("quarto")

while True:
  # Usuário digita coordenada
  x, y = map(int, input("Digite a coordenada de X e de Y (separados por espaço): ").split())

  # Chama função localizadora
  local(x, y)

  # Se alguma coordenada for 0, encerra o programa
  if ((x == 0) or (y == 0)):
    break

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

### r1 ###

# Verifica se valores do colchão estão de acordo com os limites
def verifica0 (a, b, c):
    while((a < 1 or a > 300) or (b < 1 or b > 300) or (c < 1 or c > 300)):
        a, b, c = map(int, input("Dimensões do colchão erradas, digite novamente: ").split())

# Verifica se valores da porta estão de acordo com os limites
def verifica1 (h, l):
    while((h < 10 or h > 250) or (l <10 or l > 250)):
       h, l = map(int, input("Dimensões da porta erradas, digite novamente: ").split())

# Interpreta se colchão passa ou não ela porta e retorna variável r
def verifica2 (a, b, c, h, l):
    if(a <= h and b <= l) or (a <= l and b <= h):
        r = 0
    
    elif(a <= h and c <= l) or (a <= l and c <= h):
        r = 0
        
    elif(b <= h and c <= l) or (b <= l and c <= h):
        r = 0

    else:
        r = 2
        
    return r
    
# Usuário digita as dimensões do colchão, em seguida, as dimensões são verificadas
a, b, c = map(int, input("Digite as dimensões do colchão (separadas por espaço): ").split())
verifica0(a, b, c)

# Usuário digita as dimensões da porta, em seguida, as dimensões são verificadas
h, l = map(int, input("Digite as dimensões da porta (separadas por espaço): ").split())
verifica1( h , l)

# Chama a função verifica2() com os seguintes parâmetros
verifica2(a, b, c, h, l)
    
# Dependendo do valor da variável r, diz ao usuário se o colchão passa ou não pela porta
if(verifica2(a, b, c, h, l) == 0):
    print("O colchão está adequado ao tamanho. Parabéns por sua compra!")
    
elif (verifica2(a, b, c, h, l) == 2):
    print("Você deve procurar outro colchão.")
        
### 2 ###

# Função calcula melhor nota e media
def notas(nome, nota, mNome, mNota, somaNota, media):
      # Soma as notas
      somaNota += nota
      # Verificar qual aluno tirou a melhor nota
      if(i == 1):
              mNome = nome
              mNota = nota
              
      elif(i != 1):
         if(mNota < nota):
             mNome = nome
             mNota = nota
                  
      # Calcula a média das notas
      media = round((somaNota/i), 2)

      # Retorna seguintes variáveis
      return media, mNome, mNota, somaNota
    
# Função verifica se nota obedece os limites, se não, pede outro input
def verifica(nota):
    while ((nota < 0) or (nota > 10)):
      nota = round(float(input("Nota inválida. Digite novamente: ")), 2)

# Função define situação do melhor aluno
def situacao(mNota):

    # Interpreta a melhor nota e define situação
    if(mNota >= 5.75):
        situacao = "aprovado"

    elif(mNota >= 2.75):
        situacao = "de recuperação"

    elif(mNota < 2.75):
        situacao = "reprovado"

    # Retorna a situação 
    return situacao
    
# Define variáveis
mNome = ""
mNota = 0
somaNota = 0
media = 0
    
# Faz seguintes procedimentos ara 5 alunos diferentes
for i in range(1, 6):
    # Usuário digita o nome dos alunos e das notas
    nome = input("Digite seu nome: ")
    nota = round(float(input("Digite sua nota média (entre 0 e 10): ")), 2)

    # Chama função verifica()
    verifica(nota)

    # Armazena valores retornados
    media, mNome, mNota, somaNota = notas(nome, nota, mNome, mNota, somaNota, media)
    
# Chama função situacao()
situacao(mNota)

# Mostra qual foi o melhor aluno, sua nota e situação, além da média da turma
print(f"A pessoa com a melhor nota foi o(a): {mNome} \nSua nota foi: {mNota}\nEle/Ela foi {situacao(mNota)}\nA média da turma foi: {media}")

### 3 ###

# Função verifica se número n é par ou ímpar
def verifica(n):

    if (n%2 == 0):
        return "par"
    else:
        return "impar"
    
# Função conta quantos números pares foram digitados
def contpar(contapar):

    return contapar + 1

# Função conta quantos números ímpares foram digitados
def contimpar(contaimpar):
     
     return contaimpar + 1

# Define variáveis de contagem e as converte para inteiro
contapar = 0
contaimpar = 0

int(contapar)
int(contaimpar)
    
# Pede 10 vezes..;    
for i in range(10):
    # Que o usuário digite um número inteiro
    n = int(input("Digite um número inteiro: "))

    # Mostra se número é par ou ímpar
    print(f"O número é {verifica(n)}.")

    # Armazena variáveis com os valores retornados
    if (n%2 == 0):
        contapar = contpar(contapar)

    else:
        contaimpar = contimpar(contaimpar)
    
# Mostra quantidade de números pares e ímpares
print(f"Você digitou {contapar} números pares.\nVocê digitou {contaimpar} números ímpares.")

### 4 ###

# Função que conta primos
def contaPrimo (n, m): 
  somaP = 0

  for i in range (m, n-1, -1):

    # Variável de controle (np == 0 -> primo, np == 1 -> não primo)
    np = 0 

    for j in range (2, i):

      # Divide i por j, a fim de descobrir se ele é divisível por algum número, se for, incrementa 1 na variável np e interrompe o loop
      if (i%j == 0):
        np += 1
        break

    # Se número for primo, acrescenta na contagem de primos
    if (np == 0):
      somaP += 1

  # Retorna quantidade de rimos no intervalo
  return somaP

# Usuário digita intervalo
n, m = map(int, input("Digite o primeiro e o útimo número do intervalo (separados por espaço): ").split())

# Mostra ao usuário quantos primos existem naquele intervalo
print(f"Existem {contaPrimo(n, m)} números primos nesse intervalo")

### 5 ###

# Função soma as idades inseridas
def soma(somaidade, idade, i):
    
    somaidade += idade
    i += 1
    
    # Retorna valor da soma e quantas idades foram inseridas
    return somaidade, i

# Função calcula e retorna média das idades
def media(somaidade, i):
    media = somaidade/i
    return media

# Define variáveis no escopo global
i = 0
idade = 0
somaidade = 0

# Enquanto a idade inserida não for negativa, pede ao usuário digitar idade
while True:
    idade = int(input("Digite a idade: "))
    if(idade < 0):
        break
    else:
        somaidade, i = soma(somaidade, idade, i)

# Mostra média de idade
print(f"A média das idades é {media(somaidade, i)}")

### 6 ###

# Função calcula quantos positivos foram digitados e qual a média deles
def positivo (n, qtdPos, somaPos, media):
  if (n > 0):
    qtdPos += 1
    somaPos += n
    media = round(somaPos/qtdPos, 1)

  # Retorna quantidade, média e soma de positivos
  return qtdPos, media, somaPos

# Define variáveis
qtdPos = 0
somaPos = 0
media = 0

# Pede 6 vezes...
for i in range (6):
  # Que o usuário digite um número
  n = float(input("Digite um número: "))

  # Armazena variáveis retornadas da função positivo()
  qtdPos, media, somaPos = positivo(n, qtdPos, somaPos, media)

# Mostra quantos valores positivos foram digitados, além de sua média
print(f"{qtdPos} valores positivos\n{media}")

### 7 ###

# Funções verificam se os números digitados obedecem aos limites, caso não obedecerem, pede para usuário digitar novamente
def verifica0 (n):
  while ((n < 1) or (n > 10)):
    n = int(input("Quantidade incorreta! Digite novamente: "))

def verifica1 (p):
  while ((p < 1) or (p > 100)):
    p = int(input("Valor incorreto! Digite novamente: "))

  return p

# Função calcula distância percorrida e a acrescenta ao contador da distância total
def calcula_distancia (t, v, dtotal):
  d = t*v
  dtotal += d

  # Retorna a distância total
  return dtotal

# Cria contador da distância total
dtotal = 0

# Usuário digita quantos trechos serão lidos e em seguida verifica se quantidade é válida
n = int(input("Digite a quantidade de trechos a serem lidos: "))
verifica0(n)

# Para n trechos...
for i in range (n):
  # Usuário insere tempo decorrido e velocidade média
  t, v = map(int, input("Digite o tempo decorrido (em horas) e a velocidade média (em km/h) (separados por espaço): ").split())
  # Verifica valores inseridos
  t = verifica1(t)
  v = verifica1(v)

  # Armazena distância total retornada da função
  dtotal = calcula_distancia(t, v, dtotal)

# Mostra ao usuário a distância total percorrida e quantidades de trechos
print(f"Distância total percorrida: {dtotal} km considerando os {n} trechos.")



