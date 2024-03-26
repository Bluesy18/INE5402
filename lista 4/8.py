### 8 ###

# Cria variável de soma
sum = 0

# Usuário digita o valor de M e N
m, n = map(int, input("Digite o valor de M e de N (separados por espaço): ").split())

# Enquanto M e N forem diferentes de 0... 
while (m != 0 and n != 0):
  # Gera sequência do menor para o maior e soma os números presentes na sequência
  if (m > n):
    for i in range (n, m+1):
      sum += i
      print(i, end = " ")
    print(f"Sum = {sum}")
  if (n > m):
    for i in range (m, n+1):
      sum += i
      print(i, end = " ")
    print(f"Sum = {sum}")

  # Zera variável de soma
  sum = 0

  # Pede novamente para digitar o valor de M e de N
  m, n = map(int, input("Digite o valor de M e de N (separados por espaço): ").split())
      
 
