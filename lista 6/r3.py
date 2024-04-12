### 3 ###

# Função verifica se número n é par ou ímpar
def verifica(n):

    if (n%2 == 0):
        return "par"
    else:
        return "impar"
    
# Função conta quantos números pares foram digitados
def contpar(contapar):

    return contapar + 1

# Função conta quantos números ímpares foram digitados
def contimpar(contaimpar):
     
     return contaimpar + 1

# Define variáveis de contagem e as converte para inteiro
contapar = 0
contaimpar = 0

int(contapar)
int(contaimpar)
    
# Pede 10 vezes..;    
for i in range(10):
    # Que o usuário digite um número inteiro
    n = int(input("Digite um número inteiro: "))

    # Mostra se número é par ou ímpar
    print(f"O número é {verifica(n)}.")

    # Armazena variáveis com os valores retornados
    if (n%2 == 0):
        contapar = contpar(contapar)

    else:
        contaimpar = contimpar(contaimpar)
    
# Mostra quantidade de números pares e ímpares
print(f"Você digitou {contapar} números pares.\nVocê digitou {contaimpar} números ímpares.")