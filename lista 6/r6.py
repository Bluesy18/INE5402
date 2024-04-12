### 6 ###

# Função calcula quantos positivos foram digitados e qual a média deles
def positivo (n, qtdPos, somaPos, media):
  if (n > 0):
    qtdPos += 1
    somaPos += n
    media = round(somaPos/qtdPos, 1)

  # Retorna quantidade, média e soma de positivos
  return qtdPos, media, somaPos

# Define variáveis
qtdPos = 0
somaPos = 0
media = 0

# Pede 6 vezes...
for i in range (6):
  # Que o usuário digite um número
  n = float(input("Digite um número: "))

  # Armazena variáveis retornadas da função positivo()
  qtdPos, media, somaPos = positivo(n, qtdPos, somaPos, media)

# Mostra quantos valores positivos foram digitados, além de sua média
print(f"{qtdPos} valores positivos\n{media}")