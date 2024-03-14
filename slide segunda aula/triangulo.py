i = 1

while i == 1:
  unidade = str(input("Escolha entre m-metro ou cm-centímetro: "))

  if(unidade == "cm"):
    base = float(input("Digite o valor da base do triângulo: "))
    altura = float(input("Digite o valor da altura do triângulo: "))
    area = base*altura/2
    if (area >= 100):
      area/100
      unidade = "m"
      print(f"A área do triângulo é: {area} {unidade}")
      resposta = str(input("Digite s para calcular de novo. "))
      if(resposta != "s"):
        break
    else:
      print(f"A área do triângulo é: {area} {unidade}")
      resposta = str(input("Digite s para calcular de novo. "))
      if(resposta != "s"):
        break

  elif(unidade == "m"):
    base = float(input("Digite o valor da base do triângulo: "))
    altura = float(input("Digite o valor da altura do triângulo: "))
    area = base*altura/2

    if(area < 1):
      area*100
      unidade = "cm"
      print(f"A área do triângulo é: {area} {unidade}")
      resposta = str(input("Digite s para calcular de novo. "))
      if(resposta != "s"):
        break
    else:
      print(f"A área do triângulo é: {area} {unidade}")
      resposta = str(input("Digite s para calcular de novo. "))
      if(resposta != "s"):
        break

  else:
    print("Erro! Tente novamente.")
