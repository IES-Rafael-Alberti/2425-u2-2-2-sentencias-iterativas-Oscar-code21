# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

def numero_entero():
    '''
    Pedir al usuario un número entero positivo
    '''
    numeroentero = int(input("Introduce número entero: "))
    return numeroentero

def cuenta_atras(numeroentero):

    '''
    Cuenta atras desde el número introducido hasta cero con comas
    '''
    numero = ""
    
    for i in range(numeroentero, -1, -1):  
      numero += str(i)  
    return numero

def mostra_pantalla(numero):
    '''
    Muestra por panatalla la cuenta atras desde el número introducio hasta cero separado por comas
    '''
    print(numero)



def main ():
    
    #Entrada
    numeroentero = numero_entero()

    #Desarrollo
    numero = cuenta_atras (numeroentero)

    #Salida
    print (numero)

if __name__=="__main__":
    main()
    