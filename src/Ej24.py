# Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.
#Entrada
def solicite_ingresar():
    '''
    pediremos al usuario que ingrese números
    '''

#desarrollo
def desarrollo_numeros_primos_ingresados():
    '''
    desarrollaremos ingresar un número indeterminado de números hasta que escribas 1

    '''
#Salida
def imprime_numeros_primos():
    '''
    imprimiremos todos los números primos que ingresamos.
    '''




def main ():
    cantidad = 0 
    numeroentero= int(input("Ingresa números"))

    #desarrollo
    while numeroentero!=0:
        primo=True
        for i in range (2,numeroentero):
            if numeroentero%i==0:
                primo=False
        if primo:
            cantidad+=1
        numeroentero=int(input("número: "))
    
    #salida
    print("primos: ", cantidad)

if __name__=="__main__":
    main() 
