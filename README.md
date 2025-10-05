____________________________________________________________________________________________KATA 01__________________________________________________________________________________________

Quiero contar cuantas veces aparece cada caracter en un texto, ignorando los espacios. Recorro la cadena letra por letra y uso un diccioanrio contador: si la letra ya esta, sumo 1; si no, 
la inicio en 0 con dict.get y sumo 1. Si pongo ignorar_mayusculas=True paso todo a minusculas para que A y a cuenten igul. Hice pruebas con casos tipicos (texto normal, vacio, solo espacios y 
mezcla de mayusculas). La complejidad es O(n) y el codigo queda simple y claro, aunque seguro que algo se me pudo pasar.


____________________________________________________________________________________________KATA 02__________________________________________________________________________________________

Quiero una funcion que reciba una lista de numeros y me devuelva otra con cada valor x2. Uso map con una lambda lambda x: x*2, que me da un iterador, asi que lo convierto a lista con list(...).
Uso map porque el enunciado lo pide (aunque una compresion de lista tambien valdria). Hice asserts para casos tipicos: lista normal, vacia y con negativos/decimales. 
La complejidad es O(n) y el codigo queda simple; si algo falla es facil ver donde esta el resutlado raro.

____________________________________________________________________________________________KATA 03__________________________________________________________________________________________

Quiero una funcion que reciba una lista de palabras y un objetivo y me devuelva solo las que contienen ese objetivo como subcadena. Uso una compresion de lista:
[p for p in palabras if objetivo in p] → recorro cada palabra p y me quedo con ella si objetivo in p es verdad (el operador in mira si el trozo aparece dentro).
La busqueda es sensible a mayusculas/minusculas; si quisera ignorarlas haria objetivo.lower() in p.lower().
Las pruebas cubren casos tipicos (coincidencias, subcadenas y lista vacia). El resultado mantiene el orden de entrada (no ordeno nada).

____________________________________________________________________________________________KATA 04__________________________________________________________________________________________

Funcion que recibe dos listas y calcula la diferencia de sus valores usando map().
Uso lambda x, y: x - y para restar pares de elementos.
Controlo que las listas tengan el mismo tamaño o lanzo un ValueError.
Las pruebas incluyen:
Casos normales con listas iguales en longitud.
Caso de error con longitudes distintas (debe lanzar excepcion).

____________________________________________________________________________________________KATA 05__________________________________________________________________________________________

Quiero una funcion que reciba una lista de números (notas) y un valor opcional nota_aprobado (por defecto 5). Calculo la media con sum(notas) / len(notas). 
Luego comparo esa media con nota_aprobado: si es mayor o igual, el estado es "aprobado", si no, "suspenso". Devuelvo una tupla con la media y el estado.
Las pruebas incluyen distintos casos:
medias por encima, igual o debajo del aprobado, nota_aprobado personalizado y una nota sola.
También controlo que la lista no esté vacía: si lo está, lanzo un ValueError, ya que no tendría sentido calcular una media de nada.

____________________________________________________________________________________________KATA 06__________________________________________________________________________________________

Funcion recursiva para calcular factorial:
Caso base: n == 0 o n == 1 → devuelve 1
Caso recursivo: n * factorial(n-1).
Control: si n es negativo, lanzo ValueError porque factorial no se define para negativos
Pruebas:
Casos normales con factoriales conocidos.
Caso de error con negativo (debe lanzar excepcion).

____________________________________________________________________________________________KATA 07__________________________________________________________________________________________

Funcion que convierte una lista de tuplas en strings, usando map() dos veces:
- map(str, t) para convertir los elementos de la tupla a string
- " ".join(...) para unirlos con espacios
Todo dentro de un map() general que recorre cada tupla.
Controlo que todos los elementos sean tuplas usando all(...), si no lanzo TypeError.
Pruebas:
Tuplas de strings y de numeros
Caso donde un elemento no es tupla (debe lanzar error)

____________________________________________________________________________________________KATA 08__________________________________________________________________________________________

Este programa pide al usuario dos numeros reales usando input().

Convierte los valores a float y los divide.
Si el usuario ingresa algo que no sea un numero, se lanza ValueError.
Si el segundo numero es cero, se lanza ZeroDivisionError.
Si no hay errores, muestra el resultado en el bloque else.
El bloque finally siempre se ejecuta para mostrar que el programa termino.
Este es un ejemplo clasico del uso completo de try / except / else / finally para manejar errores de entrada y control de flujo.

