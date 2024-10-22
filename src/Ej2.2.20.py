# Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución

def solicita_frase_letra():
    '''
    Pediremos que el usuario introduzca una frase y una letra
    
    '''
def encontrado_noencontrado():
    '''
    aqui introduciremos si encotro la posicion de la letra si, si no si la encontro
    '''






def main():
    #Entrada
    frase = input("Ingresa una frase")
    letra = input("Ingresa una letra")
    i=0

    #Desarrollo
    while i!=len(frase):
        if i!=frase[i]:
            print("No se encontro la posición", i)
        else:
            print("Se encontro en la posición", i)

if __name__=="__main__":
    main() 