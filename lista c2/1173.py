### 1173 ###

x = int(input("Digite um valor para N[0]: "))

for i in range (10):

  if (i == 0):
    print (f"N[{i}] = {x}")
    xPassado = x

  else:
    print(f"N[{i}] = {xPassado*2}")
    xPassado = xPassado*2
         

