print("Ejercicio 9")
clave = int(0)
intentos = int(0)

while True:
    clave = int(input("Dame la clave: "))
    intentos = intentos + 1

    if clave == 352 or clave == 259 or clave == 569 or intentos == 4:

        if intentos == 4:
            print("Demasiados Intentos.")

        elif clave == 352 or clave == 259 or clave == 569:
            print("Clave Correcta.")

        break
    
