def operaciones(num1,num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    if num2!=0:
        division = num1/num2
    else:
        print("No se puede dividir entre 0")
    return suma,resta,multiplicacion,division

resultado = operaciones(1,2)
print("El resultado es:",resultado)