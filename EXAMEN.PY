precios = (50, 75, 46, 22, 80, 65, 8)
menor = precios[0]
mayor = precios[0]

for precio in precios:
    if precio < menor:
        menor=precio
    if precio > mayor:
        mayor=precio
print(f"{menor}")
print(f"{mayor}")