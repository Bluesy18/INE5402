############# Fiz a 1003, 1004, 1005 e 1009 em sala com o André #############

############# As variáveis estão em maísculo pois na dúvida eu decidi seguir a risca o texto #############

### 1003 ###

#usuário digita dois valores
A = int(input("Digite um número: "))
B = int(input("Digite um número: "))

# Soma
SOMA = A+B

# Resultado
print(f"SOMA = {SOMA}")

###1004###

# Usuário digita dois valores
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))

# Produto
PROD = a*b

# Resultado
print(f"PROD = {PROD}")

### 1005 ###

# Usuário digita suas notas
A = float(input("Digite sua nota (de 0 a 10, com uma casa após o ponto): "))
B = float(input("Digite sua outra nota (de 0 a 10, com uma casa após o ponto): "))

# Atribuindo os pesos
AP = A*3.5
BP = B*7.5

# Media ponderada
media = (AP+BP)/11
mediaA = round(media, 5)

# Resultado
print(f"MEDIA = {mediaA}")

### 1006 ###

# Usuário digita suas notas
A = float(input("Digite sua primeira nota (limite de uma casa decimal): "))
B = float(input("Digite sua segunda nota (limite de uma casa decimal): "))
C = float(input("Digite sua terceira nota (limite de uma casa decimal): "))

# Aplicação de pesos
Ap = A*2
Bp = B*3
Cp = C*5

# Cálculo e arredondamento da média
media = (Ap+Bp+Cp)/10
mediaA = round(media, 1)

# Média
print(f"MEDIA = {mediaA}")

### 1007 ###

# Usuário digita seus valores
A = int(input("Digite o valor A: "))
B = int(input("Digite o valor B: "))
C = int(input("Digite o valor C: "))
D = int(input("Digite o valor D: "))

# Aplica-se a fórmula
diferenca = (A*B - C*D)

# Diferençaa
print(f"DIFERENCA = {diferenca}")

### 1008 ###

# Usuário digita suas informações
numero = int(input("Digite seu número: "))
horas = float(input("Digite suas horas trabalhadas: "))
phora = float(input("Digite o quanto você recebe por hora: "))

# Cálculo e arredondamento do salário
salario = horas*phora
salarioA = round(salario, 2)

# Número e salário
print(f"NUMBER = {numero}\nSALARY = U$ {salarioA}")

### 1009 ###

# Usuário digita suas informações
nome = input("Digite seu nome: ")
sal = float(input("Digite seu salário: "))
venda = float(input("Digite o total que você vendeu: "))

# Cálculo do bônus
bonus = venda*0.15

# Cálculo e arredondamento do salário acrescido
salSoma = sal+bonus
salF = round(salSoma, 2)

print(f"Seu salário acrescido do bônus é de R${salF}")

### 1012 ###

# Definição de pi
pi = 3.14159

# Usuário digita seus valores
a = float(input("Digite o valor de A (uma casa decimal): "))
b = float(input("Digite o valor de B (uma casa decimal): "))
c = float(input("Digite o valor de C (uma casa decimal): "))

# Arredondamento dos valores
A = round(a, 1)
B = round(b, 1)
C = round(c, 1)

# a) Cálculo da altura do triângulo retângulo
areaTri = A*C/2

# b) Cálculo da área do circulo
areaCir = pi*C**2

# c) Cálculo da área do trapézio
areaTra = (A+B)*C/2

# d) Cálculo da área do quadrado
areaQua = B**2

# e) Cálculo da área do retângulo
areaRet = A*B

# Arredondamento das áreas
areaTriA = round(areaTri, 3)
areaCirA = round(areaCir, 3)
areaTraA = round(areaTra, 3)
areaQuaA = round(areaQua, 3)
areaRetA = round(areaRet, 3)

# Resposta mostrando as áreas
print(f"TRIANGULO: {areaTriA}\nCIRCULO: {areaCirA}\nTRAPEZIO: {areaTraA}\nQUADRADO: {areaQuaA}\nRETANGULO: {areaRetA}")

### 1014 ###

# Usuário digita a ditância total percorrida e o gasto total de combustível
distancia = float(input("Digite a distância total percorrida: "))
gastoT = float(input("Digite o gasto total de combustível: "))

# Arredondamento do gasto
gastoTA = round(gastoT, 1)

# Cálculo e arredondamento do consumo médio de combustível
consumo = distancia/gastoTA
consumoA = round(consumo, 3)

# Apresenta o consumo médio do automóvel ao usuário
print(f"O consumo médio do automóvel é de {consumoA} km/l")

### 1015 ###

# Usuário digita as coordenadas dos pontos

x1 = float(input("Digite x1: "))
x2 = float(input("Digite x2: "))
y1 = float(input("Digite y1: "))
y2 = float(input("Digite y2: "))

# Cálculo da distância entre dois pontos
dab = ((x2-x1)**2 + (y2-y1)**2)**1.0/2

# Apresenta a distância entre os dois pontos ao usuário
print(f"A distãncia entre os pontos é {dab}")

### 1017 ###

# Usuário digita o tempo gasto na viagem e a velocidade média do veículo pelo trajeto
tempo = float(input("Digite o tempo gasto na viagem: "))
velmed = float(input("Digite a velocidade média durante a viagem: "))

# Distância percorrida na viagem
distancia = tempo*velmed

# Cálculo e arredondadmento de litros de combústivel que serão necessários para concluir a viagem
litros = distancia/12
litrosA = round(litros, 3)

# Apresenta ao usuário a quantidade de litros necessária para a viagem 
print(f"A quantidade de litros de combustível necessária para completar a viagem é de {litrosA}")

### 1019 ###

# Usuário digita o tempo em segundos
N = int(input("Digite o tempo em segundos: "))

# Conversão de segundos para horas, minutos e segundos
horas = N // 3600
min = (N % 3600) // 60
seg = (N % 3600) % 60

# Apresenta as horas, minutos e segundos para o usuário
print(f"{horas}:{min}:{seg}")

### 1020 ###

# Usuário digita sua idade em dias
diasT = int(input("Digite sua idade em dias: "))

# Cálculo da idade em ano(s), mes(es) e dia(s)
ano = int(diasT // 365)
mes = int(diasT % 365) // 30
dias = int(diasT % 365) % 30

# Idade em ano(s), mes(es) e dia(s)
print(f"{ano} ano(s)\n{mes} mes(es)\n{dias} dia(s)")

### 2374 ###

# Usuário digita os valores das pressões
n = int(input("Digite a pressão desejada (entre 1 e 40): "))
m = int(input("Digite a pressão lida pela bomba (entre 1 e 40): "))

# Cálculo da diferença entre pressões
diferenca = n-m

# Mensagem informando a diferença entre as pressões
print(f"A diferença entre a pressão desejada e a pressão lida pela bomba é de {diferenca}")

### 2413 ###

# Usuário digita o número t de pessoas que clicaram no terceiro link
t = int(input("Digite o número de pessoas que clicaram no terceiro link (entre 1 e 1000): "))

# Cálculo do número de pessoas que clicaram no segundo e no primeiro link
s = t*2
p = s*2

# Apresenta ao usuário o número de pessoas que clicaram no primeiro link
print(f"O número de pessoas que clicaram no primeiro link é {p}")

