num1 = input("Introduce un número")
rango = input("Dime hasta que número quieres multiplicar al anterior número")

num1 = int(num1)
rango = int(rango)

print("TABLA DEL",num1)
for i in range(1,rango+1):
    resultado = num1*i
    print(num1,"x",i,"=",resultado)