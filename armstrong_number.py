print('I am going to guess if your number is a armstrong number')
print('An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.')
number = int(input('Write a number: '))

digits = [int(d) for d in str(number)]
print(digits)
print(len(digits))
sum_digits = 0

for i in range(len(digits)):
    vAux = digits[i] ** len(digits) 
    sum_digits += vAux
    print(sum_digits)

if sum_digits == number:
    print('Your number is a armstrong number')