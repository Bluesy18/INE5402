### r1 ###

# Verifica se valores do colchão estão de acordo com os limites
def verifica0 (a, b, c):
    while((a < 1 or a > 300) or (b < 1 or b > 300) or (c < 1 or c > 300)):
        a, b, c = map(int, input("Dimensões do colchão erradas, digite novamente: ").split())

# Verifica se valores da porta estão de acordo com os limites
def verifica1 (h, l):
    while((h < 10 or h > 250) or (l <10 or l > 250)):
       h, l = map(int, input("Dimensões da porta erradas, digite novamente: ").split())

# Interpreta se colchão passa ou não ela porta e retorna variável r
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
    
# Usuário digita as dimensões do colchão, em seguida, as dimensões são verificadas
a, b, c = map(int, input("Digite as dimensões do colchão (separadas por espaço): ").split())
verifica0(a, b, c)

# Usuário digita as dimensões da porta, em seguida, as dimensões são verificadas
h, l = map(int, input("Digite as dimensões da porta (separadas por espaço): ").split())
verifica1( h , l)

# Chama a função verifica2() com os seguintes parâmetros
verifica2(a, b, c, h, l)
    
# Dependendo do valor da variável r, diz ao usuário se o colchão passa ou não pela porta
if(verifica2(a, b, c, h, l) == 0):
    print("O colchão está adequado ao tamanho. Parabéns por sua compra!")
    
elif (verifica2(a, b, c, h, l) == 2):
    print("Você deve procurar outro colchão.")
        
