class Nodo:

    def __init__(self, id):
        self.id = id

        # Apuntadores, recordemos que es una lista doblemente enlazada, apuntador
        # hacia el siguiente y otro hacia anterior
        self.siguiente = None
        self.anterior = None
        self.valor = None