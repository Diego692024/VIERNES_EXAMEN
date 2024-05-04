# DICCIONARIO
telefonos = {
    "liz":76126968,
    "Marco":79169449,
    "Carla":72597109,
    "Omar":75985122,
    "Ana":65054823,
}
# type sirve para obtener el tipo de objeto DA RESULTADO = dict (abrev diccionario)
print(type(telefonos))
print(telefonos["liz"])

print("guido" in telefonos)
print("pedro" not in telefonos)
print ("liz" in telefonos)
"""
"liz": 76126968
clave    valor
"""
for clave, valor in telefonos.items():
    print(f"clave: {clave} valor:{valor}")