____________________________________________________________________________________________KATA 09__________________________________________________________________________________________

La funcion recibe una lista de nombres de mascotas y elimina las que aparecen en la lista de prohibidas.
Uso filter() con una funcion lambda que conserva solo las que no estan en PROHIBIDAS.
Antes de eso, reviso que todos los elementos de la lista sean str. Si no, lanzo un TypeError.
Pruebas:
Casos con mascotas permitidas y prohibidas mezcladas
Lista vacia
Caso con un elemento no string para forzar un error

____________________________________________________________________________________________KATA 10__________________________________________________________________________________________

La funcion calcular_promedio toma una lista de numeros y devuelve su promedio.
Si la lista esta vacia, lanza una excepcion personalizada ListaVaciaError.
Esto permite identificar el error claramente y manejarlo con un try/except
Pruebas:
Casos con listas normales de numeros
Caso con una lista vacia para forzar el error
La definicion de una excepcion personalizada (class ListaVaciaError) permite extender el control de errores mas alla de las excepciones estandar.

____________________________________________________________________________________________KATA 11__________________________________________________________________________________________

El programa pide la edad al usuario y valida:
Si el valor no es numerico (por ejemplo "hola" o "veinte") → se lanza un TypeError.
Esto se detecta con .isdigit() antes de convertir a int.
Si la edad esta fuera del rango permitido (0 a 120) → se lanza un ValueError.
Si todo esta bien, muestra la edad ingresada.
Siempre imprime "Fin del programa" al final con finally.

____________________________________________________________________________________________KATA 12__________________________________________________________________________________________

La funcion longitudes_palabras recibe una frase y devuelve una lista con la longitud de cada palabra.
Comprueba que el argumento sea un string. Si no, lanza un TypeError.
Usa split() para separar la frase por espacios.
Aplica map(len, palabras) para calcular la longitud de cada palabra.
Convierte el resultado de map() en una lista.
Pruebas:
Casos normales con frases con varias palabras.
Frase vacia (devuelve lista vacia).
Caso de error cuando el parametro no es string.

____________________________________________________________________________________________KATA 13__________________________________________________________________________________________

La funcion recibe una cadena y devuelve una lista de tuplas con cada letra en mayuscula y minuscula, sin repetir y manteniendo el orden original.
Primero elimino los espacios y guardo solo las letras unicas recorriendo el texto.
Luego uso map() con lambda c: (c.upper(), c.lower()) para crear las tuplas.
Las pruebas cubren letras repetidas, orden y tipo de dato incorrecto (lanza TypeError).

____________________________________________________________________________________________KATA 14__________________________________________________________________________________________

La funcion recibe una lista de palabras y una letra, y devuelve solo las que empiezan con esa letra.
Uso filter() con lambda p: p.lower().startswith(letra.lower()) para comparar sin distinguir mayusculas.
Controlo que todos los elementos sean strings y que la letra sea un unico caracter.
Las pruebas incluyen listas vacias, coincidencias y errores por letra no valida.

____________________________________________________________________________________________KATA 15__________________________________________________________________________________________

La funcion recibe una lista de numeros y usa una lambda para sumar 3 a cada elemento.
La expresion lambda n: n + 3 se aplica con map() para crear una nueva lista.
Verifico que todos los elementos sean numericos antes de operar.
Las pruebas cubren listas normales, vacias y un caso de error con un valor no numerico.

____________________________________________________________________________________________KATA 16__________________________________________________________________________________________

La funcion recibe un texto y un numero entero n, y devuelve las palabras cuya longitud es mayor que n.
Primero separo el texto en palabras con split().
Luego uso filter() con lambda p: len(p) > n para quedarme solo con las mas largas.
Controlo que el texto sea un str y n un entero.
Las pruebas cubren frases normales, texto vacio y un caso de error con tipo de dato incorrecto.

____________________________________________________________________________________________KATA 17__________________________________________________________________________________________

La funcion recibe una lista de digitos y los combina para formar el numero completo.
Uso reduce() con lambda x, y: x * 10 + y para acumular los digitos uno a uno.
Primero verifico que todos los elementos sean enteros entre 0 y 9, y que la lista no este vacia.
Las pruebas cubren numeros normales, un solo digito y un caso de error con valor no valido.

____________________________________________________________________________________________KATA 18__________________________________________________________________________________________

