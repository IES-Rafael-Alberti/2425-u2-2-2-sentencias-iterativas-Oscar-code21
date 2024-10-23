# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

def pide_palabra():
    '''
    Pedir al usuario una palabra
    '''
    palabra = input("DIme una palabra")
    return palabra

def una_una(palabra):
    '''
    desarrollo para que se muestres una a una empezando desde la ultima
    '''
    mensaje =""
   
    for i in range(len(palabra)-1, -1, -1):

        mensaje += palabra[i] + "\n"
    return mensaje


def muestra_pantalla(mensaje):
    '''
    Muestra por pantalla letra a letra desde la ultima
    '''
    
    print(mensaje)



def main():

    #Entrada
    palabra = pide_palabra()

    #Desarrollo
    mensaje = una_una(palabra)

    #Salida
    print(mensaje)
    
if __name__=="__main__":
    main() 