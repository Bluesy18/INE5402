### 4 ###

# Cria lista vazia de quadrados pretos e de letras
preto = []
letras = ["A", "B", "C", "D", "E"]

# Usuário digita número de questões
n = int(input("Digite o número de questões: "))

# Enquanto n for diferente de 0
while (n != 0):
  # Usuário digita valor referente ao nível de cinza das opções da questão
  for i in range (n):
    questao = [int(x) for x in (input(f"Digite um número de 0 a 255: ")).split()]

    # Se for menor ou igual a 127, é considerado preto
    for p in questao:
      if (p <= 127):
        preto.append(p)

    # Se não houver exatamente 1 opção preenchida, mostra "*"
    if (len(preto) != 1):
      print("*")
      preto.clear()
      
    # Traduz a opção marcada para uma das letras
    else:
      letra = questao.index(preto[0])
      print(letras[letra])
      preto.clear()
      
  # Continua (ou não) o loop
  n = int(input("Digite o número de questões: "))