### 2478 ###

amigoSec = {}
resp = "S"

n = int(input("Digite a quantidade de participantes do amigo secreto: "))

for i in range (n):
  digitado = input("Digite o nome da pessoa e seus presentes desejados: ")
  listaDig = digitado.split(" ", 1)
  nomeDig = listaDig[0]
  amigoSec[nomeDig] = listaDig[1]

while (resp == "S"):
  acertou = 0

  escolha = input("Digite o nome do amigo secreto e os presentes que ele irá receber: ")
  listaEsc = escolha.split(" ", 1)
  nomeEsc = listaEsc[0]
  presentesEsc = listaEsc[1].split(" ")

  for l in presentesEsc:
    if (l in amigoSec.get(nomeEsc, "Tente Novamente!")):
      acertou = 1

  if(acertou == 0):
    print("Tente Novamente!")
  
  else:
    print("Uhul! Seu amigo secreto vai adorar o/")

  resp = input("Deseja tentar acertar as escolhas novamente? (S/N): ").upper()




