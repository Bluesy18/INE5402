def interpreta (r, n):
  if(r <= n):
    return "0"

  elif(n*27 < r):
    return "impossible"

  else:
    d = 1
    while(n*d < r):
      d += 1

    return d-1

end = 0
case = 0

while (end == 0):
  case += 1
  r, n = map(int, input("Digite a quantidade de ruas e quantos inteiros estão disponíveis: ").split())
  if((r == 0) and (n == 0)):
    end = 1

  print(f"Case {case}: {interpreta(r, n)}")

  