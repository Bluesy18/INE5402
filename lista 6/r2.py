''' 2 '''
somaNota = 0
mNota = 0
mNome = 0
media = 0

def notas(nome, nota):
    
      global somaNota
      global mNota
      global mNome
      global media
    
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
                  
                  
      return media, mNome, mNota
    
def verifica(nota):
    if((nota < 0) or (nota > 10)):
      print("Nota inválida.")
      quit()
      
def situacao(mNota):
    if(mNota >= 5.75):
        situacao = "aprovado"

    elif(mNota >= 2.75):
        situacao = "de recuperação"

    elif(mNota < 2.75):
        situacao = "reprovado"
        
    return situacao
    
    

for i in range(1, 6):
    # Usuário digita o nome dos alunos e das notas
    nome = input("Digite seu nome: ")
    nota = round(float(input("Digite sua nota média (entre 0 e 10): ")), 2)
    verifica(nota)
    notas(nome, nota)
    
situacao(mNota)

print(f"A pessoa com a melhor nota foi o(a): {mNome} \nSua nota foi: {mNota}\nEle/Ela foi {situacao(mNota)}\nA média da turma foi: {media}")
