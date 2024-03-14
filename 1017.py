### 1017 ###

# Usuário digita o tempo gasto na viagem e a velocidade média do veículo pelo trajeto
tempo = float(input("Digite o tempo gasto na viagem: "))
velmed = float(input("Digite a velocidade média durante a viagem: "))

# Distância percorrida na viagem
distancia = tempo*velmed

# Cálculo e arredondadmento de litros de combústivel que serão necessários para concluir a viagem
litros = distancia/12
litrosA = round(litros, 3)

# Apresenta ao usuário a quantidade de litros necessária para a viagem 
print(f"A quantidade de litros de combustível necessária para completar a viagem é de {litrosA}")