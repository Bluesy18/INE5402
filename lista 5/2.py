''' 2 '''

n1, n2, n3 = map(int, input("Digite três números inteiros separados por espaço: ").split())

for i in range(2):
    if n1 > n2:
        n1, n2 = n2, n1
    if n2 > n3:
        n2, n3 = n3, n2
        
print(f"Primeiro: {n1}\nSegundo: {n2}\nTerceiro: {n3}")




