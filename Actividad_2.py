mayor_edad = False

while mayor_edad == False:
    edad = int(input("Ingrese su edad: "))
    if edad < 18:
        print("Aún no tienes edad para ingresar")
    if edad >= 18:
        mayor_edad = True

print("Felicitaciones ya puedes ingresar")
