# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

def numero_enetero():
   '''
   Pedir al usuario introducir la altura del triangulo
   '''
   numeroentero =  int(input("Introduce la altura del triangulo: "))
   return numeroentero


def triangulo_rectangulo(numeroentero):
   '''
   desarrollo de triangulo rectangulo como el de mas bajo, de altura el núimero introducido
   '''
   mensaje = ""

   
   for i in range(1, numeroentero, +1):
      mensaje += "*" * i + "\n"
   return mensaje

       

def mostrar_pantalla(mensaje):
   '''
   
   Muestra por pantalla el resultado
   '''
   print(mensaje)

def main ():

   #Entrada
   numeroentero = numero_enetero()


   #Desarrollo
   mensaje = mostrar_pantalla(numeroentero)


   #Salida
   print(mensaje)
   
   if __name__=="__main__":
      main()