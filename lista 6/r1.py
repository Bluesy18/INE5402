### 1 ###

def verifica1 (a, b, c, h, l):
    r = 0
    if((a < 1 or a > 300) or (b < 1 or b > 300) or (c < 1 or c > 300) or (h < 1 or h > 250) or (l < 1 or l > 250)):
        r +=1 
    return r

def verifica2 (a, b, c, h, l):
    if(a <= h and b <= l) or (a <= l and b <= h):
        r = 0
    
    elif(a <= h and c <= l) or (a <= l and c <= h):
        r = 0
        
    elif(b <= h and c <= l) or (b <= l and c <= h):
        r = 0

    else:
        r = 2
        
    return r
    

a, b, c = map(int, input("Digite as dimensões do colchão (separadas por espaço): ").split())
h, l = map(int, input("Digite as dimensões da porta (separadas por espaço): ").split())

verifica1(a, b, c, h , l)

if (verifica1(a, b, c, h , l) != 1):
    verifica2(a, b, c, h, l)
    
    if(verifica2(a, b, c, h, l) == 0):
        print("O colchão está adequado ao tamanho. Parabéns por sua compra!")
    
    elif (verifica2(a, b, c, h, l) == 2):
        print("Você deve procurar outro colchão.")
        
else:
    print("Dimensões inválidas.")