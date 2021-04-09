from Nodo import Nodo
from Contacto import Contacto

class Lista_doble_enlace:

    def __init__(self):
        self.primero = None

    def setContacto(self, nombre, apellido, telefono):

        conta = Contacto(nombre, apellido, telefono)
        nuevo = Nodo()
        nuevo.valor = conta

        if self.primero == None: #Lista vacía
            self.primero = nuevo
        
        else: #Lista con elementos
            actual = self.primero
            while actual.siguiente != None:
                actual = actual.siguiente
            nuevo.anterior = actual
            actual.siguiente = nuevo


    def getContacto(self, telefono):
        # Nos va a devolver un nodo de tipo encabezado
        actual = self.primero
        encontrado = False
        while actual != None:
            if actual.getTelefono() == telefono:
                encontrado = True
                return actual
            actual = actual.siguiente
        if encontrado == False:
            return None

    def recorrer(self):
        actual = self.primero
        while actual != None:
            print (actual.valor.getTelefono())
            actual = actual.siguiente

#lista = Lista_doble_enlace()
#lista.setContacto("adolfo", "Perex", 22222222)
#lista.setContacto("adolfo", "Perex", 4)
#lista.setContacto("adolfo", "Perex", 1)
#lista.setContacto("adolfo", "Perex", 22222)
#lista.setContacto("adolfo", "Perex", 8)
#lista.recorrer()

