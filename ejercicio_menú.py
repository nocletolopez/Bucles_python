# 1 ejercicio menú con opciones
a = int(input("Ingrese un número:  "))
b = int(input("Ingrese un número:  "))

opcion_1 = "Mostrar la suma de los dos números"
opcion_2 = "Mostrar la resta de los dos números"
opcion_3 = "Mostrar la multiplicación de los dos números"
opcion_4 = "Finalizar programa"
opcion_5 = "Opción no válida, no es correcta"


lista = [opcion_1,opcion_2, opcion_3, opcion_4, opcion_5]

print(f"Menú{lista}")

for x in lista:
    print("Escoja entre 1 y 5 según la opción que desee")
    variable = int(input())

    if variable == 1:
        suma = a + b
        print(suma)
    elif variable == 2:
        resta = a - b
        print(resta)
    elif variable == 3:
        multi = a * b
        print(multi)
    elif variable == 4:
        break
    elif variable == 5:
        print("Opción no válida, elija otra")
        continue
    else:
        print(lista)
