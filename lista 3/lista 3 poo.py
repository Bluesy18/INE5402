### 1 ###

# Mostra anos de 4 em 4 anos (bissextos)
for i in range(2004, 2100, 4):
    print(i)
    
### 2 ###
    
# Mostra números ímpares
for i in range(1, 51, 2):
    print(i)
    
### 3 ###
    
# Define quantiadade de vezes os próximos comandos são executados
for i in range(1, 6):

    # Usuário digita o nome do aluno, sua média e a mensalidade
    nome = input("Digite seu nome: ")
    media = round(float(input("Digite sua nota/média geral: ")), 2)
    mensal = float(input("Digite o valor de sua mensalidade: "))

    # Verfica qual o aluno com a melhor nota
    if(i == 1):
        mNome = nome
        mMedia = media
        mMensal = mensal
        
    elif(i != 1):
        if(mMedia < media):
            mNome = nome
            mMedia = media
            mMensal = mensal
            
# Mostra o aluno que receberá o desconto, sua mensalidade antes e após o desconto
print(f"""O aluno que receberá o desconto é {mNome}
\nA mensalidade antes do desconto era de R${mMensal}
\nA mensalidade após o deconto ficou com o valor de R${mMensal-(mMensal*0.3)}""")
