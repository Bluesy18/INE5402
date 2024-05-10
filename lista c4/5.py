''' 5 '''

medTop = 0    
somaTop = 0
somaPar = 0
somaPrin = 0
somaUlt = 0
medPrin = 0
prodSec = 1 
                

t = int(input("Digite a ordem da matriz: "))

linha = [0] * t
matriz = [linha] * t
    
for i in range (t):
    linha = []
    for j in range (t):
        nume = int(input(f"Digite o número {i}, {j}: "))
        if (nume%2 == 0):
            somaPar += nume
        
        if (i == j):
            somaPrin += nume
            medPrin = somaPrin/t
            
        if (i+j == t):
            prodSec = nume*prodSec
            
        if (j-i == 1):
            somaTop += nume
            mediaTop = somaTop/(t-1)
            
        if (j == t):
            somaUlt += nume
        
        
        linha.append(nume)
        
    matriz[i] = linha
    
for k in range(t):
    if (k == 0):
        menor = matriz[0][k]
        
    elif (matriz[0][k] < menor):
        menor = matriz[0][k]
        
for p in matriz:    
    print(*p, end="\n")
    

print(f"a) {somaPar}\nb) {medPrin}\nc) {prodSec}\nd) {mediaTop}\ne) {somaUlt}\nf) {menor}")