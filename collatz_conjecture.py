print("One evening, you stumbled upon an old notebook filled with cryptic scribbles,")
print("as though someone had been obsessively chasing an idea.")
print("On one page, a single question stood out: Can every number find its way to 1?")
print("It was tied to something called the Collatz Conjecture, a puzzle that has baffled thinkers for decades.\n")

print("The rules were deceptively simple. Pick any positive integer.\n")

print("If it's even, divide it by 2.")
print("If it's odd, multiply it by 3 and add 1.")
print("Then, repeat these steps with the result, continuing indefinitely.\n")

number = int(input('Write a number:'))

while True:
    if number % 2 == 0:
        number  = number / 2
        print(number)
    else:
        number = (number * 3) + 1
        print(number)

    if number == 1:
        print('END')
        break
