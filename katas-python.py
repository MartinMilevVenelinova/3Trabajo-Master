# %% KATA 01 - Frecuencias de letras
# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
# de cada letra en la cadena. Los espacios no deben ser considerados.

from typing import Dict                                 # pistas de tipos para mayor clarisad y evitar errores

def frecuencia_letras(cadena: str, *, ignorar_mayusculas: bool = False) -> Dict[str, int]:
    
    """
    Devuelve un diccionario con cuantas veces aparece cada caracter NO espacio.
    E ignorar_mayusculas = True, convierte todo a minsuculas antes de contar.
    """


    if ignorar_mayusculas:
        cadena = cadena.lower()
    
    contador: Dict[str, int] = {}
    for letra in cadena:                                # recorro la cadena caracter a caracter     
        if letra != " ":                                # ignoro los espacios
            # si la clave existe, sumo 1; si no existe, empiezo en 0 y luego sumo 1
            contador[letra] = contador.get(letra, 0) + 1
    return contador

if __name__ == "__main__":  
    # pruebas  
    assert frecuencia_letras("Buenas Mundo") == {'B': 1, 'u': 2, 'e': 1, 'n': 2, 'a': 1, 's': 1, 'M': 1, 'o': 1, 'd': 1}
    assert frecuencia_letras("") == {}
    assert frecuencia_letras("   ") == {}
    # prueba de mayúsculas/minúsculas unificadas
    assert frecuencia_letras("Aa", ignorar_mayusculas=True) == {'a': 2}

    # Demostracion visible
    print(frecuencia_letras("Buenas Mundo")) # {'B': 1, 'u': 2, 'e': 1, 'n': 2, 'a': 1, 's': 1, 'M': 1, 'o': 1, 'd': 1}
    print("KATA 01 - Frecuencias de letras - OK")


# %% KATA 02 - Duplicar valores con map()
# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

from typing import List, Iterable, Union
Number = Union[int, float]  # Definición de tipo para números (enteros y flotantes)

def duplicar_lista(numeros: Iterable[Number]) -> List[Number]:
    """
    Devuelve una lista nueva con cada numero multiplicado por 2.
    Uso de map() como se pide.
    """
    # map va a aplicar la funcion de lambda x: x*2 a cada elemento y devuelve un iterable
    # por eso lo convierto a list() para obetener una lista final

    return list(map(lambda x: x * 2, numeros))

if __name__ == "__main__": 
    # pruebas  
    assert duplicar_lista([1, 2, 3]) == [2, 4, 6]
    assert duplicar_lista([1.5, 2.0]) == [3.0, 4.0]
    assert duplicar_lista([]) == []
    # Demostracion visible
    print(duplicar_lista([19, -5, 0.7])) # [38, -10, 1.4]
    print("KATA 02 - Duplicar valores con map() - OK")
# %%
