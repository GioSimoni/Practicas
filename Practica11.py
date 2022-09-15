#
#--------------------------Ejercicio 11---------------------------------
#
#Desarrollar un programa que pida al usuario una unidad de medida de 
#temperatura. Seguido a esto, debe ingresar un valor de temperatura 
#para luego pasar de temperatura a la que el usuario desee. Debe 
#recordar que:
#	-°C a °F = (°C * 9/5) + 32
#	-°C a K = °C + 273
#	-°F a °C = (°F - 32 ) * 5/9 
#	-°F a K = [(°F - 32) * 5/9] + 273
#	- K a °C = K - 273
#	- K a °F = [(K -273) * 9/5] +32
#
#-----------------------------------------------------------------------
#
print("\n----------------------------")
print(" Conversión de Temperaturas")
print("----------------------------\n")
print("Ingrese su unidad de medida: ")
print("(Solo puede ser C, F o K)")
x = str(input("Medida: "))
med = x.upper()
print("\n Ahora ingrese su valor de temperatura: ")
temp = float(input("Valor: "))

if med == "C":
	y = str(input("Ingrese a que temperatura desea pasar: "))
	nmed = y.upper()
	if nmed == "K":
		print("Su nueva temperatura es: ",temp+273," K.")
	elif nmed == "F":
		print("Su nueva temperatura es: ",(temp*9/5)+32," °F.")
	else:
		print("seleccionó la misma temperatura o escribió otra cosa.")
elif med == "F":
	y = input("Ingrese a que temperatura desea pasar: ")
	nmed = y.upper()
	if nmed == "K":
		print("Su nueva temperatura es: ",((temp-32)*5/9)+273," K.")
	elif nmed == "C":
		print("Su nueva temperatura es: ",(temp-32)*5/9," °C.")
	else:
		print("seleccionó la misma temperatura o escribió otra cosa.")
elif med == "K":
	y = input("Ingrese a que temperatura desea pasar: ")
	nmed = y.upper()
	if nmed == "C":
		print("Su nueva temperatura es: ",temp-273," °C.")
	elif nmed == "F":
		print("Su nueva temperatura es: ",((temp-273)*9/5)+32," °F.")
	else:
		print("seleccionó la misma temperatura o escribió otra cosa.")
else:
	print("Intente de nuevo, escribio otra cosa.")
