from dao_interface import DAOInterface
from model.transaccion import Transaccion
from src.utils.mysql_connector import MySQLConnector

class TransaccionDAO(DAOInterface):
    def __init__(self):
        self._conector_mysql = MySQLConnector()
                
    def crear(self, transaccion):
        consulta = "INSERT INTO transaccion (id_transaccion, id_inversor, id_accion, tipo, fecha, precio, cantidad, comision) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        valores_a_insertar = (transaccion.id_transaccion, transaccion.id_inversor, transaccion.id_accion, transaccion.tipo, transaccion.fecha, transaccion.precio, transaccion.cantidad, transaccion.comision)
        try:
            self._conector_mysql.conectar_a_base_datos()
            self._conector_mysql.ejecutar_consulta(consulta, valores_a_insertar)
        except Exception as e:
            print(f"Error al crear transaccion en la base de datos: {e} ")
        finally:
            self._conector_mysql.desconectar_de_base_datos()

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