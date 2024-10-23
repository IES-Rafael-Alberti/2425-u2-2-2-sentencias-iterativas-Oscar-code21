# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

def programa_eco():
    '''
    escribe algo hasta que pones salir
    '''
    Vozpersona = input("di algo")
    return Vozpersona

def salir(Vozpersona):
    '''
    escribir salir para que teermine de preguntar
    '''
    eco = ""
    for i in Vozpersona:
        eco = i + Vozpersona
        return eco
 
def usuario_salir(Vozpersona):
    return Vozpersona != "salir"

def termina_frase(eco):
    '''
    La frase la escribe hasta que escribas salir
    '''
    print(eco)
   






def main():

    #Entrada
    Vozpersona = programa_eco()
   
   #Desarrollo
    eco = salir(Vozpersona)
        
    
    #Salida
            
    print(eco)

if __name__=="__main__":
    main() 



    
    