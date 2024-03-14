### 1019 ###

# Usuário digita o tempo em segundos
N = int(input("Digite o tempo em segundos: "))

# Conversão de segundos para horas, minutos e segundos
horas = N // 3600
min = (N % 3600) // 60
seg = (N % 3600) % 60

# Apresenta as horas, minutos e segundos para o usuário
print(f"{horas}:{min}:{seg}")
