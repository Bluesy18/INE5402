#1
for i in range(2004, 2100, 4):
    print(i)
    
#2
for i in range(1, 51, 2):
    print(i)
    
#3
for i in range(1, 6):
    nome = input("Digite seu nome: ")
    media = round(float(input("Digite sua nota/média geral: ")), 2)
    mensal = float(input("Digite o valor de sua mensalidade: "))

    if(i == 1):
        mNome = nome
        mMedia = media
        mMensal = mensal
        
    elif(i != 1):
        if(mMedia < media):
            mNome = nome
            mMedia = media
            mMensal = mensal
            
print(f"""O aluno que receberá o desconto é {mNome}
\nA mensalidade antes do desconto era de R${mMensal}
\nA mensalidade após o deconto ficou com o valor de R${mMensal-(mMensal*0.3)}""")
