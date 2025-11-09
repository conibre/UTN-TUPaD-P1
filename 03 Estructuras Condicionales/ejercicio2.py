nota = int (input("Ingrese su nota (0-10): "))
if nota <=0: 
    print("La nota no puede ser negativa.")
elif nota >= 6: 
    print("Aprobado.")
else:
    print("Desaprobado.")    