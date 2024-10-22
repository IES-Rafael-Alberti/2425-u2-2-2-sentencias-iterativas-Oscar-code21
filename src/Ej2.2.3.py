# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

def pedir_numeroentero():
    '''
    pedimos al usuario que introduzca un número entero
    '''

def numeros_impares():

    '''
    rango de números impares desde 1 hasta el número introducido
    '''
  

def muestra_pantalla():
    '''
    Muestra por pantalla todos los números impares desde 1 hasta el número introducido
    '''
 



def main():

    #Entrada
    numeroentero = int(input("Introduce número entero: "))

    #Desarrollo
    for i in range(1, numeroentero+1, 2):

    #Salida
        print(i, end=",")

if __name__=="__main__":
    main()