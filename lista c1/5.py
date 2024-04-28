### 5 ###

# Cria lista
x = list(range(20))

# Organiza de maneira decrescente
x[0], x[19] = x[19], x[0]
x[1], x[18] = x[18], x[1]
x[2], x[17] = x[17], x[2]
x[3], x[16] = x[16], x[3]
x[4], x[15] = x[15], x[4]
x[5], x[14] = x[14], x[5]
x[6], x[13] = x[13], x[6]
x[7], x[12] = x[12], x[7]
x[8], x[11] = x[11], x[8]
x[9], x[10] = x[10], x[9]

# Mostra lista de maneira decrescente
print(x)


