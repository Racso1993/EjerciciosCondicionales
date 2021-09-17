# Ejercicio 1 - Camisas.
cantidadcamisas = int(input("Escribe cuantas camisas compraste: "))
precio = int(input("Digite el valor de las camisas que compro: $ "))
if cantidadcamisas >= 3:
    total = precio * 0.30
else:
    total = precio * 0.10
print(f"El total por pagar es: ${precio-total}")
print(f"El descuento a favor es: ${total}")
