### 1046 ###

# Usuário digita as horas
i, f = input("Digite a hora de início e a hora de fim (separadas por um espaço): ").split()

# Conversão para inteiro
i1 = int(i)
f1 = int(f)

# Verifica se os horários atendem às especificações da questão
if (i1 < 1 or i1 > 24):
  print("Horário inválido.")

elif (f1 < 1 or f1 > 24):
  print("Horário inválido.")

# Calcula duração
else:
  if (f1 > i1):
    d = f1 - i1

  elif (f1 < i1):
    d = (24 - i1) + f1

  else:
    d = 24

print(f"O JOGO DUROU {d} HORA (S)")

