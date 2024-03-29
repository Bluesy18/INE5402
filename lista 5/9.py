### 9 ###

# Variável de contagem de teste
t = 1

# Variável de resposta
r = "S"

# Variável de débito
d = 0

while (r == "S"):
  # Usuário digita o númerod e depósitos
  n = int(input("Digite o número de depósitos: "))

  for i in range (n):

    # Usuário digita os valores dos depósitos
    j, z = map(int, input("Digite o valor depositado para Joãozinho e para Zezinho, respectivamente (separado por espaço): ").split())
    
    # Calcula débito
    d = j - z + d

    # Mostra qual o teste
    if (i == 0):
      print(f"Teste {t}")
    
    # Mostra o débito
    print(d)

    # Ao fim, pergunta se o usuário gostaria de testar novamente
    if (i == n-1):
      t += 1
      r = input("Deseja testar novamente? (S/N): ").upper()