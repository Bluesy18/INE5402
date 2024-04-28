### 1 ###

notas = []
soma = 0

def melhornota(notas):
    for i in range(2):
        if notas[0] > notas[1]:
            notas[0], notas[1] = notas[1], notas[0]
        if notas[1] > notas[2]:
            notas[1], notas[2] = notas[2], notas[1]
            
    dif = notas[2] - notas[0]        
    
    return notas, dif





def media(notas):
    return (soma/len(notas))

def verifica (notas):
    
    while ((0 > notas[i]) or (10 < notas[i])):
        notas[i] = int(input("Nota inválida! Digite novamente uma nota: "))
        
    return notas[i]
    

for i in range (3):
    notas.append(int(input("Digite uma nota: ")))
    notas[i] = verifica(notas)
    soma += notas[i]
    
media = media(notas)    
notas, dif = melhornota(notas)
        
print(f"Média: {media}\nMaior nota: {notas[2]}\nMenor nota: {notas[0]}\nDiferença: {dif}")
           
    