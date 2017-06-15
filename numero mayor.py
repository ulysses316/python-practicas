num1=int(raw_input("Dame un numero "))
num2=int(raw_input("Dame otro numero "))
num3=int(raw_input("Dame un ultimo numero "))
if num1>num2 and num1 > num3:
    print("El primer numero es el mayor")
if num2>num1 and num2 > num3:
    print("El segundo numero es el mayor")
if num3>num2 and num3 > num1:
    print("El tercer numero es el mayor")
