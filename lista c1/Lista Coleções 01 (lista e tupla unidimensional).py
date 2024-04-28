### 1 ###

# Cria lista e contador
notas = []
soma = 0

# Cria função que organiza a lista de maneira crescente
def melhornota(notas):
    for i in range(2):
        if notas[0] > notas[1]:
            notas[0], notas[1] = notas[1], notas[0]
        if notas[1] > notas[2]:
            notas[1], notas[2] = notas[2], notas[1]
            
    dif = notas[2] - notas[0]        
    
    return notas, dif

# Cria função que calcula média das notas
def media(notas):
    return (soma/len(notas))

# Cria função que verifica se notas obedecem intervalo
def verifica (notas):
    while ((0 > notas[i]) or (10 < notas[i])):
        notas[i] = int(input("Nota inválida! Digite novamente uma nota: "))
        
    return notas[i]
    
# Usuário digita 3 notas
for i in range (3):
    notas.append(int(input("Digite uma nota: ")))
    notas[i] = verifica(notas)
    soma += notas[i]

# Variáveis recebem retorno de funções    
med = media(notas)    
notas, dif = melhornota(notas)

# Mostra ao usuário a média, a maior, a menor nota e a diferença entre elas
print(f"Média: {med}\nMaior nota: {notas[2]}\nMenor nota: {notas[0]}\nDiferença: {dif}")
           
### 2 ###

# Cria lista e variável de controle
num = []
r = 0

# Usuário digita quantos números irá adicionar
n = int(input("Digite quantos números você adicionará: "))

# Usuário digita número inteiro
for i in range(n):
    num.append(int(input("Digite um número inteiro: ")))

# Verifica se há números repetidos e informa ao usuário
for j in range (n):
    rep = num.count(num[j])
        
    if (rep > 1):
        r = 1
        print("Existem números repetidos.")
        break

if (r == 0):
    print("Não existem número repetidos.")
    
### 3 ###

# Cria tupla
tupla = (6,8,4,9,2,5,7,3,10,1)

# Converte tupla e lista
lista = list(tupla)

# Cria cópia da lista
lista0 = lista[:]

# Organiza lista de forma crescente
for i in range(9):
        if lista[0] > lista[1]:
            lista[0], lista[1] = lista[1], lista[0]
        if lista[1] > lista[2]:
            lista[1], lista[2] = lista[2], lista[1]
        if lista[2] > lista[3]:
            lista[2], lista[3] = lista[3], lista[2]
        if lista[3] > lista[4]:
            lista[3], lista[4] = lista[4], lista[3]
        if lista[4] > lista[5]:
            lista[4], lista[5] = lista[5], lista[4]
        if lista[5] > lista[6]:
            lista[5], lista[6] = lista[6], lista[5]
        if lista[6] > lista[7]:
            lista[6], lista[7] = lista[7], lista[6]
        if lista[7] > lista[8]:
            lista[7], lista[8] = lista[8], lista[7]
        if lista[8] > lista[9]:
            lista[8], lista[9] = lista[9], lista[8]

# Mostra qual o maior e o menor número da tupla
print(f"A posição do maior número da tupla é {lista0.index(lista[9])} e do menor é {lista0.index(lista[0])}")

### 4 ###

# Define função para calcular números da lista multiplicados por k
def calc(x,k,n):
    res = []
    for i in range (n):
        res.append(k*x[i])
    return res

# Cria lista
x = []

# Usuário digita quantos números digitará
n = int(input("Digite quantos números inteiros voce digitará: "))

# Usuário digita números da lista
for i in range(n):
    x.append(int(input("Adicione um número inteiro à sua lista: ")))

# Usuário digita número que multiplicará a lista
k = int(input("Digite um número inteiro: "))

# Variável recebe retorno de função
res = calc(x,k,n)

# Mostra lista resultante
print(f" Sua lista após ser multiplicada por {k}, é: {res}")

### 5 ###

# Cria lista
x = list(range(20))

# Organiza de maneira decrescente
x[0], x[19] = x[19], x[0]
x[1], x[18] = x[18], x[1]
x[2], x[17] = x[17], x[2]
x[3], x[16] = x[16], x[3]
x[4], x[15] = x[15], x[4]
x[5], x[14] = x[14], x[5]
x[6], x[13] = x[13], x[6]
x[7], x[12] = x[12], x[7]
x[8], x[11] = x[11], x[8]
x[9], x[10] = x[10], x[9]

# Mostra lista de maneira decrescente
print(x)

### 6 ###

# Cria lista
saltos = []

# Usuário digita o nome do atleta
nome = input("Digite o nome do atleta: ")

# Enquanto nome não for O...
while nome != "o" and nome != "O" :
    
    # Usuário digita distância dos saltos
    for i in range (5):
        saltos.append(float(input(f"Digite a distância do {i+1}º salto: ")))

    # Cria cópia da lista    
    saltoOrdem = saltos[:] 
    
    # Organiza lista de forma crescente
    for i in range (4):
        if saltos[0] > saltos[1]:
            saltos[0], saltos[1] = saltos[1], saltos[0]
        if saltos[1] > saltos[2]:
            saltos[1], saltos[2] = saltos[2], saltos[1]
        if saltos[2] > saltos[3]:
            saltos[2], saltos[3] = saltos[3], saltos[2]
        if saltos[3] > saltos[4]:
            saltos[3], saltos[4] = saltos[4], saltos[3]

    # Tira média entre os saltos excluindo o melhor e o pior        
    media = round(((saltos[1]+saltos[2]+saltos[3])/3), 1) 
    
    # Mostra as informações pedidas
    print(f"""Atleta: {nome}

Primeiro Salto: {saltoOrdem[0]} m
Segundo Salto: {saltoOrdem[1]} m
Terceiro Salto: {saltoOrdem[2]} m
Quarto Salto: {saltoOrdem[3]} m
Quinto Salto: {saltoOrdem[4]} m

Melhor salto:  {saltos[4]} m
Pior salto: {saltos[0]} m
Média dos demais saltos: {media} m

Resultado final:
{nome}: {media} m""")
    
    # Pede nome do atleta novamente
    nome = input("Digite o nome do atleta: ")
    
        


        
        
        
            




    

    



