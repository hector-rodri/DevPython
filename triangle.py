def is_triangle(side1,side2,side3):
    phase1 = False
    phase2 = False
    if side1 > 0 and side2 > 0 and side3 > 0:
        phase1 = True
    else: print('All the sides must be have a lenght bigger than 0')
    if ((side1 + side2) >= side3) or ((side3 + side2) >= side1) or ((side1 + side3) >= side2):
        phase2 = True
    else: print('The sum of the lengths of any two sides must be greater than or equal to the length of the remaining side')
    if phase1 == True and phase2 == True:
        print('Your shape it is a triangle')
        return True
    else: print('ERROR, your shape it is not a triangle')

print('I am going to know if your shape it is a triangle equilateral, isosceles, or scalene')
print('-Equilateral it is if the triangle have the sides of the same lenght')
print('-Isosceles it is if the triangle have two sides of the same lenght')
print('-Scalene it is if the triangle have all the sides of different lenght')
print('First, I am going to check if the shape it is a triangle')
print('For a start I need the lenght of the sides of the triangle')
side1 = input('Side 1: ')
side2 = input('Side 2: ')
side3 = input('Side 3: ')
