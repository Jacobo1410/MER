#Un algoritmo para calculr el promedio a partir de 5 notas de un estudiante.

#Pedimos las notas al usuario
nota1 = float (input("Ingrese la nota 1: "))
nota2 = float (input("Ingrese la nota 2: "))
nota3 = float (input("Ingrese la nota 3: "))
nota4 = float (input("Ingrese la nota 4: "))
nota5 = float (input("Ingrese la nota 5: "))

resultado = (nota1 + nota2 + nota3 + nota4 + nota5)/5

print ("El promedio de sus notas es de: ", resultado)