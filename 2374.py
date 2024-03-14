### 2374 ###

# Usuário digita os valores das pressões
n = int(input("Digite a pressão desejada (entre 1 e 40): "))
m = int(input("Digite a pressão lida pela bomba (entre 1 e 40): "))

# Cálculo da diferença entre pressões
diferenca = n-m

# Mensagem informando a diferença entre as pressões
print(f"A diferença entre a pressão desejada e a pressão lida pela bomba é de {diferenca}")