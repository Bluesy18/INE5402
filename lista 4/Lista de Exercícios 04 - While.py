############ Fiz até a 7 com o André ############

### 1  ###

# Usuário digita o seu sexo
sexo = (input("Digite seu sexo: ")).upper()

# Enquanto o sexo não for M ou F, o input persiste
while ((sexo != "M") and (sexo != "F")):
    sexo = input("Digite novamente: ").upper()
    
### 2 ###

# Importa função "randrange" da biblioteca "random"
from random import randrange

# Seleciona um número aleatório de 0 a 10 e o armazena
num = randrange(11)

# Cria variável de contagem
cont = 1

# Usuário digita sua tentativa
usuario = int(input("Tente acertar o número entre 0 e 10: "))

# Enquanto o número que o usuário digita não for igual ao número armazenado, o input persiste
while (usuario != num):
    cont += 1
    usuario = int(input("Tente novamente: "))
    
# Informa o usuário que ele acertou e o número de tentativas
print(f"Acertou, o número era {num}\nVocê tentou {cont} vez(es).")

### 3 ###

# Cria variável de resposta e define ela como "S"
resp = "S"

# Cria a variável de porcentagem
porcentagem = 0

# Enquanto a resposta for "S", pede para o usuário digitar seu salário
while (resp == "S"):
    sal = float(input("Digite seu salário: "))

    # Calcula o desconto
    desc = sal*0.11

    # Se o desconto ultrapassar o valor de 320, o deconto passa a ser 320
    if (desc > 320.00):
        
        # Calcula porcentagem equivalente de 320 em relação ao salário
        porcentagem = sal/32000.00
        print(f"A porcentagem aplicada foi de {porcentagem}")

    # Verifica se a resposta continua "S" ou não
    resp = input("Deseja verificar novamente? (S/N): ").upper()
    
### 4 ###

# Usuário digita um número inteiro
n = int(input("Digite um número inteiro: "))

# Gera e imprime números que resultam em resto 2 caso sejam divididos com o número digitado 
for i in range(1, 10001):
    if (i%n == 2):
        print(i)
        
### 5 ###

# Usuário digita um número
n = int(input("Digite um número: "))

# Se o número estiver nesse intervalo, gera tabuada (até 10) do número
while (2 < n < 1000):
    for i in range(1, 11):
        print(f"{i} x {n} = {n*i}")
    break
    
### 6 ###

# Cria a variável num
num = 1

# Enquanto o número for diferente de 0, gera a sequência de 1 até o número digitado
while (num != 0):
    num = int(input("\nDigite um número: "))
    for i in range (1, num+1):
        print(i, end=' ')
    
### 7 ###

# Cria as variáveis de contagem
contA = 0
contG = 0
contD = 0

# Usuário digita qual combustível ele deseja
comb = int(input("Digite o número do combústivel -> 1.Álcool 2.Gasolina 3.Diesel 4.Fim: "))
    
# Enquanto o número digita obedecer o intervalo, contabiliza o número digitado para a contagem correspondente, pergunta novamente o número do combustível e finaliza o processo quando o número 4 é digitado
while (1 <= comb <= 4):
    if(comb == 1):
            contA += 1
    
    elif(comb == 2):
            contG += 1
            
    elif(comb == 3):
            contD += 1
            
    elif(comb == 4):
        break
    comb = int(input("Digite o número do combústivel -> 1.Álcool 2.Gasolina 3.Diesel 4.Fim: "))        
    
# Mostra a quantidade pedida de cada combustível
print(f"MUITO OBRIGADO\nAlcool: {contA}\nGasolina: {contG}\nDiesel: {contD}")
    
### 8 ###

# Cria variável de soma
sum = 0

# Usuário digita o valor de M e N
m, n = map(int, input("Digite o valor de M e de N (separados por espaço): ").split())

# Enquanto M e N forem diferentes de 0... 
while (m != 0 and n != 0):
  # Gera sequência do menor para o maior e soma os números presentes na sequência
  if (m > n):
    for i in range (n, m+1):
      sum += i
      print(i, end = " ")
    print(f"Sum = {sum}")
  if (n > m):
    for i in range (m, n+1):
      sum += i
      print(i, end = " ")
    print(f"Sum = {sum}")

  # Zera variável de soma
  sum = 0

  # Pede novamente para digitar o valor de M e de N
  m, n = map(int, input("Digite o valor de M e de N (separados por espaço): ").split())
      
 

    