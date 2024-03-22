### 1061 ###

# Usuário digita data e horário
diaI1 = int(input("Digite o dia de íncio do evento: "))
horaI1, minI1, segI1 = input("Digite o horário de íncio do evento: ").split(" : ")
diaF1 = int(input("Digite o dia de fim do evento: "))
horaF1, minF1, segF1 = input("Digite o horário de fim do evento: ").split(" : ")

# Conversão para inteiro
diaI2 = int(diaI1)
horaI2 = int(horaI1)
minI2 = int(minI1)
segI2 = int(segI1)
diaF2 = int(diaF1)
horaF2 = int(horaF1)
minF2 = int(minF1)
segF2 = int(segF1)

if(diaI2 > 31 or horaI2 > 24 or minI2 >= 60 or segI2 >= 60 or diaF2 > 31 or horaF2 > 24 or minF2 >= 60 or segF2 >= 60):
  print("Digite valores válidos!")
else:

# Transformar valores em segundos para calcular
  segCalcI = (diaI2*86400)+(horaI2*3600)+(minI2*60)+segI2
  segCalcF = (diaF2*86400)+(horaF2*3600)+(minF2*60)+segF2
  segCalcR = segCalcF - segCalcI

# Conversão para dias, horas, minutos e segundos
  diaR = segCalcR // 86400
  horasR = (segCalcR % 86400) // 3600
  minR = ((segCalcR % 86400) % 3600) // 60
  segR = ((segCalcR % 86400) % 3660) % 60

# Resultado
  print(f"{diaR} dia (s)\n{horasR} hora (s)\n{minR} minuto (s)\n{segR} segundo (s)")

