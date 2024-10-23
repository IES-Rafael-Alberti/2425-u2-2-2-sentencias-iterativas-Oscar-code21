# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

def frase_letra():
    '''
    pedirle al usuario frase y letra
    '''
    Frase = input("Dime una frase")
    letra = input("Dime una letra")
    return Frase,letra

def numero_veces(Frase,letra):
    '''
    desarrollo cuantas veces aparece la letra seleccionada en la frase
    '''
    contador = 0
    for i in Frase:
        if i == letra:
            contador += 1
    return contador



def mensaje_escrito(contador):

    mensaje = "La letra aparece: " + str(contador) + " veces."
    return mensaje
def muestra_pantalla(mensaje):
    '''
    Muestra por pantallla el número de veces que aparece la letra por pantalla en la frase seleccionada
    '''
    print(mensaje)




def main():

    #Entrada
    Frase,letra = frase_letra()
     #Desarrollo
   
    contador = numero_veces(Frase,letra)

    mensaje = mensaje_escrito(contador)
    #Salida
    muestra_pantalla(mensaje)
if __name__=="__main__":
    main() 