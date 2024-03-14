############# Fiz a 1003, 1004, 1005 e 1009 em sala com o André #############

############# As variáveis estão em maísculo pois na dúvida eu decidi seguir a rica o texto #############

###1003###

#usuário digita dois valores#
A = int(input("Digite um número: "))
B = int(input("Digite um número: "))

#soma#
SOMA = A+B

#resultado#
print(f"SOMA = {SOMA}")

###1004###

#usuário digita dois valores#
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))

#produto#
PROD = a*b

#resultado#
print(f"PROD = {PROD}")

###1005###

#usuário digita suas notas#
A = float(input("Digite sua nota (de 0 a 10, com uma casa após o ponto): "))
B = float(input("Digite sua outra nota (de 0 a 10, com uma casa após o ponto): "))

#atribuindo os pesos#
AP = A*3.5
BP = B*7.5

#media ponderada#
media = (AP+BP)/11

#resultado#
print(f"MEDIA = {media}")

###1009###

# Usuário digita suas informações
nome = input("Digite seu nome: ")
sal = float(input("Digite seu salário: "))
venda = float(input("Digite o total que você vendeu: "))

# Cálculo do bônus
bonus = venda*0.15

# Cálculo e arredondamento do salário acrescido
salSoma = sal+bonus
salF = round(salSoma, 2)

print(f"Seu salário acrescido do bônus é de R${salF}")