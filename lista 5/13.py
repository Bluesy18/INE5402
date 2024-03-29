### 13 ###

# Cria variável caminho
caminho = ""

# Cria variável dos flippers
p = 2
r = 3

# Verifica se valores são compatíveis com 1 e 0
while ((p != 1) and (p != 0)) or ((r != 1) and (r != 0)):
  # Usuário digita estado do flipper
  p, r = map(int, input("Digite o valor de P e de R (separados por espaço): ").split())

# Verifica os valores dos flippers e seleciona o caminho
if (p == 0):
  caminho = "C"
  
elif((p == 1) and (r == 0)):
  caminho = "B"

elif((p == 1) and (r == 1)):
  caminho = "A"
  
# Informa o caminho
print(caminho)
