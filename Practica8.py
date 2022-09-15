#
#--------------------------Ejercicio 8----------------------------------
#
#Necesitamos un programa que pida a un entrenador cuantos corredores está
#preparando y le pida para cada uno de los corredores, la distancia que
#pueden correr y los clasifique:
#Si pueden correr menos de 5000 metros, no están aptos para la carrera.
#Si pueden correr entre 5000 y 10000 mts, entran en categoría A.
#Si pueden correr entre 10000 y 15000 mts, entran en categoría B.
#Si pueden correr más de 15000 mts, entran en categoría C.
#Adicionalmente, al final del programa debe indicar cuántos corredores 
#hay en cada categoría.
#
#-----------------------------------------------------------------------
#
corredores = int(input("Por favot, indique el numero de corredores que está preparando: "))
a = 0
b = 0
c = 0

for i in range(corredores):
	print("Corredor ",i+1,": ")
	x = int(input("Indique cual es la disancia recorrida por el corredor: "))
	if x >= 15000:
		print("El jugador pertenece a la categoria C")
		c += 1
	elif x >= 10000:
		print("El jugador pertenece a la categoria B")
		b += 1
	elif x >= 5000:
		print("El jugador pertenece a la categoria A")
		a += 1
	else:
		print("El corredor no está calificado para correr.")
print("Tiene ",a," jugador/es en la categoria A.")
print("Tiene ",b," jugador/es en la categoria B.")
print("Tiene ",c," jugador/es en la categoria C")
