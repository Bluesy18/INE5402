### 2 ###

# Calcula e mostra área de um quadrilátero
def area(l, c):
    areac = l*c
    print(areac)

# Usuário digita largura e comprimento, em seguida passa esses valores como parâmetros para a função área()
l, c = map(float, input("Digite a largura e comprimento: ").split())
area(l, c)




