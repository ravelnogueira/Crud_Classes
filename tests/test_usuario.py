from logging import exception
from re import A
import pytest
from datetime import date
from src.Enum.gender_enum import Gender

from src.domain.usuario import Usuario

def test_valida_nome():
  with pytest.raises(Exception) as exception:
    ravel =  Usuario("  ","rt","raveld12",219861135, date(1999,3,12),15103414716,21986111355)
    
    ravel.valida() 
  assert str(exception.value) == "Espaços em demasia"

def test_valida_nome_vazio():
  with pytest.raises(Exception) as exception:
    ravel =  Usuario("","rt","raveld12",219861135, date(1999,3,12),15103414716,21986111355)
    
    ravel.valida() 
  assert str(exception.value) == "Insira um nome"

def test_valida_email():
  with pytest.raises(Exception) as exception:
    ravel =  Usuario("ravel ","ravel","",219861135, date(1999,3,12),15103414716,21986111355)
    
    ravel.valida() 
  assert str(exception.value) == "Insira um email valido"

def test_valida_senha_curta():
  with pytest.raises(Exception) as exception:
    ravel =  Usuario("ravel ","ravel.santos@hotmail.com.br","ravel",219861135, date(1999,3,12),15103414716,21986111355)
    
    ravel.valida() 
  assert str(exception.value) == "Senha muito curta, digito uma senha com no minimo 8 digitos"

def test_valida_senha_sem_string():
  with pytest.raises(Exception) as exception:
    ravel =  Usuario("ravel ","ravel.santos@hotmail.com.br","12345678",219861135, date(1999,3,12),15103414716,21986111355)
    
    ravel.valida() 
  assert str(exception.value) == "A sua senha deve conter letras e números"

def test_valida_senha_sem_digitos():
  with pytest.raises(Exception) as exception:
    ravel =  Usuario("ravel ","ravel.santos@hotmail.com.br","ravelsantos",219861135, date(1999,3,12),15103414716,21986111355)
    
    ravel.valida() 
  assert str(exception.value) == "A sua senha deve conter letras e números"

def test_valida_senha_sem_digitos():
  with pytest.raises(Exception) as exception:
    ravel =  Usuario("ravel ","ravel.santos@hotmail.com.br","ravelsantos",219861135, date(1999,3,12),15103414716,21986111355)
    
    ravel.valida() 
  assert str(exception.value) == "A sua senha deve conter letras e números"

def test_valida_celular_numero1_incompleto():
  with pytest.raises(Exception) as exception:
    ravel =  Usuario("ravel ","ravel.santos@hotmail.com.br","ravelsantos123",2198611, date(1999,3,12),15103414716,21986111355)
    
    ravel.valida() 
  assert str(exception.value) == "Numero incompleto"

def test_valida_celular_numero2_incompleto():
  with pytest.raises(Exception) as exception:
    ravel =  Usuario("ravel ","ravel.santos@hotmail.com.br","ravelsantos123",21986111355, date(1999,3,12),"15103414716",219811355)
    
    ravel.valida() 
  assert str(exception.value) == "Segundo Numero incompleto"

def test_valida_cpf_numeros_incorreta():
  with pytest.raises(Exception) as exception:
    ravel =  Usuario("ravel ","ravel.santos@hotmail.com.br","ravelsantos123",21986111355, date(1999,3,12),"1503414716",21986111355)
    
    ravel.valida() 
  assert str(exception.value) == "Número de digitos invalido"

def test_valida_data_maior_que_atual():
  with pytest.raises(Exception) as exception:
    ravel =  Usuario("ravel ","ravel.santos@hotmail.com.br","ravelsantos123",21986111355, date(2023,3,12),15103414716,21986111355)
    
    ravel.valida() 
  assert str(exception.value) == "Você é do futuro?"

def test_valida_data_menor_de_idade():
  with pytest.raises(Exception) as exception:
    ravel =  Usuario("ravel ","ravel.santos@hotmail.com.br","ravelsantos123",21986111355, date(2007,3,12),15103414716,21986111355)
    
    ravel.valida() 
  assert str(exception.value) == "Precisa ser de maior para realizar cadastro"

def test_valida_genero():
  with pytest.raises(Exception) as exception:
    ravel =  Usuario("ravel ","ravel.santos@hotmail.com.br","ravelsantos123","21986111355", date(1999,3,12),"15103414716","21986111355","26")
    
    ravel.valida() 
  assert str(exception.value) == "Genero invalido"