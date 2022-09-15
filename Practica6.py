#
#--------------------------Ejercicio 6----------------------------------
#
#Escribí un programa que, dada una frase por el usuario, muestre la 
#cantidad total de vocales (tanto mayúsculas como minúsculas) que 
#contiene.
#
#-----------------------------------------------------------------------
#

frase = input("Ingrese una frase: ")
frase2 = frase.lower()
vocales = "aeiou"
c = 0
for x in frase2:
	if x in vocales:
		c += 1
print("Su frase tiene ",c," vocales.")
