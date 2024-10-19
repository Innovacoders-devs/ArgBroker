class Accion:
    def __init__(self, nombre_accion, simbolo_accion, id_accion = None):
        self._nombre_accion = nombre_accion
        self._simbolo_accion = simbolo_accion
        self.__id_accion = id_accion

    @property
    def nombre_accion (self):
        return self._nombre_accion
    

    @nombre_accion.setter
    def nombre_accion (self, nuevo_nombre):
        self._nombre_accion = nuevo_nombre

    @property
    def simbolo_accion(self):
        return self._simbolo_accion

    @simbolo_accion.setter
    def simbolo_accion(self, nuevo_simbolo):
        self._simbolo_accion = nuevo_simbolo

    @property
    def id_accion(self):
        return self.__id_accion
    
