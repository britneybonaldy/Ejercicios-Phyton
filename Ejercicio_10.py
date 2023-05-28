print("Ejercicio 10\n")
contador = int(0)
positivos = int(0)
numero = int(0)

for cotador in range(1, 11):
    numero = int(input("Dame un numero: "))

    if numero > 0:
        positivos = positivos + 1

print("Has Introducido", positivos, "numeros mayores de cero")
print("Fin.")
