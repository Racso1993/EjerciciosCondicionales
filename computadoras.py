#Ejercicio 6 - Computadoras
computers = int(input("Digite la suma de computadoras compradas: "))
precio = computers * 11000
if computers < 5:
    descuento = precio * 0.10
if computers <10:
    descuento = precio * 0.20
else:
    descuento = precio * 0.40
print(f"El monto a pagar por la suma de computadoras es de: ${precio-descuento}")
print(f"El descuento es de: ${descuento}")