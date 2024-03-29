''' 4 '''

cont = 0
v = 1

n = int(input("Digite o número de testes que deseja fazer: "))

while (v != (1+n)):
    for i in range(n):
        v += 1
        x, y = map(int, input("Digite dois números inteiros separados por espaço: ").split())
        for j in range(x+1, y):
            if(j%2 != 0):
                cont += j                  
        print(cont)
        cont = 0
        