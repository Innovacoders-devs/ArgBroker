from dao_interface import DAOInterface
from Inversor import Inversor
from src.utils.mysql_connector import MySQLConnector

class InversorDAO(DAOInterface):
    def __init__(self):
        self._db = MySQLConnector()

    def crear(self, inversor):
        query = "INSERT INTO inversores (nombre, apellido, cuil, email, contrasena) VALUES (%s, %s, %s, %s, %s)"
        values = (inversor.nombre, inversor.apellido, inversor.cuil, inversor.email, inversor.contrasena)
        with self._db as db:
            db.execute(query, values)

    def obtener(self, id_inversor):
        query = "SELECT * FROM inversores WHERE id = %s"
        result = self._db.fetch_one(query, (id_inversor,))
        if result:
            return Inversor(*result)
        return None

    def actualizar(self, inversor):
        query = """
        UPDATE inversores SET nombre = %s, apellido = %s, cuil = %s, email = %s, contrasena = %s 
        WHERE id = %s
        """
        values = (inversor.nombre, inversor.apellido, inversor.cuil, inversor.email, inversor.contrasena, inversor.id)
        with self._db as db:
            db.execute(query, values)

    def eliminar(self, id_inversor):
        query = "DELETE FROM inversores WHERE id = %s"
        with self._db as db:
            db.execute(query, (id_inversor,))

    def obtener_inversor_por_email(self, email):
        query = "SELECT * FROM inversores WHERE email = %s"
        result = self._db.fetch_one(query, (email,))
        if result:
            return Inversor(*result)
        return None

    def autenticar(self, email, contrasena):
        query = "SELECT * FROM inversores WHERE email = %s AND contrasena = %s"
        result = self._db.fetch_one(query, (email, contrasena))
        return result is not None