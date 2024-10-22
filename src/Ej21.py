# Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.

def main():
    #Entrada
    total = 0
    montos = float(input("Monto de compra de cliente: $"))

    #Desarrollo
    while montos !=0:
        if montos<0:
            print("Monto no valido")
        else:
            total+=montos
        montos=float(input("Monto de una venta: $"))
    if total>1000:
        total-=total*0.1
    #Salida
    print("Monto total a pagar:$", total)


if __name__=="__main__":
    main() 