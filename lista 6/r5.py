### 5 ###
i = 0
idade = 0
somaidade = 0

def soma(somaidade,idade,i):
    
    somaidade += idade
    i += 1
    
    return somaidade, i

def media(somaidade, i):
    media = somaidade/i
    return media

while (idade >= 0):
    if (idade < 0):
        break
    else:
        idade = int(input("Digite a idade: "))
        s,i=soma(somaidade,idade,i)
print(somaidade,i)   
print(media(somaidade, i))
    
