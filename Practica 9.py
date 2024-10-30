print() #para una linea en blanco
print("SOSA LUIS OMAR 1217_3-W: MI PRACTICA DE FUNCIONES") #el nombre del creador 
print() #para una linea en blanco
def mi_informacion(escuela="prepa 128", edad=18, año_nacimiento=2006):  #se colocan las variables que se mostraran
    print("Estudio en la " + escuela + ", tengo " + str(edad) + " años y nací en el año " + str(año_nacimiento))

mi_informacion() #la primer funcion 
mi_informacion(escuela="otra escuela") #mostrara otra escuela si la hay
mi_informacion(edad=19) #otro año o otra edad
print() #para una linea en blanco