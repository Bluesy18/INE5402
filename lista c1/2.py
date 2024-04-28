### 2 ###

num = []
r = 0

n = int(input("Digite quantos números você adicionará: "))

for i in range(n):
    num.append(int(input("Digite um número inteiro: ")))

for j in range (n):
    rep = num.count(num[j])
        
    if (rep > 1):
        r = 1
        print("Existem números repetidos.")
        break

if (r == 0):
    print("Não existem número repetidos.")
    

    

    



