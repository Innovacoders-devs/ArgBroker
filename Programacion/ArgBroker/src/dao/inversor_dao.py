from dao_interface import DAOInterface
from Inversor import Inversor
from src.utils.mysql_connector import MySQLConnector

class InversorDAO(DAOInterface):
    def __init__(self):
        self._db = MySQLConnector()

    def crear(self, inversor: Inversor):
        query = "INSERT INTO inversores (nombre, apellido, cuil, email, contrasena) VALUES (%s, %s, %s, %s, %s)"
        values = (inversor.nombre, inversor.apellido, inversor.cuil, inversor.email, inversor.contrasena)
        self._db.execute(query, values)

    def obtener(self, id_inversor: int) -> Inversor:
        query = "SELECT * FROM inversores WHERE id = %s"
        result = self._db.fetch_one(query, (id_inversor,))
        if result:
            return Inversor(*result)
        return None

    def actualizar(self, inversor: Inversor):
        query = """
        UPDATE inversores SET nombre = %s, apellido = %s, cuil = %s, email = %s, contrasena = %s 
        WHERE id = %s
        """
        values = (inversor.nombre, inversor.apellido, inversor.cuil, inversor.email, inversor.contrasena, inversor.id)
        self._db.execute(query, values)

    def eliminar(self, id_inversor: int):
        query = "DELETE FROM inversores WHERE id = %s"
        self._db.execute(query, (id_inversor,))

    def obtener_inversor_por_email(self, email: str) -> Inversor:
        query = "SELECT * FROM inversores WHERE email = %s"
        result = self._db.fetch_one(query, (email,))
        if result:
            return Inversor(*result)
        return None

    def autenticar(self, email: str, contrasena: str) -> bool:
        query = "SELECT * FROM inversores WHERE email = %s AND contrasena = %s"
        result = self._db.fetch_one(query, (email, contrasena))
        return result is not None