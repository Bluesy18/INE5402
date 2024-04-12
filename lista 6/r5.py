### 5 ###

# Função soma as idades inseridas
def soma(somaidade, idade, i):
    
    somaidade += idade
    i += 1
    
    # Retorna valor da soma e quantas idades foram inseridas
    return somaidade, i

# Função calcula e retorna média das idades
def media(somaidade, i):
    media = somaidade/i
    return media

# Define variáveis no escopo global
i = 0
idade = 0
somaidade = 0

# Enquanto a idade inserida não for negativa, pede ao usuário digitar idade
while True:
    idade = int(input("Digite a idade: "))
    if(idade < 0):
        break
    else:
        somaidade, i = soma(somaidade, idade, i)

# Mostra média de idade
print(f"A média das idades é {media(somaidade, i)}")



    
