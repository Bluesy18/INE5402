from classe_funcionario import Funcionario

def verifica0(consulta):
  while((consulta != 1) and (consulta != 2)):
    consulta = int(input("Opção de consulta inválida! Digite 1 para consultar por nome ou digite 2 para consultar por matrícula: "))

  return consulta

res = "S"
op = 0
lista_func = []

while (res == "S"):
  op = int(input("Digite qual operação deseja realizar: 1 - Cadastro, 2 - Consulta, 3 - Solictar adiantamento, 4 - Calcular pagamento: "))

  if(op == 1):
    nome = input("Digite o nome do funcionário: ")
    matricula = int(input("Digite a matrícula do funcionário: "))
    salario = float(input("Digite o salário do funcionário: "))

    funcionario = Funcionario(nome, matricula, salario)
    lista_func.append(funcionario)

  elif(op == 2):
    if(len(lista_func) != 0):
      consulta = int(input("Digite 1 para consultar por nome ou digite 2 para consultar por matrícula: "))
      consulta = verifica0(consulta)

      if(consulta == 1):
        consulta_nome = input("Digite o nome que deseja procurar: ")
        for func1 in lista_func:
          if(func1.get_nome() == consulta_nome):
            print(f"Nome: {func1.get_nome()}")
            print(f"Matricula: {func1.get_matricula()}")
            print(f"Salário: R$ {func1.get_salario()}")

          else:
            print("Funcionário não encontrado.")
      else:
        consulta_matricula = int(input("Digite a matrícula que deseja procurar: "))
        for func2 in lista_func:
          if(func2.get_matricula() == consulta_matricula):
            print(f"Nome: {func2.get_nome()}")
            print(f"Matricula: {func2.get_matricula()}")
            print(f"Salário: R$ {func2.get_salario()}")
          else:
            print("Funcionário não encontrado.")
    else:
      print("Não há funcionários.")

  elif(op == 3):
    if(len(lista_func) != 0):
      adiantamento_nome = input("Digite o nome do funcionário que vai solicitar o adiantamento: ")
      for func3 in lista_func:
        if(func3.get_nome() == adiantamento_nome):
          adiantamento = float(input("Digite o quanto deseja adiantar: "))
          func3.pedir_adiantamento(adiantamento)

        else:
            print("Funcionário não encontrado.")
          

    else:
      print("Não há funcionários.")

  elif(op == 4):
    if(len(lista_func) != 0):
      pagamento_nome = input("Digite o nome do funcionário que vai checar o pagamento: ")
      for func4 in lista_func:
        if(func4.get_nome() == pagamento_nome):
          print(f"Pagamento: R$ {func4.get_pagamento()}")

    else:
            print("Funcionário não encontrado.")


  else:
    print("Operação inválida.")

  res = input("Deseja continuar? (S/N): ").upper()


