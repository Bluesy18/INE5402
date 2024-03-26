### 1  ###

# Usuário digita o seu sexo
sexo = (input("Digite seu sexo: ")).upper()

# Enquanto o sexo não for M ou F, o input persiste
while ((sexo != "M") and (sexo != "F")):
    sexo = input("Digite novamente: ").upper()
    