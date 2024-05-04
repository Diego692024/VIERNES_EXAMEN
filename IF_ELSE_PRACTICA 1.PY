#Escriba un programa en Python que solicite al usuario ingresar un número entero y determine si dicho número es par o impar. 
#A continuación, muestre un mensaje indicando si el número es par o impar.

#Su tarea es completar el programa siguiendo las siguientes instrucciones:

#Solicite al usuario que introduzca un número entero.
#Almacene el número ingresado en una variable llamada "numero", convirtiéndolo a tipo entero.
#Utilice una estructura condicional para verificar si el número es divisible entre 2 sin dejar residuo.
#Si el número es divisible entre 2 sin dejar residuo, imprima el siguiente mensaje: "El número [numero] es par", donde "[numero]" representa el número ingresado por el usuario.
#Si el número no es divisible entre 2 sin dejar residuo, imprima el siguiente mensaje: "El número [numero] es impar", donde "[numero]" representa el número ingresado por el usuario.

numero = input("Introdusca su numero: ")
numero = int(numero)
if numero % 2 == 0:
    print(f"su numero es {numero} y es entero")
else:
    print(f"su numero es {numero} y no es entero")