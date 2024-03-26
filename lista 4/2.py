### 2 ###

# Importa função "randrange" da biblioteca "random"
from random import randrange

# Seleciona um número aleatório de 0 a 10 e o armazena
num = randrange(11)

# Cria variável de contagem
cont = 1

# Usuário digita sua tentativa
usuario = int(input("Tente acertar o número entre 0 e 10: "))

# Enquanto o número que o usuário digita não for igual ao número armazenado, o input persiste
while (usuario != num):
    cont += 1
    usuario = int(input("Tente novamente: "))
    
# Informa o usuário que ele acertou e o número de tentativas
print(f"Acertou, o número era {num}\nVocê tentou {cont} vez(es).")
