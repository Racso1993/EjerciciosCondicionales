#Ejercicio 5 - Auto Terreno
autoterreno = int(input("Digite el monto total del auto y el terreno: $"))
incremento = int(input("Digite el incremento anual del terreno: %"))
decremento = int(input("Digite la devaluacion anual del auto: %"))
x = (((autoterreno* incremento)/100)*3)/2
decremento = ((autoterreno * decremento)/100)*3
print(f"La mitad del incremento por 3 años del terreno es: ${incremento}")
print(f"La devaluacion del auto en 3 años es de: ${decremento}")
if decremento < incremento:
    print("Es provechoso comprar el auto")
else:
    print("Es provechoso comprar el terreno")