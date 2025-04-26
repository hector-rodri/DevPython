num1 = input("Introduce un primer número")
num2 = input("Introduce un segundo número")

num1 = int(num1)
num2 = int(num2)

if num1 > num2:
    print("El primer número es mayor")
elif num2 > num1:
    print("El segundo número es mayor")
else:
    print("Los números son iguales")

if num1 == 0 or num2 == 0:
    print("Uno de los números es igual a 0")

if num1 < 0 or num2 < 0:
    print("Uno de los números es negativo")