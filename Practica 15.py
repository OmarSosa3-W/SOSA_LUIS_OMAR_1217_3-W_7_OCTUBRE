print() #para una linea en blanco
print("SOSA LUIS OMAR 1217_3-W") #nombre del creador
print() #para una linea en blanco
def mi_funcion(nombre, /):
    print(nombre)

# Esto generará un error porque se está usando un argumento de palabra clave
mi_funcion(nombre="Juan")  # Esto causará un TypeError

