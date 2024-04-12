### 2 ###

# Função calcula melhor nota e media
def notas(nome, nota, mNome, mNota, somaNota, media):
      # Soma as notas
      somaNota += nota
      # Verificar qual aluno tirou a melhor nota
      if(i == 1):
              mNome = nome
              mNota = nota
              
      elif(i != 1):
         if(mNota < nota):
             mNome = nome
             mNota = nota
                  
      # Calcula a média das notas
      media = round((somaNota/i), 2)

      # Retorna seguintes variáveis
      return media, mNome, mNota, somaNota
    
# Função verifica se nota obedece os limites, se não, pede outro input
def verifica(nota):
    while ((nota < 0) or (nota > 10)):
      nota = round(float(input("Nota inválida. Digite novamente: ")), 2)

# Função define situação do melhor aluno
def situacao(mNota):

    # Interpreta a melhor nota e define situação
    if(mNota >= 5.75):
        situacao = "aprovado"

    elif(mNota >= 2.75):
        situacao = "de recuperação"

    elif(mNota < 2.75):
        situacao = "reprovado"

    # Retorna a situação 
    return situacao
    
# Define variáveis
mNome = ""
mNota = 0
somaNota = 0
media = 0
    
# Faz seguintes procedimentos ara 5 alunos diferentes
for i in range(1, 6):
    # Usuário digita o nome dos alunos e das notas
    nome = input("Digite seu nome: ")
    nota = round(float(input("Digite sua nota média (entre 0 e 10): ")), 2)

    # Chama função verifica()
    verifica(nota)

    # Armazena valores retornados
    media, mNome, mNota, somaNota = notas(nome, nota, mNome, mNota, somaNota, media)
    
# Chama função situacao()
situacao(mNota)

# Mostra qual foi o melhor aluno, sua nota e situação, além da média da turma
print(f"A pessoa com a melhor nota foi o(a): {mNome} \nSua nota foi: {mNota}\nEle/Ela foi {situacao(mNota)}\nA média da turma foi: {media}")
