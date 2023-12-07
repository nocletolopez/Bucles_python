#2 ejercicio numero impar
while True:
    impar = int(input("Ingrese un número impar: "))

    if impar % 2 == 0:
        print("Número incorrecto, ingrese otro")
    else:
        print(f"Este número es impar y es: {impar}")
        break
