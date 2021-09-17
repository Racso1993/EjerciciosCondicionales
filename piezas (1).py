#Ejercicio 8 - Piezas
piezas = int(input("Digita la cantidad de piezas: #"))
precio = int(input("escribe el costo por pieza: $"))
total = piezas * precio
if total > 500000:
    i = total * 0.55
    p = total * 0.30
    c = total * 0.15
else:
    i = total * 0.70
    p = 0
    c = total * 0.30
print(f"La suma total a invertir es de: ${i}")
print(f"La suma total del prestamo es de: ${p}")
print(f"La suma total del credito es de: ${c}")
print(f"El interes total es: ${i}")