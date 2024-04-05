### 11 ###

# Cria variável de soma
soma = 0

# Usuário digita um número inteiro
x = int(input("Digite um número inteiro: "))

# Guarda primeiro número
xini = x

while True:
    # Usuário digita outro número inteiro
    z = int(input("Digite um outro número inteiro: "))
    
    # Quando z for maior que x, interrompe o loop
    if z > x:
        break

# Enquanto a soma for menor que z, acrescenta o próximo número
while soma <= z:
    soma += x
    x += 1

# Mostra quantos números tiveram que ser somados para ultrapassar z
print(x - xini)