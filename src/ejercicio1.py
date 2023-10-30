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

def invertir_palabra(cadena:str) -> str:
    palabra_invertida = ""
    contador = 0
    #debe tener while
    while contador != len(cadena):
        palabra_invertida += cadena[-(contador+1)]+ "\n"   
        contador +=1
    return palabra_invertida

#Salida

def mostrar_resultado(cadena_invertida:str)->str:
    return f"Aquí tiene la cadena invertida: {cadena_invertida}"

if __name__ == "__main__":
    cadena_ingresada = solicitar_palabra()
    
    cadena_invertida = invertir_palabra(cadena_ingresada)
    
    mensaje_de_la_cadena_invertida = mostrar_resultado(cadena_invertida)
    
    print(mensaje_de_la_cadena_invertida)