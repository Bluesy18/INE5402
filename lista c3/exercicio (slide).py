par = []
impar = []
resultado = []


for i in range(10):
    n = int(input("Digite um número inteiro: "))
    if (n%2) == 0 :
        par.append(n)
    
    else:
        impar.append(n)
    

par.sort()
impar.sort()

resultado.append(par)
resultado.append(impar)

print(resultado)
        