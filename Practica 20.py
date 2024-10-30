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