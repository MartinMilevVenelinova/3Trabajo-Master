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


# %% KATA 22 - Producto total de una lista con reduce
# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .

from functools import reduce
from typing import List

def producto_total(numeros: List[int]) -> int:
    """
    Devuelve el producto total de los valores de una lista usando reduce().
    """
    if not all(isinstance(n, (int, float)) for n in numeros):
        raise TypeError("Todos los elementos deben ser numeros")

    if not numeros:
        raise ValueError("La lista no puede estar vacia")

    return reduce(lambda x, y: x * y, numeros)

if __name__ == "__main__":
    # Pruebas validas
    assert producto_total([1, 2, 3, 4]) == 24
    assert producto_total([5, 5]) == 25
    assert producto_total([10]) == 10
    assert producto_total([2.0, 3.0]) == 6.0

    # Prueba de error: lista vacia
    print("Probando producto_total con lista vacia...")
    try:
        producto_total([])
    except ValueError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    # Demostracion visible
    print(producto_total([2, 3, 4]))  # 24
    print("KATA 22 - Producto total de una lista con reduce - OK")


# %%
# 23. Concatena una lista de palabras.Usa la función reduce() .

from functools import reduce
from typing import List

def concatenar_palabras(palabras: List[str]) -> str:
    """
    Devuelve una sola cadena con todas las palabras concatenadas.
    """
    if not all(isinstance(p, str) for p in palabras):
        raise TypeError("Todos los elementos deben ser cadenas de texto")

    if not palabras:
        raise ValueError("La lista no puede estar vacia")

    return reduce(lambda x, y: x + y, palabras)

if __name__ == "__main__":
    # Pruebas validas
    assert concatenar_palabras(["Hola", "Mundo"]) == "HolaMundo"
    assert concatenar_palabras(["Python", "Es", "Genial"]) == "PythonEsGenial"
    assert concatenar_palabras(["A", "B", "C"]) == "ABC"

    # Prueba de error: lista vacia
    print("Probando concatenar_palabras con lista vacia...")
    try:
        concatenar_palabras([])
    except ValueError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    # Demostracion visible
    print(concatenar_palabras(["Big", "Data", "Analytics"]))  # BigDataAnalytics
    print("KATA 23 - Concatenar lista de palabras con reduce - OK")


# %% KATA 24 - Diferencia total de los valores de una lista con reduce
# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

from functools import reduce
from typing import List

def diferencia_total(numeros: List[int]) -> int:
    """
    Calcula la diferencia total de los valores de una lista usando reduce().
    """
    if not all(isinstance(n, (int, float)) for n in numeros):
        raise TypeError("Todos los elementos deben ser numeros")

    if not numeros:
        raise ValueError("La lista no puede estar vacia")

    return reduce(lambda x, y: x - y, numeros)

if __name__ == "__main__":
    #Pruebas validas
    assert diferencia_total([10, 5, 2]) == 3    # 10 - 5 - 2 = 3
    assert diferencia_total([100, 50, 25]) == 25
    assert diferencia_total([5]) == 5
    assert diferencia_total([20.5, 5.5]) == 15.0

    #prueba de error: lista vacia
    print("Probando diferencia_total con lista vacia...")
    try:
        diferencia_total([])
    except ValueError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    # Demostracion visible
    print(diferencia_total([50, 10, 5, 2]))  # 33
    print("KATA 24 - Diferencia total de los valores de una lista - OK")


# %% KATA 25 - Contar caracteres en una cadena
# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(texto: str) -> int:
    """
    Devuelve el numero total de caracteres en una cadena de texto.
    """
    if not isinstance(texto, str):
        raise TypeError("El parametro debe ser una cadena de texto")

    return len(texto)

