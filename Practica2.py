#
#--------------------------Ejercicio 2----------------------------------
#
#El programa debe pedir un número y analizar si es par o impar. 
#Tambien, debe analizar si el número es positivo o negativo e imprimir 
#un mensaje que diga ambas cosas.
#Adicionalmente le proponemos que ambas cosas las haga en una funcion
#definida por ustedes.
#
#-----------------------------------------------------------------------
#
def paridad(num):
	if (num % 2) == 0:
		print("El numero es par")
	else:
		print("El numero es impar")
def positividad(num):
	if num < 0:
		print("El numero es negativo")
	elif num > 0:
		print("El numero es positivo")
num = int(input("ingrese un numero para iniciar:"))
paridad(num)
positividad(num)
