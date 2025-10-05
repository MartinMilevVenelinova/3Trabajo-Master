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

    #demostracion visible
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
    #pruebas validas
    assert filtrar_mascotas(["Perro", "Gato", "Mapache"]) == ["Perro", "Gato"]
    assert filtrar_mascotas(["Oso", "Conejo", "Tigre"]) == ["Conejo"]
    assert filtrar_mascotas([]) == []

    #prueba de error: lista con un elemento no string
    print("Probando filtrar_mascotas con valor no string...")
    try:
        filtrar_mascotas(["Perro", 123, "Gato"])
    except TypeError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    #demostracion visible
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
    #pruebas validas
    assert calcular_promedio([5, 10, 15]) == 10.0
    assert calcular_promedio([2]) == 2.0
    assert calcular_promedio([0, 0, 0]) == 0.0

    #prueba de error: lista vacia
    print("Probando calcular_promedio con lista vacia...")
    try:
        calcular_promedio([])
    except ListaVaciaError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    #demostracion visible
    print(calcular_promedio([3, 6, 9]))  # 6.0
    print("KATA 10 - Promedio con excepcion personalizada - OK")


# %% KATA 11 - Validar edad del usuario
# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
# adecuadamente.

def pedir_edad():
    """
    Pide al usuario su edad y valida que sea un numero entre 0 y 120.
    Maneja errores de entrada no numerica y de rango.
    """
    try:
        edad_str = input("Introduce tu edad: ")
        if not edad_str.isdigit():
            raise TypeError("El valor ingresado no es un numero valido.")
        
        edad = int(edad_str)
        if edad < 0 or edad > 120:
            raise ValueError("Edad fuera de rango permitido (0-120).")
    except TypeError as e:
        print("Error:", e)
    except ValueError as e:
        print("Error:", e)
    else:
        print("Edad valida. Tienes", edad, "años.")
    finally:
        print("Fin del programa.")

if __name__ == "__main__":
    pedir_edad()


# %% KATA 12 - Longitud de palabras con map
# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

from typing import List

def longitudes_palabras(frase: str) -> List[int]:
    """
    Devuelve una lista con la longitud de cada palabra en la frase.
    """
    if not isinstance(frase, str):
        raise TypeError("El parametro debe ser una cadena de texto")

    palabras = frase.split()
    return list(map(len, palabras))

if __name__ == "__main__":
    #pruebas validas
    assert longitudes_palabras("Hola mundo Python") == [4, 5, 6]
    assert longitudes_palabras("Kata doce lista longitudes") == [4, 4, 5, 10]
    assert longitudes_palabras("") == []

    #prueba de error: parametro no string
    print("Probando longitudes_palabras con valor no string...")
    try:
        longitudes_palabras(12345)
    except TypeError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    #demostracion visible
    print(longitudes_palabras("Hola Mundo"))  
    print("KATA 12 - Longitud de palabras con map - OK")

    
# %% KATA 13 - Lista de tuplas mayusculas y minusculas
# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
# mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

from typing import List, Tuple

def letras_mayus_minus(caracteres: str) -> List[Tuple[str, str]]:
    """
    Devuelve una lista de tuplas con cada letra en mayusculas y minusculas,
    sin repetir caracteres y manteniendo el orden original.
    """
    if not isinstance(caracteres, str):
        raise TypeError("El parametro debe ser una cadena de texto")

    unicos = []
    for c in caracteres.replace(" ", ""):
        if c not in unicos:
            unicos.append(c)

    return list(map(lambda c: (c.upper(), c.lower()), unicos))

if __name__ == "__main__":
    #pruebas validas
    assert letras_mayus_minus("abc") == [('A', 'a'), ('B', 'b'), ('C', 'c')]
    assert letras_mayus_minus("aabbcc") == [('A', 'a'), ('B', 'b'), ('C', 'c')]
    assert letras_mayus_minus("Python") == [('P', 'p'), ('Y', 'y'), ('T', 't'), ('H', 'h'), ('O', 'o'), ('N', 'n')]

    #prueba de error: parametro no string
    print("Probando letras_mayus_minus con valor no string...")
    try:
        letras_mayus_minus(123)
    except TypeError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    #demostracion visible
    print(letras_mayus_minus("hola mundo"))  # [('H', 'h'), ('O', 'o'), ('L', 'l'), ('A', 'a'), ('M', 'm'), ('U', 'u'), ('N', 'n'), ('D', 'd')]
    print("KATA 13 - Lista de tuplas mayusculas y minusculas - OK")

    
# %% KATA 14 - Palbras que comienzan con una letra
# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
# función filter()
 
from typing import List

