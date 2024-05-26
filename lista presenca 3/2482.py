### 2482 ###

n = int(input("Digite a quantidade de traduções: "))

etiquetas = []
saudacoes = {}
etiqueta = {}

for i in range(n):
  idioma = input("Digite o idioma: ")
  saudacoes[idioma] = input("Digite a saudação no respectivo idioma: ")

m = int(input("Digite quantas crianças receberão as etiquetas: "))

for j in range(m):
  etiqueta["nome"] = input("Digite o nome da criança: ")
  idioma = input("Digite o idioma nativo da respectiva criança: ")
  etiqueta["saudacao"] = saudacoes.get(idioma)
  etiquetas.append(etiqueta)

for l in etiquetas:
    print(l.get("nome"))
    print(l.get("saudacao"))


