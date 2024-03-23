### 1038 ###

# Usuário digita código e quantidade do item
cdg, qtd = input("Digite o código e a quantidade do item desejado (separado por espaços): ").split()

# Conversão para inteiro
cdg1 = int(cdg)
qtd1 = int(qtd)

# Verifica o código e a quantidade desejada
if(cdg1 < 1 or cdg1 > 5):
  print("Código inválido")

else:
  if(cdg1 == 1):
    vlr = round(qtd1*4, 2)

  elif(cdg1 == 2):
    vlr = round(qtd1*4.50, 2)

  elif(cdg1 == 3):
    vlr = round(qtd1*5, 2)

  elif(cdg1 == 4):
    vlr = round(qtd1*2, 2)

  elif(cdg1 == 5):
    vlr = round(qtd1*1.50, 2)

# Mostra o total a ser pago
  print(f"Total: R$ {vlr}")