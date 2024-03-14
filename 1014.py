### 1014 ###

# Usuário digita a ditância total percorrida e o gasto total de combustível
distancia = float(input("Digite a distância total percorrida: "))
gastoT = float(input("Digite o gasto total de combustível: "))

# Arredondamento do gasto
gastoTA = round(gastoT, 1)

# Cálculo e arredondamento do consumo médio de combustível
consumo = distancia/gastoTA
consumoA = round(consumo, 3)

# Apresenta o consumo médio do automóvel ao usuário
print(f"O consumo médio do automóvel é de {consumoA} km/l")