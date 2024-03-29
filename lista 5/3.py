### 3 ###

# Cria variável dos números
x = 0
y = 1

while (x != y):
    # Usuário informa os números
    x, y = map(int, input("Digite dois números inteiros separados por espaço: ").split())
    
    # Verifica e informa se números foram informados em ordem crescente os decrescente
    if (x < y):
        print("Crescente")
        
    elif (x > y):
        print("Decrescente")

