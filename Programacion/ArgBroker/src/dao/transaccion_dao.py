from dao_interface import DAOInterface
from model.transaccion import Transaccion
from src.utils.mysql_connector import MySQLConnector

class TransaccionDAO(DAOInterface):
    def __init__(self):
        self._db = MySQLConnector()
        
    def crear(self, transaccion):
        query = "INSERT INTO transaccion (id_transaccion, id_inversor, id_accion, tipo, fecha, precio, cantidad, comision) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (transaccion.id_transaccion, transaccion.id_inversor, transaccion.id_accion, transaccion.tipo, transaccion.fecha, transaccion.precio, transaccion.cantidad, transaccion.comision)
        with self._db as db:
            db.execute(query, values)
    def obtener(self, id_transaccion):
        query = "SELECT * FROM transaccion WHERE id = %s"
        result = self._db.fetch_one(query, (id_transaccion))
        if result:
            return Transaccion(*result)
        return None

    def actualizar(self, objeto):
        pass

    def eliminar(self, id):
        pass