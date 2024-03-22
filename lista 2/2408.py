### 2408 ###

# Usuário digita pontuação dos jogadores
a, b, c = input("Digite a pontuação dos jogadores (separadas por espaço): ").split()

# Converte para inteiro
a1 = int(a)
b1 = int(b)
c1 = int(c)

# Verifica se as pontuações atendem às especificações da questão
if(a1 < 1 or a1 > 100):
  print("Pontuação inválida.")

elif(b1 < 1 or b1 > 100):
  print("Pontuação inválida.")

elif(b1 < 1 or b1 > 100):
  print("Pontuação inválida.")

# Determina e apresenta o vice-campeão
else:
  if((a1 < b1 and a1 > c1) or (a1 > b1 and a1 < c1)):
    print(a1)

  elif((b1 < a1 and b1 > c1) or (b1 > a1 and a1 < c1)):
    print(b1)

  elif((c1 < a1 and c1 > b1) or (c1 > a1 and c1 < b1)):
    print(c1)


