### 8 ###

# Usuário digita as notas
n1a, n2a, n3a, n4a, n5a = map(float, input("Digite as cinco notas separados por espaço: ").split())

# Arredondamento das notas
n1 = round(n1a, 1)
n2 = round(n2a, 1)
n3 = round(n3a, 1)
n4 = round(n4a, 1)
n5 = round(n5a, 1)

# Verifica a qual a menor e a maior nota
for i in range(4):
    if n1 > n2:
        n1, n2 = n2, n1
    if n2 > n3:
        n2, n3 = n3, n2
    if n3 > n4:
        n3, n4 = n4, n3
    if n4 > n5:
        n4, n5 = n5, n4

# Calcula nota final
nf = round(n2+n3+n4, 1)

# Mostra a nota final
print(nf)




