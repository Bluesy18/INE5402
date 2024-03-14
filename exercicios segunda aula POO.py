############# Fiz essas atividades em sala junto com o André, por isso o código está praticamente igual #############

#1 - ÁREA DO TRIÂNGULO

# Usuário digita os valores do triângulo
base = int(input("Digite a base do seu triângulo: "))
altura = int(input("Digite a altura do seu triângulo: "))

# Cálculo da área do triângulo
area = base*altura/2

# Resultado do cálculo
print(f"A área do seu triângulo é igual a: {area}")

#2 - DESCONTO DO PRODUTO

# Usuário digita o preço do produto
produto = float(input("Digite o preço do produto: "))

# Operações para saber o desconto
desconto = produto/4           
resultado = produto-desconto

# Resultado do cálculo
print(f"O preço do produto será de: R${resultado}")

#3 - IDADE

# Usuário informa idade
idadeA = int(input("Digite quanto anos você tem: "))
idadeM = int(input("Agora, digite quantos meses você tem (descontando os anos já informados): "))
idadeD = int(input("Digite quantos dia você tem (descontando os anos e meses já informados): "))

# Conversão de anos e meses para dia
idadeAD = idadeA*365
idadeMD = idadeM*30

# Soma dos dias
idadeFinal = idadeD+idadeAD+idadeMD

# Resultado final de quantidade de dias
print(f"Você tem {idadeFinal} dias de vida.")