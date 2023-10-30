from src.ejercicio1 import invertir_palabra,mostrar_resultado

def test_invertir_palabra():
    assert invertir_palabra("hola") == "a\nl\no\nh\n"

def test_invertir_cadena():
    assert invertir_palabra(" ")== " \n"
    
def test_mostrar_cadena_invertida():
    assert mostrar_resultado("a\nl\no\nh\n") == "Aquí tiene la cadena invertida: \n a\nl\no\nh\n"