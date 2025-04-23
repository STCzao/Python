#CADENAS DE CARACTERES

#Las cadenas de caracteres o mejor conocidos como strings, es una serie de caracteres compuests por letras, numeros , signos y simbolos, que dentro de sus funciones, destaca la interaccion de un programa con el usuario
#En python existen distintas operaciones para manejar una cadena de caracteres (strings). Dentro de las cuales se encuentran:

#La asignacion, consiste en asignar una cadena de caracteres a otra. Para lo cual es necesario utilizar el operador +=

mensaje = "Hola"
mensaje += " "
mensaje += "Santiago"
#Cuando utilizamos el signo += es para que el valor se sobrescriba al final del valor anterior
print(mensaje)

#La concatenacion, es una operacion que consiste en unir dos cadenas o mas, para formar una cadena de mayor tamaño. Para lo cual es necesario utilizar el operador +

print("Concatenacion:")
mensaje = "Hola"
espacio = " "
nombre = "Santiago"
#A cada variable le asignamos un valor y lo concatenamos ya que son el mismo tipo de dato(string)
print(mensaje + espacio + nombre)

numero_uno = 2
numero_dos = 4
resultado = numero_uno + numero_dos 

resultado = str(resultado)
#En este ejemplo utilizamos el metodo str para convertir al valor de la variable resultado que es un entero (int) a un string 
print ("El resultado de la suma es: " + resultado)

#La busqueda, consiste en localizar dentro de una cadena, una subcadena mas pequeña a un caracter. Para lo cual es necesario utilizar el metodo find

print("Busqueda: ")
mensaje = "Hola Santiago"
buscar_subcadena = mensaje.find ("Santiago")
#Con el metodo find buscamos el valor que pasamos como parametro en la variable "mensaje" y nos devuelve la posicion (del string) en la cual se encuentra
print(buscar_subcadena)

#La extraccion, se trata de sacar fuera de una cadena, una porcion de la misma segun su posicion dentro de ella. Para ello es necesario indicar la posicion a extraer [1:8]

mensaje = "Hola Santiago"
extraer_cadena = mensaje[1:8]
print(extraer_cadena)

#La comparacion, se utiliza para comparar dos cadenas de caracteres. Para ello se utiliza el operador == 

print("Comparacion: ")

mensaje_uno = "Hola"
mensaje_dos = "Hola"
#La comparacion se maneja con true y false, si el valor o el tipo de dato no es el mismo, sera incorrecto
print(mensaje_uno == mensaje_dos)