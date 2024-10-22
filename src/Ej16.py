# Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.

def numero_entero():
    '''
    Leeremos un numero entero psotivo que introducimos 
    '''

def nume_entero_cero():
    '''
    escribiremos el proceso para que cuando ingresemos cero, pare y informe cuál fue el mayor de todos los numero introducidos
    '''

def mayor_introducido():
    '''
    Nos dira cual es el mayor numero introducido
    '''






def main():

    #Entrada

    mayor=-1
    numeroentero = int(input("Número positivo: "))

    #desarrollo
    while numeroentero>=0:
        if numeroentero>mayor:
            mayor=numeroentero
        numeroentero=int(input("número positivo:"))
    
    #Salida
    print("Mayor número ingresado: ", mayor)


if __name__=="__main__":
    main() 