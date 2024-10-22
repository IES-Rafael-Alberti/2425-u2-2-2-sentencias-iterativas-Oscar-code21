# Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.
#Entrada
def numero_positivo():
    '''
    Le pediremos a la maquina que leea el numero entero  positivo que introduzcas
    '''


#Desarrollo
def leer_numero():
    '''
    comprobaremos que el numero metido, sume los digitos que los componen
    
    '''

#salida
def suma_digitos():
    '''
    
    Aqui imprimira la suma de  los digitos del numero introducido
    '''







def main ():
    #Entrada
    suma = 0
    numeroentero = int(input("numero entero positivo: "))
    #desarrollo
    while numeroentero!=0:
        digitos = numeroentero%10
        suma+=digitos
        numeroentero=numeroentero//10
    #Salida
    print("Suma de los digitos", suma)

if __name__=="__main__":
    main() 