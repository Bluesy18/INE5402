### 4 ###

preto = []
letras = ["A", "B", "C", "D", "E"]

n = int(input("Digite o número de questões: "))

while (n > 0):
  for i in range (n):
    questao = [int(x) for x in (input(f"Digite um número de 0 a 255: ")).split()]

    for p in questao:
      if (p <= 127):
        preto.append(p)

    if (len(preto) != 1):
      print("*")
      preto.clear()
      
    else:
      letra = questao.index(preto[0])
      print(letras[letra])
      preto.clear()
      

  n = int(input("Digite o número de questões: "))