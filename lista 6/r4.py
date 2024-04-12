### 4 ###

# Função que conta primos
def contaPrimo (n, m): 
  somaP = 0

  for i in range (m, n-1, -1):

    # Variável de controle (np == 0 -> primo, np == 1 -> não primo)
    np = 0 

    for j in range (2, i):

      # Divide i por j, a fim de descobrir se ele é divisível por algum número, se for, incrementa 1 na variável np e interrompe o loop
      if (i%j == 0):
        np += 1
        break

    # Se número for primo, acrescenta na contagem de primos
    if (np == 0):
      somaP += 1

  # Retorna quantidade de rimos no intervalo
  return somaP

# Usuário digita intervalo
n, m = map(int, input("Digite o primeiro e o útimo número do intervalo (separados por espaço): ").split())

# Mostra ao usuário quantos primos existem naquele intervalo
print(f"Existem {contaPrimo(n, m)} números primos nesse intervalo")







  
