#Ejercicio 3 - Compañia
precio = int(input("Digite la suma que desea financiar: $"))
x = int(input("Esciba un numero: $"))
if precio >= 50000:
    total = precio * 0.02
else:
    total = precio * 0.03
print(f"El interes por la suma financiada es: ${total}")
print(f"El total por pagar con interes incluido es: ${precio+total}")
