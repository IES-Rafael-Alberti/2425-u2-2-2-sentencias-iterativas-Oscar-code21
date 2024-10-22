# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

def numero_entero():
    '''
    Pide al usuario que introduzca un número entero
    '''

def desarrollo_triangulo():
    '''
    Desarrollo para mostrar triangulo apartir de mi número entero
    '''
    
def muestra_triangulo():
    '''
    Muestra el triangulo gracias al desarrollo anterior
    '''
    



def main():

    #Entrada
    numeroentero = int(input("Introduce la altura del triangulo"))

    #desarrollo
    for i in range(1, numeroentero+1, 2):
        for j in range (i,  0, -2):
    
    #Salida
            print(j, end=" ")
    print("")

if __name__=="__main__":
    main() 