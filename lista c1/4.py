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