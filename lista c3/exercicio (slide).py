# Exercico do slide

# Cria lista de pares, ímpares e do resultado
par = []
impar = []
resultado = []

# Usuário digita 10 inteiros
for i in range(10):
    n = int(input("Digite um número inteiro: "))
    # Separa os pares e os ímpares
    if (n%2) == 0 :
        par.append(n)
    
    else:
        impar.append(n)
    
# Ordena as listas de maneira crescente
par.sort()
impar.sort()

# Junta os pares e ímpares em uma só lista
resultado.append(par)
resultado.append(impar)

# Mostra o resultado
print(resultado)
        