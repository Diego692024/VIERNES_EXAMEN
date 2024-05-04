numero = input("introdusca su numero entero: ")
numero = int(numero)
if numero < 0:
    print(f"su nuermero {numero} es negativo")
elif numero == 0:
    print(f"su nuermero {numero} es cero")
elif numero > 0 and numero < 10:
    print(f"su nuermero {numero} es positivo y menor que 10")
elif numero in range(10,21):
    print(f"su nuermero {numero} esta en el rango de 10 y 20")
else:
    print(f"su nuermero {numero} es mayor que 20")