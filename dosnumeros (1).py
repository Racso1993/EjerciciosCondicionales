#Ejercicio 9 - Dos numeros
primero = float(input("Escribe el primer numero: "))
segundo = float(input("Escribe el segundo numero: "))
if primero == segundo:
    mayor = (primero * segundo)
    print(f"La respuesta es: {mayor}")
elif primero > segundo:
    resultado = (primero - segundo)
    print(f"La respuesta es: {mayor}")
elif segundo > primero:
    resultado = (primero + segundo)
    print(f"El resultado de la operacion es: {mayor}")