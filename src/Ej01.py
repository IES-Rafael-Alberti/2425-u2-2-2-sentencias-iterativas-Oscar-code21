# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

#Pedir una palabra
#mostrar 10 veces

def pedir_palabra():
    '''

    El programa le pide al usuario introducir una palabra.
    '''
    palabra = input("Intrdouce una palabra")
    return palabra

def cuantas_veces(palabra):
    '''
    
    Escribe cuantas veces quieres que te lo muestre
    '''
    mensaje =""
    for i  in range(1, 11):
         mensaje += str(i) + palabra + " "

    return mensaje
      
def mostrar_palabra(mensaje):
    '''
    
    Te muestra por pantalla las veces que le has pedido
    '''
    print(mensaje)
    


def main():

    # Entrada
    palabra = pedir_palabra()

    #Desarrollo
    mensaje = cuantas_veces(palabra)

    #salida
    print(mensaje)



if __name__=="__main__":
    main()