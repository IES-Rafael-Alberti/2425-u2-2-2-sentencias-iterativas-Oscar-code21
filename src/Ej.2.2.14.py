# Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

def main():
    #Entrada
    total = 0
    numeroentero = int(input("Leer número"))
    #desarrollo
    while numeroentero != 0:
        total+=numeroentero
        numeroentero=int(input("leer número: "))
if __name__=="__main__":
    main()