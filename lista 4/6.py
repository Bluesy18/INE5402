### 6 ###

# Cria a variável num
num = 1

# Enquanto o número for diferente de 0, gera a sequência de 1 até o número digitado
while (num != 0):
    num = int(input("\nDigite um número: "))
    for i in range (1, num+1):
        print(i, end=' ')
    