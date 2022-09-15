#
#--------------------------Ejercicio 7----------------------------------
#
#Escribí un programa que muestre los primeros 10 números de la sucesión
#de Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de
#éstos, cada elemento es la suma de los dos números anteriores en 
#la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
#
#-----------------------------------------------------------------------
#

n1 = 0
n2 = 1

print(n1)
print (n2)
for x in range(8):
	n3 = n1 + n2
	print (n3)
	n1 = n2
	n2 = n3
#es simple de entender, primero imprimimos n1 y n2 originales. 
#Despues se comenzará a repetir un bucle, donde ambos valores se suman
#en n3. Seguidamente el valor n1 toma el valor de n2 y n2 toma el
#valor de n3.
