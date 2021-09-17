#Ejercicio 4 - Fabrica
itinerario = int(input("Digite los puntos contaminados de la compañia: $"))
ganancias = int(input("Esciba las ganancias diarias: $"))
if itinerario > 170:
    multa = ganancias * 0.05
else:
    multa = 0
print(f"El balance de puntos contaminados de la compañia es: {itinerario}")
print(f"Las ganacias por semana son: ${ganancias}")
print(f"El deficit por la contaminacion fue de: ${multa}")