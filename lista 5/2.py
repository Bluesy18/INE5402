### 2 ###

# Usuário digita 3 números inteiros
n1, n2, n3 = map(int, input("Digite três números inteiros separados por espaço: ").split())

# Organiza em ordem crescente
for i in range(2):
    if n1 > n2:
        n1, n2 = n2, n1
    if n2 > n3:
        n2, n3 = n3, n2
        
# Mostra os números em ordem
print(f"Primeiro: {n1}\nSegundo: {n2}\nTerceiro: {n3}")




