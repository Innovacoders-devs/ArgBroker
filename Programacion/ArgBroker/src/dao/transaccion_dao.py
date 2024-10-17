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
        consulta = "SELECT * FROM transaccion WHERE id = %s"
        try:
            self._conector_mysql.conectar_a_base_datos()
            resultado = self._conector_mysql.traer_solo_uno(consulta, (id_transaccion))
            if resultado:
                return Transaccion(*resultado)
            return None
        except Exception as e:
            print(f"Ocurrio un error al obtener transaccion: {e}")
        
        finally:
            self._conector_mysql.desconectar_de_base_datos()

    def actualizar(self, transaccion):
        consulta = "UPDATE transaccion SET id_inversor = %s, id_accion = %s, tipo = %s, fecha = %s, precio = %s, cantidad = %s, comision = %s WHERE id = %s"
        valores_a_insertar = (transaccion.id_inversor, transaccion.id_accion, transaccion.tipo, transaccion.fecha, transaccion.precio, transaccion.cantidad, transaccion.comision, transaccion.id_transaccion)
        try:
            self._conector_mysql.conectar_a_base_datos()
            self._conector_mysql.ejecutar_consulta(consulta, valores_a_insertar)
        except Exception as e:
            print(f"Error al actualizar transaccion en la base de datos: {e} ")
        finally:
            self._conector_mysql.desconectar_de_base_datos()

    def eliminar(self, id_transaccion):
        consulta = "DELETE FROM transaccion WHERE id = %s"
        try:
            self._conector_mysql.conectar_a_base_datos()
            self._conector_mysql.ejecutar_consulta(consulta, (id_transaccion,))
            return True
        except Exception as e:
            print(f"Error al eliminar transaccion en la base de datos: {e} ")
            return False
        finally:
            self._conector_mysql.desconectar_de_base_datos()

    def obtener_transaccion_por_inversor(self, id_inversor):
        consulta = "SELECT * FROM transaccion WHERE id_inversor = %s"
        try:
            self._conector_mysql.conectar_a_base_datos()
            resultados = self._conector_mysql.traer_todos(consulta, (id_inversor,))
            if resultados:
                return [Transaccion(*resultado) for resultado in resultados]
            return []
        except Exception as e:
            print(f"Ocurrio un error al obtener transaccion por inversor: {e}")
        finally:
            self._conector_mysql.desconectar_de_base_datos()