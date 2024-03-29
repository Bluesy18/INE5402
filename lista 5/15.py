### 15 ###

# Usuário digita os valores
a, g, rA, rG = map(float, input("Digite preço do álcool, preço da gasolina, rendimento do álcool e rendimento da gasolina (separados por espaço): ").split())

# Verifica o custo-benefício, depois informa qual combustível mais vale a pena
if(rA/a <= rG/g):
  print("G")

else:
  print("A")