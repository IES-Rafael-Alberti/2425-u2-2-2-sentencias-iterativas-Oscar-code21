# Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.

def leer_numero_entero():
    '''
    Lee numero entero hasta poner 0
    '''


def sumatorio(positivo):
    '''
    Si no ingresa 0, sigue sumando numero positivo
    '''
 

def cuantos_positivos(positivo):
    '''
    Muestra cuantos positivos hay en total
    '''
    








def main():
    #Entrada
    positivo = 0
    numeroentero =int (input("0 para terminar): "))

    #Desarrollo 
    while numeroentero !=0:
        if numeroentero>0:
            positivo+=1
        numeroentero=int(input("número(0 para terminar):"))
    
    #Salida
        print("Cuantos positivos hay:", positivo)

if __name__=="__main__":
    main() 