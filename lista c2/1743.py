### 1743 ###

def verifica0(conectores1):
  while (len(conectores1) != 5):
    conectores1 = [int(x) for x in (input(f"Quantidade errada! Digite novamente 5 números (0 ou 1): ")).split()]

  return conectores1

res = "Y"

conectores1 = [int(x) for x in (input(f"Digite 5 números (0 ou 1): ")).split()]
conectores1 = verifica0(conectores1)

conectores2 = [int(x) for x in (input(f"Digite 5 números (0 ou 1): ")).split()]
conectores2 = verifica0(conectores2)

for i in range (5):
  if((conectores1[i] - conectores2[i]) == 0):
    res = "N"
    break

print(res)