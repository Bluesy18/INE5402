### 3 ###

def verifica(n):

    if (n%2 == 0):
        return "par"
    else:
        return "impar"
    
def contpar(contapar):

    return contapar + 1

def contimpar(contaimpar):
     
     return contaimpar + 1

contapar = 0
contaimpar = 0

int(contapar)
int(contaimpar)
    
for i in range(10):
    n = int(input("Digite um número inteiro: "))
    print(f"O número é {verifica(n)}.")

    if (n%2 == 0):
        contapar = contpar(contapar)

    else:
        contaimpar = contimpar(contaimpar)
    
print(f"Você digitou {contapar} números pares.\nVocê digitou {contaimpar} números ímpares.")