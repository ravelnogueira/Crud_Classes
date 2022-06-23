from Enum.gender_enum import Gender

def test_valida_nome():
  usuario = Usuario("RAVEL@.","96485140",21986111355,1203199,15103414716,0,Gender.MASCULINO)

  msg = usuario.valida_nome()

  assert msg == "Insira um nome"

