### 1281 ###

def somador(preco, qntd, precoTotal):
  precoTotal += preco*qntd

  return precoTotal

def verifica0(nome, qntd, precoTotal):
  existe = 0
  while True:
    for l in produtos:
      if ((nome in l.values()) and (qntd >= 1)):
        existe = 1
        break
    if (existe == 1):
      preco = l.get("preço")
      precoTotal = somador(preco, qntd, precoTotal)
      break
    else:
      nome, qntd = input("Algo deu errado! Digite novamente o nome e quantidade comprada: ").split()
      qntd = int(qntd)
  
  return nome, qntd, precoTotal

def verifica1(p, m):
  while (p > m):
    p = int(input("Quantiade inválida! Digite novamente a quantidade de produtos diferentes que serão comprados: "))

  return p

n = int(input("Digite a quantidade de idas à feira: "))

for i in range(n):
  precoTotal = 0
  produtos = []
  m = int(input("Digite a quantidade de produtos que estão disponíveis para compra: "))
  for j in range(m):
    prod = {}
    prod["nome"], prod["preço"] = input("Digite o nome e o preço do produto: ").split()
    prod["preço"] = float(prod["preço"])
    produtos.append(prod)
  p = int(input("Digite a quantidade de produtos diferentes que serão comprados: "))
  p = verifica1(p, m)
  for k in range(p):
    nome, qntd, = input("Digite o nome e quantidade comprada: ").split()
    qntd = int(qntd)
    nome, qntd, precoTotal = verifica0(nome, qntd, precoTotal)
  print(f"R$ {round(precoTotal, 2)}")

### 2482 ###

n = int(input("Digite a quantidade de traduções: "))

etiquetas = []
saudacoes = {}
etiqueta = {}

for i in range(n):
  idioma = input("Digite o idioma: ")
  saudacoes[idioma] = input("Digite a saudação no respectivo idioma: ")

m = int(input("Digite quantas crianças receberão as etiquetas: "))

for j in range(m):
  etiqueta["nome"] = input("Digite o nome da criança: ")
  idioma = input("Digite o idioma nativo da respectiva criança: ")
  etiqueta["saudacao"] = saudacoes.get(idioma)
  etiquetas.append(etiqueta)

for l in etiquetas:
    print(l.get("nome"))
    print(l.get("saudacao"))

### 1911 ###

n = int(input("Digite a quantidade de assinaturas existentes: "))

while (n > 0):
  assinaturas = {}
  fake = 0
  for i in range(n):
    nome, assinaturas[nome] = input("Digite o nome do aluno e sua assinatura original: ").split()

  m = int(input("Digite quantas assinaturas deseja conferir: "))
  for j in range(m):
    nome2, assinatura2 = input("Digite o nome do aluno e a assinatura na sala: ").split()
    if (assinaturas.get(nome2) != assinatura2):
      fake += 1

  print(fake)
  n = int(input("Digite a quantidade de assinaturas existentes: "))

### 1763 ###

natal = {"brasil": "Feliz Natal!",
"alemanha":           "Frohliche Weihnachten!",
"austria"  :           "Frohe Weihnacht!",
"coreia"    :        "Chuk Sung Tan!",
"espanha"    :         "Feliz Navidad!",
"grecia"     :         "Kala Christougena!",
"estados-unidos":    "Merry Christmas!",
"inglaterra" :        "Merry Christmas!",
"australia"   :        "Merry Christmas!",
"portugal"     :       "Feliz Natal!",
"suecia"        :     "God Jul!",
"turquia"        :     "Mutlu Noeller",
"argentina"       :    "Feliz Navidad!",
"chile"           :    "Feliz Navidad!",
"mexico"          :    "Feliz Navidad!",
"antardida"        :   "Merry Christmas!",
"canada"            :  "Merry Christmas!",
"irlanda"      :       "Nollaig Shona Dhuit!",
"belgica"       :      "Zalig Kerstfeest!",
"italia"         :     "Buon Natale!",
"libia"           :    "Buon Natale!",
"siria"            :   "Milad Mubarak!",
"marrocos"       :     "Milad Mubarak!",
"japao"           :    "Merii Kurisumasu!"}

pais = input("Digite o país: ")
print(natal.get(pais, "--- NOT FOUND ---"))

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

  
