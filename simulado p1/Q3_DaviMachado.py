#Davi Roberge Machado
#24100573

# Cria variável de resposta
res = "S"

# Define função que soma números pertencentes ao intervalo
def soma(inicio, fim):

    # Cria variável de soma
    somacalc = 0

    # Cria loop obedecendo o intervalo
    for i in range(inicio, fim+1):

        # Soma números pertencentes ao intervalo
        somacalc += i

        # Mostra soma
    print(f"Soma do intervalo = {somacalc}")

# Define função de subtração de maior pelo menor
def subtracao(a,b):

    # Define qual variável é a menor e a subtrai da maior  
    if a>b :
        dif = a-b
    else :
        dif = b-a

    # Mostra a diferença
    print(f"Diferença = {dif}")

# Enquanto a resposta for sim, continua a pedir valores
while (res == "S"):

    # Usuário digita o intervalo
    inicio, fim = map(int, input("Digite o intervalo: ").split())

    # Chama função de soma
    soma(inicio, fim)

    # Usuário digita 2 valores
    a, b = map(int, input("Digite 2 valores: ").split())
    
    # Chama função de subtração
    subtracao(a,b)

    # Pergunta se usuário deseja continuar
    res = input("Deseja continuar? (S ou N): ").upper()
    