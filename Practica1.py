#
#--------------------------Ejercicio 1----------------------------------
#
#Pedirle 3 números al usuario, comparar cual de los 3 es el más grande 
#e imprimir un mensaje que diga "el mayor numero es el valor (x)" y nos 
#ponga el valor del número más grande según el caso. Adicionalmente se 
#propone que esto se haga en un programa de menos de 15 líneas de código.
#
#-----------------------------------------------------------------------
#
while True:
numero1 = float(input("Por favor, ingrese el primer valor: "))
numero2 = float(input("Por favor, ingrese el segundo valor: "))
numero3 = float(input("Por favor, ingrese el tercer valor: "))
if numero1 > numero2 and numero1 > numero3:
	print("El mayor numero es el primer valor, ", numero1)
elif numero2 > numero1 and numero2 > numero3:
	print("El mayor numero es el segundo valor, ", numero2)
elif numero3 > numero1 and numero3 > numero2:
	print("El mayor numero es el tercer valor, ", numero3)
elif numero1 == numero2 == numero3:
	print("Los 3 numeros son iguales")
#Tiene 11 lineas, cumple con la condicion adicional.
