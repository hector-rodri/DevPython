total = 0

for i in range(5):
    num = input("Introduce un número: ")
    num = int(num)

    if num < 0:
        continue 

    total += num

print("El total de los números positivos es:", total)
