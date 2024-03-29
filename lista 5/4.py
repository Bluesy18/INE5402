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
        