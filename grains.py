def grains_on_square(square):
    if square < 1 or square > 64:
        raise ValueError("The square number must be between 1 and 64")
    return 2 ** (square - 1)

def total_grains_on_board():
    return 2 ** 64 - 1

try:
    square = int(input("Enter a square number (1-64): "))
    grains = grains_on_square(square)
    print(f"There are {grains} grains on square {square}")
except ValueError as e:
    print("Error:", e)

total = total_grains_on_board()
print(f"The total number of grains on the whole chessboard is: {total}")
