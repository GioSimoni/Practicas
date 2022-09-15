#
#--------------------------Ejercicio 15---------------------------------
#
#Las consignas están en el documento, es demasiado largo para ponerlo.
#Revisar de ser necesario.
#
#-----------------------------------------------------------------------
#
x = str(input("Para comenzar, precione S: ")).upper()
while x == "S":
	nombre = str(input("\nPor favor, ingrese su nombre: "))
	clave = int(input("\nPor favor, ahora ingrese su clave de departamento: "))
	años = int(input("\nPor favor, indique cuantos años tiene de antiguedad, si todavia no tiene un año, introduzca 0: "))
#------------------------------Sector_1---------------------------------
	if clave == 1:
		if años > 7:
			print(nombre," le corresponden 20 dias de vacaciones.")
		elif años <= 7:
			print(nombre," le corresponden 14 dias de vacaciones.")
		elif años <= 2:
			print(nombre," le corresponden 6 dias de vacaciones.")
		elif años <= 1:
			print(nombre,"todavia no le corresponden vacaciones.")
		x = str(input("\nSi desea continuar, precione S: ")).upper()
#------------------------------Sector_2---------------------------------
	elif clave == 2:
		if años > 7:
			print(nombre," le corresponden 22 dias de vacaciones.")
		elif años <= 7:
			print(nombre," le corresponden 15 dias de vacaciones.")
		elif años <= 2:
			print(nombre," le corresponden 7 dias de vacaciones.")
		elif años <= 1:
			print(nombre,"todavia no le corresponden vacaciones.")
		x = str(input("\nSi desea continuar, precione S: ")).upper()
#------------------------------Sector_3---------------------------------
	elif clave == 3:
		if años > 7:
			print(nombre," le corresponden 30 dias de vacaciones.")
		elif años <= 7:
			print(nombre," le corresponden 20 dias de vacaciones.")
		elif años <= 2:
			print(nombre," le corresponden 10 dias de vacaciones.")
		elif años <= 1:
			print(nombre,"todavia no le corresponden vacaciones.")
		x = str(input("\nSi desea continuar, precione S: ")).upper()
	else:
		print("Ingresó una clave incorrecta de departamento, intentelo nuevamente.")
		x = str(input("\nSi desea continuar, precione S: ")).upper()
