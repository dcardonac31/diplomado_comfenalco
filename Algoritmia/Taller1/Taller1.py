# 1)	Crear un algoritmo que lea el nombre de un usuario y lo imprima.
print("=====================================")
print("Ejercicio 1")
nombre_usuario = str(input("Nombre usuario: "))
print("Nombre usuario: "+nombre_usuario)
print("=====================================")

# 2)	Crear un algoritmo que le pida al usuario 3 números, calcular la suma de los 3 números e imprimir el resultado.
print("=====================================")
print("Ejercicio 2")
n_1 = int(input("Numero 1: "))
n_2 = int(input("Numero 2: "))
n_3 = int(input("Numero 3: "))
suma = n_1+n_2+n_3
print("La suma de los 3 numeros es: "+str(suma))
print("=====================================")
# 3)	Crear un algoritmo que permita leer la edad y peso de una persona y posteriormente imprimirla.
print("=====================================")
print("Ejercicio 3")
edad = int(input("Ingrese Edad: "))
peso = float(input("Ingrese Peso: "))
print("La edad: "+str(edad))
print("El peso: "+str(peso))
print("=====================================")

# 4)	Crear un algoritmo que calcule cuantos meses de embarazo tiene una mujer, pedir como dato de entrada las semanas de embarazo.
print("=====================================")
print("Ejercicio 4")
cant_semanas = int(input("Ingrese cantidad semanas: "))
meses_embarazo = cant_semanas/4 
print("Cantidad meses embarazo: "+str(meses_embarazo))
print("=====================================")


# 5)	Crear un algoritmo que calculo el precio total a pagar para un usuario del metro que desea recargar la cívica, el usuario solo ingresa el número de viajes que quiere comprar, se le debe decir cuánto le cuesta. Suponga que el viaje vale $2.200
print("=====================================")
print("Ejercicio 5")
valor_viaje = 2200
cant_viajes = int(input("Ingrese cantidad viajes: "))
precio_total = cant_viajes * valor_viaje
print("Precio total: $"+str(precio_total))
print("=====================================")
