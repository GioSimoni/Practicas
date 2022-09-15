#
#--------------------------Ejercicio 16---------------------------------
#
#Las consignas están en el documento, es demasiado largo para ponerlo.
#Revisar de ser necesario.
#
#-----------------------------------------------------------------------
#
def apodes():
	if leng < 6: 
		print("El alumno está desaprobado en Lengua.")
	else:
		print("El alumno está aprobado en Lengua.")
	if mate < 6: 
		print("El alumno está desaprobado en Matematica.")
	else:
		print("El alumno está aprobado en Matematica.")
	if hist < 6: 
		print("El alumno está desaprobado en Historia.")
	else:
		print("El alumno está aprobado en Historia")
	if geo < 6: 
		print("El alumno está desaprobado en Geografia.")
	else:
		print("El alumno está aprobado en Geografia.")
#-----------------------------------------------------------------------
x = str(input("Para comenzar, precione S: ")).upper()
notas = {"Lengua":0,"Matematica":0,"Historia":0,"Geografia":0}
while x == "S":
	alumno = str(input("\nIngrese el nombre del alumno: "))
	leng = float(input("Ingrese la nota en lengua: "))
	mate = float(input("Ingrese la nota en matematica: "))
	hist = float(input("Ingrese la nota en historia: "))
	geo = float(input("Ingrese la nota en geografia: "))
	notas.update({"Lengua":leng,"Matematica":mate,"Historia":hist,"Geografia":geo})
	apodes()
	print("\nEl promedio de ",alumno," es ",sum(notas.values())/4)
	x = str(input("\nSi desea continuar, precione S: ")).upper()
