### 8 ###

# Cria uma variável para armazenar o valor da soma
somaint = 0

# Usuário digita primeiro e último número da sequência
pn, un = map(int, input("Digite o primeiro e o último número da sequência (separados por espaço): ").split())
for i in range(pn+1, un):
  # Soma números do intervalo
  somaint += i
  
# Mostra a soma dos números do intervalo
print(f"A soma dos números do intervalo vale {somaint}")