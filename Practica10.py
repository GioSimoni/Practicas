#
#--------------------------Ejercicio 10---------------------------------
#
#Escribe un programa que solicite la cantidad de números, luego que
#guarde los números en una lista, que elimine el primer y último 
#elemento de la lista y cree una nueva lista con los elementos que no 
#fueron eliminados. 
#Luego, que devuelva la media de la nueva lista que contenga todos los 
#elementos de la lista anterior menos el primero y el último.
#
#-----------------------------------------------------------------------
#
num = []
c = int(input("Por favor, ingrese la cantidad de numeros que quiere agregar a su lista: "))
for i in range(c):
	n = float(input("ingrese un numero: "))
	num.append(n)
print("Su lista es ",num)
num.pop(0) #Elimina el primer valor
num.pop() #Elimina el ultimo valor
print("Su nueva lista es ",num,"\n")
print("La media de la nueva lista es: ", sum(num)/len(num))
