### 5 ###

def verifica0 (ano, ano2):
  while(ano2 < ano):
    ano2 = int(input("Ano inválido! Digite novamente o ano que a pessoa foi contratada: "))

  return ano2

cadastrodepessoas = []

menu = int(input("Digite: 1 - Cadastrar usuário, 2 - Imprimir dados (pesquisar pelo nome), 3 - Imprimir dados (todos os usuários), 4 - Encerrar programa: "))

while True:
  if (not((menu == 1) or (menu == 2) or (menu == 3))):
    exit()
    
  while (menu == 1):
    pessoa = {}
    pessoa["Nome"] = input("Digite o nome da pesoa: ")
    ano = int(input("Digite o ano que a pessoa nasceu: "))
    pessoa["Idade"] = 2024 - ano
    pessoa["Carteira de trabalho"] = int(input("Digite o número da carteira de trabalho: "))

    if (pessoa["Carteira de trabalho"] != 0):
      ano2 = int(input("Digite o ano que a pessoa foi contratada: "))
      ano2 = verifica0(ano, ano2)
      pessoa["Ano de contratação"] = ano2
      pessoa["Salário"] = float(input("Digite o salário da pessoa: "))
      anosApos = (35 - (2024 - pessoa["Ano de contratação"]))
      if (anosApos <= 0):
        pessoa["Idade de aposentadoria"] = "Aposentado"
      else:
        pessoa["Idade de aposentadoria"] = anosApos + pessoa["Idade"]
    
    cadastrodepessoas.append(pessoa)
    menu = int(input("Digite: 1 - Cadastrar usuário, 2 - Imprimir dados (pesquisar pelo nome), 3 - Imprimir dados (todos os usuários), 4 - Encerrar programa: "))

  while (menu == 2):
    existe = 0
    nome = input("Digite o nome da pessoa: ")
    for l in cadastrodepessoas:
      if (l.get("Nome") == nome):
        cadastro = cadastrodepessoas.index(l)
        existe = 1
        print(cadastrodepessoas[cadastro])
        break
    if(existe == 0):
      print("Pessoa não encontrada.")

    menu = int(input("Digite: 1 - Cadastrar usuário, 2 - Imprimir dados (pesquisar pelo nome), 3 - Imprimir dados (todos os usuários), 4 - Encerrar programa: "))

  while (menu == 3):
    print(cadastrodepessoas)
    menu = int(input("Digite: 1 - Cadastrar usuário, 2 - Imprimir dados (pesquisar pelo nome), 3 - Imprimir dados (todos os usuários), 4 - Encerrar programa: "))

  