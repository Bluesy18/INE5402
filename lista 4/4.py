### 4 ###

# Usuário digita um número inteiro
n = int(input("Digite um número inteiro: "))

# Gera e imprime números que resultam em resto 2 caso sejam divididos com o número digitado 
for i in range(1, 10001):
    if (i%n == 2):
        print(i)
        