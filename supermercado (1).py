#Ejercicio 2 - Supermercado
precio = int(input("Escribe el valor total de la compra: "))
numeroescogido = int(input("Digita el numero que escogio: "))
if numeroescogido >= 74:
    total = precio * 0.20
else:
    total = precio * 0.15
print(f"El descuento a favor es: ${total}")
print(f"El total por pagar incluyendo el descuento es: ${precio-total}")