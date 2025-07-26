print("Hola")
print("Dime nombres de personas y los guardaré en una lista")
print("Cuando digas exit te enseñaré todos los nombres guardados")

lista_nombres = []

while True:
    
    nombre = input("Dime un nombre ")

    if not(nombre.lower == "exit"):
        lista_nombres.append(nombre)
    else:
        print(lista_nombres)
        break
