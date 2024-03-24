### 12 ###

# Cria variável de soma
somaDist = 0
soma1520 = 0

# Usuário digita quantidade de praias que irá inserir
n = int(input("Digite a quantidade de praias que serão lidas pelo teclado: "))

for i in range(n):
    # Usuário digita o nome das praia e sua distância até o centro
    praia = input("Digite o nome da praia: ")
    dist = int(input("Digite sua distância em relação ao centro (em km): "))

    # Soma as distâncias digitadas
    somaDist += dist

    # Verifica se a distância da praia até o centro está entre 15 a 20 km
    if(20 >= dist >= 15):
        soma1520 += 1

    # Verifica qual praia é a mais distante
    if(i == 0):
        mDist = dist
        mPraia = praia

    elif(i != 0):

      if(dist > mDist):
          mDist = dist
          mPraia = praia
    
# Calcula a distância média das praias até o centro
media = round((somaDist/n), 1)

# Mostra qual é a praia mais distante do centro, quantidade de praias com a distância entre 15 e 20 km e a distância média das praias
print(f"A praia mais distante do centro é a praia {mPraia}\nExistem {soma1520} praia(s) com uma distância entre 15 a 20 km\nA distância média das praias é de {media} km")