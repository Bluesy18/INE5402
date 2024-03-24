### 9 ###

# Usuário digita o número que deseja ver a tabuada 
num = int(input("Escreva o número que você deseja ver a tabuada (1 até 10): "))

# Mostra a tabuada
print(f"Tabuada do {num}:")
for i in range(1, 11):
  print(f"- {num} X {i} = {num*i}")
