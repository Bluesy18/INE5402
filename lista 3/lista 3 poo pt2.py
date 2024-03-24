#7
somaidade = 0
n = int(input("Digite o número de pessoas: "))
for i in range (1, n+1):
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))
    somaidade += idade
    
media = somaidade/n

if (media <= 25):
    print("A turma é jovem")
    
elif (media <= 60):
    print("A turma é adulta")
    
elif (media > 60):
    print("A turma é idosa")
        

#6
co = 0
num = int(input("Digite um número inteiro: "))
for i in range (2, num):
    res = num%i
    if(res == 0):
        co += 1
        final = str(i)
        print(f"O número é divisível por {final}")
if(co != 0):
    print("Não é primo.")
if(co == 0):
    print("É primo.")

#4
par = 0
impar = 0
for i in range(1, 11):
    num = int(input("Digite um número inteiro: "))
    if (num%2 == 0):
        par += 1
    else:
        impar += 1

print(f"""A quantidade de números pares é: {par}
A quantidade de números impares é: {impar}""")

#5
co = 0
num = int(input("Digite um número inteiro: "))
for i in range (2, num):
    res = num%i
    if(res == 0):
        co += 1
if(co != 0):
    print("Não é primo.")
if(co == 0):
    print("É primo.")
    
    

