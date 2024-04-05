### 5 ###

# Define função para somar sucessor até ultrapassar z
def soma(x, xini, z):
  soma = 0

  while soma <= z:
      soma += x
      x += 1

  # Mostra quantos números foram necessários ser somados para ultrapassar z
  print(x - xini)


# Usuário digita um número inteiro
x = int(input("Digite um número inteiro: "))

# Armazena x inicial
xini = x

while True:
    # Usuário digita outro número inteiro
    z = int(input("Digite um outro número inteiro: "))
    
    # Quando z for maior que x, interrompe o loop
    if z > x:
        break
    
# Chama a função de soma
soma(x, xini, z)

