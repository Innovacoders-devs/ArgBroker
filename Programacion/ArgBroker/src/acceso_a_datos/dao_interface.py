import abc

class DAOInterface(abc.ABC):
    @abc.abstractmethod
    def crear(self, objeto):
        pass

    @abc.abstractmethod
    def obtener_uno(self, id):
        pass

    @abc.abstractmethod
    def obtener_todos(self, id):
        pass

    @abc.abstractmethod
    def actualizar(self, objeto):
        pass

    @abc.abstractmethod
    def eliminar(self, id):
        pass