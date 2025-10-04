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


# %% KATA 04 - Diferencia entre dos listas con map
# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

from typing import List

def diferencias_listas(lista1: List[int], lista2: List[int]) -> List[int]:
    """
    Calcula la diferencia elemento a elemento entre dos listas del mismo tamaño.
    """
    if len(lista1) != len(lista2):
        raise ValueError("Las listas deben tener el mismo tamaño")
    
    return list(map(lambda x, y: x - y, lista1, lista2))

if __name__ == "__main__":
    #pruebas validas
    assert diferencias_listas([1, 2, 3], [1, 1, 1]) == [0, 1, 2]
    assert diferencias_listas([10, 20], [5, 5]) == [5, 15]
    assert diferencias_listas([0, 0], [0, 0]) == [0, 0]

    #prueba de error: listas con distinto tamaño
    try:
        diferencias_listas([1, 2], [1])
    except ValueError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    # demostracion visible
    print(diferencias_listas([5, 7, 9], [2, 4, 1]))  # [3, 3, 8]
    print("KATA 04 - Diferencia entre dos listas con map - OK")


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

def factorial(n: int) -> int:
    """
    Calcula el factorial de un numero n de forma recursiva.
    """
    if n < 0:
        raise ValueError("El numero no puede ser negativo")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    #pruebas validas
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(3) == 6
    assert factorial(5) == 120
    assert factorial(7) == 5040

    #prueba de error: numero negativo
    try:
        factorial(-3)
    except ValueError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    # demostracion visible
    print(factorial(4))    # 24
    print(factorial(6))    # 720
    print("KATA 06 - Factorial recursivo - OK")


# %% KATA 07 - Convertir tuplas en strings con map
# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

from typing import List, Tuple

def tuplas_a_strings(tuplas: List[Tuple]) -> List[str]:
    """
    Convierte una lista de tuplas en una lista de strings.
    Cada tupla se convierte en un string uniendo sus elementos con espacios.
    """
    if not all(isinstance(t, tuple) for t in tuplas):
        raise TypeError("Todos los elementos deben ser tuplas")
    
    return list(map(lambda t: " ".join(map(str, t)), tuplas))

if __name__ == "__main__":
    #pruebas validas
    assert tuplas_a_strings([("hola", "mundo"), ("python", "rocks")]) == ["hola mundo", "python rocks"]
    assert tuplas_a_strings([(1, 2), (3, 4)]) == ["1 2", "3 4"]
    assert tuplas_a_strings([]) == []

    #prueba de error: un elemento no es tupla
    print("Probando tuplas_a_strings con elemento no-tupla...")
    try:
        tuplas_a_strings([("bien", "ahi"), "no es tupla"])
    except TypeError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    # demostracion visible
    print(tuplas_a_strings([("vamos", "bien"), ("KATA", 7)]))  #['vamos bien', 'KATA 7']
    print("KATA 07 - Convertir tuplas en strings con map - OK")


# %% KATA 08 - Division con manejo de errores
# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
# o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no.

def dividir_usuario():
    """
    Pide al usuario dos numeros y los divide, manejando errores de entrada o division por cero.
    """
    try:
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
        resultado = a / b
    except ValueError:
        print("Error: uno de los valores no es numerico.")
    except ZeroDivisionError:
        print("Error: no se puede dividir por cero.")
    else:
        print("Division exitosa. Resultado:", resultado)
    finally:
        print("Fin del programa.")

if __name__ == "__main__":
    dividir_usuario()


# %% KATA 09 - Filtrar mascotas prohibidas
# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
# "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

from typing import List

PROHIBIDAS = ["Mapache", "Tigre", "Serpiente Piton", "Cocodrilo", "Oso"]

def filtrar_mascotas(mascotas: List[str]) -> List[str]:
    """
    Devuelve una nueva lista con las mascotas permitidas, excluyendo las prohibidas.
    """
    if not all(isinstance(nombre, str) for nombre in mascotas):
        raise TypeError("Todos los elementos deben ser strings")

    return list(filter(lambda m: m not in PROHIBIDAS, mascotas))

if __name__ == "__main__":
    # Pruebas validas
    assert filtrar_mascotas(["Perro", "Gato", "Mapache"]) == ["Perro", "Gato"]
    assert filtrar_mascotas(["Oso", "Conejo", "Tigre"]) == ["Conejo"]
    assert filtrar_mascotas([]) == []

    # Prueba de error: lista con un elemento no string
    print("Probando filtrar_mascotas con valor no string...")
    try:
        filtrar_mascotas(["Perro", 123, "Gato"])
    except TypeError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    # Demostracion visible
    print(filtrar_mascotas(["Gato", "Serpiente Piton", "Tortuga"]))  # ['Gato', 'Tortuga']
    print("KATA 09 - Filtrar mascotas prohibidas - OK")


# %% KATA 10 - Promedio con excepcion personalizada
# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
# excepción personalizada y maneja el error adecuadamente.

from typing import List

class ListaVaciaError(Exception):
    """Excepcion personalizada para listas vacias."""
    pass

def calcular_promedio(numeros: List[float]) -> float:
    """
    Calcula el promedio de una lista de numeros.
    Lanza ListaVaciaError si la lista esta vacia.
    """
    if not numeros:
        raise ListaVaciaError("La lista de numeros esta vacia")
    return sum(numeros) / len(numeros)

if __name__ == "__main__":
    # Pruebas validas
    assert calcular_promedio([5, 10, 15]) == 10.0
    assert calcular_promedio([2]) == 2.0
    assert calcular_promedio([0, 0, 0]) == 0.0

    # Prueba de error: lista vacia
    print("Probando calcular_promedio con lista vacia...")
    try:
        calcular_promedio([])
    except ListaVaciaError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    # Demostracion visible
    print(calcular_promedio([3, 6, 9]))  # 6.0
    print("KATA 10 - Promedio con excepcion personalizada - OK")


# %%
