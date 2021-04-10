if __name__ == '__main__':

    from graphviz import Digraph
    from Contacto import Contacto
    from Nodo import Nodo
    from Lista_Doble import Lista_doble_enlace


    lista = Lista_doble_enlace()

    def agregar():
        print("Ingrese nombre:")
        nombre = str(input())
        if nombre != "":          
            print("Ingrese apellido:")
            apellido = str(input())
            if apellido != "":          
                print("Ingrese número telefónico:")
                valido = False
                try:
                    numero = int(input()) 
                    valido = True     
                except:
                    pass
                if valido:
                    # Verificando si el número ya está registrado
                    if lista.getContacto(numero) == None:
                        lista.setContacto(nombre, apellido, numero)
                        print("Se agregó el contácto exitosamente")
                    else:
                        print("No se pudo agregar el contacto")
                        print("El número ingresado ya se encuentra registrado")
                else:
                    print("No se pudo agregar el contacto")
                    print("Número no válido")
            else: 
                print("No se pudo agregar el contacto")
                print("No se permite un apellido vacío")
        else: 
            print("No se pudo agregar el contacto")
            print("No se permite un nombre vacío")

        print("")

    def agregar2(numero):
        print("Ingrese nombre:")
        nombre = str(input())
        if nombre != "":          
            print("Ingrese apellido:")
            apellido = str(input())
            if apellido != "":                  
                lista.setContacto(nombre, apellido, numero)
                print("Se agregó el contácto exitosamente")
            else: 
                print("No se pudo agregar el contacto")
                print("No se permite un apellido vacío")
        else: 
            print("No se pudo agregar el contacto")
            print("No se permite un nombre vacío")
        print("")
        
    def buscar():
        print("Ingrese el numero a buscar")
        valido = False
        try:
            numero = int(input())
            valido = True            
        except:
            print("Número ingresado no válido")
        if valido:
            datos = lista.getContacto(numero)
            if datos == None:
                print("El número de teléfono no existe. ¿Desea agregarlo?")
                print("     1. Sí")
                print("     2. No")
                b = input()
                if b == "1":
                    agregar2(numero)
                elif b == "2":
                    print("No")
                else:
                    print("Opción no válida")
            else:
                print("Datos del contacto:")
                print("    Nombre: " + str(datos.valor.getNombre()))
                print("    Apellido: " + str(datos.valor.getApellido()))
                print("    Teléfono: " + str(datos.valor.getTelefono()))         

    def grafico():
        contador = 0
        g = Digraph('G', filename='Agenda.gv')
        g.attr('node', shape='box')
        g.attr('edge', arrowhead = 'none')
        #edge [arrowhead=normal,arrowtail=dot]

        if lista.primero != None:
            actual = lista.primero
            val = "Nombre: " + str(actual.valor.getNombre()) + "\n" + "Apellido: " + str(actual.valor.getApellido()) + "\n" + "Teléfono: " + str(actual.valor.getTelefono()) 
            g.node(str(contador), str(val)) 
            contador += 1
            actual = actual.siguiente

            while actual != None:
                val = "Nombre: " + str(actual.valor.getNombre()) + "\n" + "Apellido: " + str(actual.valor.getApellido()) + "\n" + "Teléfono: " + str(actual.valor.getTelefono()) 
                g.node(str(contador), str(val))                               
                g.edge(str(contador-1), str(contador))          
                contador += 1
                actual = actual.siguiente
        g.view()


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
                agregar()
                Menu_principal() 
            elif a == 2:
                buscar()
                Menu_principal()
            elif a == 3:
                grafico()
                Menu_principal()
            elif a == 4:
                print("Gracias por usar el programa")
            else:
                print("Opcion ingresada no válida")
                Menu_principal()

    Menu_principal()
