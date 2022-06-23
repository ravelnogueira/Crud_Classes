import string
import sys
sys.path.append('C:\\Users\\aluno01\\Desktop\\Desafio Porto\\src')
from Enum.gender_enum import Gender

from datetime import date

asc3 = string.ascii_letters

class Usuario():
  def __init__(self, nome: str, email: str, senha: str, celular1: int, data_nasci: date,cpf: int, celular2:int, genero: Gender = Gender.NAO_DEFINIDO):
    self.nome = nome 
    self.email = email
    self.senha = senha 
    self.celula1 = celular1
    self.celula2 = celular2
    self.data_nascimento = data_nasci
    self.cpf = cpf 
    self.genero = genero 

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

  def valida_celular(self):
    if (len(self.celula1) != 11):
      raise Exception("Numero incompleto")
    
    if(len(self.celula2) != 0):
      if (len(str(self.celula2)) != 11):
        raise Exception("Numero incompleto")
  
  def valida_cpf(self):
    if(len(str(self.cpf)) != 11):
      raise Exception("Número de digitos invalido")
    
    elif(isinstance(self.cpf, str)):
      raise Exception("Digite apenas números")
  
  def valida_data(self):
    maioridade = date.today().year - self.data_nascimento.year 
    if( maioridade < 18 ):
      raise Exception("Precisa ser de maior para realizar cadastro")


ravel = Usuario("r4vel","rt",98482020,219861135, date(2007,3,12),15103414716,21986111355)
print(ravel.valida_data())