#
#--------------------------Ejercicio 13---------------------------------
#
#Escribí un programa que solicite al usuario el ingreso de un texto y 
#almacena ese texto en una variable. A continuación, mostrar en pantalla
#la primera letra del texto ingresado. Luego, solicitar al usuario que
#ingrese un número positivo menor a la cantidad de caracteres que tiene
#el texto que ingresó (por ejemplo, si escribió la palabra “HOLA”,
#tendrá que ser un número entre 0 y 4) y almacenar este número en una
#variable llamada índice. Mostrar en pantalla el carácter del texto 
#ubicado en la posición dada por índice.
#
#-----------------------------------------------------------------------
#
pal = str(input("Ingrese su palabra/frase: "))
print("La primera letra de su palabra/frase es: ",pal[0],".\n")
print("Ahora ingrese un numero entre 0 y ",(len(pal)-1),": ")
ind = int(input())
print("La letra en ese indice seleccionado es: ",pal[ind])
