#Ejercicio 7 - Estereos
marcaequipos = input("escriba la marca del equipo: ")
precio = int(input("escibe el costo del producto: $"))
if precio >= 2000:
    total = precio - (precio * 0.10)
else:
    total = precio + (precio * 0.16)
if (marcaequipos == "NOSY"):
    total = total - (precio * 0.05)
print(f"El costo definitivo del producto es de: ${total}")