"""
Escribe un bucle while que comience con el último carácter en la cadena 
y haga un recorrido hacia atrás hasta el primer carácter en la cadena, imprimiendo cada letra en una línea independiente.
"""

#Entrada
def solicitar_palabra()-> str:
    palabra_ingresada = input("Ingrese una palabra: ")
    while palabra_ingresada == "":
            palabra_ingresada = input("Ingrese una palabra: ")
    return palabra_ingresada
#Procesado
#Salida

if __name__ == "__main__":
    print()