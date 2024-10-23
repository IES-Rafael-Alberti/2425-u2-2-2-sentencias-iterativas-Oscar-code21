# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

def tabla_multiplicar():
    '''
    desarrollo de el rango que le pedimos para que muestre tabla multiplicar
    '''
    mensaje = ""
   
    for i in range (1, 10 + 1):

        mensaje =  ("1 por" + str(i) + "=")  + 1 * str(i) + "\n"
        
        
        return mensaje



def mostrar_tabla(mensaje):
    '''
    Muestra el resultado del desarrollo hecho
    '''
   

    print(mensaje)





def main ():
    
    #Desarrollo
    mensaje = tabla_multiplicar()
    
    #Salida
    
    print(mensaje)


if __name__=="__main__":
    main()