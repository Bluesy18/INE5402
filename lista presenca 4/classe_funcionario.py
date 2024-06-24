class Funcionario:
  def __init__(self, nome, matricula, salario):
    self.__nome = nome
    self.__matricula = matricula
    self.__salario = salario
    pagamento = salario
    self.__pagamento = pagamento

  def set_nome(self, nome):
    self.__nome = nome

  def set_matricula(self, matricula):
    self.__matricula = matricula

  def set_salario(self, salario):
    self.__salario = salario

  def get_nome(self):
    return self.__nome

  def get_matricula(self):
    return self.__matricula

  def get_salario(self):
    return self.__salario
  
  def get_pagamento(self):
    return self.__pagamento
  
  def pedir_adiantamento(self, adiantamento):
    self.__pagamento -= self.__salario*0.05
    self.__pagamento -= adiantamento

  