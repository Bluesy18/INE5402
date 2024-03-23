### 2417 ###

# Usuário digita os dados dos times
cv, ce, cs, fv, fe, fs = input("Digite o número de vitórias, empates e saldo de gols do Cormengo e número de vitórias, empates e saldo de gols do Flaminthians (separados por espaço): ").split()

# Conversão para inteiro
cv1 = int(cv)
ce1 = int(ce)
cs1 = int(cs)
fv1 = int(fv)
fe1 = int(fe)
fs1 = int(fs)

# Verifica se as pontuações atendem às especificações da questão
if(cv1 < 1 or cv1 > 100):
  print("Pontuação inválida.")

elif(ce1 < 1 or ce1 > 100):
  print("Pontuação inválida.")

elif(cs1 < -1000 or cs1 > 1000):
  print("Pontuação inválida.")

elif(fv1 < 1 or fv1 > 100):
  print("Pontuação inválida.")

elif(fe1 < 1 or fe1 > 100):
  print("Pontuação inválida.")

elif(fs1 < -1000 or fs1 > 1000):
  print("Pontuação inválida.")

# Converte pra pontuação
else:
  cp = (cv1*3) + ce1
  fp = (fv1*3) + fe1

# Checa possibilidades e mostra resultado do campeonato
  if(cp > fp):
    print("C")

  elif(fp > cp):
    print("F")

  elif(cs1 > fs1):
    print("C")

  elif(fs1 > cs1):
    print("F")

  else:
    print("=")
