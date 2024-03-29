### 5 ###

# Usuário digita o valor
valor = round(float(input("Digite um valor: ")), 2)

# Calcula quantidade mínima de notas
n100 = valor/100
r100 = valor % 100
n50 = r100/50
r50 = r100 % 50
n20 = r50/20
r20 = r50 % 20
n10 = r20/10
r10 = r20 % 10
n5 = r10/5
r5 = r10 % 5
n2 = r5/2
r2 = r5 % 2

# Calcula quantidade mínima de moedas
valorC = int(valor*100)
rm100 = valorC % 100
m50 = rm100/50
rm50 = rm100 % 50
m25 = rm50/25
rm25 = rm50 % 25
m10 = rm25/10
rm10 = rm25 % 10
m5 = rm10/5
rm5 = rm10 % 5

# Mostra quantidade mínima de notas e moedas
print(f"NOTAS:\n{int(n100)} nota(s) de R$ 100.00\n{int(n50)} nota(s) de R$ 50.00\n{int(n20)} nota(s) de R$ 20.00\n{int(n10)} nota(s) de R$ 10.00\n{int(n5)} nota(s) de R$ 5.00\n{int(n2)} nota(s) de R$ 2.00\nMOEDAS:\n{int(r2)} moeda(s) de R$ 1.00\n{int(m50)} moeda(s) de R$ 0.50\n{int(m25)} moeda(s) de R$ 0.25\n{int(m10)} moeda(s) de R$ 0.10\n{int(m5)} moeda(s) de R$ 0.05\n{int(rm5)} moeda(s) de R$ 0.01")