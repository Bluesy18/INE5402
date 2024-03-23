### 1047 ###

# Usuário digita horário inicial e horário final

hi, mi, hf, mf = input("Digite a hora de início, minuto de início, hora de fim e minuto de fim (separados por espaço): ").split()

# Conversão para inteiro
hi1 = int(hi)
mi1 = int(mi)
hf1 = int(hf)
mf1 = int(mf)

# Verifica se os horários atendem às especificações da questão
if (hi1 > 24 or hi1 < 0):
  print("Horário inválido.")

elif (mi1 > 60 or mi1 < 0):
  print("Horário inválido.")

elif (hf1 > 24 or hf1 < 0):
  print("Horário inválido.")

elif (mf1 > 60 or mf1 < 0):
  print("Horário inválido.")

# Calcula duração
else:
  if(hf1 > hi1):
    ti = (hi1*60) + mi1
    tf = (hf1*60) + mf1

    dcalc = tf - ti
    dh = dcalc // 60
    dm = dcalc % 60

  elif(hf1 < hi1):
    ti = (hi1*60) + mi1
    tf = (hf1*60) + mf1

    dcalc = (1440 - ti) + tf
    dh = dcalc // 60
    dm = dcalc % 60

  elif(hf1 == hi1 and mf1 > mi1):
    dh = 0
    dm = mf1 - mi1

  elif(hf1 == hi1 and mf1 < mi1):
    dh = 23
    dm = 60-(mi1 - mf1)

  elif(hf1 == hi1 and mf1 == mi1):
    dh = 24
    dm = 0

  else:
    print("Valores inválidos.")

# Mostra a duração
print(f"O JOGO DUROU {dh} HORA(S) E {dm} MINUTO(S)")  