#
#--------------------------Ejercicio 4----------------------------------
#
#Escribí un programa que, dado un número entero, muestre su valor 
#absoluto. Recordá que, para los números positivos su valor absoluto 
#es igual al número (el valor absoluto de 52 es 52), mientras que, para 
#los negativos, su valor absoluto es el número multiplicado por -1
#(el valor absoluto de -52 es 52).
#
#-----------------------------------------------------------------------
#
num = int(input("Ingrese un numero entero: "))
if num > 0:
	print("el valor absoluto de ",num," es ",num)
elif num < 0:
	print("el valor absoluto de ",num," es ",(num * -1))
else:
	print("el numero es 0")
