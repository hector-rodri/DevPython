def cuadrado(numero):
    return numero * numero

def doble(numero):
    return numero * 2

def numero_par(numero):
    if numero%2 == 0:
        return True
    else: 
        return False


num1 = input("Introduce un número ")

num1 = int(num1)

print("El cuadrado de",num1,"es",cuadrado(num1))
print("El doble de",num1,"es",doble(num1))
if numero_par(num1):
    print("El número",num1,"es par")
else:
    print("El número",num1,"es impar")