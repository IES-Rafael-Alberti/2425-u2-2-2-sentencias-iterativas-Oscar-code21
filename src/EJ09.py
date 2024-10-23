#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

def introduce_contraseña():
    contraseña = input("Introduce la contraseña")
    return contraseña




def cadena_caracteres():
    '''
    Escribo desarrollo quue almacena la cadena de caracteres contraseña en una variable
    '''
    clave = "pablo"
    Contraseña = ""
    while Contraseña != clave:
        Contraseña = introduce_contraseña() # pide la contraseña al usuario
    return clave

def contraseña_correcta(clave):
    '''
    aviso cuando la contraseña es correcta
    '''
    print(clave)


def main ():
    
   #Desarrollo
    clave = cadena_caracteres()

    #Salida

    contraseña_correcta (clave)

if __name__=="__main__":
    main() 
