#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año :
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#el año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#i el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio = input("Ingrese su hemisferio (N para Norte, S para Sur): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))
if hemisferio == 'N':
    if (mes == 12 and dia >= 21) or (mes <= 3 and (mes < 3 or (mes == 3 and dia < 20))):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 20) or (mes <= 6 and (mes < 6 or (mes == 6 and dia < 21))):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes <= 9 and (mes < 9 or (mes == 9 and dia < 22))):
        estacion = "Verano"
    else:
        estacion = "Otoño"
elif hemisferio == 'S':
    if (mes == 6 and dia >= 21) or (mes <= 9 and (mes < 9 or (mes == 9 and dia < 22))):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 22) or (mes <= 12 and (mes < 12 or (mes == 12 and dia < 21))):
        estacion = "Primavera"
    elif (mes == 12 and dia >= 21) or (mes <= 3 and (mes < 3 or (mes == 3 and dia < 20))):
        estacion = "Verano"
    else:
        estacion = "Otoño"
else:
    estacion = "Hemisferio no válido"   

print(f"Usted se encuentra en: {estacion}.")