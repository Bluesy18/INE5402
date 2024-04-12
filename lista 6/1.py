### 1 ###

# Define função de contador
def contador(i,f,p):
    
    # Mostra os parâmetros da contagem
    print(f"Contagem de {i} até {f} de {p} em {p}.")
    
    # Se passo for negativo, transforma-o em positivo
    if (p < 0) :
        p *= -1
    
    # Se passo for nulo, assume-se passo 1
    if (p==0):
        p=1
        
    # Se início da contagem for menor, começa a contagem
    if i<f:
        cont = i
        while (cont <= f):
            print(f"{cont}",end=" ")
            cont += p
        print(" Fim! ")
    else:
        cont = i
        while (cont >= f):
            print(f"{cont}",end=" ")
            cont -= p
        print(" Fim! ")
 
# Passa parâmetros pra função contador
contador(1,10,1)

contador(10,0,2)

print("Contagem personalizada: ")

# Usuário digita quais devem ser os parâmetros para uma contagem personalizada
ini,fim, pas = [int(x) for x in input("Digite inicio, fim e passo: ").split()]
contador(ini,fim,pas)