def palabras_con_letra(palabras: List[str], letra: str) -> List[str]:
    """
    Devuelve una lista con las palabras que comienzan con la letra indicada.
    """
    if not all(isinstance(p, str) for p in palabras):
        raise TypeError("Todos los elementos de la lista deben ser strings")
    if not isinstance(letra, str) or len(letra) != 1:
        raise ValueError("La letra debe ser un solo caracter")

    return list(filter(lambda p: p.lower().startswith(letra.lower()), palabras))

if __name__ == "__main__":
    # Pruebas validas
    assert palabras_con_letra(["python", "java", "perl", "php"], "p") == ["python", "perl", "php"]
    assert palabras_con_letra(["gato", "perro", "pez"], "p") == ["perro", "pez"]
    assert palabras_con_letra([], "a") == []

    # Prueba de error: letra no valida
    print("Probando palabras_con_letra con letra no valida...")
    try:
        palabras_con_letra(["hola", "adios"], "ab")
    except ValueError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    # Demostracion visible
    print(palabras_con_letra(["casa", "coche", "perro", "conejo"], "c"))  # ['casa', 'coche', 'conejo']
    print("KATA 14 - Palabras que comienzan con una letra - OK")


# %% KATA 15 - Sumar 3 a cada numero con lambda
# 15. Crea una función lambda que sume 3 a cada número de una lista dada.

from typing import List

def sumar_tres(lista: List[int]) -> List[int]:
    """
    Devuelve una nueva lista con cada numero aumentado en 3.
    """
    if not all(isinstance(n, (int, float)) for n in lista):
        raise TypeError("Todos los elementos deben ser numeros")

    sumar = lambda n: n + 3
    return list(map(sumar, lista))

if __name__ == "__main__":
    # Pruebas validas
    assert sumar_tres([1, 2, 3]) == [4, 5, 6]
    assert sumar_tres([0, -3, 7]) == [3, 0, 10]
    assert sumar_tres([]) == []

    # Prueba de error: elemento no numerico
    print("Probando sumar_tres con valor no numerico...")
    try:
        sumar_tres([1, "a", 3])
    except TypeError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    # Demostracion visible
    print(sumar_tres([10, 20, 30]))  # [13, 23, 33]
    print("KATA 15 - Sumar 3 a cada numero con lambda - OK")

    
# %% KATA 16 - Palabras mas largas que n
# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
# todas las palabras que sean más largas que n. Usa la función filter()

from typing import List

def palabras_largas(texto: str, n: int) -> List[str]:
    """
    Devuelve una lista con las palabras del texto que tienen longitud mayor que n.
    """
    if not isinstance(texto, str):
        raise TypeError("El primer parametro debe ser una cadena de texto")
    if not isinstance(n, int):
        raise TypeError("El segundo parametro debe ser un numero entero")

    palabras = texto.split()
    return list(filter(lambda p: len(p) > n, palabras))

if __name__ == "__main__":
    #pruebas validas
    assert palabras_largas("Python es un lenguaje poderoso y versatil", 6) == ["lenguaje", "poderoso", "versatil"]
    assert palabras_largas("Hola mundo", 3) == ["Hola", "mundo"]
    assert palabras_largas("", 2) == []

    #prueba de error: parametro incorrecto
    print("Probando palabras_largas con parametro no valido...")
    try:
        palabras_largas(123, 4)
    except TypeError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    #demostracion visible
    print(palabras_largas("Aprender Python es divertido", 5))  # ['Aprender', 'Python', 'divertido']
    print("KATA 16 - Palabras mas largas que n - OK")
    

# %% KATA 17 - Convertir lista de digitos a numero con reduce
# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
# corresponde al número quinientos setenta y dos (572). Usa la función reduce()

from functools import reduce
from typing import List

def lista_a_numero(digitos: List[int]) -> int:
    """
    Convierte una lista de digitos en el numero correspondiente.
    """
    if not all(isinstance(d, int) and 0 <= d <= 9 for d in digitos):
        raise ValueError("Todos los elementos deben ser digitos enteros entre 0 y 9")

    if not digitos:
        raise ValueError("La lista no puede estar vacia")

    return reduce(lambda x, y: x * 10 + y, digitos)

if __name__ == "__main__":
    #pruebas validas
    assert lista_a_numero([5, 7, 2]) == 572
    assert lista_a_numero([0, 1, 2, 3]) == 123
    assert lista_a_numero([9]) == 9

    #prueba de error: valor fuera de rango
    print("Probando lista_a_numero con valor no valido...")
    try:
        lista_a_numero([1, 15, 3])
    except ValueError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    #demostracion visible
    print(lista_a_numero([2, 0, 2, 5]))  # 2025
    print("KATA 17 - Convertir lista de digitos a numero - OK")


