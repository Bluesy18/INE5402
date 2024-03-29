### 14 ###

# Cria variável de contagem
cont = 0

# Usuário digita quantas bandejas foram usadas
n = int(input("Digite quantas bandejas foram usadas: "))

for i in range(n):
    # Usuário digita quantidade de latas e de copos
    l, c = map(int, input("Digite quantas latas e copos, respectivamente, foram usados (separados por espaço): ").split())
    
    # Verifica se existem mais latas que copos
    if l>c :
        # Aumenta contagem de copos derrubados
        cont += c

# Mostra quantos copos foram derrubados
print(cont)