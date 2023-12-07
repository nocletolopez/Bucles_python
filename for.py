lista = [1,2,3,4,5]
for x in lista:
    print("Soy un ítem de la lista y valgo",x) #la variable x es una copia local del bucle, por 
    x = x * 10  #lo tanto fuiera del bucle no afectaría en nada a menos de que la llamemos
    print(x) #se afect+o dentro del bucle pero fuera no, como se puede ver
print(lista)