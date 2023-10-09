from app.texto import Texto

def test_imprimir():
    assert Texto.imprimir("Hello World!") == "Hello World!"