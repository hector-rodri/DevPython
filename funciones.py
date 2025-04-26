def cuadrado(numero):
    return numero * numero

def doble(numero):
    return numero * 2

num1 = input("Introduce un número ")

num1 = int(num1)

print("El cuadrado de",num1,"es",cuadrado(num1))
print("El doble de",num1,"es",doble(num1))