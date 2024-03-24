############# Fiz da 1 até a 4 e a 1051 em sala com o André #############

### 2600 ###

# Não compreendi o que a questão pede para fazer

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

### 1035 ###

# Usuário digita os valores
a, b, c, d = input("Digite os valores de A, B, C e D (separados por espaço): ").split()

# Conversão para inteiro
a1 = int(a)
b1 = int(b)
c1 = int(c)
d1 = int(d)

# Verifica a condição imposta pelo problema e mostra se ela foi satisfeita ou não
if(b1 > c1 and d1 > a1 and (c1+d1) > (a1+b1) and c1 > 0 and d1 > 0 and (a1 % 2 == 0)):
  print("Valores aceitos")

else:
  print("Valores nao aceitos")

### 1036 ###

# Usuário digita os valores
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Calcula discriminante
delta = (b**2) - 4 * a * c

# Calcula (ou não) raízes
if (delta < 0 or a == 0):
  print ("Impossível calcular")
else:
  r1 = (-b + (delta**0.5))/(2*a)
  r2 = (-b - (delta**0.5))/(2*a)

  r1r = round(r1, 5)
  r2r = round(r2, 5)

# Apresenta raízes ao usuário
  print(f"R1 = {r1r}\nR2 = {r2r}")

### 1038 ###

# Usuário digita código e quantidade do item
cdg, qtd = input("Digite o código e a quantidade do item desejado (separado por espaços): ").split()

# Conversão para inteiro
cdg1 = int(cdg)
qtd1 = int(qtd)

# Verifica o código e a quantidade desejada
if(cdg1 < 1 or cdg1 > 5):
  print("Código inválido")

else:
  if(cdg1 == 1):
    vlr = round(qtd1*4, 2)

  elif(cdg1 == 2):
    vlr = round(qtd1*4.50, 2)

  elif(cdg1 == 3):
    vlr = round(qtd1*5, 2)

  elif(cdg1 == 4):
    vlr = round(qtd1*2, 2)

  elif(cdg1 == 5):
    vlr = round(qtd1*1.50, 2)

# Mostra o total a ser pago
  print(f"Total: R$ {vlr}")

### 1045 ###

# Usuário digita os valores dos lados do triângulo
c, b, a = input("Digite os valores de C, B e A (separados por esaço) respectivamente, sendo A o maior lado: ").split()

# Conversão para racional
a1 = float(a)
b1 = float(b)
c1 = float(c)

# Verifica se é um triângulo
if(a1 >= (b1+c1)):
  print("NAO FORMA TRIANGULO")

# Classifica o triângulo
else:
  if((a1**2) == ((b1**2)+(c1**2))):
    print("TRIANGULO RETANGULO")

  elif((a1**2) > ((b1**2)+(c1**2))):
    print("TRIANGULO OBTUSANGULO")

  elif((a1**2) < ((b1**2)+(c1**2))):
    print("TRIANGULO ACUTANGULO")

  if(a1 == b1 == c1 == a1):
    print("TRIANGULO EQUILATERO")

  elif((a1 == b1) ^ (b1 == c1) ^ (c1 == a1)):
    print("TRIANGULO ISOSCELES")

### 1046 ###

# Usuário digita as horas
i, f = input("Digite a hora de início e a hora de fim (separadas por um espaço): ").split()

# Conversão para inteiro
i1 = int(i)
f1 = int(f)

# Verifica se os horários atendem às especificações da questão
if (i1 < 1 or i1 > 24):
  print("Horário inválido.")

elif (f1 < 1 or f1 > 24):
  print("Horário inválido.")

# Calcula duração
else:
  if (f1 > i1):
    d = f1 - i1

  elif (f1 < i1):
    d = (24 - i1) + f1

  else:
    d = 24

print(f"O JOGO DUROU {d} HORA (S)")

### 1047 ###

# Usuário digita horário inicial e horário final

hi, mi, hf, mf = input("Digite a hora de início, minuto de início, hora de fim e minuto de fim (separados por espaço): ").split()

# Conversão para inteiro
hi1 = int(hi)
mi1 = int(mi)
hf1 = int(hf)
mf1 = int(mf)

# Verifica se os horários atendem às especificações da questão
if (hi1 > 24 or hi1 < 0):
  print("Horário inválido.")

elif (mi1 > 60 or mi1 < 0):
  print("Horário inválido.")

elif (hf1 > 24 or hf1 < 0):
  print("Horário inválido.")

elif (mf1 > 60 or mf1 < 0):
  print("Horário inválido.")

# Calcula duração
else:
  if(hf1 > hi1):
    ti = (hi1*60) + mi1
    tf = (hf1*60) + mf1

    dcalc = tf - ti
    dh = dcalc // 60
    dm = dcalc % 60

  elif(hf1 < hi1):
    ti = (hi1*60) + mi1
    tf = (hf1*60) + mf1

    dcalc = (1440 - ti) + tf
    dh = dcalc // 60
    dm = dcalc % 60

  elif(hf1 == hi1 and mf1 > mi1):
    dh = 0
    dm = mf1 - mi1

  elif(hf1 == hi1 and mf1 < mi1):
    dh = 23
    dm = 60-(mi1 - mf1)

  elif(hf1 == hi1 and mf1 == mi1):
    dh = 24
    dm = 0

  else:
    print("Valores inválidos.")

