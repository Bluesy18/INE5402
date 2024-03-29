### 6 ###

# Usuário digita distância e velocidades
d, vf, vg = map(int, input("Digite a distância entre os barcos, a velocidade do fugitivo e a velocidade da guarda costeira, repectivamente (separadas por espaço): ").split())

# Verifica se os valores são válidos
if ((1 <= d <= 100) and (1 <= vf <= 100) and (1 <= vg <= 100)):
  
  # Calcula distância da guarda e o tempo de ambos
  dg = (144 + (d**2))**0.5
  tf = 12/vf
  tg = dg/vg

  # Verifica se a guarda chega a tempo e mostra o resultado
  if (tg <= tf):
    print("S")
  
  else:
    print("N")

else:
  print("Valores inválidos!")