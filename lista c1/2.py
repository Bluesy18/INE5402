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
    

    

    



