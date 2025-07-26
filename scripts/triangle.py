def is_triangle(side1,side2,side3):
    phase1 = False
    phase2 = False
    if side1 > 0 and side2 > 0 and side3 > 0:
        phase1 = True
    else: print('All the sides must be have a lenght bigger than 0')
    if ((side1 + side2) >= side3) and ((side3 + side2) >= side1) and ((side1 + side3) >= side2):
        phase2 = True
    else: print('The sum of the lengths of any two sides must be greater than or equal to the length of the remaining side')
    if phase1 == True and phase2 == True:
        return True
    else: print('ERROR, your shape is not a triangle')
    return False

def type_triangle(side1,side2,side3):
    if side1 == side2 == side3:
        return 'Equilateral'
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return 'Isosceles'
    else: return 'Scaleno'
        
while True:
    print('I am going to know if your shape is a triangle equilateral, isosceles, or scalene')
    print('-Equilateral is if the triangle have the sides of the same lenght')
    print('-Isosceles is if the triangle have two sides of the same lenght')
    print('-Scalene is if the triangle have all the sides of different lenght')
    print('First, I am going to check if the shape is a triangle')
    print('For a start I need the lenght of the sides of the triangle')
    side1 = input('Side 1: ')
    side2 = input('Side 2: ')
    side3 = input('Side 3: ')

    if is_triangle(int(side1),int(side2),int(side3)) == False:
        continue
    type = type_triangle(side1,side2,side3)
    print('Your shape is a triangle '+type)
    print('Thanks for use my program')
    print('If you want to stop the program, you must write stop')
    seguir = input()
    if seguir.lower() == 'stop':
        break