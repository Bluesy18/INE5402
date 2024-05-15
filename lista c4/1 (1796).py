### 1 (1796) ###

# Define funções para verificar o valor de q, o tamanho da lista "pesquisa" e se seu itens estão de acordo com as limitações
def verifica0 (q):
  while ((q < 4) or (q > 233000)):
    q = int(input("Número inválido! Digite novamente quantas pessoas fizeram parte da pesquisa: "))

def verifica1 (pesquisa):
  while (len(pesquisa) != q):
    pesquisa = [int(x) for x in (input(f"Número inválido de opiniões! Digite novamente {q} opiniões que variam entre satisfatório (0) e não satisfatório (1) (separadas por espaço): ")).split()]
  for p in pesquisa:
      if((p != 0) and (p != 1)):
        certo = 0
        break
      else:
        certo = 1
  while (certo == 0):
    pesquisa = [int(x) for x in (input(f"Número inválido para opiniões! Digite novamente {q} opiniões que variam entre satisfatório (0) e não satisfatório (1) (separadas por espaço): ")).split()]
    for p in pesquisa:
      if((p != 0) and (p != 1)):
        certo = 0
        break
      else:
        certo = 1
  return pesquisa

# Verifica se 0 é maioria ou não
def maioria(pesquisa):
  soma = 0
  res = ""
  for l in pesquisa:
    soma += l

  if (soma < len(pesquisa)/2):
    res = "S"

  else:
    res = "N"

  return res  

# Usuário digita quantas pessoas fizeram parte da pesquisa
q = int(input("Digite quantas pessoas fizeram parte da pesquisa: "))

# Usuário digita as opiniões das pessoas
pesquisa = [int(x) for x in (input(f"Digite {q} opiniões que variam entre satisfatório (0) e não satisfatório (1) (separadas por espaço): ")).split()]
pesquisa = verifica1(pesquisa)
res = maioria(pesquisa)

# Mostra se a maioria acha a situação atual satisfatória (ou não)
print(res)