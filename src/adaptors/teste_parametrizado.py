import pytest
from datetime import date
from ..domain.usuario import Usuario
class Test_Valida_nome():

  @pytest.mark.parametrize(
    (
      'parametro_test', 'msg'
    ),
    pytest.param('  ', "Espaços em demasia", id= 'Nome_grande'),
  ) 

  def test_nome_grande(parametro_test, msg):
    with pytest.raises(Exception) as Excepetion:
      usuario = Usuario(parametro_test,"rt","raveld12",219861135, date(1999,3,12),15103414716,21986111355)
      usuario.Valida_nome()
    
    assert str(Excepetion.value) == msg