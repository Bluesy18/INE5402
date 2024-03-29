''' 2+1 '''

x = 0
y = 1

while (x != y):
    x, y = map(int, input("Digite dois números inteiros separados por espaço: ").split())
    
    if (x < y):
        print("Crescente")
        
    elif (x > y):
        print("Decrescente")

