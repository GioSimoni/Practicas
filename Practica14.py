#
#--------------------------Ejercicio 14---------------------------------
#
#Escribí un programa que permita al usuario ingresar los montos de las 
#compras de un cliente (se desconoce la cantidad de datos que cargará,
#la cual puede cambiar en cada ejecución), cortando el ingreso de datos
#cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, no
#se debe procesar y se debe pedir que ingrese un nuevo monto. Al 
#finalizar, informar el total a pagar teniendo que cuenta que, si las
#ventas superan el monto total de 1000, se le debe aplicar un 10% 
#de descuento.
#-----------------------------------------------------------------------
#
def compras(precio):
	valor = float(input("Ingrese el valor de su compra:"))
	while valor != 0:
		precio.append(valor)
		if valor < 0:
			print("El valor ingresado es negativo, intente de nuevo.")
		valor = float(input("Ingrese el valor de su compra:"))
nombre = str(input("Por favor, ingrese su nombre: "))
print("\n",nombre," ingrese los valores de sus compras, para finalizar la lista, precione 0.\n")
precio =[]
compras(precio)
print("La suma total de gastos es de: ",sum(precio))
if sum(precio)>1000:
	print("Su monto supera los $1000, le aplicamos un descuento del 10%, su monto total es de: ",sum(precio)-sum(precio)*0.1)
