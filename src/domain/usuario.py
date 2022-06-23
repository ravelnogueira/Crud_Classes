import string
import sys
sys.path.append('C:\\Users\\aluno01\\Desktop\\Desafio Porto\\src')
from Enum.gender_enum import Gender
from datetime import date

class Usuario():
  def __init__(self, nome: str, email: str, senha: str, celular1: str, data_nasci: date,cpf: str, celular2:str, genero: Gender = Gender.NAO_DEFINIDO):
    self.nome = nome 
    self.email = email
    self.senha = senha 
    self.celula1 = celular1
    self.celula2 = celular2
    self.data_nascimento = data_nasci
    self.cpf = cpf 
    self.genero = genero 

  def valida(self):
    self.valida_nome()
    self.valida_email()
    self.valida_senha()
    self.valida_celular()
    self.valida_cpf()
    self.valida_data()
    self.valida_genero()


  def valida_nome(self):
    if (len(self.nome) == 0 ):
      raise Exception("Insira um nome")
    
    elif (len(self.nome) >100):
      raise Exception("Nome muito longo")

    elif ("  " in self.nome):
      raise Exception("Espaços em demasia")

  def valida_email(self):
    if ("@" and "." not in self.email):
      raise ValueError("Insira um email valido")

  def valida_senha(self):
    if (len(str(self.senha)) < 8):
      raise Exception("Senha muito curta, digito uma senha com no minimo 8 digitos")
    
    elif(str(self.senha).isalpha() or str(self.senha).isdigit()):
      raise Exception("A sua senha deve conter letras e números")

  def valida_celular(self):
    if (len(str(self.celula1)) != 11):
      raise Exception("Numero incompleto")
    
    if(len(str(self.celula2)) > 0):
      if (len(str(self.celula2)) != 11):
        raise Exception("Segundo Numero incompleto")
  
  def valida_cpf(self):
    if(len(str(self.cpf)) != 11):
      raise Exception("Número de digitos invalido")
  
  def valida_data(self):
    maioridade = date.today().year - self.data_nascimento.year 
    date.today() < self.data_nascimento

    if(date.today() < self.data_nascimento):
      raise Exception("Você é do futuro?")

    if( maioridade < 18 ):
      raise Exception("Precisa ser de maior para realizar cadastro")
  
  def valida_genero(self):
    if (self.genero != Gender.FEMININO or self.genero != Gender.MASCULINO or self.genero != Gender.NAO_DEFINIDO):
      raise Exception("Genero invalido")
