edades = (3,45,17,33,12,34,22,10,28)
for edad in edades:
    if edad > 18:
        print(f"{edad} es mayor de edad ")
    elif edad < 18 and edad > 5:
        print(f"{edad} es menor de edad ")
    else:
        print(f"{edad} es infante")        