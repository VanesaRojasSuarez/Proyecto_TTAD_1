import json
with open("data.json", "r") as file:
    data = json.load(file)
    


#Ejercicio 1: Total Facturado

total = 0
for venta in data["ventas"]:
    importe = venta["cantidad"] * venta["precio_unitario"]
    total = total + importe
    
print("Total facturado:", total)

#Ejercicio 2: Ventas por categoría

ventas_categoria = {}
for venta in data["ventas"]:
    categoria = venta["categoria"]
    importe = venta["cantidad"] * venta["precio_unitario"]
    
    if categoria not in ventas_categoria:
        ventas_categoria[categoria] = 0
        
    ventas_categoria[categoria] = ventas_categoria[categoria] + importe
    
print("ventas por categoria:", ventas_categoria)


#Ejercicio 3. Producto más vendido

ventas_producto = {}

for venta in data["ventas"]:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    
    if producto not in ventas_producto:
        ventas_producto[producto] = 0
        
    ventas_producto[producto] = ventas_producto[producto] + cantidad

producto_mas_vendido = ""
max_cantidad = 0

for producto in ventas_producto:
    if ventas_producto[producto] > max_cantidad:
        max_cantidad = ventas_producto[producto]
        producto_mas_vendido = producto
        
print("producto más vendido:", producto_mas_vendido)
print("unidades vendidas:", max_cantidad)

