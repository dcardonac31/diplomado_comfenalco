import math
import statistics

print("1.	Crear un algoritmo que le permita al usuario ingresar el nombre de un estudiante y las 4 notas que obtuvo en una materia y el computador le imprima el nombre, la nota definitiva y un mensaje que le indique si “GANA” O “PIERDE”. (LAS NOTAS SON DE 0 A 5.0, GANA SI LA NOTA ES MAYOR O IGUAL A 3.0 Y PIERDE SI ES MENOR A 3.0)")

listNotas = []
nombreEstudiante = input("Nombre estudiante: ")

for item in range(4):
    nota = float(input(f"Nota {item+1}: "))
    listNotas.append(nota)

notaPromedio = statistics.mean(listNotas)

if notaPromedio >= 3.0:    
    print(f"Estudiante: {nombreEstudiante}")
    print(f"Nota promedio: {notaPromedio}")
    print(f"El estudiante gano la materia")
else:
    print(f"Estudiante: {nombreEstudiante}")
    print(f"Nota promedio: {notaPromedio}")
    print(f"El estudiante perdio la materia")


print("2.	Crear un algoritmo que le permita al usuario ingresar 3 números diferentes entre sí y el computador se los muestre en orden ascendente")

numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))
numero3 = int(input("Numero 3: "))

numeroMayor = numero1
numeroMedio = numero1
numeroMenor = numero1

if numero2 > numero1 and numero2 > numero3:
    numeroMayor = numero2
elif numero3 > numero1 and numero3 > numero2:
    numeroMayor = numero3

if numero2 < numero1 and numero2 < numero3:
    numeroMenor = numero2
elif numero3 < numero1 and numero3 < numero2:
    numeroMenor = numero3

if numero2 > numeroMenor and numero2 < numeroMayor:
    numeroMedio = numero2
elif numero3 > numeroMenor and numero3 < numeroMayor:
    numeroMedio = numero3

posicion1 = numeroMenor
posicion2 = numeroMedio
posicion3 = numeroMayor


print("Orden ascendente")
print(posicion1)
print(posicion2)
print(posicion3)

print("3.	Se tiene un código, número de artículos vendidos y el valor del artículo con ese código. Calcule el valor de la compra, teniendo en cuenta lo siguiente: si la compra es de 50 o más artículos se le da al cliente 10% de descuento; si la compra es menor de 50 artículos no se hace descuento. Mostrar el código, el total de la compra y el valor del descuento.")

codigo = int(input("Ingrese codigo de producto: "))
cantidad = int(input("Cantidad articulos vendidos: "))
precioUnitario = float(input("Ingrese valor unitario: "))
valorNeto = precioUnitario * cantidad
descuento = 0
if cantidad >= 50:
    descuento = 0.1

valorTotal = valorNeto - (valorNeto*descuento)

print(f"Codigo: {codigo}")
print(f"Total compra: ${valorTotal}")
print(f"Descuento: {descuento*100} %")


print("4.	Se necesita un programa que diga si una persona es apta para un equipo de baloncesto o no, para que sea apto debe cumplir que si es hombre sea mayor de edad, que mida más de 1.70 mts., que pese menos de 75 kg., o si es mujer que tenga más de 16 años, que mida como mínimo 1.70 y que pese como máximo 60 kg. Se debe leer el nombre, el sexo (F = femenino, M = masculino), la edad, la estatura y el peso.")


sexo = input("Sexo- F = femenino, M = masculino: ")
edad = int(input("Edad: "))
estatura = float(input("Estatura: "))
peso = float(input("Peso: "))
apto = 0
mensaje = "La persona no es apta"

if sexo == 'M' and edad >= 18 and estatura > 1.70 and peso < 75:
    apto = 1
elif sexo == 'F' and edad >= 16 and estatura >= 1.70 and peso <= 60:
    apto = 1

if apto == 1:
    mensaje = "La persona es apta"

print(mensaje)


print("5.	Se tienen el área, el valor del metro cuadrado de una propiedad y la forma de pago de la cuota inicial. Se pide calcular el precio de venta de la propiedad y el valor de la cuota inicial, que sería el 20% del valor del precio de venta. Si la forma de pago es 1, se otorga un descuento del 10% sobre la cuota inicial y si la forma de pago es 2, se le recarga un 8% en el valor de la misma. Mostrar el valor del precio de venta y el de la cuota inicial de la propiedad (solo hay 2 formas de pago).")

