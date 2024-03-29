''' 14 '''

cont = 0

n = int(input("Digite quantas bandejas foram usadas: "))

for i in range(n):
    l, c = map(int, input("Digite quantas latas e copos, respectivamente, foram usados (separados por espaço): ").split())
    if l>c :
        cont += c

print(cont)