"""
Tienes este código:

palabra = 'banana'
contador = 0
for letra in palabra:
    if letra == 'a':
        contador = contador + 1
print(contador)

Encapsúlalo en una función llamada cuenta, y hazla genérica de tal modo que pueda aceptar una cadena y una letra como argumentos.
"""

#Entrada

def ingresar_palabra()->str:
    palabra_ingresada = input("Ingrese una palabra: ")
    while len(palabra_ingresada.split()) == 0:
        palabra_ingresada = input("Ingrese una palabra: ")
    return palabra_ingresada

def ingresar_letra() -> str:
    letra_ingresada = input("Ingrese una letra: ")
    while len(letra_ingresada) != 1:
        letra_ingresada = input("Ingrese una letra: ")
    return letra_ingresada

#Procesado

def cuenta(palabra:str,letra_a_contar:str)->int:
    contador = 0
    for letra in palabra:
        if letra == letra_a_contar:
            contador += 1
    return contador

#Salida

def mostrar_repeticiones_de_la_letra(palabra_analizada:str,letra_contada:str,veces_contada:int)->str:
    return f"La palabra {palabra_analizada} tiene la letra {letra_contada} repetida {veces_contada} veces"
    
if __name__== "__main__":
    palabra_a_ser_analizada = ingresar_palabra()
    letra_a_ser_contada = ingresar_letra()
    
    veces_contada = cuenta(palabra_a_ser_analizada,letra_a_ser_contada)
    
    repeticiones_string = mostrar_repeticiones_de_la_letra(palabra_a_ser_analizada,letra_a_ser_contada,veces_contada)
    
    print(repeticiones_string)