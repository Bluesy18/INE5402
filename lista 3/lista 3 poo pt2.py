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
    
    

