# CREAR UN PROGRAMA QUE IMPRIMA UN TABLERO DE AJEDRES DE TAMAÑO VARIABLE 
n =int(input("ingrese su dimension: "))
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            print("#", end= " ")
        else:
            print(" ", end= " ")
    print(" ")