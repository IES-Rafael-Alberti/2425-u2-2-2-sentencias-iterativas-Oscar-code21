# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

def numero_entero():
    '''
    Pedir al usuario un número entero positivo
    '''

def cuenta_atras():

    '''
    Cuenta atras desde el número introducido hasta cero con comas
    '''
        

def mostra_pantalla():
    '''
    Muestra por panatalla la cuenta atras desde el número introducio hasta cero separado por comas
    '''




def main ():
    
    #Entrada
    numeroentero = int(input("Introduce número entero: "))

    #Desarrollo
    for i in range(numeroentero, -1, -1):

    #Salida
        print(i, end=",")

if __name__=="__main__":
    main()
    