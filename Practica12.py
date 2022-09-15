#
#--------------------------Ejercicio 12---------------------------------
#
#Crea un programa que incluya una función inversa() que calcule la 
#inversión de una cadena. Por ejemplo la cadena "estoy probando" debería
#devolver la cadena "odnaborp yotse". El programa debe ejecutarse tantas
#veces como el usuario lo desee.
#
#-----------------------------------------------------------------------
#
def inversa(cadena):
	nueva = ""
	i = len(cadena)-1
	while i >= 0:
		nueva = nueva + cadena[i]
		i = i-1
	print("Su cadena invertida es: ",nueva)

x = str(input("Precione S para comenzar: "))
upx = x.upper()
while upx == "S":
	cadena = str(input("\n Por favor, ingrese una frase o palabra que desee invertir: "))
	inversa(cadena)
	x = input("Precione S para volver a ejecutar el programa: ")
	upx = x.upper()
