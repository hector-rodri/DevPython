def grains_on_square(square):
    if square < 1 or square > 64:
        raise ValueError("The square number must be between 1 and 64.")
    return 2 ** (square - 1)