area = 52
valorMetroCuadrado = 800000
valorPrecioVenta = area * valorMetroCuadrado
porcCuotaInicial = 0.2
porcDescuento = 0.1
porcRecarga = 0.08
valorCuotaInicial = valorPrecioVenta * porcDescuento
formaPago = int(input("Ingrese forma de pago 1 - 2:"))
aux = 1
if formaPago == 1 or formaPago == 2:
    aux = 0

while aux == 1:
    formaPago = int(input("Ingrese forma de pago 1 - 2:"))
    if formaPago == 1 or formaPago == 2:
        aux = 0

if formaPago == 1:
    valorCuotaInicial = valorCuotaInicial - (valorCuotaInicial*porcDescuento)
elif formaPago == 2:
    valorCuotaInicial = valorCuotaInicial + (valorCuotaInicial*porcRecarga)

print(f"Valor Precio venta: ${valorPrecioVenta}")
print(f"Valor cuota inicial: ${valorCuotaInicial}")


print("6.	Elaborar un programa que le permita a un usuario ingresar el nombre de un trabajador, el número de horas trabajadas y valor hora, se pide que el programa le imprima el salario bruto, las bonificaciones, las deducciones y el salario neto; teniendo en cuenta que las bonificaciones serán de $20.000 si trabajó como máximo 48 horas, de $50.000 si trabajo entre 49 y 58 horas y de $100.000 si trabajó más de 58 horas. Las deducciones son de $10.000 si el salario básico hora es menor de $5.000, de $20.000 si el salario básico hora es mayor de $5.000 y menor de $8.000 y de $ 50.000 si su salario básico hora es de $8.000 o más.")


nombre = input("Nombre empleado: ")
horasTrabajadas = int(input("Horas trabajadas: "))
valorHora = float(input("Valor hora: $"))
bonificaciones = 0
deducciones = 0
salarioNeto = 0


if horasTrabajadas <= 48:
    bonificaciones = 20000
elif horasTrabajadas >= 49 and horasTrabajadas <= 58:
    bonificaciones = 50000
elif horasTrabajadas > 58:
    bonificaciones = 100000

if valorHora <= 5000:
    deducciones = 10000
elif valorHora > 5000 and valorHora < 8000:
    deducciones = 20000
elif valorHora >= 8000:
    deducciones = 50000


salarioNeto = (horasTrabajadas * valorHora) + bonificaciones - deducciones

print(f"Bonificaciones: ${bonificaciones}")
print(f"Deducciones: ${deducciones}")
print(f"Salario Neto: ${salarioNeto}")

print("7.	Para la materia de Destrezas se determinó con los estudiantes que, si la nota del primer quiz era menor que la del segundo, se sustituía la primera nota por la segunda. La tercera y cuarta nota no se modifican. Elabore un algoritmo que le permita al profesor ingresar las 4 notas que obtuvo un alumno y el computador le muestre la nota definitiva y la calificación cualitativa que es: “E” si es mayor o igual a 4.5, “S” si es mayor o igual a 4.0 y menor de 4.5, “B” si es mayor o igual a 3.5 y menor de 4.0, “A” si es mayor o igual a 3.0  y menor de 3.5, “D” si es mayor o igual a 2.0 y menor de 3.0  “I” si es menor de 2.0.")

listNotas = []
nombreEstudiante = input("Nombre estudiante: ")
calificacionCualitativa = ''

for item in range(4):
    nota = float(input(f"Nota {item+1}: "))
    while nota > 5:
        nota = float(input(f"Nota {item+1}: "))
    listNotas.append(nota)

if listNotas[0] < listNotas[1]:
    listNotas[0] = listNotas[1]

for item in range(4):
    print(f"Nota{item}: {listNotas[item]}")

notaDefinitiva = statistics.mean(listNotas)

print(f"Nota definitiva: {notaDefinitiva}")

if notaDefinitiva >= 4.5:
    calificacionCualitativa = 'E'
elif notaDefinitiva >= 4.0 and notaDefinitiva < 4.5:
    calificacionCualitativa = 'S'
elif notaDefinitiva >= 3.5 and notaDefinitiva < 4:
    calificacionCualitativa = 'B'
elif notaDefinitiva >= 3.0 and notaDefinitiva < 3.5:
    calificacionCualitativa = 'A'
elif notaDefinitiva >= 2.0 and notaDefinitiva < 3.0:
    calificacionCualitativa = 'D'
else:
    calificacionCualitativa = 'I'

print(f"Calificación cualitativa: {calificacionCualitativa}")