def verifica0 (t):
  while ((t < 1) or (t > 300)):
    t = int(input("Número de testes inválido! Digite novamente a quantidades de testes: "))

def verifica1 (pa, pb, g1, g2):
  while ((pa < 100) or (pa > 1000000) or (pb < 100) or (pb > 1000000) or (g1 < 0.001) or (g1 > 0.1) or (g2 < 0) or (g2 > 0.1) or (g1 < g2) or (pa > pb)):
    pa, pb, g1, g2 = input("Valores inválidos! Digite novamente a população da A e da B, seguida de suas respectivas taxas de crescimento: ").split()
    pa, pb, g1, g2 = int(pa), int(pb), float(g1), float(g2)


t = int(input("Digite a quantidades de testes: "))
verifica0(t)

for i in range (0, t):
  pa, pb, g1, g2 = input("Digite a população da A e da B, seguida de suas respectivas taxas de crescimento: ").split()
  pa, pb, g1, g2 = int(pa), int(pb), float(g1)/100, float(g2)/100
  verifica1(pa, pb, g1, g2)
  count = 0


  while True:
    pa += int(pa*g1)
    pb += int(pb*g2)

    count += 1

    if(pa > pb or count > 100):
      break
    
  if (count <= 100):
    print(f"{count} anos")

  else:
    print("Mais de 1 seculo.")


 
  

