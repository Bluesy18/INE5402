### 3 ###

tupla = (6,8,4,9,2,5,7,3,10,1)

lista = list(tupla)

lista0 = lista[:]

for i in range(9):
        if lista[0] > lista[1]:
            lista[0], lista[1] = lista[1], lista[0]
        if lista[1] > lista[2]:
            lista[1], lista[2] = lista[2], lista[1]
        if lista[2] > lista[3]:
            lista[2], lista[3] = lista[3], lista[2]
        if lista[3] > lista[4]:
            lista[3], lista[4] = lista[4], lista[3]
        if lista[4] > lista[5]:
            lista[4], lista[5] = lista[5], lista[4]
        if lista[5] > lista[6]:
            lista[5], lista[6] = lista[6], lista[5]
        if lista[6] > lista[7]:
            lista[6], lista[7] = lista[7], lista[6]
        if lista[7] > lista[8]:
            lista[7], lista[8] = lista[8], lista[7]
        if lista[8] > lista[9]:
            lista[8], lista[9] = lista[9], lista[8]
            
print(f"A posição do maior número da tupla é {lista0.index(lista[9])} e do menor é {lista0.index(lista[0])}")


            



