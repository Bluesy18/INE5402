### 6 ###

# Define função que localiza ponto no plano cartesiano
def local(x, y):
  if ((x > 0) and (y > 0)):
    print("primeiro")

  elif ((x < 0) and (y > 0)):
    print("segundo")

  elif ((x < 0) and (y < 0)):
    print("terceiro")

  elif ((x > 0) and (y < 0)):
    print("quarto")

while True:
  # Usuário digita coordenada
  x, y = map(int, input("Digite a coordenada de X e de Y (separados por espaço): ").split())

  # Chama função localizadora
  local(x, y)

  # Se alguma coordenada for 0, encerra o programa
  if ((x == 0) or (y == 0)):
    break



