''' 4 '''

saida = -1
tempo = 0
fuso = 6

def app(saida, tempo, fuso):
    soma = saida+tempo+fuso
    while (soma >= 24):
        soma -= 24
    print(soma)
    
    
while ((0 > saida) or (saida > 23) or (1 > tempo) or (tempo > 12) or (-5 > fuso) or (fuso > 5)):
    saida, tempo, fuso = map(int,input("Digite a hora de saida, o tempo de viagem e o fuso: ").split())

if ((0 <= saida <= 23) and (1 <= tempo <= 12) and (-5 <= fuso <= 5)):
    app(saida, tempo, fuso)
