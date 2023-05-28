print("Leer tres números y deducir si se han introducido en orden creciente \n")
print("Dame tres numeros \n")
num1 = int(input("Dame un primer numero: "))
num2 = int(input("Dame un segundo numero: "))
num3 = int(input("Dame un tercer numero: "))
if num1 < num2 and num2 < num3:
    print("\nEn orden creciente\n")
else :
    print("\nEn orden no creciente\n")
print("Fin")