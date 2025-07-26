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
    try:
        num1 = input('Número: ')
        suma(int(num1),1)
    except ValueError as error:
        print('Error',error)
        continue

    try:
        num2 = input('Número: ')
        suma(int(num2),1)
    except ValueError as error:
        print('Error',error) 
        continue

    while True:
        print('Elige una operación introduciendo su número:')
        print('1-Suma')
        print('2-Resta')
        print('3-División')
        print('4-Multiplicación')
        print('----------------------')
        operación = input()

        match(operación):
            case '1':
                print('Resultado '+str(suma(int(num1),int(num2))))
                break
            case '2':
                print('Resultado '+str(resta(int(num1),int(num2))))
                break
            case '3':
                try:
                    print('Resultado '+str(division(int(num1),int(num2))))
                except ZeroDivisionError:
                    print('Error división entre 0',ZeroDivisionError)
                continue
            case '4':
                print('Resultado '+str(multiplicacion(int(num1),int(num2))))
                break
            case _:
                print('Operación no válida')
                continue
            


    