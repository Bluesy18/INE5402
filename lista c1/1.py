### 1 ###

# Cria lista e contador
notas = []
soma = 0

# Cria função que organiza a lista de maneira crescente
def melhornota(notas):
    for i in range(2):
        if notas[0] > notas[1]:
            notas[0], notas[1] = notas[1], notas[0]
        if notas[1] > notas[2]:
            notas[1], notas[2] = notas[2], notas[1]
            
    dif = notas[2] - notas[0]        
    
    return notas, dif

# Cria função que calcula média das notas
def media(notas):
    return (soma/len(notas))

# Cria função que verifica se notas obedecem intervalo
def verifica (notas):
    while ((0 > notas[i]) or (10 < notas[i])):
        notas[i] = int(input("Nota inválida! Digite novamente uma nota: "))
        
    return notas[i]
    
# Usuário digita 3 notas
for i in range (3):
    notas.append(int(input("Digite uma nota: ")))
    notas[i] = verifica(notas)
    soma += notas[i]

# Variáveis recebem retorno de funções    
med = media(notas)    
notas, dif = melhornota(notas)

# Mostra ao usuário a média, a maior, a menor nota e a diferença entre elas
print(f"Média: {med}\nMaior nota: {notas[2]}\nMenor nota: {notas[0]}\nDiferença: {dif}")
           
    