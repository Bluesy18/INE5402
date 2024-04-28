### 4 ###

def calc(x,k,n):
    res = []
    for i in range (n):
        res.append(k*x[i])
    return res

x = []

n = int(input("Digite um número inteiro: "))

for i in range(n):
    x.append(int(input("Adicione um número inteiro à sua lista: ")))
    
k = int(input("Digite um número inteiro: "))

res = calc(x,k,n)

print(res)