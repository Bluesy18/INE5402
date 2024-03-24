### 1 ###

# Mostra anos de 4 em 4 anos (bissextos)
for i in range(2004, 2100, 4):
    print(i)
    
### 2 ###
    
# Mostra números ímpares
for i in range(1, 51, 2):
    print(i)
    
### 3 ###
    
# Define quantiadade de vezes os próximos comandos são executados
for i in range(1, 6):

    # Usuário digita o nome do aluno, sua média e a mensalidade
    nome = input("Digite seu nome: ")
    media = round(float(input("Digite sua nota/média geral: ")), 2)
    mensal = float(input("Digite o valor de sua mensalidade: "))

    # Verfica qual o aluno com a melhor nota
    if(i == 1):
        mNome = nome
        mMedia = media
        mMensal = mensal
        
    elif(i != 1):
        if(mMedia < media):
            mNome = nome
            mMedia = media
            mMensal = mensal
            
# Mostra o aluno que receberá o desconto, sua mensalidade antes e após o desconto
print(f"""O aluno que receberá o desconto é {mNome}
\nA mensalidade antes do desconto era de R${mMensal}
\nA mensalidade após o deconto ficou com o valor de R${mMensal-(mMensal*0.3)}""")

### 4 ###
    
# Cria variáveis para mostrar quantidades de números pares e ímpares
par = 0
impar = 0

for i in range(1, 11):

    # Usuário digita um número inteiro
    num = int(input("Digite um número inteiro: "))

    #Verifica se o número é par ou ímpar
    if (num%2 == 0):
        par += 1

    else:
        impar += 1

# Mostra a quantidade de números pares e ímpares
print(f"\nA quantidade de números pares é: {par}\nA quantidade de números impares é: {impar}")

### 5 ###

# Cria variável de controle para números primos ou não
co = 0

# Usuário digita número inteiro
num = int(input("Digite um número inteiro: "))

for i in range (2, num):
    # Pega resto da divisão do número digitado pelos números no intervalo de 2-num
    res = num%i
    if(res == 0):
        co += 1

# Verifica e mostra se o número digitado é ou não primo
if(co != 0):
    print("Não é primo.")

if(co == 0):
    print("É primo.")

### 6 ###

# Cria variável de controle para verificação se número é primo ou não
co = 0

# Usuário digita número inteiro qualquer
num = int(input("Digite um número inteiro: "))
for i in range (2, num):

    # Pega resto da divisão do número digitado por outros números inteiros no intervalo de 2-num
    res = num%i

    # Mostra os números por qual o número digitado é divisível
    if(res == 0):
        co += 1
        final = str(i)
        print(f"O número é divisível por {final}")

# Mostra se o número é ou não é primo
if(co != 0):
    print("Não é primo.")

if(co == 0):
    print("É primo.")

### 7 ###

# Cria variável de soma
somaIdade = 0

# Usuário digita quantidade de pessoas
n = int(input("Digite o número de pessoas: "))
for i in range (1, n+1):

    # Usuário digita a idade da i pessoa
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))
    
    # Soma as idades
    somaIdade += idade
    
# Calcula a média das idades    
media = somaIdade/n

# Mostra se a turma é jovem, adulta ou idosa
if (media <= 25):
    print("A turma é jovem")
    
elif (media <= 60):
    print("A turma é adulta")
    
elif (media > 60):
    print("A turma é idosa")

### 8 ###

# Cria uma variável para armazenar o valor da soma
somaInt = 0

# Usuário digita primeiro e último número da sequência
pn, un = map(int, input("Digite o primeiro e o último número da sequência (separados por espaço): ").split())
for i in range(pn+1, un):
  # Soma números do intervalo
  somaInt += i
  
# Mostra a soma dos números do intervalo
print(f"A soma dos números do intervalo vale {somaInt}")

### 9 ###

# Usuário digita o número que deseja ver a tabuada 
num = int(input("Escreva o número que você deseja ver a tabuada (1 até 10): "))

# Mostra a tabuada
print(f"Tabuada do {num}:")
for i in range(1, 11):
  print(f"- {num} X {i} = {num*i}")

### 10 ###

# Cria variáveis de soma e de situação
somaNota = 0
situacao = ""

for i in range(1, 6):
    # Usuário digita o nome dos alunos e das notas
    nome = input("Digite seu nome: ")
    nota = round(float(input("Digite sua nota média (entre 0 e 10): ")), 2)

    # Verifica se as notas são válidas
    if((nota < 0) or (nota > 10)):
      print("Nota inválida.")
      quit()  
    else:
      # Soma as notas
      somanota += nota

      # Verificar qual aluno tirou a melhor nota
      if(i == 1):
          mNome = nome
          mNota = nota
          
      elif(i != 1):
          if(mNota < nota):
              mNome = nome
              mNota = nota

# Calcula a média das notas
media = round((somaNota/5), 2)

# Determina a situação do melhor aluno
if(mNota >= 5.75):
        situacao = "aprovado"

elif(mNota >= 2.75):
        situacao = "de recuperação"

elif(mNota < 2.75):
        situacao = "reprovado"

# Mostra a média e a situação do melhor aluno
print(f"A média das notas foi de {media}.\nO aluno com a maior nota foi {mNome} e ele está {situacao}.")

### 11 ###

# Cria variável de soma
somaNum = 0

# Usuário digita quantidade de números que irá inserir
n = int(input("Digite a quantidade n de números que serão lidos pelo teclado: "))

for i in range (n):
  # Usuário digita os números
  num = int(input("Digite um número inteiro: "))
  
  # Soma os números digitados
  somaNum += num

  # Verifica o maior e o menor número
  if(i == 0):
        maNum = num
        meNum = num
        
  elif(i != 0):
      
      if(num > maNum):
          maNum = num
      
      elif(num < meNum):
          meNum = num

# Calcula a média dos números digitados
media = somaNum/n

# Mostra a média, o maior e o menor número
print(f"A média entre os números foi {media}, o maior número foi {maNum} e o menor número foi {meNum}")

### 12 ###

# Cria variável de soma
somaDist = 0
soma1520 = 0

# Usuário digita quantidade de praias que irá inserir
n = int(input("Digite a quantidade de praias que serão lidas pelo teclado: "))

for i in range(n):
    # Usuário digita o nome das praia e sua distância até o centro
    praia = input("Digite o nome da praia: ")
    dist = int(input("Digite sua distância em relação ao centro (em km): "))

    # Soma as distâncias digitadas
    somaDist += dist

    # Verifica se a distância da praia até o centro está entre 15 a 20 km
    if(20 >= dist >= 15):
        soma1520 += 1

    # Verifica qual praia é a mais distante
    if(i == 0):
        mDist = dist
        mPraia = praia

    elif(i != 0):

      if(dist > mDist):
          mDist = dist
          mPraia = praia
    
# Calcula a distância média das praias até o centro
media = round((somaDist/n), 1)

# Mostra qual é a praia mais distante do centro, quantidade de praias com a distância entre 15 e 20 km e a distância média das praias
print(f"A praia mais distante do centro é a praia {mPraia}\nExistem {soma1520} praia(s) com uma distância entre 15 a 20 km\nA distância média das praias é de {media} km")