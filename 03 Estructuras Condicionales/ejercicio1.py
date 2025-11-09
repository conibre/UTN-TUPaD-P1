edad = int (input("Por favor, ingresa tu edad: "))
if edad < 0:
    print("La edad no puede ser negativa.")
elif edad < 18:
    print("Eres menor de edad.")
elif edad >= 18:
    print("Eres mayor de edad.")