# %% KATA 18 - Filtrar estudiantes con nota mayor o igual a 90
# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
# 90. Usa la función filter()

from typing import List, Dict

def filtrar_estudiantes(estudiantes: List[Dict[str, any]]) -> List[Dict[str, any]]:
    """
    Devuelve una lista con los estudiantes cuya calificacion es mayor o igual a 90.
    """
    if not all(isinstance(e, dict) for e in estudiantes):
        raise TypeError("Todos los elementos deben ser diccionarios")

    return list(filter(lambda e: e.get("calificacion", 0) >= 90, estudiantes))

if __name__ == "__main__":
    #lista de estudiantes
    estudiantes = [
        {"nombre": "Ana", "edad": 20, "calificacion": 95},
        {"nombre": "Luis", "edad": 22, "calificacion": 88},
        {"nombre": "Marta", "edad": 21, "calificacion": 90},
        {"nombre": "Jose", "edad": 23, "calificacion": 75},
    ]

    #pruebas validas
    resultado = filtrar_estudiantes(estudiantes)
    assert resultado == [
        {"nombre": "Ana", "edad": 20, "calificacion": 95},
        {"nombre": "Marta", "edad": 21, "calificacion": 90},
    ]

    #prueba de error: elemento no diccionario
    print("Probando filtrar_estudiantes con valor no diccionario...")
    try:
        filtrar_estudiantes([{"nombre": "Ana"}, "no es diccionario"])
    except TypeError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    #demostracion visible
    print(filtrar_estudiantes(estudiantes))
    print("KATA 18 - Filtrar estudiantes con nota mayor o igual a 90 - OK")


# %% KATA 19 - Filtrar numeros impares con lambda
# 19. Crea una función lambda que filtre los números impares de una lista dada.

from typing import List

def filtrar_impares(numeros: List[int]) -> List[int]:
    """
    Devuelve una lista con los numeros impares de la lista original.
    """
    if not all(isinstance(n, int) for n in numeros):
        raise TypeError("Todos los elementos deben ser numeros enteros")

    impares = lambda x: x % 2 != 0
    return list(filter(impares, numeros))

if __name__ == "__main__":
    #pruebas validas
    assert filtrar_impares([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert filtrar_impares([2, 4, 6, 8]) == []
    assert filtrar_impares([7, 9, 11]) == [7, 9, 11]
    assert filtrar_impares([]) == []

    #prueba de error: elemento no numerico
    print("Probando filtrar_impares con valor no numerico...")
    try:
        filtrar_impares([1, "a", 3])
    except TypeError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    #demostracion visible
    print(filtrar_impares([10, 11, 12, 13, 14, 15]))  # [11, 13, 15]
    print("KATA 19 - Filtrar numeros impares con lambda - OK")


# %% KATA 20 - Filtrar solo numeros enteros
# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
# filter()

from typing import List, Any

def filtrar_enteros(elementos: List[Any]) -> List[int]:
    """
    Devuelve una nueva lista solo con los elementos de tipo entero.
    """
    if not isinstance(elementos, list):
        raise TypeError("El parametro debe ser una lista")

    return list(filter(lambda e: isinstance(e, int), elementos))

if __name__ == "__main__":
    #pruebas validas
    assert filtrar_enteros([1, "a", 2, "b", 3]) == [1, 2, 3]
    assert filtrar_enteros(["hola", "mundo"]) == []
    assert filtrar_enteros([10, 20, 30]) == [10, 20, 30]
    assert filtrar_enteros([]) == []

    #prueba de error: parametro no lista
    print("Probando filtrar_enteros con parametro no lista...")
    try:
        filtrar_enteros("no es lista")
    except TypeError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    #demostracion visible
    print(filtrar_enteros([1, "2", 3, "cuatro", 5]))  # [1, 3, 5]
    print("KATA 20 - Filtrar solo numeros enteros - OK")


# %% KATA 21 - Calcular el cubo con lambda
# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

def cubo(numero):
    """
    Devuelve el cubo de un numero usando una funcion lambda.
    """
    if not isinstance(numero, (int, float)):
        raise TypeError("El valor debe ser un numero")

    calcular_cubo = lambda n: n ** 3
    return calcular_cubo(numero)

if __name__ == "__main__":
    #pruebas validas
    assert cubo(2) == 8
    assert cubo(-3) == -27
    assert cubo(0) == 0
    assert cubo(1.5) == 3.375

    #prueba de error: valor no numerico
    print("Probando cubo con valor no numerico...")
    try:
        cubo("a")
    except TypeError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    #demostracion visible
    print(cubo(5))   # 125
    print("KATA 21 - Calcular el cubo con lambda - OK")


# %%
