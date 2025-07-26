def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def dividir(num1, num2):
    if num2 == 0:
        return "No se puede dividir entre 0"
    return num1 / num2

def multiplicar(num1, num2):
    return num1 * num2

print("CALCULADORA:")

while True:
    numero1 = int(input("Introduce un primer número: "))
    numero2 = int(input("Introduce un segundo número: "))
    
    operacion = input("Elige una operación: sumar, restar, multiplicar, dividir o salir: ").lower()

    if operacion == "sumar":
        print("La suma de estos números es", sumar(numero1, numero2))
    elif operacion == "restar":
        print("La resta de estos números es", restar(numero1, numero2))
    elif operacion == "dividir":
        print("La división de estos números es", dividir(numero1, numero2))
    elif operacion == "multiplicar":
        print("La multiplicación de estos números es", multiplicar(numero1, numero2))
    elif operacion == "salir":
        print("Gracias por usar mi calculadora")
        break
    else:
        print("Error")
        print("Importante: elija entre sumar, restar, dividir, multiplicar o salir.")
