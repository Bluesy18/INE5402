### 10 ###

# Cria variáveis de soma e de situação
somaNota = 0
situacao = ""

for i in range(1, 6):
    # Usuário digita o nome dos alunos e das notas
    nome = input("Digite seu nome: ")
    nota = round(float(input("Digite sua nota média (entre 0 e 10): ")), 2)

    # Verifica se as notas são válidas
    if((nota < 0) or (nota > 10)):
      print("Nota inválida.")
      quit()  
    else:
      # Soma as notas
      somanota += nota

      # Verificar qual aluno tirou a melhor nota
      if(i == 1):
          mNome = nome
          mNota = nota
          
      elif(i != 1):
          if(mNota < nota):
              mNome = nome
              mNota = nota

# Calcula a média das notas
media = round((somaNota/5), 2)

# Determina a situação do melhor aluno
if(mNota >= 5.75):
        situacao = "aprovado"

elif(mNota >= 2.75):
        situacao = "de recuperação"

elif(mNota < 2.75):
        situacao = "reprovado"

# Mostra a média e a situação do melhor aluno
print(f"A média das notas foi de {media}.\nO aluno com a maior nota foi {mNome} e ele está {situacao}.")
