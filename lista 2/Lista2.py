############# Fiz da 1 até a 4 e a 1051 em sala com o André #############

### 1 ###

# Usuário digita seus dados
valor = float(input("Digite o valor total da casa: "))
salario = float(input("Digite o valor de seu salário: "))
anos = int(input("Digite em quanto anos você pagará o empréstimo: "))

# Valor das prestações
meses = anos*12
prestacao = valor/meses

# Caso a prestação exceda 30%, o empréstmo é negado
if(prestacao > (salario*0.3)):
    print("Seu empréstimo foi negado")

else:
    print("Seu empréstimo foi aceito")
    
### 2 ###
    
# Usuário digita seus dados    
valor = float(input("Digite o valor do produto: "))
forma = str(input("Digite sua forma de pagamento: (a) à vista, (b) 1x cartão, (c) 2x cartão e (d) 3x+ cartão: "))

# Verifica a forma de pagameto e apresenta o valor a ser pago
if(forma == "a"):
    valorF = valor-(valor*0.1)
    print(f"O valor a ser pago é de R${valorF}") 
elif(forma == "b"):
    valorF = valor-(valor*0.05)
    print(f"O valor a ser pago é de R${valorF}") 
elif(forma == "c"):
    valorF = valor
    print(f"O valor a ser pago é de R${valorF}") 
elif(forma == "d"):
    valorF = valor+(valor*0.2)
    print(f"O valor a ser pago é de R${valorF}") 
else:
    print("Erro! Selecione uma opção válida.")
    
### 3 ###

# Usuário digita seu peso e altura
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

# Cálculo IMC
imc = peso/(altura**2)

# Resultado IMC
if (imc > 40):
    print("Obesidade mórbida")
elif (imc >= 30):
    print("Obesidade")
elif (imc >= 25):
    print("Sobrepeso")
elif (imc >= 18.5):
    print("Peso ideal")
elif (imc < 18.5):
    print("Abaixo do peso")

### 4 ###
    
# Usuário digita suas notas
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

# Cálculo da média
media = (nota1 + nota2 + nota3)/3

# Resultado final
if (media < 5):
    print("Você foi reprovado!")
elif(media < 7):
    print("Você está de recuperação.")
elif(media >= 7):
    print("Você foi aprovado!")

### 1051 ###
    
valor = float(input("Digite seu sálario com dois dígitos após a vírgula: "))

if (valor <= 2000.00):
    print("Isento")
elif (valor <= 3000.00):
    vd = valor-2000.00
    print(f"R$ {round(vd*0.08, 2)}")
elif (valor <= 4500.00):
    vd = valor-3000.00
    print(f"R$ {round(vd*0.18+80, 2)}")
elif (valor > 4500.00):
    vd = valor-4500.00
    print(f"R$ {round(vd*0.28+350, 2)}")

   
    

