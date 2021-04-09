from Nodo import Nodo

class Lista_doble_enlace:

    def __init__(self):
        self.primero = None

    def setContacto(self, nuevo):

        if self.primero == None: #Lista vacía
            self.primero = nuevo
        
        else: #Lista con elementos
            actual = self.primero
            while actual.siguiente != None:
                actual = actual.siguiente
            nuevo.anterior = actual
            aux.siguiente = nuevo


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
