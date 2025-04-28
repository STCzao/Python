#TIPOS DE DATOS

#En Python, existen los siguientes tipos de datos: Enteros y largos, flotantes, numeros complejos, cadenas y booleanos

#Los numeros enteros, son aquellos que no tienen decimales, tanto positivos como negativos. En Python se pueden representar mediante el tipo int (entero) o el tipo long (largo)

numero = 15
print (numero, type(numero))

#Los numeros flotantes o reales, son los que tienen decimales, tanto positivos como negativos. En Python se expresan mediante el float

numero_flotante = 15.5
print (numero_flotante, type(numero_flotante))

#Los numeros complejos, son aquellos que tienen una parte real y una parte imaginaria. La mayor parte de lenguajes de programacion carecen de este tipo, aunque sea muy utilizado por ingenieros  cientificos en general. En Python se expresan mediante el tipo complex

numero_complejo = 5 + 6j
print (numero_complejo, type(numero_complejo))

#Las cadenas o tambien conocidas como Strings, mismas que ya hemos estudiado anteriormente, no son mas que texto encerrado entre comilas simples ('cadena') o dobles ("cadena"). Tambien es posible encerrar una cadena entre triples comillas (simples o dobles). De esta forma podremos escribir el texto en varias lieas, y al imprimir la cadena, se respetaran los saltos en linea que introdujimos sin tener que recurrir al caracter \n

nombre = "Santiago"
print (nombre, type(nombre))

#El tipo booleano, solo puede tener dos valores: True (cierto) y False (falso). Estos valores son especialmente importantes para las expresiones condiciones y los bucles, mismos que ya estudiaremos en videos posteriores. En Python se expresan mediante el tipo bool

verdadero_falso = 3 == 3
print (verdadero_falso, type(verdadero_falso))
