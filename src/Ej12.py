# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

def frase_letra():
    '''
    pedirle al usuario frase y letra
    '''


def numero_veces():
    '''
    desarrollo cuantas veces aparece la letra seleccionada en la frase
    '''
   
def muestra_pantalla():
    '''
    Muestra por pantallla el número de veces que aparece la letra por pantalla en la frase seleccionada
    '''





def main():

    #Entrada
    Frase = input("Dime una frase")
    letra = input("Dime una letra")
    contador = 0
     #Desarrollo
    for i in Frase:
       if i == letra:
            contador +=1
    
    #Salida
    print("La letra ´%s´ aparece %2i veces en la frase ´%s´. " (letra, contador,Frase))

if __name__=="__main__":
    main() 