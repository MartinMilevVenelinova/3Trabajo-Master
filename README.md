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
