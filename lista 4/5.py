### 5 ###

# Usuário digita um número
n = int(input("Digite um número: "))

# Se o número estiver nesse intervalo, gera tabuada (até 10) do número
while (2 < n < 1000):
    for i in range(1, 11):
        print(f"{i} x {n} = {n*i}")
    break
    