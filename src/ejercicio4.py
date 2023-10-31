"""
Hay un método de cadenas llamado count que es similar a find. 
y escribe el código necesario para invocar a este método 
y contar el número de veces que una letra aparece en “banana”.
"""

#Entrada
def ingresar_letra() -> str:
    letra_ingresada = input("Ingrese una letra: ")
    while len(letra_ingresada) != 1:
        letra_ingresada = input("Ingrese una letra: ")
    return letra_ingresada

#procesado
def cuantas_letras_tiene_banana(letra_a_contar:str)->int:
    veces_que_se_repite = "banana".count(letra_a_contar.lower())
    return veces_que_se_repite

#Salida

def mostrar_resultados_de_conteo(letra_a_contar,veces_contada:int)->str:
    return f"En la palabra banana se repitió la letra {letra_a_contar} {veces_contada} veces"

if __name__ == "__main__":
    letra_ingresada = ingresar_letra()
    cuantas_veces_sale_en_banana = cuantas_letras_tiene_banana(letra_ingresada)
    
    mostrar_descubrimiento = mostrar_resultados_de_conteo(letra_ingresada,cuantas_veces_sale_en_banana)
    
    print(mostrar_descubrimiento)