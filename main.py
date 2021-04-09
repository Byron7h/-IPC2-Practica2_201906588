if __name__ == '__main__':
    from Contacto import Contacto
    from Nodo import Nodo
    from Lista_Doble import Lista_doble_enlace

    lista = Lista_doble_enlace()

    def Menu_principal():
        print("")
        print("Menú Principal:")
        print("     1. Ingresar nuevo contacto")
        print("     2. Buscar contacto")
        print("     3. Visualizar agenda")
        print("     4. Salir")
        print("")

        valido= False

        try:
            a = int(input())
            valido = True            
        except:
            print("Opcion ingresada no válida")
            Menu_principal()

        if valido:
            if a == 1:
                Menu_principal() 
            elif a == 2:
                Menu_principal()
            elif a == 3:
                Menu_principal()
            elif a == 4:
                print("Gracias por usar el programa")
            else:
                print("Opcion ingresada no válida")
                Menu_principal()
    
    Menu_principal()