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


# %% KATA 03 - Palabras que contienen la palabra objetio
# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
# devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

from typing import List

def palabras_que_contienen(palabras: List[str], objetivo: str) -> List[str]:
    """
    Devuelve una lista con las palabras de 'palabras' que contienen la subcadena 'objetivo'.
    """
    return [p for p in palabras if objetivo in p]

if __name__ == "__main__":
    # pruebas  
    assert palabras_que_contienen(["python", "py", "java"], "py") == ["python", "py"]
    assert palabras_que_contienen(["hola", "adios", "ola"], "ola") == ["hola", "ola"]
    assert palabras_que_contienen([], "x") == []
    # Demostracion visible
    print(palabras_que_contienen(["hola", "adios", "ola"], "la")) # ['ola', 'hola']
    print("KATA 03 - Palabras que contienen la palabra objetio - OK")


# %% KATA 05 - Media y estado segun nota de aprobado
# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por 
# defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
# que nota_aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
# una tupla que contenga la media y el estado.

from typing import List, Tuple

def evaluar_media(notas: List[float], nota_aprobado: float = 5.0) -> Tuple[float, str]:
    """
    Calcula la media de una lista de numeros y determina si esta aprobada o suspendida.
    Devuelve una tupla con la media y el estado ('aprobado' o 'suspenso').
    """
    if not notas:
        raise ValueError("La lista de notas no puede estar vacia.")

    media = sum(notas) / len(notas)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return media, estado

if __name__ == "__main__":
    # pruebas
    assert evaluar_media([5, 6, 7]) == (6.0, "aprobado")
    assert evaluar_media([4, 5, 6], 6) == (5.0, "suspenso")
    assert evaluar_media([3, 3, 3]) == (3.0, "suspenso")
    assert evaluar_media([10], 7) == (10.0, "aprobado")

    # Demostración visible
    print(evaluar_media([5, 3, 7]))        # (5.0, 'aprobado')
    print(evaluar_media([2, 3, 4, 5]))     # (3.5, 'suspenso')
    print("KATA 05 - Media y estado segun nota de aprobado - OK")


# %% KATA 06 - Factorial recursivo
# 6. Escribe una funcion que calcule el factorial de un numero de manera recursiva.