La funcion recibe una lista de diccionarios con informacion de estudiantes (nombre, edad, calificacion).
Usa filter() con lambda e: e.get("calificacion", 0) >= 90 para quedarse solo con los que tienen nota igual o superior a 90.
Primero verifica que todos los elementos sean diccionarios.
Las pruebas incluyen casos normales, con calificaciones varias, y un caso de error con un elemento que no es diccionario.

____________________________________________________________________________________________KATA 19__________________________________________________________________________________________

La funcion recibe una lista de numeros y devuelve solo los impares.
Uso una lambda lambda x: x % 2 != 0 junto con filter() para quedarme con los numeros que no son divisibles por 2.
Controlo que todos los elementos sean enteros.
Las pruebas incluyen listas mixtas, solo pares, solo impares y una vacia, ademas de un caso de error con un valor no numerico.

____________________________________________________________________________________________KATA 20__________________________________________________________________________________________

La funcion recibe una lista con elementos mezclados (enteros y strings) y devuelve solo los que son enteros.
Uso filter() con lambda e: isinstance(e, int) para quedarme unicamente con los valores de tipo int.
Controlo que el parametro sea una lista antes de aplicar el filtro.
Las pruebas cubren listas mixtas, solo texto, solo numeros, lista vacia y un caso de error con un valor que no es lista.

____________________________________________________________________________________________KATA 21__________________________________________________________________________________________

La funcion recibe un numero y devuelve su cubo utilizando una lambda:
lambda n: n ** 3.
Primero verifica que el valor sea numerico (entero o flotante).
Las pruebas incluyen valores positivos, negativos, cero, decimales y un caso de error con un tipo no numerico.

____________________________________________________________________________________________KATA 22__________________________________________________________________________________________

La funcion recibe una lista de numeros y devuelve el producto total de todos sus elementos.
Usa reduce(lambda x, y: x * y, numeros) para multiplicar acumulativamente cada valor de la lista.
Verifica que todos los elementos sean numericos y que la lista no este vacia.
Las pruebas cubren casos normales, con flotantes y el error cuando la lista esta vacia.

____________________________________________________________________________________________KATA 23__________________________________________________________________________________________

La funcion recibe una lista de palabras y devuelve una sola cadena con todas concatenadas.
Usa reduce(lambda x, y: x + y, palabras) para unir cada palabra de la lista.
Verifica que todos los elementos sean strings y que la lista no este vacia.
Las pruebas incluyen listas normales y una prueba de error con lista vacia.

____________________________________________________________________________________________KATA 24__________________________________________________________________________________________

La funcion recibe una lista de numeros y calcula la diferencia total de izquierda a derecha.
Usa reduce(lambda x, y: x - y, numeros) para restar cada elemento sucesivo.
Primero valida que todos los valores sean numericos y que la lista no este vacia.
Las pruebas incluyen listas de enteros, flotantes y una prueba de error con lista vacia.

____________________________________________________________________________________________KATA 25__________________________________________________________________________________________

La funcion recibe una cadena y devuelve la cantidad total de caracteres usando len().
Controlo que el parametro sea un str antes de contar.
Las pruebas incluyen cadenas normales, vacias, con espacios y un caso de error cuando el parametro no es texto.

____________________________________________________________________________________________KATA 26__________________________________________________________________________________________

La funcion recibe dos numeros y devuelve el resto de su division usando una lambda:
lambda x, y: x % y.
Primero verifica que ambos parametros sean numericos y que el divisor no sea cero.
Las pruebas incluyen divisiones exactas, con decimales y un caso de error por division por cero.

____________________________________________________________________________________________KATA 27__________________________________________________________________________________________

La funcion recibe una lista de numeros y devuelve su promedio usando sum(numeros) / len(numeros).
Primero valida que todos los elementos sean numericos y que la lista no este vacia.
Las pruebas incluyen listas normales, con flotantes y una prueba de error cuando la lista esta vacia.

____________________________________________________________________________________________KATA 28__________________________________________________________________________________________

La funcion recorre la lista y guarda los elementos vistos en un conjunto.
Cada vez que encuentra un elemento que ya estaba en el conjunto, lo devuelve como el primer duplicado.
Si no hay duplicados, devuelve None.
Tambien valida que el parametro sea una lista antes de procesar.
Las pruebas incluyen listas con duplicados, sin duplicados, vacias y un caso de error con un parametro no valido.
