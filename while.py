num1 = input("Introduce un número ")

num1 = int(num1)
numX = 0

if num1 > 0:
    while numX != num1:
        numX = numX+1
        print(numX)
else:
    print("El número no puede ser negativo")