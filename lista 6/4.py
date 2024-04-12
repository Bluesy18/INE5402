### 4 ### 

# Função verifica se valores estão dentro dos limites, caso não estiverem, pede novo input
def verificaG (saida, tempo, fuso):
    while ((0 > saida) or (saida > 23) or (1 > tempo) or (tempo > 12) or (-5 > fuso) or (fuso > 5)):
        saida, tempo, fuso = map(int,input("Valores incorretos! Digite novamente: ").split())

# Função calcula tempo de chegada
def app(saida, tempo, fuso):
    soma = saida+tempo+fuso
    while (soma >= 24):
        soma -= 24
    print(soma)

# Usuário digita hora de saída, tempo de viagem e o fuso horário
saida, tempo, fuso = map(int,input("Digite a hora de saida, o tempo de viagem e o fuso: ").split())

# Chama funções para verificar valores e horário de chegada
verificaG(saida, tempo, fuso)
app(saida, tempo, fuso)
