# 1)	Se requiere conocer el área de un rectángulo. Realice un algoritmo para tal fin
#             El área del rectángulo se halla así: (base*altura)
print("=====================================")
print("Ejercicio 1")
base = int(input("Valor base: "))
altura = int(input("Valor altura: "))
area_rectangulo = base*altura
print("El valor de la altura es: "+str(area_rectangulo))
print("=====================================")

# 2)	Se requiere obtener el área de una circunferencia. Realizar el algoritmo correspondiente
#              El área de la circunferencia se halla así: PI * R *R
#              RECUERDE QUE PI=3.1416
print("=====================================")
print("Ejercicio 2")
pi = 3.1415926535897932384626433832795
radio = float(input("Valor radio: "))
area_circunferencia = pi * (radio**2)
print("El valor de área es: "+str(area_circunferencia))
print("=====================================")

# 3)	De un triángulo se tiene la longitud de la base y la longitud de la altura. Determine el valor de su área.
#              El área del triángulo se halla así: (base*altura) /2
print("=====================================")
print("Ejercicio 3")
base = float(input("Valor base: "))
altura = float(input("Valor altura: "))
area_triangulo = (base*altura)/2
print("El valor de área es: "+str(area_triangulo))
print("=====================================")

# 4)	Una modista, para realizar sus prendas de vestir, encarga las telas al extranjero. Para cada pedido, tiene que proporcionar las medidas de la tela en pulgadas, pero ella generalmente las tiene en metros. Realice un algoritmo para ayudar a resolver el problema, determinando cuantas pulgadas debe pedir con base en los metros que requiere. (1 pulgada = 0.0254 m).
print("=====================================")
print("Ejercicio 4")
cant_metros = float(input("Ingrese cantidad metros: "))
cant_pulgadas = cant_metros/0.0254 
print("La cantidad de pulgadas requerida: "+str(cant_pulgadas))
print("=====================================")

# 5)	Un estacionamiento requiere determinar el cobro que debe aplicar a las personas que lo utilizan. Considere que el cobro es con base en las horas Realizar el algoritmo que permita determinar el cobro.
print("=====================================")
print("Ejercicio 5")
valor_hora = float(input("Ingrese valor hora: "))
cant_hora = float(input("Ingrese cantidad horas: "))
cant_hora = cant_hora * valor_hora 
print("Valor parqueo: $"+str(cant_hora))
print("=====================================")


# 6)	Un amigo suyo acaba de iniciar un negocio de venta de zapatos. Por ahora sólo vende tres tipos de zapatos: sandalias con un valor de $100, tenis con un valor de $200 y mocasines con un valor de $300. Cuando un cliente llega le dice la cantidad que desee de cada uno de ellos . El cliente tiene derecho a un 8% de descuento sobre la compra que realiza. Ayúdele a su amigo a crear un programa que, para un cliente dado, muestre su nombre, el valor de la venta sin descuento, el descuento, valor de la venta con descuento y valor de la venta incluyendo IVA (venta neta final)
print("=====================================")
print("Ejercicio 6")
precio_sandalias = 100.0
precio_tenis = 200.0
precio_mocasines = 300.0
porcentaje_descuento = 0.08
porcentaje_iva = 0.19
nombre_cliente = str(input("Ingrese nombre cliente: "))
cant_sandalias = float(input("Ingrese cantidad sandalias: "))
cant_tenis = float(input("Ingrese cantidad tenis: "))
cant_mocasines = float(input("Ingrese cantidad mocasines: "))
valor_sandalias = precio_sandalias * cant_sandalias
valor_tenis = precio_tenis * cant_tenis
valor_mocasines = precio_mocasines * cant_mocasines
valor_venta_sin_descuento = valor_sandalias + valor_tenis + valor_mocasines
valor_descuento = valor_venta_sin_descuento * porcentaje_descuento
valor_venta_con_descuento = valor_venta_sin_descuento + valor_descuento
venta_neta = valor_venta_con_descuento + (valor_venta_con_descuento * porcentaje_descuento)
print("Nombre cliente: "+nombre_cliente)
print("Valor venta sin descuento: $"+str(valor_venta_sin_descuento))
print("Valor descuento: $"+str(valor_descuento))
print("valor venta con descuento: $"+str(valor_venta_con_descuento))
print("valor venta neto: "+str(venta_neta))
print("=====================================")

# 7)	Un productor de leche lleva el registro de lo que produce en litros, pero cuando entrega le pagan en galones. Realice un algoritmo que ayude al productor a saber cuánto recibirá por la entrega de su producción de un día (1 galón = 3.785 litros).
print("=====================================")
print("Ejercicio 7")
cant_litros = float(input("Ingrese cantidad litros: "))
valor_galon = float(input("Ingrese valor galon: "))
cant_galones = cant_litros/3.785
valor_a_pagar = cant_galones * valor_galon  
print("Valor a pagar: "+str(valor_a_pagar))
print("=====================================")

# 8)	La compañía de autobuses “La curva loca” requiere determinar el costo que tendrá el boleto de un viaje sencillo, esto basado en los kilómetros por recorrer y en el costo por kilómetro.
print("=====================================")
print("Ejercicio 8")
cant_kilometros = float(input("Ingrese cantidad kilometros: "))
costo_kilometros = float(input("Ingrese costos por kilometro: "))
valor_boleto = cant_kilometros * costo_kilometros  
print("Valor a pagar: $"+str(valor_boleto))
print("=====================================")


# 9)	Se requiere determinar el tiempo que tarda una persona en llegar de una ciudad a otra en bicicleta teniendo como datos los kilómetros a recorrer y la velocidad en km, considerando que lleva una velocidad constante.
print("=====================================")
print("Ejercicio 9")
cant_kilometros = float(input("Ingrese cantidad kilometros: "))
valor_velocidad = float(input("Ingrese valor velocidad km/h: "))
tiempo_recorrido = cant_kilometros/valor_velocidad
print("Tiempo recorrido: "+str(tiempo_recorrido))
print("=====================================")

# 10)	Se requiere determinar el costo que tendrá realizar una llamada telefónica con base en el tiempo que dura la llamada y en el costo por minuto
print("=====================================")
print("Ejercicio 10")
cant_minutos = float(input("Ingrese cantidad minutos llamada: "))
costo_minuto = float(input("Ingrese costo minuto: "))
valor_llamada = cant_minutos * costo_minuto  
print("Valor llamada: $"+str(valor_llamada))
print("=====================================")
