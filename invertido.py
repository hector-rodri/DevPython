def invertido(frase):
    palabras = frase.split(" ")
    invertidas = []
    for palabra in palabras:
        invertidas.append(palabra[::-1])

    return " ".join(invertidas)

print("Escribe una frase:")
frase = input()
resultado = invertido(frase)
print("Frase invertida:", resultado)