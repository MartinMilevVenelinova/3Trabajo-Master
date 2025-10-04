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
