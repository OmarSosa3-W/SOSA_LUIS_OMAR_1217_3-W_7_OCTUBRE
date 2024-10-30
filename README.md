# SOSA_LUIS_OMAR_1217_3-W_7_OCTUBRE
Practicas del 7 de octubre "FUNCIONES"
# PROGRAMA 1:
print() #para dejar una linea en blanco
print("SOSA LUIS OMAR 1217_3-W: PRACTICA DE HOLA MUNDO") #le nombre del creador del codigo
print() #para dejar una linea en blanco
def my_function(): #llamamos o declaramos la función
    print("¡Hola Omar Sosa!") #lo que imprimira la función 
    print()

![image](https://github.com/user-attachments/assets/59c90bb9-7e09-47bd-bd0b-e9c6d3545a48)
![image](https://github.com/user-attachments/assets/10f07663-d63c-46c7-b053-73f0925e9d66)

# PROGRAMA 2:
print() #para dejar una linea en blanco
print("SOSA LUIS OMAR 1217_3-W: PRACTICA DE HOLA MUNDO #2") #le nombre del creador del codigo
print() #para dejar una linea en blanco
def my_function(): #llamamos o declaramos la función
    print("¡Hola Omar Sosa!") #lo que imprimira la función 
my_function() #dale la indicacion que imprima la funcion 
print() #para dejar una linea en blanco

![image](https://github.com/user-attachments/assets/d54e8ce7-749c-4bbd-ba4c-9e4cd6710c75)
![image](https://github.com/user-attachments/assets/07d1eb2e-dfc5-4cbe-ab7a-2fc8811793bc)

# PROGRAMA 3:
print() #para dejar una linea en blanco
print("SOSA LUIS OMAR 1217_3-W: MI PRACTICA DE fname") #nombre del creador del codigo
print()  #para dejar una linea en blanco
def my_function(fname): #la funcion se define con la condicion de un nombre
    print(fname + " ROCK Y METAL") #lo que se mnostra al lado del nombre 

my_function("OMAR:") #1er nombre
my_function("SOSA:") #2do nombre
my_function("LUIS:") #3er nombre
print()  #para dejar una linea en blanco

![image](https://github.com/user-attachments/assets/79a43baf-e172-4fb1-ac83-1ba86582a52b)
![image](https://github.com/user-attachments/assets/5f0eca91-8d4f-47fe-8532-16aabac4d567)

# PROGRAMA 4:
print() #se coloca para una linea en blanco
print("SOSA LUIS OMAR 1217_3-W: MI PRACTICA DE FNAME/INAME") #nombre del creador
print() #se coloca para una linea en blanco
def my_function(fname, lname): #las variables que se usarana en la funcion
    print(fname + " " + lname) #las variables ingresadas se sumaran formando una cadena de caracteres

my_function("Omar", "Sosa") #los nombres ungresador por el usuario
print() #se coloca para una linea en blanco

![image](https://github.com/user-attachments/assets/1cc1bb96-8af3-42ea-ad97-0b349a5c1b7f)
![image](https://github.com/user-attachments/assets/b993daee-d1e0-47d6-a3c6-b35d633b0fa5)

# PROGRAMA 5:
print() #se coloca para una linea en blanco
print("SOSA LUIS OMAR 1217_3-W: MI PRACTICA DE FNAME/INAME") #nombre del creador
print() #se coloca para una linea en blanco
def my_function(banda1, banda2): #las variables que se usarana en la funcion
    print(banda1 + " vs " + banda2) #las variables ingresadas se sumaran formando una cadena de caracteres

my_function("Metallica", "Megadeth") #las bandas ingresadas
print() #se coloca para una linea en blanco

![image](https://github.com/user-attachments/assets/2368585a-32fc-4a8a-9544-505b16938160)
![image](https://github.com/user-attachments/assets/06ca6f52-13b3-49f6-a0bd-9f463d0c1ca3)

# PROGRAMA 6:
print() #se coloca para una linea en blanco
print("SOSA LUIS OMAR 1217_3-W: MI PRACTICA DE VECTOR EN FUNCIONES") #nombre del creador
print() #se coloca para una linea en blanco
def my_function(*kids): #El nombre de la función 
    print("The youngest child is " + kids[2]) #indicacion de que nos muestre la variable numero 2 iniciando por 0 [0, 1, 2]

my_function("Omar", "Coockies", "Daniel") #imprima las variables 

![image](https://github.com/user-attachments/assets/d48c07ac-670f-4d01-800e-60150734208d)
![image](https://github.com/user-attachments/assets/3f6c2d1e-28f6-4a67-b8f5-71d40fdb461e)

# PROGRAMA 7: 
print() #se coloca para una linea en blanco
print("SOSA LUIS OMAR 1217_3-W: MI PRACTICA DE VECTOR EN FUNCIONES") #nombre del creador
print() #se coloca para una linea en blanco
def my_function(child3, child2, child1): #el nombre de la funcion 
    print("The youngest child is " + child3)

my_function(child1 = "KORN", child2 = "SLIPKNOT", child3 = "METALLICA") #las variables editadas
print() #una linea en blnaco

![image](https://github.com/user-attachments/assets/f48b6092-204b-4d40-8585-f10f75cfb44c)
![image](https://github.com/user-attachments/assets/63f1ae16-495d-49f1-b159-a4152d362ad7)

# PROGRAMA 8: 
print() #para una linea en blanco
print("SOSA LUIS OMAR 1217_3-W: MI PRACTICA DE BANDAS DE ROCK") #nombre del creador
print()  #para una linea en blanco
def mi_funcion(**banda): #el nombre de la funcion o lo que imprimira
    print("El nombre de la banda es " + banda["nombre"]) #indicamos que mostrara la funcion banda

mi_funcion(nombre="Queen", genero="Rock", año="1970") #declaramos lo que se mostrara la función
print()  #para una linea en blanco

![image](https://github.com/user-attachments/assets/60d4315f-251a-4020-afb8-8b512263e358)
![image](https://github.com/user-attachments/assets/cbdcdcee-a1d6-4b22-ac3a-a246d603b4cd)

# PROGRAMA 9:
print() #para una linea en blanco
print("SOSA LUIS OMAR 1217_3-W: MI PRACTICA DE FUNCIONES") #el nombre del creador 
print() #para una linea en blanco
def mi_informacion(escuela="prepa 128", edad=18, año_nacimiento=2006):  #se colocan las variables que se mostraran
    print("Estudio en la " + escuela + ", tengo " + str(edad) + " años y nací en el año " + str(año_nacimiento))

mi_informacion() #la primer funcion 
mi_informacion(escuela="otra escuela") #mostrara otra escuela si la hay
mi_informacion(edad=19) #otro año o otra edad
print() #para una linea en blanco

![image](https://github.com/user-attachments/assets/f82ad8f3-1f26-492a-8de6-1c144b648479)
![image](https://github.com/user-attachments/assets/a3eb0ab7-9669-432d-ae7a-ebb05e537fde)

# PROGRAMA 10:
print() #para una linea en blanco
print("SOSA LUIS OMAR 1217_3-W: MI PRACTICA DE MATERIAS EN FUNCIONES") #nombre del creador 
print() #para una linea en blanco
def mi_funcion(materias): #definir la función 
    for x in materias: #para que muestre la funcion 
        print(x)

materias = ["Pensamiento matemático", "Español", "Inglés", "Química", "Civismo", "Francés"] #las variables ingresadas

mi_funcion(materias) #que imprima la materia 
print() #para una linea en blanco

![image](https://github.com/user-attachments/assets/84f3227c-e09c-4b35-934b-5ef41300a98f)
![image](https://github.com/user-attachments/assets/8c072da9-e253-437b-8497-c8f5e5794f05)

# PROGRAMA 11:
print() #para una linea en blanco
print("SOSA LUIS OMAR 1217_3-W: MI PRACTICA DE NUMEROS EN FUNCIONES")
print() #para una linea en blanco
def mi_funcion(x):
    return x * x

print(mi_funcion(3))
print(mi_funcion(5))
print(mi_funcion(9))
print() #para una linea en blanco

![image](https://github.com/user-attachments/assets/a69f5171-100f-49a5-b318-425940250bdf)
![image](https://github.com/user-attachments/assets/1944d409-55c0-481b-a8bb-8724cb338d4e)

# PROGRAMA 12:
print() #para un espacio al ejecutar
print("SOSA LUIS OMAR 1217_3-W: MI PRACTICA DE PASS") #el nombre del creador
print() #para un espacio al ejecutar
def mi_funcion(): #la función que sera
    pass #para que no te marque error
print() #para un espacio al ejecutar

![image](https://github.com/user-attachments/assets/08889f79-54f2-49bb-b3d6-8db970cab7f2)
![image](https://github.com/user-attachments/assets/07eec5f3-3506-4084-a3b1-059d70218158)

# PROGRAMA 13:
print() #una linea en blanco
print("SOSA LUIS OMAR 1217_3-W: MI PRACTICA DE ARGUMENTOS POSICIONALES") #el nombre del creador
print() #una linea en blanco
def mi_funcion(x, /): #se define la funcion 
    print(x) #para que imprima la funcion 

mi_funcion(3) #que muestre el resultado en pantalla
print() #una linea en blanco

![image](https://github.com/user-attachments/assets/ef68e17f-6d43-4e89-8c24-cd6b5169da19)
![image](https://github.com/user-attachments/assets/256bbda7-3a26-473f-beae-a75494e3dce2)

# PROGRAMA 14:
print() #una linea en blanco
print("SOSA LUIS OMAR 1217_3-W: MI PRACTICA DE EDAD") #nombre del creador
print() #una linea en blanco
def mi_funcion(edad): #definir la funcion
    print(edad) #que imprima la funcion

mi_funcion(edad=18) #como o que imprimira
print() #una linea en blanco

![image](https://github.com/user-attachments/assets/060ee973-3e7f-4c56-8848-e7015c183b99)
![image](https://github.com/user-attachments/assets/00eacc84-8361-484b-90e5-33b6927e772e)

# PROGRAMA 15:
print() #para una linea en blanco
print("SOSA LUIS OMAR 1217_3-W") #nombre del creador
print() #para una linea en blanco
def mi_funcion(nombre, /):
    print(nombre)

# Esto generará un error porque se está usando un argumento de palabra clave
mi_funcion(nombre="Juan")  # Esto causará un TypeError

![image](https://github.com/user-attachments/assets/ee517c6b-e24c-4779-bd45-fde7c3038e8e)
![image](https://github.com/user-attachments/assets/1dc4cbbd-ee86-4b6f-a793-f128f9e7cefe)

# PROGRAMA 16: 
print() #para una linea en blanco
print("SOSA LUIS OMAR 1217_3-W") #nombre del creador
print() #para una linea en blanco
def mi_funcion(*, x): #definir la función 
    print(x) #imprimir la función indicada

mi_funcion(x=3) #Esto funciona correctamente
print() #para una linea en blanco

![image](https://github.com/user-attachments/assets/444f5629-b869-4823-9679-a3372c2cd387)
![image](https://github.com/user-attachments/assets/14a0c0af-626b-4138-a9f7-121867ff3376)

# PROGRAMA 17: 
print() #para una linea en blanco
print("SOSA LUIS OMAR 1217_3-W") #nombre del creador
print() #para una linea en blanco
def mi_funcion(x): #definir la función
    print(x) #la función se debe imprimir

mi_funcion(3)  #Esto funciona correctamente
print() #para una linea en blanco

![image](https://github.com/user-attachments/assets/061697fb-e1e9-40d8-9b7f-7964c4c737d8)
![image](https://github.com/user-attachments/assets/a0c1156a-fce7-483b-91a8-19572c3013be)

# PROGRAMA 18:
print() #para una linea en blanco
print("SOSA LUIS OMAR 1217_3-W") #nombre del creador
print() #para una linea en blanco
def my_function(*, x):
    print(f"El valor de x es: {x}") #para imprimir el valor de x
    cuadrado = x ** 2 #la operacio que se debe realizar
    print(f"El cuadrado de {x} es: {cuadrado}") #el resultado de la operacion osea el cuadrado

my_function(x=3) #para que imprima la función 
print() #para una linea en blanco

![image](https://github.com/user-attachments/assets/f1598b82-c297-4fed-a9c5-4d1e17fa8048)
![image](https://github.com/user-attachments/assets/bf8e97e8-1729-4fb8-8df9-e7e7b97ebed7)

# PROGRAMA 19:
print() #para una linea en blanco
print("SOSA LUIS OMAR 1217_3-W") #nombre del creador
print() #para una linea en blanco
def my_function(z, h, /, *, c, d): #definir las variables de la función 
    print(z + h + c + d) #se rescriben laa variables pero ahora para que se sumen solamente 

my_function(50, 26, c = 12, d = 16) #se le dan los valores a las letras (caracteres) para que realize la suma
print() #para una linea en blanco

![image](https://github.com/user-attachments/assets/85c5ab7b-5172-47bc-96a6-7a589526e894)
![image](https://github.com/user-attachments/assets/ff226f6b-0f8b-4ac6-ace7-820fefdb3f63)

# PROGRAMA 20:
print() #para una linea en blanco
print("SOSA LUIS OMAR 1217_3-W") #nombre del creador
print() #para una linea en blanco
def tri_recursion(n): #se difine la función 
    if n > 0: #para dar la indicación que debe cumplir una condición 
        result = n + tri_recursion(n - 1) #indica que el carater tendra cierto valor el cual se le samara 
        print(result) #indica que debe imprimie el resultado
    else: #de otro modo
        result = 0 #muestra que el resultado sera 0
    return result #devuelve el resultado calculado 

print("\n\nRecursion Example Results") #muestre este mensaje 
tri_recursion(6) #que lo imprima hasta el numero 6
print() #para una linea en blanco

![image](https://github.com/user-attachments/assets/2b3c55d8-d812-4c90-b061-16e0c5dbe92f)
![image](https://github.com/user-attachments/assets/ceb346e7-16ba-49d8-a546-073b3d0e6fb1)
