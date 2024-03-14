### 1020 ###

# Usuário digita sua idade em dias
diasT = int(input("Digite sua idade em dias: "))

# Cálculo da idade em ano(s), mes(es) e dia(s)
ano = int(diasT // 365)
mes = int(diasT % 365) // 30
dias = int(diasT % 365) % 30

# Idade em ano(s), mes(es) e dia(s)
print(f"{ano} ano(s)\n{mes} mes(es)\n{dias} dia(s)")