# Mostra a duração
print(f"O JOGO DUROU {dh} HORA(S) E {dm} MINUTO(S)")  

### 1048 ###

# Usuário digita seu salário
sal = round(float(input("Digite seu salário: ")), 2)

# Verifica o valor do salário e aplica o reajuste
if(0 <= sal <= 400.00):
  rea = round((sal*0.15), 2)
  nsal = round((sal + rea), 2)
  perc = 15

elif(400.01 <= sal <= 800.00):
  rea = round((sal*0.12), 2)
  nsal = round((sal + rea), 2)
  perc = 12

elif(800.01 <= sal <= 1200.00):
  rea = round((sal*0.10), 2)
  nsal = round((sal + rea), 2)
  perc = 10

elif(1200.01 <= sal <= 2000.00):
  rea = round((sal*0.07), 2)
  nsal = round((sal + rea), 2)
  perc = 7

elif(sal > 2000.00):
  rea = round((sal*0.4), 2)
  nsal = round((sal + rea), 2)
  perc = 4

# Mostra os novos valores
print(f"Novo salário: {nsal}\nReajuste ganho: {rea}\nEm percentual: {perc}%")

### 1050 ###

# Usuário digita o DDD
ddd = int(input("Digite seu DDD: "))

# Interpretação do DDD digitado
if (ddd == 61):
  print("Brasília")
  
elif (ddd == 71):
  print("Salvador")

elif (ddd == 11):
  print("São Paulo")

elif (ddd == 21):
  print("Rio de Janeiro")

elif (ddd == 32):
  print("Juiz de Fora")

elif (ddd == 19):
  print("Campinas")

elif (ddd == 27):
  print("Vitória")

elif (ddd == 31):
  print("Belo Horizonte")

else:
  print("DDD não cadastrado")

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

### 1052 ###

# Usuário digita número
mes = int(input("Digite um número de 1 a 12: "))

# Interpreta o número digitado para um mês do ano
if (mes == 1):
  print("January")

elif (mes == 2):
  print("Februrary")

elif (mes == 3):
  print("March")

elif (mes == 4):
  print("April")

elif (mes == 5):
  print("May")

elif (mes == 6):
  print("June")

elif (mes == 7):
  print("July")

elif (mes == 8):
  print("August")

elif (mes == 9):
  print("Setember")

elif (mes == 10):
  print("October")

elif (mes == 11):
  print("November")

elif (mes == 12):
  print("December")

else:
  print("Número inválido.")

### 1061 ###

# Usuário digita data e horário
diaI1 = int(input("Digite o dia de íncio do evento: "))
horaI1, minI1, segI1 = input("Digite o horário de íncio do evento: ").split(" : ")
diaF1 = int(input("Digite o dia de fim do evento: "))
horaF1, minF1, segF1 = input("Digite o horário de fim do evento: ").split(" : ")

# Conversão para inteiro
diaI2 = int(diaI1)
horaI2 = int(horaI1)
minI2 = int(minI1)
segI2 = int(segI1)
diaF2 = int(diaF1)
horaF2 = int(horaF1)
minF2 = int(minF1)
segF2 = int(segF1)

if(diaI2 > 31 or horaI2 > 24 or minI2 >= 60 or segI2 >= 60 or diaF2 > 31 or horaF2 > 24 or minF2 >= 60 or segF2 >= 60):
  print("Digite valores válidos!")
else:

# Transformar valores em segundos para calcular
  segCalcI = (diaI2*86400)+(horaI2*3600)+(minI2*60)+segI2
  segCalcF = (diaF2*86400)+(horaF2*3600)+(minF2*60)+segF2
  segCalcR = segCalcF - segCalcI

# Conversão para dias, horas, minutos e segundos
  diaR = segCalcR // 86400
  horasR = (segCalcR % 86400) // 3600
  minR = ((segCalcR % 86400) % 3600) // 60
  segR = ((segCalcR % 86400) % 3660) % 60

# Resultado
  print(f"{diaR} dia (s)\n{horasR} hora (s)\n{minR} minuto (s)\n{segR} segundo (s)")

### 2339 ###

# Usuário digita a quantidade de competidores, folhas de papel compradas e folhas de papel para cada competidor
c, p, f = map(int, input("Digite a quantidade de competidores, de folhas compradas e a quantidade de folhas por competidor (separado por espaço): ").split())

# Conversão para inteiro
c1 = int(c)
p1 = int(p)
f1 = int(f)

if(c1 < 1 or c1 > 1000):
  print("Quantidade inválida")

elif(p1 < 1 or p1 > 1000):
  print("Quantidade inválida")

elif(f1 < 1 or f1 > 1000):
  print("Quantidade inválida")

