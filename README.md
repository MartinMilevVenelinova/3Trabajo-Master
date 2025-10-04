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
