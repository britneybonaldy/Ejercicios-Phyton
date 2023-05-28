print("Pedir dos valores y en caso de que no sean iguales indicar cuál es el mayor\n")
print("Dame dos numeros\n")
num1 = int(input("Ingrese un primer numero: "))
num2 = int(input("Ingrese un segundo numero: "))
if num1 == num2:
    print("Son iguales")
elif num1 > num2:
    print("El numero mayor es: ", num1)
elif num1 < num2:
    print("El numero mayor es: ", num2)