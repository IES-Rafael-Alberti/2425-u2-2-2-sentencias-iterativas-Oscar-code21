#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

def pregunta_edad():
    '''
    El programa le pregunta al usuario su edad
    '''
    edad = int(input("¿Cuantos años tienes?"))
    return edad

def años_cumplidos(edad):

    '''
    Rango de de edad que introduces ( desde 1 hasta su edad).

    '''
    años = " "
    for i in range(1, edad + 1):
        años += str(i) + " "
    return años

def Mostrar_edad(años):
    '''
    Muestra por pantalla todos los años cumplido (desde 1 hasta ahora)
    '''
    print(años)



def main():

    # Entrada
    edad = pregunta_edad()

    #Desarrollo
    años = años_cumplidos(edad)

    #Salida
    print(años)

if __name__=="__main__":
    main()