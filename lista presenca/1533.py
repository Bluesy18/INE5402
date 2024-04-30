### 1533 ###

def verifica0(n):
  while (((n < 2) and (n != 0)) or (n > 1000)):
    n = int(input("Valor inválido! Digite novamente a quantidade de suspeitos: "))

  return n

n = int(input("Digite a quantidade de suspeitos: "))
n = verifica0(n)

while (n != 0):
    sus = [int(x) for x in (input("Digite quais são os suspeitos (separados por espaço): ")).split()]
    
    susOrd = sorted(sus)
    
    culpado = susOrd[len(susOrd) - 2]
    
    for i in range(len(sus)):
    
        if culpado == sus[i]:
          culpadoIndice = i + 1
    
    print(f" O índice do culpado é {culpadoIndice}")
    
    n = int(input("Digite a quantidade de suspeitos: "))
    n = verifica0(n)