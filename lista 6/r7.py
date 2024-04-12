### 7 ###

# Funções verificam se os números digitados obedecem aos limites, caso não obedecerem, pede para usuário digitar novamente
def verifica0 (n):
  while ((n < 1) or (n > 10)):
    n = int(input("Quantidade incorreta! Digite novamente: "))

def verifica1 (p):
  while ((p < 1) or (p > 100)):
    p = int(input("Valor incorreto! Digite novamente: "))

  return p

# Função calcula distância percorrida e a acrescenta ao contador da distância total
def calcula_distancia (t, v, dtotal):
  d = t*v
  dtotal += d

  # Retorna a distância total
  return dtotal

# Cria contador da distância total
dtotal = 0

# Usuário digita quantos trechos serão lidos e em seguida verifica se quantidade é válida
n = int(input("Digite a quantidade de trechos a serem lidos: "))
verifica0(n)

# Para n trechos...
for i in range (n):
  # Usuário insere tempo decorrido e velocidade média
  t, v = map(int, input("Digite o tempo decorrido (em horas) e a velocidade média (em km/h) (separados por espaço): ").split())
  # Verifica valores inseridos
  t = verifica1(t)
  v = verifica1(v)

  # Armazena distância total retornada da função
  dtotal = calcula_distancia(t, v, dtotal)

# Mostra ao usuário a distância total percorrida e quantidades de trechos
print(f"Distância total percorrida: {dtotal} km considerando os {n} trechos.")


