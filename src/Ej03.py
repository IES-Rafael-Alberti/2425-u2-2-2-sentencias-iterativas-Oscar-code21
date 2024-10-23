# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

def pedir_numeroentero():
    '''
    pedimos al usuario que introduzca un número entero
    '''
    numeroentero = int(input("Introduce número entero: "))
    return numeroentero

def numeros_impares(numeroentero):

    '''
    rango de números impares desde 1 hasta el número introducido
    '''
    numero = ""
    
    for i in range(1, numeroentero+1, 2):
        numero += str(i) 
    return numero

def muestra_pantalla(numero):
    '''
    Muestra por pantalla todos los números impares desde 1 hasta el número introducido
    '''
 
    print(numero) 


def main():

    #Entrada
    numeroentero = pedir_numeroentero()

    #Desarrollo
    numero = numeros_impares(numeroentero)

    #Salida
    print(numero)

if __name__=="__main__":
    main()