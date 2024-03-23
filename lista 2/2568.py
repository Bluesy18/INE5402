### 2568 ###

# Usuário digita seus valores
d, i, x, f = input("Digite o dia que a ação foi registrada, o preço inicial da ação, a variação diária do reço e a quantidade de dias futuros (separados por espaço): ").split()

# Conversão para inteiro
d1 = int(d)
i1 = int(i)
x1 = int(x)
f1 = int(f)

# Verifica se as pontuações atendem às especificações da questão
if (d1 < 1 or d1 > 365):
  print("Valor inválido.")

elif (i1 < x1 or i1 > 1000):
  print("Valor inválido.")

elif (x1 < 1 or x1 > i1):
  print("Valor inválido.")

elif (f1 < 1 or f1 > 365):
  print("Valor inválido.")

# Verifica e mostra se houve um acréscimo, establidade ou decréscimo do valor
else:
  if(d1 % 2 == 0 and f1 % 2 == 0):
    p = i1
    
  elif(d1 % 2 == 0 and f1 % 2 != 0):
    p = i1 - x1
    
  elif(d1 % 2 != 0 and f1 % 2 == 0):
    p = i1
   
  elif(d1 % 2 != 0 and f1 % 2 != 0):
    p = i1 + x1

print(p) 