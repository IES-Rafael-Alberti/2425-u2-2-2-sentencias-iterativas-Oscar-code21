# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

def usuario_invierte():
    '''
    Preguntar al usuario una cantidad a invertir, el interes anual y el número de años
    '''




def rango_años():
    '''
    Desarrollo de operación para encontra el total del capital obtenido
    '''

   

def resultado_capital( ):
    '''
    Muestrar por pantalla el resultado de la capital obtenida habiendo preguntado la cantidad, interes y número
    '''
 

    


def main ():
    
    
    #Entrada
    cantidadinvertir = float(input("¿Cuanto inviertes?"))
    Interes = float(input("¿Intererds anual?"))
    años = int(input("Número de años"))

    #Procesamiento
    for i in range (años):
        cantidadinvertir *= 1 + Interes / 100

    #Salida
    print("Capital tras " + str(i+1) + " años:" + str (round(cantidadinvertir, 2)))

if __name__=="__main__":
    main()
        