### 5  ###

# Cria variáveis para operação
somaTop = 0
somaPar = 0
somaPrin = 0
somaUlt = 0
medPrin = 0
prodSec = 1 
                
# Usuário digita ordem da matriz
t = int(input("Digite a ordem da matriz: "))

# Cria matriz
linha = [0] * t
matriz = [linha] * t

# Usuário insere números na matriz
for i in range (t):
    linha = []
    for j in range (t):
        nume = int(input(f"Digite o número {i}, {j}: "))

        # Interpreta se casos solicitados ocorreram
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

# Verifica qual o menor número    
for k in range(t):
    if (k == 0):
        menor = matriz[0][k]
        
    elif (matriz[0][k] < menor):
        menor = matriz[0][k]
        
for p in matriz:    
    print(*p, end="\n")
    
# Mostra resultados solicitados
print(f"a) {somaPar}\nb) {medPrin}\nc) {prodSec}\nd) {mediaTop}\ne) {somaUlt}\nf) {menor}")