if __name__ == "__main__":
    #pruebas validas
    assert contar_caracteres("Hola") == 4
    assert contar_caracteres("Python") == 6
    assert contar_caracteres("") == 0
    assert contar_caracteres("Big Data") == 8  # incluye espacio

    # Prueba de error: parametro no string
    print("Probando contar_caracteres con parametro no string...")
    try:
        contar_caracteres(123)
    except TypeError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    # demostracion visible
    print(contar_caracteres("BigDataAnalytics")) # 16
    print("KATA 25 - Contar caracteres en una cadena - OK")


# %% KATA 26 - Calcular el resto de la division con lambda
# 26. Crea una función lambda que calcule el resto de la división entre dos números dados

def resto_division(a, b):
    """
    Devuelve el resto de la division entre dos numeros usando una funcion lambda.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ambos valores deben ser numeros")
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")

    resto = lambda x, y: x % y
    return resto(a, b)

if __name__ == "__main__":
    #pruebas validas
    assert resto_division(10, 3) == 1
    assert resto_division(25, 5) == 0
    assert resto_division(7, 4) == 3
    assert resto_division(9.5, 2.5) == 2.0

    # Prueba de error: division por cero
    print("Probando resto_division con division por cero...")
    try:
        resto_division(10, 0)
    except ZeroDivisionError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    # Demostracion visible
    print(resto_division(20, 6))  # 2
    print("KATA 26 - Calcular el resto de la division con lambda - OK")

# %% KATA 27 - Calcular el promedio de una lista
# 27. Crea una función que calcule el promedio de una lista de números

from typing import List

def promedio(numeros: List[float]) -> float:
    """
    Calcula el promedio (media) de una lista de numeros.
    """
    if not all(isinstance(n, (int, float)) for n in numeros):
        raise TypeError("Todos los elementos deben ser numeros")
    if not numeros:
        raise ValueError("La lista no puede estar vacia")

    return sum(numeros) / len(numeros)

if __name__ == "__main__":
    #Pruebas validas
    assert promedio([1, 2, 3, 4, 5]) == 3.0
    assert promedio([10, 20, 30]) == 20.0
    assert promedio([5]) == 5.0
    assert promedio([2.5, 3.5, 4.5]) == 3.5

    #Prueba de error: lista vacia
    print("Probando promedio con lista vacia...")
    try:
        promedio([])
    except ValueError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    # Demostracion visible
    print(promedio([6, 8, 10]))  # 8.0
    print("KATA 27 - Calcular el promedio de una lista - OK")

# %% KATA 28 - Buscar el primer elemento duplicado en una lista
#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

from typing import List, Any

def primer_duplicado(elementos: List[Any]) -> Any:
    """
    Devuelve el primer elemento duplicado encontrado en la lista.
    Si no hay duplicados, devuelve None.
    """
    if not isinstance(elementos, list):
        raise TypeError("El parametro debe ser una lista")

    vistos = set()
    for e in elementos:
        if e in vistos:
            return e
        vistos.add(e)
    return None

if __name__ == "__main__":
    # Pruebas validas
    assert primer_duplicado([1, 2, 3, 2, 5]) == 2
    assert primer_duplicado(["a", "b", "c", "a", "d"]) == "a"
    assert primer_duplicado([10, 20, 30, 40]) is None
    assert primer_duplicado([]) is None

    # Prueba de error: parametro no lista
    print("Probando primer_duplicado con parametro no lista...")
    try:
        primer_duplicado("no es lista")
    except TypeError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    #demostracion visible
    print(primer_duplicado([9, 7, 3, 5, "leon", "león", 5]))  
    print("KATA 28 - Buscar el primer elemento duplicado en una lista - OK")


# %% KATA 29 - Enmascarar una cadena de texto
# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
# carácter '#', excepto los últimos cuatro.

def enmascarar(valor) -> str:
    """
    Convierte el valor en texto y reeemplaza todos los caracteres con '#',
    excepto los ultimos cuatro.
    """
    texto = str(valor)

    if len(texto) <= 4:
        return texto

    return "#" * (len(texto) - 4) + texto[-4:]

if __name__ == "__main__":
    #pruebas validas
    assert enmascarar("123456789") == "#####6789"
    assert enmascarar(987654321) == "#####4321"
    assert enmascarar("abcd") == "abcd"
    assert enmascarar("hi") == "hi"

    #prueba de error: valor None
    print("Probando enmascarar con valor None...")
    try:
        enmascarar(None)
    except Exception as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    # Demostracion visible
    print(enmascarar("claveSecreta_1234"))  # ###########1234
    print("KATA 29 - Enmascarar una cadena de texto - OK")


# %% KATA 30 - Comprobar si dos palabras son anagramas
# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
# pero en diferente orden.

def son_anagramas(palabra1: str, palabra2: str) -> bool:
    """
    Devuelve True si las dos palabras son anagramas, False en caso contrario.
    """
    if not isinstance(palabra1, str) or not isinstance(palabra2, str):
        raise TypeError("Ambos parametros deben ser cadenas de texto")

    #convertir a minusculas y eliminar espacios
    p1 = palabra1.replace(" ", "").lower()
    p2 = palabra2.replace(" ", "").lower()

    return sorted(p1) == sorted(p2)

if __name__ == "__main__":
    # Pruebas validas
    assert son_anagramas("amor", "roma") is True
    assert son_anagramas("python", "typhon") is True
    assert son_anagramas("hola", "adios") is False
    assert son_anagramas("Ana", "Naa") is True
    assert son_anagramas("cosa", "caso") is True

    # Prueba de error: parametro no string
    print("Probando son_anagramas con parametro no string...")
    try:
        son_anagramas("hola", 123)
    except TypeError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    #Demostracion visible
    print(son_anagramas("listen", " Silent"))  # True
    print("KATA 30 - Comprobar si dos palabras son anagramas - OK")


# %% KATA 31 - Buscar un nombre en una lista ingresada por el usuario 
# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
#lanza una excepción.

def buscar_nombre():
    """
    Solicita una lista de nombres y busca un nombre especifico dentro de ella.
    """
    try:
        nombres = input("Ingresa una lista de nombres separados por comas: ")
        lista_nombres = [n.strip() for n in nombres.split(",") if n.strip()]

        if not lista_nombres:
            raise ValueError("La lista de nombres no puede estar vacia.")

        nombre_buscar = input("Ingresa el nombre que deseas buscar: ").strip()

        if nombre_buscar in lista_nombres:
            print(f"El nombre '{nombre_buscar}' fue encontrado en la lista.")
        else:
            raise ValueError(f"El nombre '{nombre_buscar}' no se encuentra en la lista.")

    except ValueError as e:
        print("Error:", e)
    finally:
        print("Fin del programa.")

if __name__ == "__main__":
    buscar_nombre()

"""
Ingresa una lista de nombres separados por comas: Martin, Nerea, Julian
Ingresa el nombre que deseas buscar: Martin
El nombre 'Martin' fue encontrado en la lista.
En caso de buscar "Pedro" devolvera -El nombre 'Pedro' no se encuentra en la lista.-
Fin del programa.
"""


# %% KATA 32 - Buscar el puesto de un empleado por nombre 
# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
# no trabaja aquí.

from typing import List, Dict

def buscar_empleado(nombre: str, empleados: List[Dict[str, str]]) -> str:
    """
    Busca un empleado por nombre completo y devuelve su puesto si existe.
    """
    if not isinstance(nombre, str):
        raise TypeError("El nombre debe ser una cadena de texto")
    if not all(isinstance(e, dict) for e in empleados):
        raise TypeError("La lista de empleados debe contener diccionarios")

    for e in empleados:
        if e.get("nombre", "").lower() == nombre.lower():
            return e.get("puesto", "Puesto no especificado")
    
    return f"La persona '{nombre}' no trabaja aqui."

if __name__ == "__main__":
    #lista de empleados
    empleados = [
        {"nombre": "Ana Lopez", "puesto": "Analista de datos"},
        {"nombre": "Luis Perez", "puesto": "Desarrollador"},
        {"nombre": "Marta Ruiz", "puesto": "Gerente de proyecto"}
    ]

    # Pruebas validas
    assert buscar_empleado("Ana Lopez", empleados) == "Analista de datos"
    assert buscar_empleado("Luis Perez", empleados) == "Desarrollador"
    assert buscar_empleado("Pedro Gomez", empleados) == "La persona 'Pedro Gomez' no trabaja aqui."

    # Prueba de error: parametro incorrecto
    print("Probando buscar_empleado con parametro no valido...")
    try:
        buscar_empleado(123, empleados)
    except TypeError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    # Demostracion visible
    print(buscar_empleado("Marta Ruiz", empleados))  # Gerente de proyecto
    print(buscar_empleado("Juan Torres", empleados)) # La persona 'Juan Torres' no trabaja aqui.
    print("KATA 32 - Buscar el puesto de un empleado por nombre - OK")


# %% KATA 33 - Sumar elementos correspondientes de dos listas con lambda
# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

from typing import List

def sumar_listas(lista1: List[int], lista2: List[int]) -> List[int]:
    """
    Devuelve una lista con la suma de los elementos correspondientes de dos listas.
    """
    if not all(isinstance(n, (int, float)) for n in lista1 + lista2):
        raise TypeError("Ambas listas deben contener solo numeros")
    if len(lista1) != len(lista2):
        raise ValueError("Las listas deben tener la misma longitud")

    sumar = lambda x, y: x + y
    return list(map(sumar, lista1, lista2))

if __name__ == "__main__":
    # Pruebas validas
    assert sumar_listas([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
    assert sumar_listas([10, 20], [1, 2]) == [11, 22]
    assert sumar_listas([0, -1, -2], [1, 2, 3]) == [1, 1, 1]

    # Prueba de error: longitudes distintas
    print("Probando sumar_listas con longitudes distintas...")
    try:
        sumar_listas([1, 2, 3], [1, 2])
    except ValueError as e:
        print("Error capturado correctamente:", e)
    else:
        print("No se capturo el error como se esperaba")

    # Demostracion visible
    print(sumar_listas([5, 10, 15], [2, 4, 6]))  # [7, 14, 21]
    print("KATA 33 - Sumar elementos correspondientes de dos listas - OK")


# %%
# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
# crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
# manipular la estructura del árbol.

from typing import List, Dict, Optional

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas: List[int] = []

    def crecer_tronco(self, cantidad: int = 1):
        if not isinstance(cantidad, int):
            raise TypeError("La cantidad de crecimiento del tronco debe ser un entero")
        if cantidad <= 0:
            raise ValueError("La cantidad de crecimiento del tronco debe ser positiva")
        self.tronco += cantidad
        print(f"El tronco ha crecido {cantidad} unidad(es). Longitud actual: {self.tronco}")

    def nueva_rama(self, cantidad: int = 1):
        if not isinstance(cantidad, int):
            raise TypeError("La cantidad de ramas debe ser un entero")
        if cantidad <= 0:
            raise ValueError("La cantidad de ramas debe ser positiva")
        for _ in range(cantidad):
            self.ramas.append(1)
        print(f"Se ha(n) agregado {cantidad} rama(s) de longitud 1. Total ramas: {len(self.ramas)} -> {self.ramas}")

    def crecer_ramas(self, cantidad: int = 1):
        if not isinstance(cantidad, int):
            raise TypeError("La cantidad de crecimiento de ramas debe ser un entero")
        if cantidad <= 0:
            raise ValueError("La cantidad de crecimiento de ramas debe ser positiva")
        if not self.ramas:
            print("No hay ramas para crecer.")
            return
        self.ramas = [r + cantidad for r in self.ramas]
        print(f"Todas las ramas han crecido {cantidad} unidad(es). Longitudes: {self.ramas}")

    def quitar_rama(self, posicion: int):
        if not isinstance(posicion, int):
            raise TypeError("La posicion debe ser un numero entero")
        if not self.ramas:
            raise IndexError("No hay ramas para quitar")
        if posicion < 0 or posicion >= len(self.ramas):
            raise IndexError(f"Posicion de rama invalida (0..{len(self.ramas)-1})")
        valor = self.ramas.pop(posicion)
        print(f"Se ha quitado la rama en la posicion {posicion} (longitud {valor}). Ramas restantes: {self.ramas}")

    def info_arbol(self) -> Dict[str, object]:
        info = {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": list(self.ramas)
        }
        print("Estado actual del arbol:", info)
        return info


def leer_entero(prompt: str, por_defecto: Optional[int] = None) -> int:
    """
    Lee un entero desde input(). Si el usuario pulsa Enter y por_defecto no es None, devuelve por_defecto.
    Lanza ValueError si no es convertible a int.
    """
    texto = input(prompt).strip()
    if texto == "" and por_defecto is not None:
        return por_defecto
    try:
        return int(texto)
    except ValueError:
        raise ValueError("Se esperaba un numero entero")


def menu():
    arbol: Optional[Arbol] = None

    while True:
        print("\n--- MENU ARBOL ---")
        print("1. Crear arbol")
        print("2. Crecer tronco (cantidad opcional)")
        print("3. Agregar nueva(s) rama(s) (cantidad opcional)")
        print("4. Crecer todas las ramas (cantidad opcional)")
        print("5. Quitar rama por posicion")
        print("6. Mostrar informacion del arbol")
        print("7. Salir")

        opcion = input("Selecciona una opcion (1-7): ").strip()

        try:
            if opcion == "1":
                if arbol is not None:
                    print("Ya existe un arbol creado. No puedes crear otro.")
                else:
                    arbol = Arbol()
                    print("Arbol creado (tronco=1, ramas=[]).")

            elif opcion == "2":
                if arbol is None:
                    print("Primero debes crear el arbol (opcion 1).")
                else:
                    cantidad = leer_entero("Cuanto debe crecer el tronco? (Enter = 1): ", por_defecto=1)
                    arbol.crecer_tronco(cantidad)

            elif opcion == "3":
                if arbol is None:
                    print("Primero debes crear el arbol (opcion 1).")
                else:
                    cantidad = leer_entero("Cuantas ramas nuevas agregar? (Enter = 1): ", por_defecto=1)
                    arbol.nueva_rama(cantidad)

            elif opcion == "4":
                if arbol is None:
                    print("Primero debes crear el arbol (opcion 1).")
                else:
                    cantidad = leer_entero("Cuanto deben crecer las ramas? (Enter = 1): ", por_defecto=1)
                    arbol.crecer_ramas(cantidad)

            elif opcion == "5":
                if arbol is None:
                    print("Primero debes crear el arbol (opcion 1).")
                else:
                    if not arbol.ramas:
                        print("El arbol no tiene ramas para quitar.")
                    else:
                        print(f"Ramas actuales (indices 0..{len(arbol.ramas)-1}): {arbol.ramas}")
                        pos = leer_entero("Introduce la posicion de la rama a quitar: ")
                        arbol.quitar_rama(pos)

            elif opcion == "6":
                if arbol is None:
                    print("Primero debes crear el arbol (opcion 1).")
                else:
                    arbol.info_arbol()

            elif opcion == "7":
                print("Saliendo del programa.")
                break

            else:
                print("Opcion no valida. Elige entre 1 y 7.")

        except (TypeError, ValueError, IndexError) as e:
            print("Error:", e)


if __name__ == "__main__":
    menu()

# %% KATA 36 - Clase UsuarioBanco
# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
#   corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
# agregar dinero al saldo.

class UsuarioBanco:
    def __init__(self, nombre: str, saldo: float, cuenta_corriente: bool):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto")
        if not isinstance(saldo, (int, float)) or saldo < 0:
            raise ValueError("El saldo debe ser un numero positivo")
        if not isinstance(cuenta_corriente, bool):
            raise TypeError("El valor de cuenta_corriente debe ser True o False")
        
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad: float):
        if not isinstance(cantidad, (int, float)):
            raise TypeError("La cantidad debe ser un numero")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if cantidad > self.saldo and not self.cuenta_corriente:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para retirar {cantidad}")
        
        self.saldo -= cantidad
        print(f"{self.nombre} ha retirado {cantidad}. Saldo actual: {self.saldo}")

    def agregar_dinero(self, cantidad: float):
        if not isinstance(cantidad, (int, float)):
            raise TypeError("La cantidad debe ser un numero")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        
        self.saldo += cantidad
        print(f"{self.nombre} ha agregado {cantidad}. Saldo actual: {self.saldo}")

    def transferir_dinero(self, otro_usuario: "UsuarioBanco", cantidad: float):
        if not isinstance(otro_usuario, UsuarioBanco):
            raise TypeError("El destinatario debe ser un objeto UsuarioBanco")
        if not isinstance(cantidad, (int, float)):
            raise TypeError("La cantidad debe ser un numero")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")

        # Validacion con sobregiro permitido solo si tiene cuenta corriente
        if cantidad > otro_usuario.saldo and not otro_usuario.cuenta_corriente:
            raise ValueError(f"{otro_usuario.nombre} no tiene suficiente saldo para transferir {cantidad}")

        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
        print(f"{otro_usuario.nombre} ha transferido {cantidad} a {self.nombre}.")
        print(f"Saldo de {otro_usuario.nombre}: {otro_usuario.saldo} | Saldo de {self.nombre}: {self.saldo}")

    def info_usuario(self):
        return {
            "nombre": self.nombre,
            "saldo": self.saldo,
            "cuenta_corriente": self.cuenta_corriente
        }


if __name__ == "__main__":
    # Caso de uso
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)

    print("Estado inicial:")
    print(alicia.info_usuario())
    print(bob.info_usuario())

    # 2.Agregar 20 unidades de saldo de Bob
    bob.agregar_dinero(20)

    #3.Hacer una transferencia de 80 unidades desde Bob a Alicia
    alicia.transferir_dinero(bob, 80)

    # 4.Retirar 50 unidades de saldo a Alicia
    alicia.retirar_dinero(50)

    print("\nEstado final:")
    print(alicia.info_usuario())
    print(bob.info_usuario())

    print("KATA 36 - Clase UsuarioBanco (version final con sobregiro permitido) - OK")


# %% 36.2. Caso de prueba con menu incluido

from typing import Dict

class UsuarioBanco:
    def __init__(self, nombre: str, saldo: float, cuenta_corriente: bool):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto")
        if not isinstance(saldo, (int, float)) or saldo < 0:
            raise ValueError("El saldo debe ser un numero positivo")
        if not isinstance(cuenta_corriente, bool):
            raise TypeError("El valor de cuenta_corriente debe ser True o False")
        
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad: float):
        if not isinstance(cantidad, (int, float)):
            raise TypeError("La cantidad debe ser un numero")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if cantidad > self.saldo and not self.cuenta_corriente:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para retirar {cantidad}")
        
        self.saldo -= cantidad
        print(f"{self.nombre} ha retirado {cantidad}. Saldo actual: {self.saldo}")

    def agregar_dinero(self, cantidad: float):
        if not isinstance(cantidad, (int, float)):
            raise TypeError("La cantidad debe ser un numero")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        
        self.saldo += cantidad
        print(f"{self.nombre} ha agregado {cantidad}. Saldo actual: {self.saldo}")

    def transferir_dinero(self, otro_usuario: "UsuarioBanco", cantidad: float):
        if not isinstance(otro_usuario, UsuarioBanco):
            raise TypeError("El destinatario debe ser un objeto UsuarioBanco")
        if not isinstance(cantidad, (int, float)):
            raise TypeError("La cantidad debe ser un numero")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")

        if cantidad > otro_usuario.saldo and not otro_usuario.cuenta_corriente:
            raise ValueError(f"{otro_usuario.nombre} no tiene suficiente saldo para transferir {cantidad}")

        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
        print(f"{otro_usuario.nombre} ha transferido {cantidad} a {self.nombre}.")
        print(f"Saldo de {otro_usuario.nombre}: {otro_usuario.saldo} | Saldo de {self.nombre}: {self.saldo}")

    def info_usuario(self) -> Dict[str, object]:
        return {
            "nombre": self.nombre,
            "saldo": self.saldo,
            "cuenta_corriente": self.cuenta_corriente
        }


def menu():
    usuarios: Dict[str, UsuarioBanco] = {}

    while True:
        print("\n--- MENU BANCO ---")
        print("1. Crear nueva cuenta")
        print("2. Consultar cuenta")
        print("3. Ingresar dinero")
        print("4. Retirar dinero")
        print("5. Transferir dinero entre cuentas")
        print("6. Listar todas las cuentas")
        print("7. Salir")

        opcion = input("Selecciona una opcion (1-7): ").strip()

        try:
            if opcion == "1":
                nombre = input("Introduce el nombre del usuario: ").strip()
                if nombre in usuarios:
                    print("Ya existe una cuenta con ese nombre.")
                    continue
                saldo_inicial = float(input("Introduce el saldo inicial: "))
                corriente = input("Tiene cuenta corriente? (s/n): ").strip().lower()
                cuenta_corriente = corriente == "s"
                usuarios[nombre] = UsuarioBanco(nombre, saldo_inicial, cuenta_corriente)
                print(f"Cuenta creada para {nombre} con saldo {saldo_inicial}.")

            elif opcion == "2":
                nombre = input("Introduce el nombre del usuario: ").strip()
                if nombre not in usuarios:
                    print("No existe una cuenta con ese nombre.")
                    continue
                info = usuarios[nombre].info_usuario()
                print("Informacion de la cuenta:", info)

            elif opcion == "3":
                nombre = input("Usuario que recibe el dinero: ").strip()
                if nombre not in usuarios:
                    print("No existe una cuenta con ese nombre.")
                    continue
                cantidad = float(input("Cantidad a ingresar: "))
                usuarios[nombre].agregar_dinero(cantidad)

            elif opcion == "4":
                nombre = input("Usuario que retira el dinero: ").strip()
                if nombre not in usuarios:
                    print("No existe una cuenta con ese nombre.")
                    continue
                cantidad = float(input("Cantidad a retirar: "))
                usuarios[nombre].retirar_dinero(cantidad)

            elif opcion == "5":
                origen = input("Nombre del usuario que envia dinero: ").strip()
                destino = input("Nombre del usuario que recibe dinero: ").strip()

                if origen not in usuarios or destino not in usuarios:
                    print("Uno de los usuarios no existe.")
                    continue
                if origen == destino:
                    print("No puedes transferir dinero a la misma cuenta.")
                    continue
                cantidad = float(input("Cantidad a transferir: "))
                usuarios[destino].transferir_dinero(usuarios[origen], cantidad)

            elif opcion == "6":
                if not usuarios:
                    print("No hay cuentas registradas.")
                else:
                    print("Listado de cuentas:")
                    for u in usuarios.values():
                        print(u.info_usuario())

            elif opcion == "7":
                print("Saliendo del programa. Gracias por usar el sistema bancario.")
                break

            else:
                print("Opcion no valida. Intenta de nuevo.")

        except (TypeError, ValueError) as e:
            print("Error:", e)


if __name__ == "__main__":
    menu()


# %%
