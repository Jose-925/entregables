# Calculadora básica
def calculadora():
    print("Calculadora básica:")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    operacion = input("Elige la operación a realizar(+, -, *, /): ")

    if operacion == "+":
        print(f"Resultado: {num1 + num2}")
    elif operacion == "-":
        print(f"Resultado: {num1 - num2}")
    elif operacion == "*":
        print(f"Resultado: {num1 * num2}")
    elif operacion == "/":
        if num2 != 0:
            print(f"Resultado: {num1 / num2}")
        else:
            print("Error: Estas realizando una división por cero.")
    else:
        print("Operación no válida.")

calculadora()

# Juego adivinanza
import random
numero_aleatorio = random.randint(1, 100)
adivinanza = -1

while adivinanza != numero_aleatorio:
    adivinanza = int(input("Adivina el número (entre 1 y 100): "))
    if adivinanza < numero_aleatorio:
        print("Mayor...")
    elif adivinanza > numero_aleatorio:
        print("Menor...")
    else:
        print("¡Correcto! Adivinaste el número.")
