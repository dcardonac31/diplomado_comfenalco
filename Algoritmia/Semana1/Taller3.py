# 1)	 La compañía de luz y sombras (CLS) requiere determinar el pago que debe realizar una persona por el consumo de energía eléctrica, la cual se mide en kilowatts (KW).
print("=====================================")
print("Ejercicio 1")
cant_kw = int(input("Cantidad Kilowats: $"))
precio_kw = int(input("Precio Kilowats: $"))
valor_kw = cant_kw * precio_kw
print("Pago consumo energía: $"+str(valor_kw))
print("=====================================")


# 2)	 Determinar cuánto pagará finalmente una persona por un artículo equis, considerando que tiene un descuento de 20%, y debe pagar 19% de IVA (debe mostrar el precio solo con el iva y el precio final, el descuento se aplica una vez el producto tenga el iva aplicado).
print("=====================================")
print("Ejercicio 2")
porc_iva = 0.19
porc_descuento = 0.20
precio_producto = float(input("Precio producto: $"))
valor_iva = precio_producto * porc_iva
valor_producto_con_iva = precio_producto + valor_iva
valor_descuento = valor_producto_con_iva * porc_descuento
valor_final =  valor_producto_con_iva - valor_descuento
print("Precio Producto: $"+str(precio_producto))
print("Valor IVA: $"+str(valor_iva))
print("Valor Descuento: $"+str(valor_descuento))
print("Valor Final: $"+str(valor_final))
print("=====================================")

# 3)	 Determinar cuánto dinero ahorra una persona en un año si considera que cada semana ahorra 15% de su sueldo (considere cuatro semanas por mes y que no cambia el sueldo)
print("=====================================")
print("Ejercicio 3")
porc_ahorro = 0.15
valor_sueldo = float(input("Valor sueldo: $"))
valor_ahorro_semana = valor_sueldo * porc_ahorro
valor_ahorro_mes = valor_ahorro_semana * 4
valor_ahorro_anual = valor_ahorro_mes * 12
print("Valor ahorro semana: $"+str(valor_ahorro_semana))
print("Valor ahorro mensual: $"+str(valor_ahorro_mes))
print("Valor ahorro anual: $"+str(valor_ahorro_anual))
print("=====================================")


# 4)	 Una empresa desea determinar el monto de un cheque que debe proporcionar a uno de sus empleados que tendrá que ir por equis número de días a la ciudad de Bogotá; los gastos que cubre la empresa son: hotel, comida y 200.000 pesos diarios para otros gastos. El monto debe estar desglosado para cada concepto (mostrar detalle a detalle y el total)
print("=====================================")
print("Ejercicio 4")
valor_otros_gastos_diario = 200000
valor_hotel_diario = int(input("Valor hotel diario: $"))
valor_alimentacion_diario = int(input("Valor alimentación diario: $"))
cantidad_dias = int(input("Cantidad días: $"))
valor_otros_gastos = valor_otros_gastos_diario * cantidad_dias
valor_hotel = valor_hotel_diario * cantidad_dias
valor_alimentacion = valor_alimentacion_diario * cantidad_dias
valor_cheque = valor_otros_gastos + valor_hotel + valor_alimentacion
print("Valor otros gastos: $"+str(valor_otros_gastos))
print("Valor hotel: $"+str(valor_hotel))
print("Valor alimentación: $"+str(valor_alimentacion))
print("Valor cheque: $"+str(valor_cheque))
print("=====================================")

# 5)	 Realice el algoritmo para determinar el promedio que obtendrá un alumno considerando que realiza tres exámenes, de los cuales el primero y el segundo tienen una ponderación de 25%, mientras que el tercero de 50%.
print("=====================================")
print("Ejercicio 5")
nota_1 = float(input("Nota 1: "))
nota_2 = float(input("Nota 2: "))
nota_3 = float(input("Nota 3: "))
porc_1 = 0.25
porc_2 = 0.25
porc_3 = 0.50
promedio_ponderado = (nota_1 * porc_1) + (nota_2 * porc_2) + (nota_3 * porc_3)
print("Promedio ponderado: "+str(promedio_ponderado))
print("=====================================")



# 6)	 El hotel “Cama Arena” requiere determinar lo que le debe cobrar a un huésped por su estancia en una de sus habitaciones. Realice el algoritmo para determinar ese cobro.
print("=====================================")
print("Ejercicio 6")
cantidad_dias = int(input("Cantidad días hospedaje: "))
precio_dia = 75000
valor_alimentacion = int(input("Valor alimentación: $"))
servicio_habitacion = int(input("Servicio habitación: $"))
costo_hospedaje = (precio_dia * cantidad_dias) + valor_alimentacion + servicio_habitacion
print("Costo hospedaje: "+str(costo_hospedaje))
print("=====================================")