else:
  if((p1/c1) >= f1):
    print("S")

  else:
    print("N")

### 2375 ###

# Usuário digita o diâmetro da bola de boliche e depois as dimensões da caixa
n = int(input("Digite o diâmetro da bola: "))
a, l, p = map(int, input("Digite as dimensões da caixa (separadas por espaço): ").split())

if((n < 1 or n > 10000) or (a < 1 or a > 10000) or (l < 1 or l > 10000) or (p < 1 or p > 10000)):
  print("Dimensões inválidas.")

elif(n <= min(a, l, p)):
  print("S")

else:
  print("N")

### 2408 ###

# Usuário digita pontuação dos jogadores
a, b, c = input("Digite a pontuação dos jogadores (separadas por espaço): ").split()

# Converte para inteiro
a1 = int(a)
b1 = int(b)
c1 = int(c)

# Verifica se as pontuações atendem às especificações da questão
if(a1 < 1 or a1 > 100):
  print("Pontuação inválida.")

elif(b1 < 1 or b1 > 100):
  print("Pontuação inválida.")

elif(b1 < 1 or b1 > 100):
  print("Pontuação inválida.")

# Determina e apresenta o vice-campeão
else:
  if((a1 < b1 and a1 > c1) or (a1 > b1 and a1 < c1)):
    print(a1)

  elif((b1 < a1 and b1 > c1) or (b1 > a1 and a1 < c1)):
    print(b1)

  elif((c1 < a1 and c1 > b1) or (c1 > a1 and c1 < b1)):
    print(c1)

### 2409 ###

# Usuário digita as dimensões do colchão e da porta
a, b, c = map(int, input("Digite as dimensões do colchão (separadas por espaço): ").split())
h, l = map(int, input("Digite as dimensões da porta (separadas por espaço): ").split())

# Verifica se as dimensões são válidas
if((a < 1 or a > 300) or (b < 1 or b > 300) or (c < 1 or c > 300) or (h < 1 or h > 250) or (l < 1 or l > 250)):
  print("Dimensões inválidas.")

# Verifica se o colchão passa pela porta
elif(a <= h and b <= l) or (a <= l and b <= h):
  print("S")

elif(a <= h and c <= l) or (a <= l and c <= h):
  print("S")

elif(b <= h and c <= l) or (b <= l and c <= h):
  print("S")

else:
  print("N")

### 2417 ###

# Usuário digita os dados dos times
cv, ce, cs, fv, fe, fs = input("Digite o número de vitórias, empates e saldo de gols do Cormengo e número de vitórias, empates e saldo de gols do Flaminthians (separados por espaço): ").split()

# Conversão para inteiro
cv1 = int(cv)
ce1 = int(ce)
cs1 = int(cs)
fv1 = int(fv)
fe1 = int(fe)
fs1 = int(fs)

# Verifica se as pontuações atendem às especificações da questão
if(cv1 < 1 or cv1 > 100):
  print("Pontuação inválida.")

elif(ce1 < 1 or ce1 > 100):
  print("Pontuação inválida.")

elif(cs1 < -1000 or cs1 > 1000):
  print("Pontuação inválida.")

elif(fv1 < 1 or fv1 > 100):
  print("Pontuação inválida.")

elif(fe1 < 1 or fe1 > 100):
  print("Pontuação inválida.")

elif(fs1 < -1000 or fs1 > 1000):
  print("Pontuação inválida.")

# Converte pra pontuação
else:
  cp = (cv1*3) + ce1
  fp = (fv1*3) + fe1

# Checa possibilidades e mostra resultado do campeonato
  if(cp > fp):
    print("C")

  elif(fp > cp):
    print("F")

  elif(cs1 > fs1):
    print("C")

  elif(fs1 > cs1):
    print("F")

  else:
    print("=")

### 2568 ###

# Usuário digita seus valores
d, i, x, f = input("Digite o dia que a ação foi registrada, o preço inicial da ação, a variação diária do reço e a quantidade de dias futuros (separados por espaço): ").split()

# Conversão para inteiro
d1 = int(d)
i1 = int(i)
x1 = int(x)
f1 = int(f)

# Verifica se as pontuações atendem às especificações da questão
if (d1 < 1 or d1 > 365):
  print("Valor inválido.")

elif (i1 < x1 or i1 > 1000):
  print("Valor inválido.")

elif (x1 < 1 or x1 > i1):
  print("Valor inválido.")

elif (f1 < 1 or f1 > 365):
  print("Valor inválido.")

# Verifica e mostra se houve um acréscimo, establidade ou decréscimo do valor
else:
  if(d1 % 2 == 0 and f1 % 2 == 0):
    p = i1
    
  elif(d1 % 2 == 0 and f1 % 2 != 0):
    p = i1 - x1
    
  elif(d1 % 2 != 0 and f1 % 2 == 0):
    p = i1
   
  elif(d1 % 2 != 0 and f1 % 2 != 0):
    p = i1 + x1

print(p) 



   
    

