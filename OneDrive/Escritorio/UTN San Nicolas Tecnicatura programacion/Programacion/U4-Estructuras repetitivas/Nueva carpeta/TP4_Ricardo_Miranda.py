
# TP 4 - Estructuras Repetitivas

# Ejercicio 1: Números del 0 al 100 en orden creciente
for i in range(101):
    print(i)

# Ejercicio 2: Contar dígitos de un número
numero = input("\nEjercicio 2 - Ingrese un número entero: ")
print(f"Cantidad de dígitos: {len(numero)}")

# Ejercicio 3: Sumar enteros entre dos valores (excluyendo los extremos)
a = int(input("\nEjercicio 3 - Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))
inicio = min(a, b) + 1
fin = max(a, b)
suma = sum(range(inicio, fin))
print(f"La suma es: {suma}")

# Ejercicio 4: Sumar números hasta ingresar 0 (sin break)
numero = -1
total = 0
while numero != 0:
    numero = int(input("\nEjercicio 4 - Ingrese un número (0 para terminar): "))
    total += numero
print(f"Total acumulado: {total}")

# Ejercicio 5: Juego de adivinar un número (sin break)
import random
numero_secreto = random.randint(0, 9)
intento = -1
intentos = 0
while intento != numero_secreto:
    intento = int(input("\nEjercicio 5 - Adivine el número entre 0 y 9: "))
    intentos += 1
print(f"¡Correcto! Lo adivinaste en {intentos} intentos.")

# Ejercicio 6: Números pares del 100 al 0 en orden decreciente
print("\nEjercicio 6 - Números pares del 100 al 0:")
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# Ejercicio 7: Suma desde 0 hasta un número dado
n = int(input("\nEjercicio 7 - Ingrese un número entero positivo: "))
suma = sum(range(n + 1))
print(f"La suma es: {suma}")

# Ejercicio 8: Ingresar 100 números y clasificar
pares = impares = positivos = negativos = 0
print("\nEjercicio 8 - Ingrese 100 números:")
for i in range(100):
    num = int(input(f"Ingrese el número {i+1}: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")

# Ejercicio 9: Media de 100 números
suma = 0
print("\nEjercicio 9 - Ingrese 100 números para calcular la media:")
for i in range(100):
    num = int(input(f"Ingrese el número {i+1}: "))
    suma += num
media = suma / 100
print(f"La media es: {media}")

# Ejercicio 10: Invertir los dígitos de un número
numero = input("\nEjercicio 10 - Ingrese un número para invertir: ")
invertido = numero[::-1]
print(f"Número invertido: {invertido}")
