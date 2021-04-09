class Contacto:
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono


    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido
    
    def getTelefono(self):
        return self.telefono