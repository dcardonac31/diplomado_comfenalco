from datetime import datetime

# 1)	Crear un algoritmo que escriba/imprima “hola mundo”
print("=====================================")
print("Ejercicio 1")
print("Hola mundo")
print("=====================================")


# 2)	Crear un algoritmo en dónde se declare/cree dos constantes con un valor numérico, sumar los dos números y guardar el resultado de la suma en una variable y escribir/imprimir la variable con el resultado.

print("=====================================")
print("Ejercicio 2")
const_1 = 50
const_2 = 60
suma = const_1 + const_2
print("El valor de la suma de "+str(const_1)+" y "+str(const_2)+" es:"+str(suma))
print("=====================================")



# 3)	Crear un algoritmo en dónde se declare/cree dos constantes con un valor numérico, multiplicar los dos números, guardar el resultado de la multiplicación en una variable y escribir/imprimir la variable con el resultado.
print("=====================================")
print("Ejercicio 3")
const_1 = 5
const_2 = 6
mult = const_1 * const_2
print("El valor de la multiplicación de "+str(const_1)+" y "+str(const_2)+" es:"+str(mult))
print("=====================================")

# 4)	Crear un algoritmo que calcule los años que usted tiene en base a su año de nacimiento, debe crear una constante con un valor numérico (año de su nacimiento) y hacer el cálculo.

print("=====================================")
print("Ejercicio 4")
nacimiento = 1991
fecha_actual = datetime.now()
edad = int(fecha_actual.strftime("%Y")) - nacimiento
print("La edad es :"+str(edad))
print("=====================================")

# 5)	Crear un algoritmo que calcule el promedio de 3 notas (n1=4.3; n2=3.5; n3=2.8)
print("=====================================")
print("Ejercicio 5")
n_1 = 4.3
n_2 = 3.5
n_3 = 2.8
promedio = (n_1+n_2+n_3)/3
print("El promedio de las 3 notas es: "+str(promedio))
print("=====================================")

# 6)	Hacer un programa que convierta los grados centígrados (30 grados) a grados Fahrenheit. La formula es la siguiente: (C*1.8) +32
print("=====================================")
print("Ejercicio 6")
grados_centigrados = 30
grados_farenheit = (grados_centigrados*1.8)+32
print(str(grados_centigrados)+" equivalen a: "+str(grados_farenheit)+" farenheit")
print("=====================================")


# 7)	Pedir un número al usuario y escribirlo/imprimirlo sumándole 10.
print("=====================================")
print("Ejercicio 7")
numero = int(input("Ingresa numero: "))
numero_2 = numero + 10
print(str(numero_2))
print("=====================================")

# 8)	Realizar el mismo programa del punto (6), pero ahora se debe pedir el dato inicial (grados centígrados) al usuario (teclear el dato).

print("=====================================")
print("Ejercicio 8")
grados_centigrados = float(input("Ingresa valor grados centigrados: "))
grados_farenheit = (grados_centigrados*1.8)+32
print(str(grados_centigrados)+" equivalen a: "+str(grados_farenheit)+" farenheit")
print("=====================================")

# 9)	Hacer un algoritmo que calcule el sueldo de un empleado dados como datos de entrada: el nombre, horas trabajadas y el valor de la hora.
print("=====================================")
print("Ejercicio 9")
nombre_empleado = str(input("Ingresa nombre empleado: "))
horas_trabajadas = int(input("Ingresa cantidas horas trabadas: "))
valor_hora = int(input("Ingresa valor hora: "))
sueldo = horas_trabajadas * valor_hora
print("Valor sueldo: $"+str(sueldo))
print("=====================================")

# 10)	Crear un algoritmo que calcule el precio final de un producto, teniendo en cuenta el iva del 19%, el usuario debe ingresar el valor del producto sin iva y el algoritmo debe retornar el valor final
print("=====================================")
print("Ejercicio 10")
iva = 0.19
valor_producto = float(input("Ingresa valor producto: "))
valor_producto_iva = valor_producto + (valor_producto * iva)
print("Valor producto - IVA incluido: $"+ str(valor_producto_iva))
print("=====================================")
