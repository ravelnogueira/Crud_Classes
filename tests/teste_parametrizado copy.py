import pytest
from datetime import date
from domain.usuario import *

class Test_Valida_nome:

  @pytest.mark.parametrize(
    'parametro_test, msg',
    [
      ('  ', "Espaços em demasia"),
      

    ]
  ) 
  def test_nome_grande(self,parametro_test, msg):
    with pytest.raises(Exception) as exception:
      usuario = Usuario(parametro_test,"rt","raveld12",219861135, date(1999,3,12),15103414716,21986111355)
      usuario.valida_nome()
    
    assert str(exception.value) == msg
  
  def test_(self,parametro_test, msg):
    with pytest.raises(Exception) as exception:
      usuario = Usuario(parametro_test,"rt","raveld12",219861135, date(1999,3,12),15103414716,21986111355)
      usuario.valida_nome()
    
    assert str(exception.value) == msg