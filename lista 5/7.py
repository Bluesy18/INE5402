### 7 ###

# Usuário digita os tempos
l, r = map(int, input("Digite o tempo do líder e do retardatário, respectivamente (separados por espaço): ").split())

# Calcula a volta em que se tornará retardatário
d = r-l
v = r/d

# Arredonda para cima
va = int(-(-v // 1))

# Mostra volta em que o líder ultrapassará o último colocado
print(va)