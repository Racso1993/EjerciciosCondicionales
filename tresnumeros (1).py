#Ejercicio 10 - Tres numeros
primero = int(input("Escribe el primer numero: "))
segundo = int(input("Escribe el segundo numero: "))
tercero = int(input("Escribe el tercer numero: "))
if primero > segundo and primero > tercero:
    resultado = primero
if segundo > primero and segundo > tercero:
    resultado = segundo
else: 
    resultado = tercero
print(f"El numero mayor es: {resultado}")