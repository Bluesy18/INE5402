end = 0

while end == 0:
    x1, y1, x2, y2 = map(int, input("Digite as coordenadas inciais e as coordenadas finais: ").split())
    if (x1+y1+x2+y2 == 0):
        end = 1
    else:
        if (x1 == x2) and (y1 == y2):
            print('0')
        elif (x1 == x2) or (y1 == y2) or (x1+y1 == x2+y2) or (x1-y1 == x2-y2):
            print('1')
        else:
            print('2')