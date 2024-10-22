# Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
def ingresa_numero_positivo():
    ''' 
    pondremos que todos los pares es igual a cero y escribiremos un numero de tipo entero y si pones -1 que se termine el programa

    '''

def desarrollo_programa():
    '''
    escribiriremos un bluce donde puedas poner numeros hasta que en algun momento pongas -1 y te el programa te diga cuantos números pares haz ingresado
    
    '''

def mostrar_pares():
    '''
    Nos imprimira cuantos numero pares hemos introducido
    '''




def main():
    #Entrada
    pares = 0
    numeroenteros= int(input("número (-1 para que corte el programa): "))
    #desarrollo
    while numeroenteros!=-1:
        if numeroenteros%2 == 0:
            pares+=1
        suma=0
        while numeroenteros!=0:
            digito=numeroenteros%10
            suma+=digito
            numeroenteros=numeroenteros//10
    #salida
    print("suma de sus digitos:", suma)
    numeroenteros=int(input("numero(-1 para que corte el programa): "))
    print("Se ingresaron", pares, "números pares")

if __name__=="__main__":
    main() 