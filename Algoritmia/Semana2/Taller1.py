print(" EJERCICIOS CON DECISIONES LÓGICAS TALLER 1")

print("1.	Elabore un algoritmo que permita averiguar cuál es el nombre del mayor de 2 hermanos no gemelos. Como datos de entrada se tiene el nombre y la edad de las 2 personas.")
nombre1 = input("Nombre hermano 1: ")
edad1 = int(input("Ingrese edad hermano 1: "))
nombre2 = input("Nombre hermano 2: ")
edad2 = int(input("Ingrese edad hermano 2: "))
nombreMayor = nombre1

if edad1 < edad2:
    nombreMayor = nombre2
    
print(f"El hermano mayor es: {nombreMayor}")    
print("---------------------------")

print("2.	Elaborar un algoritmo que muestre un mensaje según la edad ingresada; niño (menor de 10 años), preadolescente (mayor o igual a 10años  y menor o igual a 14 años), un adolescente (mayor o igual a 15 años  y menor o igual a 18 años), adulto (mayor o igual a 19 años y menor o igual a 50 años), adulto mayor (mayor de 50 años).")
edad = int(input("Ingrese edad: "))
categoria = 'niño'
if edad >= 10 and edad < 15:
    categoria = 'preadolescente'
elif edad >= 15 and edad < 19:
    categoria = 'adolescente'
elif edad >= 19 and edad < 50:
    categoria = 'adulto'
elif edad >= 50:
    categoria = 'adulto mayor'

print(f"La persona es: {categoria}")           


print("---------------------------")

print(" 3.	Elabore un algoritmo que lea el nombre, el salario bruto, las deducciones y las bonificaciones de dos trabajadores, e imprima (escriba un mensaje) el nombre del que más salario neto tiene.")

nombre1 = input("Nombre empleado 1: ")
salario1 = float(input("Ingrese salario empleado 1: "))
deducciones1 = float(input("Ingrese deducciones empleado 1: "))
bonificaciones1 = float(input("Ingrese bonificaciones empleado 1: "))
salarioNeto1 = salario1 - deducciones1 + bonificaciones1

nombre2 = input("Nombre empleado 2: ")
salario2 = float(input("Ingrese salario empleado 2: "))
deducciones2 = float(input("Ingrese deducciones empleado 2: "))
bonificaciones2 = float(input("Ingrese bonificaciones empleado 2: "))
salarioNeto2 = salario2 - deducciones2 + bonificaciones2

nombreMayor = nombre1

if salarioNeto1 < salarioNeto2:
    nombreMayor = nombre2
elif salarioNeto1 == salarioNeto2:
    nombreMayor = 'Iguales'

print(f"El empleado con mejor salario es: {nombreMayor}")
print("---------------------------")

print(" 4.	Crear un algoritmo que le permita al usuario ingresar los datos de dos buses así: Placa, El número de pasajeros transportado y el valor del pasaje, y el computador le muestre la placa del bus que más dinero recogió.")

placa1 = input("Placa 1: ")
numeroPasajeros1 = int(input("Ingrese numero pasajeros bus 1: "))
valorPasaje1 = int(input("Ingrese valor pasaje bus 1: "))
recaudoBus1 = numeroPasajeros1 * valorPasaje1

placa2 = input("Placa 2: ")
numeroPasajeros2 = int(input("Ingrese numero pasajeros bus 2: "))
valorPasaje2 = int(input("Ingrese valor pasaje bus 2: "))
recaudoBus2 = numeroPasajeros2 * valorPasaje2

placaMayor = placa1

if recaudoBus1 < recaudoBus2:
    placaMayor = placa2
elif recaudoBus1 == recaudoBus2:
    placaMayor = 'Iguales'

print(f"El bus con mayor recaudo es: {placaMayor}")


print("---------------------------")

print(" 5.	Elaborar un algoritmo donde el usuario ingrese la placa de un bus, el número de pasajeros transportados y la ruta donde prestó el servicio (A o B) el computador le debe mostrar el dinero que recolectó sabiendo que en la ruta A el pasaje es a $1.200 y en la B a $1.000.")

placa = input("Placa: ")
numeroPasajeros = int(input("Ingrese numero pasajeros: "))
ruta = input("Ingrese ruta (A o B): ")

if ruta == 'A':    
    valorPasaje = 1200
else:
    valorPasaje = 1000
recaudoBus = numeroPasajeros * valorPasaje

print(f"Valor recaudo : ${recaudoBus}")

print("---------------------------")

print(" 6.	Crear un algoritmo que le permita al usuario ingresar el tipo de trabajador (FIJO o TEMPORAL) y con base en esto pueda imprimir el nombre y el salario neto, sabiendo que si es FIJO debe leer el nombre, el número de horas trabajadas, el salario básico hora, el total de deducciones y el total de bonificaciones y si es TEMPORAL solo debe leer el nombre y el número de horas trabajadas; estos trabajadores tienen un salario básico hora fijo de $6.000 y no tienen deducciones ni bonificaciones.")

tipoTrabajador = input("ingresar el tipo de trabajador (FIJO o TEMPORAL): ")
while tipoTrabajador != 'FIJO' or tipoTrabajador != 'TEMPORAL':
    tipoTrabajador = input("ingresar el tipo de trabajador (FIJO o TEMPORAL): ")

tipoTrabajador = tipoTrabajador.upper()

if tipoTrabajador == 'FIJO':   
    nombre = input("Nombre empleado : ")
    horasTrabajadas = int(input("Ingrese cantidad de horas trabajadas : "))
    salarioBasicoPorHora = float(input("Ingrese salario basico por hora : $"))
    deducciones = float(input("Ingrese deducciones: $"))
    bonificaciones = float(input("Ingrese bonificaciones empleado : $"))
    salarioNeto = (horasTrabajadas*salarioBasicoPorHora)-deducciones+bonificaciones
else:
    nombre = input("Nombre empleado : ")
    horasTrabajadas = int(input("Ingrese cantidad de horas trabajadas : "))
    salarioBasicoPorHora = 6000
    salarioNeto = (horasTrabajadas*salarioBasicoPorHora)
    
print(f"Salario Neto : ${salarioNeto}")    
print("---------------------------")

print(" 7.	Elaborar Un algoritmo que le permita al usuario leer 3 número diferentes entre sí y el computador le imprima el mayor de ellos.")

numero1 = int(input("Ingrese numero 1: "))
numero2 = int(input("Ingrese numero 1: "))
numero3 = int(input("Ingrese numero 1: "))

numeroMayor = numero1
if numero2 > numero1 and numero2 > numero3:
    numeroMayor = numero2
elif numero3 > numero1 and numero3 > numero2:
    numeroMayor = numero3
    
print(f"Numero mayor: {numeroMayor}")    

print("---------------------------")