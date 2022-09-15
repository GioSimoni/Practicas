#
#--------------------------Ejercicio 9----------------------------------
#
#Escribí un programa que, dado un número entero positivo, calcule y 
#muestre su factorial. El factorial de un número se obtiene 
#multiplicando todos los números enteros positivos que hay entre el 1 y
#ese número. El factorial de 0 es 1. El factorial debe ser una función.
#
#-----------------------------------------------------------------------
#
def factor(num):
	if num == 1:
		return 1
	else:
		return (num * factor(num-1))
num = int(input("Ingrese un numero para saber su factorial: "))
print("El factorial de ",num," es ",factor(num))
