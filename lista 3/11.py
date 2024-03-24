### 11 ###

# Cria variável de soma
somanum = 0

# Usuário digita quantidade de números que irá inserir
n = int(input("Digite a quantidade n de números que serão lidos pelo teclado: "))

for i in range (n):
  # Usuário digita os números
  num = int(input("Digite um número inteiro: "))
  
  # Soma os números digitados
  somanum += num

  # Verifica o maior e o menor número
  if(i == 0):
        maNum = num
        meNum = num
        
  elif(i != 0):
      
      if(num > maNum):
          maNum = num
      
      elif(num < meNum):
          meNum = num

# Calcula a média dos números digitados
media = somanum/n

# Mostra a média, o maior e o menor número
print(f"A média entre os números foi {media}, o maior número foi {maNum} e o menor número foi {meNum}")