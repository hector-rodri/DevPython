palabras = []

while True:
    respuesta = input("Introduce una palabra o 'stop' para salir: ")
    if respuesta.lower() == "stop":
        break
    else:
        palabras.append(respuesta)

print("Palabras introducidas:", palabras)
