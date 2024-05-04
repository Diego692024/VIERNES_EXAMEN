#WHILE MIENTRAS

limite = 10
i = 1
while (i <= limite ):
    print(i, end= " ")
    i += 1
print (" ")

# len 

animales = ['elefante', 'caballo', 'zorillo', 'delfin', 'medusa', 'gato']
indice = 0 # 0 por que quiero q comience desde elefante que es la posicion 0
            
while indice < len(animales):
    animal=animales[indice]
    print(f"{indice+1}.- {animal}")
    indice += 1


a, b  = 0, 1
limite = 100
while a < limite:
    print(a, end = " ")
    a, b = b, a+b