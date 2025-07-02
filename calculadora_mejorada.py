def suma(a, b):
    return a + b    

def resta(a, b):
    return a - b    

def division(a, b):
    return a / b    

def multiplicacion(a, b):
    return a * b    

print('Bienvenido a mi calculadora')
while True:
    print('Dime los números con los que deseas operar:')

    num1 = input('Número: ')
    num2 = input('Número: ')

    print('Elige una operación introduciendo su número:')
    print('1-Suma')
    print('2-Resta')
    print('3-División')
    print('4-Multiplicación')
    print('----------------------')
    operación = input()

    match(operación):
        case '1':
            print(suma(int(num1),int(num2)))
        case '2':
            print(resta(int(num1),int(num2)))
        case '3':
            print(division(int(num1),int(num2)))
            #entre 0
        case '4':
            print(multiplicacion(int(num1),int(num2)))
        case _:
            print('Operación no válida')
            